# Aplikasi Python dengan CockroachDB dan SQLAlchemy

1. Menginstall SQLAlchemy :

        pip install sqlalchemy cockroachdb

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%208/Screenshot%20from%202020-03-18%2019-31-16.png)

2. Mulai shell SQL bawaan :

        cockroach sql --insecure

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%208/Screenshot%20from%202020-03-18%2019-40-49.png)

   Membuat maxroach user dan database bank :

        CREATE USER IF NOT EXISTS maxroach;

        CREATE DATABASE bank;

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%208/Screenshot%20from%202020-03-18%2019-46-32.png)

   Berikan izin maxroach yang diperlukan kepada pengguna :

        GRANT ALL ON DATABASE bank TO maxroach;
  
   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%208/Screenshot%20from%202020-03-18%2019-47-24.png)

   Keluar dari shell SQL :

        \q

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%208/Screenshot%20from%202020-03-18%2019-49-57.png)

### Menjalankan Kode Python

1. Buat file bernama sqlalchemy-basic-sample.py

        import random
        from math import floor
        from sqlalchemy import create_engine, Column, Integer
        from sqlalchemy.ext.declarative import declarative_base
        from sqlalchemy.orm import sessionmaker
        from cockroachdb.sqlalchemy import run_transaction

        Base = declarative_base()


        # The Account class corresponds to the "accounts" database table.
        class Account(Base):
            __tablename__ = 'accounts'
            id = Column(Integer, primary_key=True)
            balance = Column(Integer)


        # Create an engine to communicate with the database. The
        # "cockroachdb://" prefix for the engine URL indicates that we are
        # connecting to CockroachDB using the 'cockroachdb' dialect.
        # For more information, see
        # https://github.com/cockroachdb/cockroachdb-python.

        secure_cluster = True           # Set to False for insecure clusters
        connect_args = {}

        if secure_cluster:
            connect_args = {
                'sslmode': 'require',
                'sslrootcert': 'certs/ca.crt',
                'sslkey': 'certs/client.maxroach.key',
                'sslcert': 'certs/client.maxroach.crt'
            }
        else:
            connect_args = {'sslmode': 'disable'}

        engine = create_engine(
            'cockroachdb://maxroach@localhost:26257/bank',
            connect_args=connect_args,
            echo=True                   # Log SQL queries to stdout
        )

        # Automatically create the "accounts" table based on the Account class.
        Base.metadata.create_all(engine)


        # Store the account IDs we create for later use.

        seen_account_ids = set()


        # The code below generates random IDs for new accounts.

        def create_random_accounts(sess, n):
            """Create N new accounts with random IDs and random account balances.

            Note that since this is a demo, we don't do any work to ensure the
            new IDs don't collide with existing IDs.
            """
            new_accounts = []
            elems = iter(range(n))
            for i in elems:
                billion = 1000000000
                new_id = floor(random.random()*billion)
                seen_account_ids.add(new_id)
                new_accounts.append(
                    Account(
                        id=new_id,
                        balance=floor(random.random()*1000000)
                    )
                )
            sess.add_all(new_accounts)


        run_transaction(sessionmaker(bind=engine),
                        lambda s: create_random_accounts(s, 100))


        # Helper for getting random existing account IDs.

        def get_random_account_id():
            id = random.choice(tuple(seen_account_ids))
            return id


        def transfer_funds_randomly(session):
            """Transfer money randomly between accounts (during SESSION).

            Cuts a randomly selected account's balance in half, and gives the
            other half to some other randomly selected account.
            """
            source_id = get_random_account_id()
            sink_id = get_random_account_id()

            source = session.query(Account).filter_by(id=source_id).one()
            amount = floor(source.balance/2)

            # Check balance of the first account.
            if source.balance < amount:
                raise "Insufficient funds"

            source.balance -= amount
            session.query(Account).filter_by(id=sink_id).update(
                {"balance": (Account.balance + amount)}
            )


    # Run the transfer inside a transaction.

        run_transaction(sessionmaker(bind=engine), transfer_funds_randomly)

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%208/Screenshot%20from%202020-03-18%2019-50-29.png)

