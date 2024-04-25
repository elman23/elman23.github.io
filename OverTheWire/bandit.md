# Bandit

[https://overthewire.org/wargames/bandit/](https://overthewire.org/wargames/bandit/)

## Level 0

### Task

The goal of this level is for you to log into the game using SSH. The host to which you need to connect is `bandit.labs.overthewire.org`, on port `2220`. The username is `bandit0` and the password is `bandit0`. Once logged in, go to the Level 1 page to find out how to beat Level 1.

### Solution

Simply use the command `ssh`:

```
ssh bandit0@bandit.labs.overthewire.org -p 2220
```

and insert the password `bandit0` when asked for it.

## Level 1

### Task

The password for the next level is stored in a file called `readme` located in the home directory. Use this password to log into `bandit1` using SSH. Whenever you find a password for a level, use SSH (on port `2220`) to log into that level and continue the game.

### Solution

```
bandit0@bandit:~$ ls
readme
bandit0@bandit:~$ cat readme
NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL
```

## Level 2

### Task

The password for the next level is stored in a file called `-` located in the home directory

### Solution

```
bandit1@bandit:~$ ls
-
bandit1@bandit:~$ cat ./-
rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi
```

## Level 3

### Task

The password for the next level is stored in a file called `spaces in this filename` located in the home directory.

### Solution

```
bandit2@bandit:~$ ls
spaces in this filename
bandit2@bandit:~$ cat "spaces in this filename"
aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG
```

## Level 4

### Task

The password for the next level is stored in a hidden file in the `inhere` directory.

### Solution

```
bandit3@bandit:~$ ls
inhere
bandit3@bandit:~$ ls inhere/
bandit3@bandit:~$ ls -a inhere/
.  ..  .hidden
bandit3@bandit:~$ cat inhere/.hidden
2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe
```

## Level 5

### Task

The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the `reset` command.

### Solution

```
bandit4@bandit:~$ ls
inhere
bandit4@bandit:~$ ls inhere/
-file00  -file02  -file04  -file06  -file08
-file01  -file03  -file05  -file07  -file09
bandit4@bandit:~$ for file in $(ls inhere/); do file inhere/$file; done
inhere/-file00: data
inhere/-file01: data
inhere/-file02: data
inhere/-file03: data
inhere/-file04: data
inhere/-file05: data
inhere/-file06: data
inhere/-file07: ASCII text
inhere/-file08: data
inhere/-file09: data
bandit4@bandit:~$ cat inhere/-file07
lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR
```

## Level 6

### Task

The password for the next level is stored in a file somewhere under the `inhere` directory and has all of the following properties:

- human-readable,
- 1033 bytes in size,
- not executable.

### Solution

```
bandit5@bandit:~$ ls
inhere
bandit5@bandit:~$ find inhere/ -size 1033c
inhere/maybehere07/.file2
bandit5@bandit:~$ cat inhere/maybehere07/.file2
P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU
```

## Level 7

### Task

The password for the next level is stored somewhere on the server and has all of the following properties:

- owned by user `bandit7`,
- owned by group `bandit6`,
- 33 bytes in size.

### Solution

```
bandit6@bandit:~$ find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
/var/lib/dpkg/info/bandit7.password
bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password
z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S
```

## Level 8

### Task

The password for the next level is stored in the file `data.txt` next to the word "millionth".

### Solution

```
bandit7@bandit:~$ ls
data.txt
bandit7@bandit:~$ grep -A 3 -B 3 millionth data.txt
sermon's	F5B9EHIT1tI56VfczeBtEHWGlSTS0SWl
hoe's	HhTKj3PgrBCYxn8BAHgWg3aYyQPwNs4b
huffy	WJDdimZChuTlmWvX1f00KQgSd3DI63in
millionth	TESKZC0XvTetK0S9xNwm25STk5iWrBvP
Roderick's	zbqXMhsLoFPqc2Mf0TJwI7H6KXp75PSi
cleanup's	ptKYlwR6eOUNk2TM9jxcsg225y6CQZVa
lassie's	Bg8NBxvkuwpoyzw56P3TnFnSEqCFGpDl
bandit7@bandit:~$ grep millionth data.txt
millionth	TESKZC0XvTetK0S9xNwm25STk5iWrBvP
```

## Level 9

### Task

The password for the next level is stored in the file `data.txt` and is the only line of text that occurs only once.

### Solution

```
bandit8@bandit:~$ ls
data.txt
bandit8@bandit:~$ sort data.txt | uniq -u
EN632PlfYiZbn3PhVK3XOGSlNInNE00t
```

## Level 10

### Task

The password for the next level is stored in the file `data.txt` in one of the few human-readable strings, preceded by several `=` characters.

### Solution

```
bandit9@bandit:~$ cat data.txt | strings | grep =
=2""L(
x]T========== theG)"
========== passwordk^
Y=xW
t%=q
========== is
4=}D3
{1\=
FC&=z
=Y!m
	$/2`)=Y
