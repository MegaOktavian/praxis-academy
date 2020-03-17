# Menginstall CockroachDB

1. Unduh arsip CockroachDB untuk linux, dan ekstrak binernya :

   https://binaries.cockroachdb.com/cockroach-v19.2.4.linux-amd64.tgz

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%206/Screenshot%20from%202020-03-16%2021-56-22.png)

    wget -qO- https://binaries.cockroachdb.com/cockroach-v19.2.4.linux-amd64.tgz | tar  xvz

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%206/Screenshot%20from%202020-03-16%2021-57-09.png)

2. Salin biner ke PATH sehingga memudahkan untuk mengeksekusi :

    cp -i cockroach-v19.2.4.linux-amd64/cockroach /usr/local/bin/

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%206/Screenshot%20from%202020-03-16%2022-04-54.png)