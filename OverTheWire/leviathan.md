Leviathan
Dare you face the lord of the oceans?
Leviathan is a wargame that has been rescued from the demise of intruded.net, previously hosted on leviathan.intruded.net. Big thanks to adc, morla and reth for their help in resurrecting this game!

What follows below is the original description of leviathan, copied from intruded.net:

Summary:
Difficulty: 1/10
Levels: 8
Platform: Linux/x86

Author:
Anders Tonfeldt

Special Thanks:
We would like to thank AstroMonk for coming up with a replacement idea for the last level,
deadfood for finding a leveljump and Coi for finding a non-planned vulnerability.

Description:
This wargame doesn't require any knowledge about programming - just a bit of common
sense and some knowledge about basic \*nix commands. We had no idea that it'd be this
hard to make an interesting wargame that wouldn't require programming abilities from
the players. Hopefully we made an interesting challenge for the new ones.
Leviathan’s levels are called leviathan0, leviathan1, … etc. and can be accessed on leviathan.labs.overthewire.org through SSH on port 2223.

To login to the first level use:

Username: leviathan0
Password: leviathan0
Data for the levels can be found in the homedirectories. You can look at /etc/leviathan_pass for the various level passwords.

## Level 0 -> 1

```
$ ssh leviathan0@leviathan.labs.overthewire.org -p 2223
```

```
leviathan0@gibson:~$ ls
leviathan0@gibson:~$ ls -a
.  ..  .backup  .bash_logout  .bashrc  .profile
leviathan0@gibson:~$ cd .backup/
leviathan0@gibson:~/.backup$ ls
bookmarks.html
leviathan0@gibson:~/.backup$ cat bookmarks.html | grep pass
<DT><A HREF="http://leviathan.labs.overthewire.org/passwordus.html | This will be fixed later, the password for leviathan1 is PPIfmI1qsA" ADD_DATE="1155384634" LAST_CHARSET="ISO-8859-1" ID="rdf:#$2wIU71">password to leviathan1</A>
```

## Level 1 -> 2

```
leviathan1@gibson:~$ ls
check
leviathan1@gibson:~$ ./check
password: PPIfmI1qsA
Wrong password, Good Bye ...
leviathan1@gibson:~$ ltrace ./check
__libc_start_main(0x80491e6, 1, 0xffffd654, 0 <unfinished ...>
printf("password: ")                                   = 10
getchar(0xf7fbe4a0, 0xf7fd6f90, 0x786573, 0x646f67password: PPIfmI1qsA
)    = 80
getchar(0xf7fbe4a0, 0xf7fd6f50, 0x786573, 0x646f67)    = 80
getchar(0xf7fbe4a0, 0xf7fd5050, 0x786573, 0x646f67)    = 73
strcmp("PPI", "sex")                                   = -1
puts("Wrong password, Good Bye ..."Wrong password, Good Bye ...
)                   = 29
+++ exited (status 0) +++
leviathan1@gibson:~$ ./check
password: sexasd
$ whoami
leviathan2
$ cat /etc/leviathan_pass/leviathan2
mEh5PNl10e
```