4_Q=\
MO=(
?=|J
WX=DA
{TbJ;=l
[=lI
========== G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s
>8=6
=r=_
=uea
zl=4
```

## Level 11

### Task

The password for the next level is stored in the file `data.txt`, which contains base64 encoded data.

### Solution

```
bandit10@bandit:~$ ls
data.txt
bandit10@bandit:~$ cat data.txt
VGhlIHBhc3N3b3JkIGlzIDZ6UGV6aUxkUjJSS05kTllGTmI2blZDS3pwaGxYSEJNCg==
bandit10@bandit:~$ cat data.txt | base64 -d
The password is 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM
```

## Level 12

### Task

The password for the next level is stored in the file `data.txt`, where all lowercase (`a-z`) and uppercase (`A-Z`) letters have been rotated by 13 positions.

### Solution

```
bandit11@bandit:~$ ls
data.txt
bandit11@bandit:~$ cat data.txt
Gur cnffjbeq vf WIAOOSFzMjXXBC0KoSKBbJ8puQm5lIEi
```

[Here](https://stackoverflow.com/questions/5442436/using-rot13-and-tr-command-for-having-an-encrypted-email-address) one finds something about Rot13:

```
echo 'fooman@example.com' | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

and

```
alias rot13="tr 'A-Za-z' 'N-ZA-Mn-za-m'"
```

Thus:

```
bandit11@bandit:~$ alias rot13="tr 'A-Za-z' 'N-ZA-Mn-za-m'"
bandit11@bandit:~$ cat data.txt | rot13
The password is JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv
```

## Level 13

### Task

The password for the next level is stored in the file `data.txt`, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under `/tmp` in which you can work. Use `mkdir` with a hard to guess directory name. Or better, use the command `mktemp -d`. Then copy the datafile using `cp`, and rename it using `mv` (read the manpages!).

### Solution

```
bandit12@bandit:~$ ls
data.txt
bandit12@bandit:~$ mkdir /tmp/mysecrettmpdir
bandit12@bandit:~$ cd /tmp/mysecrettmpdir
bandit12@bandit:/tmp/mysecrettmpdir$ xxd -r data.txt > a
bandit12@bandit:/tmp/mysecrettmpdir$ ls -l
total 8
-rw-rw-r-- 1 bandit12 bandit12  606 Apr 25 19:58 a
-rw-r----- 1 bandit12 bandit12 2582 Apr 25 19:57 data.txt
bandit12@bandit:/tmp/mysecrettmpdir$ file a
a: gzip compressed data, was "data2.bin", last modified: Thu Oct  5 06:19:20 2023, max compression, from Unix, original size modulo 2^32 573
bandit12@bandit:/tmp/mysecrettmpdir$ mv a a.gz
bandit12@bandit:/tmp/mysecrettmpdir$ gunzip a.gz
bandit12@bandit:/tmp/mysecrettmpdir$ ls
a  data.txt
bandit12@bandit:/tmp/mysecrettmpdir$ file a
a: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/mysecrettmpdir$ mv a a.bz2
bandit12@bandit:/tmp/mysecrettmpdir$ bzip2 -d a.bz2
bandit12@bandit:/tmp/mysecrettmpdir$ ls -l
total 8
-rw-rw-r-- 1 bandit12 bandit12  431 Apr 25 19:58 a
-rw-r----- 1 bandit12 bandit12 2582 Apr 25 19:57 data.txt
bandit12@bandit:/tmp/mysecrettmpdir$ file a
a: gzip compressed data, was "data4.bin", last modified: Thu Oct  5 06:19:20 2023, max compression, from Unix, original size modulo 2^32 20480
bandit12@bandit:/tmp/mysecrettmpdir$ mv a a.gz
bandit12@bandit:/tmp/mysecrettmpdir$ gunzip a
bandit12@bandit:/tmp/mysecrettmpdir$ ls
a  data.txt
bandit12@bandit:/tmp/mysecrettmpdir$ file a
a: POSIX tar archive (GNU)
bandit12@bandit:/tmp/mysecrettmpdir$ mv a a.tar
bandit12@bandit:/tmp/mysecrettmpdir$ tar -xvf a.tar
data5.bin
bandit12@bandit:/tmp/mysecrettmpdir$ file data5.bin
data5.bin: POSIX tar archive (GNU)
bandit12@bandit:/tmp/mysecrettmpdir$ mv data5.bin b.tar
bandit12@bandit:/tmp/mysecrettmpdir$ tar tvf b.tar
-rw-r--r-- root/root       217 2023-10-05 06:19 data6.bin
bandit12@bandit:/tmp/mysecrettmpdir$ tar xvf b.tar
data6.bin
bandit12@bandit:/tmp/mysecrettmpdir$ file data6.bin
data6.bin: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/mysecrettmpdir$ mv data6.bin c.bz2
bandit12@bandit:/tmp/mysecrettmpdir$ bzip2 -d c.bz2
bandit12@bandit:/tmp/mysecrettmpdir$ ls
a.tar  b.tar  c  data.txt
bandit12@bandit:/tmp/mysecrettmpdir$ file c
c: POSIX tar archive (GNU)
bandit12@bandit:/tmp/mysecrettmpdir$ mv c c.tar
bandit12@bandit:/tmp/mysecrettmpdir$ tar tvf c.tar
-rw-r--r-- root/root        79 2023-10-05 06:19 data8.bin
bandit12@bandit:/tmp/mysecrettmpdir$ tar xvf c.tar
data8.bin
bandit12@bandit:/tmp/mysecrettmpdir$ file data8.bin
data8.bin: gzip compressed data, was "data9.bin", last modified: Thu Oct  5 06:19:20 2023, max compression, from Unix, original size modulo 2^32 49
9:20 2023, max compression, from Unix, original size modulo 2^32 49
bandit12@bandit:/tmp/mysecrettmpdir$ mv data8.bin d.gz
bandit12@bandit:/tmp/mysecrettmpdir$ gunzip d.gz
bandit12@bandit:/tmp/mysecrettmpdir$ ls
a.tar  b.tar  c.tar  d  data.txt
bandit12@bandit:/tmp/mysecrettmpdir$ file d
d: ASCII text
bandit12@bandit:/tmp/mysecrettmpdir$ cat d
The password is wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw
```

## Level 14

### Task

The password for the next level is stored in `/etc/bandit_pass/bandit14` and can only be read by user `bandit14`. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level.

**Note**: `localhost` is a hostname that refers to the machine you are working on.

### Solution

```
bandit13@bandit:~$ ls
sshkey.private
bandit13@bandit:~$ cat sshkey.private
-----BEGIN RSA PRIVATE KEY-----
[OMISSIS]
-----END RSA PRIVATE KEY-----
```

Therefore:

```
vim bandit14
```

and paste the private key in there;

```
chmod 600 bandit14
```

and finally:

```
ssh -i bandit14 bandit14@bandit.labs.overthewire.org -p 2220
```

Then:

```
bandit14@bandit:~$ cat /etc/bandit_pass/bandit14
fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq
```

## Level 15

### Task

The password for the next level can be retrieved by submitting the password of the current level to port `30000` on `localhost`.

### Solution

```
bandit14@bandit:~$ echo fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq | nc localhost 30000
Correct!
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt
```

## Level 16

### Task

The password for the next level can be retrieved by submitting the password of the current level to port `30001` on `localhost` using SSL encryption.

**Helpful note**: Getting `HEARTBEATING` and `Read R BLOCK`? Use `-ign_eof` and read the `CONNECTED COMMANDS` section in the manpage. Next to `R` and `Q`, the `B` command also works in this version of that command...

### Solution

```
tldr openssl s_client

openssl s_client

OpenSSL command to create TLS client connections.
More information: <https://www.openssl.org/docs/manmaster/man1/openssl-s_client.html>.

- Display the start and expiry dates for a domain's certificate:
    openssl s_client -connect host:port 2>/dev/null | openssl x509 -noout -dates

- Display the certificate presented by an SSL/TLS server:
    openssl s_client -connect host:port </dev/null

- Set the Server Name Indicator (SNI) when connecting to the SSL/TLS server:
    openssl s_client -connect host:port -servername hostname

- Display the complete certificate chain of an HTTPS server:
    openssl s_client -connect host:443 -showcerts </dev/null
```

```
bandit15@bandit:~$ openssl s_client -connect localhost:30001
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 CN = localhost
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN = localhost
verify error:num=10:certificate has expired
notAfter=Apr 24 21:15:52 2024 GMT
verify return:1
depth=0 CN = localhost
notAfter=Apr 24 21:15:52 2024 GMT
verify return:1
---
Certificate chain
 0 s:CN = localhost
   i:CN = localhost
   a:PKEY: rsaEncryption, 2048 (bit); sigalg: RSA-SHA1
   v:NotBefore: Apr 24 21:14:52 2024 GMT; NotAfter: Apr 24 21:15:52 2024 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIDCzCCAfOgAwIBAgIESbyazzANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDDAls
b2NhbGhvc3QwHhcNMjQwNDI0MjExNDUyWhcNMjQwNDI0MjExNTUyWjAUMRIwEAYD
VQQDDAlsb2NhbGhvc3QwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCN
wF8gRbbowv3UgQJSPdEmGi/GH81RGtawXf+PzQBoEqVHg1AiAR0kZA6yb2/TXKek
B04RbRRhbcPuQIVztjgV6gEI/uePTgUP/+54NR1in6/Q6e1ynBC7Ddmh17ycj8N+
OaUQXcfRSTv6Wjm53+xVjxV2W/K36xWagSf2IAsrFhJlt8IcHVSfAyNlj29tzsEK
7ReTxRDL8sfYfZrnA95r67Ery2vedKiP2e9umggzz0OReqnkGxDEhN6cmx6zF+Zl
8bvAoBred1rO62/1luLb4Bhx4uPty3roJ5s7JjF9YXL9M0ErjcydCvBiCrHh4pBg
QPFvHvHXE50rxZMBT0bBAgMBAAGjZTBjMBQGA1UdEQQNMAuCCWxvY2FsaG9zdDBL
BglghkgBhvhCAQ0EPhY8QXV0b21hdGljYWxseSBnZW5lcmF0ZWQgYnkgTmNhdC4g
U2VlIGh0dHBzOi8vbm1hcC5vcmcvbmNhdC8uMA0GCSqGSIb3DQEBBQUAA4IBAQAT
N6pKenjo+NO9pgRD21hyhECO7Y4cR9BcaCLEXAqrnLBGQzs6dN2K3q4t/pG5lyS2
cz+PyImhRO2Gg5adWvPzY/QLPGeVEcKVJZ8g/OELR+PKRjaAx9nSkCjBSdhAwKRG
Tm32wbeMRxqd7Jn0DZcE6/+YpZlw5FURNXuSIboi8HvU69hFH2Ga2zZkbC5vzjEo
/yCmwn2Q0NYT5n39KWI0H34tKWhgCfG4qE6IiPeQ0XhNJuNgE5b819cFfH6/ntYf
1B95YfPyIiJuJg26GrioXhk1OeS+Ly2LtqrSQ6Zc7AFCHCG3FsPyaJbAD4I0C+1V
MzANlV3JAm8Dl7mpO6Lb
-----END CERTIFICATE-----
subject=CN = localhost
issuer=CN = localhost
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA-PSS
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 1339 bytes and written 373 bytes
Verification error: certificate has expired
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Server public key is 2048 bit
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 10 (certificate has expired)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: E285D2379424D66070BF3912095618C79EAB0CA42517AADE2BC6F7D4F4D1E553
    Session-ID-ctx:
    Resumption PSK: E6073882CCA737EB47978C50D8847F3CF2C03DCEE758359707DC6B2B9D537CC6D2E8FF687A58EC236A93F55DCDDDF6DE
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 99 90 0e 98 29 4b d0 4b-67 3c aa 37 a8 5e 80 ad   ....)K.Kg<.7.^..
    0010 - 0a 00 81 71 52 af 99 31-c6 c0 02 f5 de c5 04 6a   ...qR..1.......j
    0020 - 42 58 98 ae 14 9d 9b 8d-3c 5b 7c 5f 13 a4 2d 93   BX......<[|_..-.
    0030 - 64 d5 8c b4 5e 26 f2 14-88 27 f1 d3 a1 42 a8 9c   d...^&...'...B..
    0040 - 8c ba bf 28 75 7a 48 b4-50 8d 47 ad da e9 1e fa   ...(uzH.P.G.....
    0050 - 4d 00 9b 24 36 14 23 b1-13 f5 15 7d 04 5f 3e 41   M..$6.#....}._>A
    0060 - d3 29 40 b9 8d 45 3f ce-36 79 6b ad 26 ca 18 37   .)@..E?.6yk.&..7
    0070 - c2 7b c7 4b fb 65 27 a7-ac d5 13 6e d1 05 6e 4f   .{.K.e'....n..nO
    0080 - e6 4c d7 87 ee 05 31 ab-42 7a 9c 15 eb a7 11 9d   .L....1.Bz......
    0090 - 0c 48 4e 4d 16 0c 39 c6-36 ed 38 64 82 cd 8e 93   .HNM..9.6.8d....
    00a0 - 88 29 c9 21 b9 5d a4 01-74 54 39 06 31 75 10 ac   .).!.]..tT9.1u..
    00b0 - 25 9a 92 1f 29 20 77 72-f4 3d 46 be fc 78 83 f0   %...) wr.=F..x..
    00c0 - 72 f2 7e 29 be e8 ea 69-e1 22 e6 e9 f3 b7 ab 4e   r.~)...i.".....N

    Start Time: 1714076433
    Timeout   : 7200 (sec)
    Verify return code: 10 (certificate has expired)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 50D9A8444B6CA0C88D1C8446B358FE57FB8E6EE7F60D646FF7BC3F57ADEA9579
    Session-ID-ctx:
    Resumption PSK: 6F2D06F99011658F421362E56ACA11F657FA492C290A32BB13655A979FB4F4FDA9C55CB2E874F96C4B6AF50D13D786E4
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 99 90 0e 98 29 4b d0 4b-67 3c aa 37 a8 5e 80 ad   ....)K.Kg<.7.^..
    0010 - f6 03 ec 32 26 24 f6 75-09 45 c0 81 cf 51 46 93   ...2&$.u.E...QF.
    0020 - b7 31 9f ef a8 a5 57 96-31 ab 5c ad c4 90 96 a1   .1....W.1.\.....
    0030 - 79 50 85 cd 2a 80 31 7e-0f da 7b 88 91 14 7d fe   yP..*.1~..{...}.
    0040 - 1e 41 8a 21 44 0b 37 29-d0 d7 c6 0a d4 ed 04 79   .A.!D.7).......y
    0050 - b0 b4 4a 64 db 1d 39 d6-53 06 40 c0 85 ba e2 2a   ..Jd..9.S.@....*
    0060 - cb 1f f1 de 6d fa 96 9f-0a 1b 07 2e 0d e0 c2 65   ....m..........e
    0070 - f5 22 3d bf b6 b0 2c 6c-96 60 e4 1a 09 f5 ec 49   ."=...,l.`.....I
    0080 - e1 e6 36 88 b7 9e 8d a6-bf 06 a9 b7 96 88 a9 72   ..6............r
    0090 - c3 b6 41 fd d7 2b d4 ff-b9 bc 3e fd 30 2e 2b d3   ..A..+....>.0.+.
    00a0 - f1 e1 82 de f7 86 45 00-55 44 57 8e f4 78 ec 4a   ......E.UDW..x.J
    00b0 - 47 ca af 87 5f 3a 8e f1-6d ba dc 6e 51 c1 c4 15   G..._:..m..nQ...
    00c0 - 0c 45 84 38 0d 57 32 91-f5 51 d4 dd a2 20 73 67   .E.8.W2..Q... sg

    Start Time: 1714076433
    Timeout   : 7200 (sec)
    Verify return code: 10 (certificate has expired)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
```

Now submit the password:

```
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt
```

and get:

```
Correct!
JQttfApK4SeyHwDlI9SXGR50qclOAil1

closed
```

## Level 17

### Task

The credentials for the next level can be retrieved by submitting the password of the current level to a port on `localhost` in the range `31000` to `32000`. First find out which of these ports have a server listening on them. Then find out which of those speak SSL and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.

### Solution

```
bandit16@bandit:~$ which nmap
/usr/bin/nmap
bandit16@bandit:~$ nmap -p 31000-32000 localhost
Starting Nmap 7.80 ( https://nmap.org ) at 2024-04-25 20:23 UTC
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00019s latency).
Not shown: 996 closed ports
PORT      STATE SERVICE
31046/tcp open  unknown
31518/tcp open  unknown
31691/tcp open  unknown
31790/tcp open  unknown
31960/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 0.07 seconds
```

and:

```
bandit16@bandit:~$ nmap -sV -p 31000-32000 localhost
Starting Nmap 7.80 ( https://nmap.org ) at 2024-04-25 20:32 UTC
Stats: 0:00:47 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 60.00% done; ETC: 20:33 (0:00:32 remaining)
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00010s latency).
Not shown: 996 closed ports
PORT      STATE SERVICE     VERSION
31046/tcp open  echo
31518/tcp open  ssl/echo
31691/tcp open  echo
31790/tcp open  ssl/unknown
31960/tcp open  echo
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port31790-TCP:V=7.80%T=SSL%I=7%D=4/25%Time=662ABDDE%P=x86_64-pc-linux-g
SF:nu%r(GenericLines,31,"Wrong!\x20Please\x20enter\x20the\x20correct\x20cu
SF:rrent\x20password\n")%r(GetRequest,31,"Wrong!\x20Please\x20enter\x20the
SF:\x20correct\x20current\x20password\n")%r(HTTPOptions,31,"Wrong!\x20Plea
SF:se\x20enter\x20the\x20correct\x20current\x20password\n")%r(RTSPRequest,
SF:31,"Wrong!\x20Please\x20enter\x20the\x20correct\x20current\x20password\
SF:n")%r(Help,31,"Wrong!\x20Please\x20enter\x20the\x20correct\x20current\x
SF:20password\n")%r(SSLSessionReq,31,"Wrong!\x20Please\x20enter\x20the\x20
SF:correct\x20current\x20password\n")%r(TerminalServerCookie,31,"Wrong!\x2
SF:0Please\x20enter\x20the\x20correct\x20current\x20password\n")%r(TLSSess
SF:ionReq,31,"Wrong!\x20Please\x20enter\x20the\x20correct\x20current\x20pa
SF:ssword\n")%r(Kerberos,31,"Wrong!\x20Please\x20enter\x20the\x20correct\x
SF:20current\x20password\n")%r(FourOhFourRequest,31,"Wrong!\x20Please\x20e
SF:nter\x20the\x20correct\x20current\x20password\n")%r(LPDString,31,"Wrong
SF:!\x20Please\x20enter\x20the\x20correct\x20current\x20password\n")%r(LDA
SF:PSearchReq,31,"Wrong!\x20Please\x20enter\x20the\x20correct\x20current\x
SF:20password\n")%r(SIPOptions,31,"Wrong!\x20Please\x20enter\x20the\x20cor
SF:rect\x20current\x20password\n");

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 98.32 seconds
```

thus:

```
bandit16@bandit:~$ openssl s_client localhost:31790
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 CN = localhost
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN = localhost
verify error:num=10:certificate has expired
notAfter=Apr 24 21:15:51 2024 GMT
verify return:1
depth=0 CN = localhost
notAfter=Apr 24 21:15:51 2024 GMT
verify return:1
---
Certificate chain
 0 s:CN = localhost
   i:CN = localhost
   a:PKEY: rsaEncryption, 2048 (bit); sigalg: RSA-SHA1
   v:NotBefore: Apr 24 21:14:51 2024 GMT; NotAfter: Apr 24 21:15:51 2024 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIDCzCCAfOgAwIBAgIEJl3U9DANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDDAls
b2NhbGhvc3QwHhcNMjQwNDI0MjExNDUxWhcNMjQwNDI0MjExNTUxWjAUMRIwEAYD
VQQDDAlsb2NhbGhvc3QwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDb
6QzTDydSCMMeoaSVCLOqwFJFWQXvzt4H5sVbdhtKtozHnB8HX0C3RGCv5taU1vm4
QHCjeWoW6DT1AEIezy3RiIyFARPPvzw8ikJ5duw2C6iDX6eRPPTm9L+Bt1ARNXhe
wFHZZh0yrUyvgHCu2V4UtMfdx+6BAY2mVyJozfhZtRVYJ6zPqzXTYn5kbEUcTWn4
RlgbjC9IVWhHWsP4RvS8Jrst0JHDmrBwu9VseyT/NBT1rjIkNlPyc4lvczIy1IeB
ZPzfEq7cwoBmRAeXtBfeFSn37T6mdnL9IZP0c4rjwWpjOLFirB4IDu8w0oB4Zwu6
LR/MPOdplaeACySO/pMRAgMBAAGjZTBjMBQGA1UdEQQNMAuCCWxvY2FsaG9zdDBL
BglghkgBhvhCAQ0EPhY8QXV0b21hdGljYWxseSBnZW5lcmF0ZWQgYnkgTmNhdC4g
U2VlIGh0dHBzOi8vbm1hcC5vcmcvbmNhdC8uMA0GCSqGSIb3DQEBBQUAA4IBAQAJ
oqN1nBg71GK4oDImAbRtt5uoM/aQ8oYawUOdqz6RC9NzehN+MagBvyqn2H/XaZsm
9W+rAxQ9vxWUoANGLGynW7WFyy+1bzz0dWlOJeE0GIhJ+NxogmV73ZIPLSqu4ioS
nofC4L1fYJx2W07+9ckhW0z56qI9Ak6bzY2RaaNQMut/C1BIVRvtRQS/Fia15Vdr
ZWfYeljVJH/jpxtK7LNOJ+Nrk458fs+MULmZX6yYEaA0Hyt/KZIM+xSDPnVoGzAA
9m9oJ1iEq2Wo07ziZ9DX6YoPq6yCNP6AuzhrP0/0Ut47ECp9VVQsYix0Agfr5LOu
i+B9mrzM5YEmUad9ZTIA
-----END CERTIFICATE-----
subject=CN = localhost
issuer=CN = localhost
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA-PSS
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 1339 bytes and written 373 bytes
Verification error: certificate has expired
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Server public key is 2048 bit
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 10 (certificate has expired)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 8010D1FADEB599EC41314F1AF719A16269E811A7E7674D574B2D201CC66DF7F9
    Session-ID-ctx:
    Resumption PSK: 6BA37972141E22104D5ED68BEA58722A507CA7BCE3ECF702D394F050493CD2B71DF3F994D26324E1C7FDFC6EB3DE740C
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 54 b0 fc 4c 0f 64 cb f1-9b f8 5a bc e2 85 27 e9   T..L.d....Z...'.
    0010 - 6c 4e 5c f5 09 d9 71 24-fc 4c 99 62 01 46 a9 7d   lN\...q$.L.b.F.}
    0020 - 03 56 84 f3 03 ba a6 04-31 56 53 df 3f 63 44 3c   .V......1VS.?cD<
    0030 - 42 d4 d9 76 be f8 79 0a-9b 68 4a f6 01 0d 6c 63   B..v..y..hJ...lc
    0040 - 06 39 e9 92 1f 2b 90 e7-15 87 e0 e6 7c 0a a9 df   .9...+......|...
    0050 - 2c 80 ce 42 68 41 e3 10-7d 4b 23 e7 26 5a 01 00   ,..BhA..}K#.&Z..
    0060 - e5 96 42 69 59 7b d3 c2-b3 74 ea eb 96 95 01 6a   ..BiY{...t.....j
    0070 - 74 20 95 a5 b6 96 5d 8f-fe 91 77 1e 07 0c b2 21   t ....]...w....!
    0080 - 11 dd 56 d8 85 0d 12 ff-46 64 58 2f f6 55 d7 50   ..V.....FdX/.U.P
    0090 - aa eb c5 33 c1 16 ca d9-d7 e7 6d 82 f0 f1 30 5d   ...3......m...0]
    00a0 - d0 52 04 60 d2 2e ff 86-60 5d 84 82 d3 3d d5 a7   .R.`....`]...=..
    00b0 - c9 3d a8 b3 b2 04 78 c9-25 d4 46 45 6d 56 2b cd   .=....x.%.FEmV+.
    00c0 - 24 4a ef c6 b1 3c 7d 29-3b 03 d2 f4 68 a0 0a 65   $J...<});...h..e

    Start Time: 1714077273
    Timeout   : 7200 (sec)
    Verify return code: 10 (certificate has expired)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: B2305A1B6E4992E81FA4F85AAA6389D2CD552696778688EA81A8944DCE04910C
    Session-ID-ctx:
    Resumption PSK: CABB41ACFB6B7B9BFBB1DBA09EDC0067C10FA29A71AB680198F7702722AC98B6C876F8F72C2A26F3A7CF69AA10DFB296
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 54 b0 fc 4c 0f 64 cb f1-9b f8 5a bc e2 85 27 e9   T..L.d....Z...'.
    0010 - 57 3c 19 3a 03 4e fb 72-cb 13 13 aa 90 a1 76 f3   W<.:.N.r......v.
    0020 - ce e2 0f cb a1 d0 a1 78-12 82 5a 97 ad e6 eb cf   .......x..Z.....
    0030 - 1c 24 75 57 bd d8 e3 18-42 50 99 72 4d eb 59 31   .$uW....BP.rM.Y1
    0040 - 05 4e 10 04 59 1e ba 6a-94 73 cc 75 eb 34 a4 c3   .N..Y..j.s.u.4..
    0050 - 2d 65 04 71 a2 ca 8d 39-10 2d 6a 22 eb f6 c4 74   -e.q...9.-j"...t
    0060 - ca 3c 9d bf c0 08 d6 11-00 46 35 3d c0 0b e2 e3   .<.......F5=....
    0070 - a1 b7 56 4e 31 44 99 74-62 15 98 2e 42 7c 96 7c   ..VN1D.tb...B|.|
    0080 - 96 01 c3 6b a7 8f ae 2f-8c 8a b3 61 21 44 ef ef   ...k.../...a!D..
    0090 - 94 7f 73 e8 29 76 79 38-90 dd 3a 23 f6 8f c7 48   ..s.)vy8..:#...H
    00a0 - 77 6f d2 ef 0f fb 5b d8-54 43 35 7e bd 48 c5 04   wo....[.TC5~.H..
    00b0 - 0c 56 1a a8 7d 28 a6 1f-7c 13 58 b6 70 50 f4 38   .V..}(..|.X.pP.8
    00c0 - 3f a0 ba d1 c3 e9 ab 89-71 5e 9a 5c 74 eb b5 3b   ?.......q^.\t..;

    Start Time: 1714077273
    Timeout   : 7200 (sec)
    Verify return code: 10 (certificate has expired)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
JQttfApK4SeyHwDlI9SXGR50qclOAil1
Correct!
-----BEGIN RSA PRIVATE KEY-----
[OMISSIS]
-----END RSA PRIVATE KEY-----

closed
```

---

Theoretical note:

```
bandit16@bandit:~$ array=( one two three )
bandit16@bandit:~$ for i in $array; do echo $i; done
one
bandit16@bandit:~$ for i in ${!array[@]}; do echo $i; done
0
1
2
bandit16@bandit:~$ for i in ${array[@]}; do echo $i; done
one
two
three
```

Can we use this to automate the port scan sending the previous password?

## Level 18

### Task

There are 2 files in the home directory: `passwords.old` and `passwords.new`. The password for the next level is in `passwords.new` and is the only line that has been changed between `passwords.old` and `passwords.new`.

**Note**: if you have solved this level and see `Byebye!` when trying to log into `bandit18`, this is related to the next level, `bandit19`.

### Solution

```
bandit17@bandit:~$ ls
passwords.new  passwords.old
bandit17@bandit:~$ diff passwords.new passwords.old
42c42
< hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg
---
> p6ggwdNHncnmCNxuAt0KtKVq185ZU7AW
```

The password is `hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg`.

## Level 19

### Task

The password for the next level is stored in a file `readme` in the home directory. Unfortunately, someone has modified `.bashrc` to log you out when you log in with SSH.

### Solution

```
ssh bandit18@bandit.labs.overthewire.org -p 2220 cat readme
                         _                     _ _ _
                        | |__   __ _ _ __   __| (_) |_
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_
                        |_.__/ \__,_|_| |_|\__,_|_|\__|


                      This is an OverTheWire game server.
            More information on http://www.overthewire.org/wargames

bandit18@bandit.labs.overthewire.org's password:
awhqfNnAbc1naukrpqDYcF95h7HoMTrC
```

## Level 20

### Task

To gain access to the next level, you should use the `setuid` binary in the home directory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (`/etc/bandit_pass`), after you have used the setuid binary.

### Solution

```
bandit19@bandit:~$ ls
bandit20-do
bandit19@bandit:~$ ./bandit20-do
Run a command as another user.
  Example: ./bandit20-do id
bandit19@bandit:~$ ./bandit20-do cat /etc/bandit_pass/bandit20
VxCazJaVykI6W36BkBU0mJTCM8rR95XT
```

## Level 21

### Task

There is a `setuid` binary in the home directory that does the following: it makes a connection to `localhost` on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (`bandit20`). If the password is correct, it will transmit the password for the next level (`bandit21`).

**Note**: Try connecting to your own network daemon to see if it works as you think.

### Solution

```
bandit20@bandit:~$ ls
suconnect
bandit20@bandit:~$ ./suconnect 9876
Could not connect
```

Split the terminal:

```
bandit20@bandit:~$ ./suconnect 9876     │ bandit20@bandit:~$ echo VxCazJaVykI6W36
Read: VxCazJaVykI6W36BkBU0mJTCM8rR95XT  │ BkBU0mJTCM8rR95XT | nc -nlvp 9876
Password matches, sending next password │ Listening on 0.0.0.0 9876
bandit20@bandit:~$                      │ Connection received on 127.0.0.1 41230
                                        │ NvEJF7oVjkddltPSrdKEFOllh9V1IBcq
                                        │ bandit20@bandit:~$
```