2. Jalankan file tersebut.

        python3 sqlalchemy-basic-sample.py

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%208/Screenshot%20from%202020-03-18%2020-02-58.png)

   Hasilnya kurang lebih :

        2018-12-06 15:59:58,999 INFO sqlalchemy.engine.base.Engine select current_schema()
        2018-12-06 15:59:58,999 INFO sqlalchemy.engine.base.Engine {}
        2018-12-06 15:59:59,001 INFO sqlalchemy.engine.base.Engine SELECT CAST('test plain returns' AS VARCHAR(60)) AS anon_1
        2018-12-06 15:59:59,001 INFO sqlalchemy.engine.base.Engine {}
        2018-12-06 15:59:59,001 INFO sqlalchemy.engine.base.Engine SELECT CAST('test unicode returns' AS VARCHAR(60)) AS anon_1
        2018-12-06 15:59:59,001 INFO sqlalchemy.engine.base.Engine {}
        2018-12-06 15:59:59,002 INFO sqlalchemy.engine.base.Engine select version()
        2018-12-06 15:59:59,002 INFO sqlalchemy.engine.base.Engine {}
        2018-12-06 15:59:59,003 INFO sqlalchemy.engine.base.Engine SELECT table_name FROM information_schema.tables WHERE table_schema=%s
        2018-12-06 15:59:59,004 INFO sqlalchemy.engine.base.Engine ('public',)
        2018-12-06 15:59:59,005 INFO sqlalchemy.engine.base.Engine SELECT id from accounts;
        2018-12-06 15:59:59,005 INFO sqlalchemy.engine.base.Engine {}
        2018-12-06 15:59:59,008 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
        2018-12-06 15:59:59,008 INFO sqlalchemy.engine.base.Engine SAVEPOINT cockroach_restart
        2018-12-06 15:59:59,008 INFO sqlalchemy.engine.base.Engine {}
        2018-12-06 15:59:59,083 INFO sqlalchemy.engine.base.Engine INSERT INTO accounts (id, balance) VALUES (%(id)s, %(balance)s)
        2018-12-06 15:59:59,083 INFO sqlalchemy.engine.base.Engine ({'id': 298865, 'balance': 208217}, {'id': 506738, 'balance': 962549}, {'id': 514698, 'balance': 986327}, {'id': 587747, 'balance': 210406}, {'id': 50148, 'balance': 347976}, {'id': 854295, 'balance': 420086}, {'id': 785757, 'balance': 364836}, {'id': 406247, 'balance': 787016}  ... displaying 10 of 100 total bound parameter sets ...  {'id': 591336, 'balance': 542066}, {'id': 33728, 'balance': 526531})
        2018-12-06 15:59:59,201 INFO sqlalchemy.engine.base.Engine RELEASE SAVEPOINT cockroach_restart
        2018-12-06 15:59:59,201 INFO sqlalchemy.engine.base.Engine {}
        2018-12-06 15:59:59,205 INFO sqlalchemy.engine.base.Engine COMMIT
        2018-12-06 15:59:59,206 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
        2018-12-06 15:59:59,206 INFO sqlalchemy.engine.base.Engine SAVEPOINT cockroach_restart
        2018-12-06 15:59:59,206 INFO sqlalchemy.engine.base.Engine {}
        2018-12-06 15:59:59,207 INFO sqlalchemy.engine.base.Engine SELECT accounts.id AS accounts_id, accounts.balance AS accounts_balance
        FROM accounts
        WHERE accounts.id = %(id_1)s
        2018-12-06 15:59:59,207 INFO sqlalchemy.engine.base.Engine {'id_1': 769626}
        2018-12-06 15:59:59,209 INFO sqlalchemy.engine.base.Engine UPDATE accounts SET balance=%(balance)s WHERE accounts.id = %(accounts_id)s
        2018-12-06 15:59:59,209 INFO sqlalchemy.engine.base.Engine {'balance': 470580, 'accounts_id': 769626}
        2018-12-06 15:59:59,212 INFO sqlalchemy.engine.base.Engine UPDATE accounts SET balance=(accounts.balance + %(balance_1)s) WHERE accounts.id = %(id_1)s
        2018-12-06 15:59:59,247 INFO sqlalchemy.engine.base.Engine {'balance_1': 470580, 'id_1': 158447}
        2018-12-06 15:59:59,249 INFO sqlalchemy.engine.base.Engine RELEASE SAVEPOINT cockroach_restart
        2018-12-06 15:59:59,250 INFO sqlalchemy.engine.base.Engine {}
        2018-12-06 15:59:59,251 INFO sqlalchemy.engine.base.Engine COMMIT

