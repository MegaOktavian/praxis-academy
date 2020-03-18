# Aplikasi Python dengan CockroachDB dan SQLAlchemy

1. Menginstall SQLAlchemy :

    pip install sqlalchemy cockroachdb

   ![0301]()

2. Mulai shell SQL bawaan :

    cockroach sql --insecure

   ![0301]()

   Membuat maxroach user dan database bank :

    CREATE USER IF NOT EXISTS maxroach;

    CREATE DATABASE bank;

   ![0301]()

   Berikan izin maxroach yang diperlukan kepada pengguna :

    GRANT ALL ON DATABASE bank TO maxroach;
  
   ![0301]()

   Keluar dari shell SQL :

    \q

   ![0301]()

