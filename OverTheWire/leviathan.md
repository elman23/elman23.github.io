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

## Level 2 -> 3

```
leviathan2@gibson:~$ ls
printfile
leviathan2@gibson:~$ ./printfile .bash_logout
# ~/.bash_logout: executed by bash(1) when login shell exits.

# when leaving the console clear the screen to increase privacy

if [ "$SHLVL" = 1 ]; then
    [ -x /usr/bin/clear_console ] && /usr/bin/clear_console -q
fi
leviathan2@gibson:~$ ltrace ./printfile .bash_logout
__libc_start_main(0x80491e6, 2, 0xffffd644, 0 <unfinished ...>
access(".bash_logout", 4)                        = 0
snprintf("/bin/cat .bash_logout", 511, "/bin/cat %s", ".bash_logout") = 21
geteuid()                                        = 12002
geteuid()                                        = 12002
setreuid(12002, 12002)                           = 0
system("/bin/cat .bash_logout"# ~/.bash_logout: executed by bash(1) when login shell exits.

# when leaving the console clear the screen to increase privacy

if [ "$SHLVL" = 1 ]; then
    [ -x /usr/bin/clear_console ] && /usr/bin/clear_console -q
fi
 <no return ...>
--- SIGCHLD (Child exited) ---
<... system resumed> )                           = 0
+++ exited (status 0) +++
leviathan2@gibson:~$ mktemp d
mktemp: too few X's in template ‘d’
leviathan2@gibson:~$ man mktemp
leviathan2@gibson:~$ mktemp -d
/tmp/tmp.xUXMnL6Ia1
leviathan2@gibson:~$ touch /tmp/tmp.xUXMnL6Ia1/"test file.txt"
leviathan2@gibson:~$ ltrace ./printfile /tmp/tmp.xUXMnL6Ia1/"test file.txt"
__libc_start_main(0x80491e6, 2, 0xffffd634, 0 <unfinished ...>
access("/tmp/tmp.xUXMnL6Ia1/test file.tx"..., 4) = 0
snprintf("/bin/cat /tmp/tmp.xUXMnL6Ia1/tes"..., 511, "/bin/cat %s", "/tmp/tmp.xUXMnL6Ia1/test file.tx"...) = 42
geteuid()                                        = 12002
geteuid()                                        = 12002
setreuid(12002, 12002)                           = 0
system("/bin/cat /tmp/tmp.xUXMnL6Ia1/tes".../bin/cat: /tmp/tmp.xUXMnL6Ia1/test: No such file or directory
/bin/cat: file.txt: No such file or directory
 <no return ...>
--- SIGCHLD (Child exited) ---
<... system resumed> )                           = 256
+++ exited (status 0) +++
leviathan2@gibson:~$ ln -s /etc/leviathan_pass/leviathan3 /tmp/tmp.xUXMnL6Ia1/test
leviathan2@gibson:~$ ./printfile /tmp/tmp.xUXMnL6Ia1/"test file"
You cant have that file...
leviathan2@gibson:~$ ./printfile /tmp/tmp.xUXMnL6Ia1/"test file.txt"
/bin/cat: /tmp/tmp.xUXMnL6Ia1/test: Permission denied
/bin/cat: file.txt: No such file or directory
leviathan2@gibson:~$ ln -s /etc/leviathan_pass/leviathan3 /tmp/tmp.xUXMnL6Ia1/test
ln: failed to create symbolic link '/tmp/tmp.xUXMnL6Ia1/test': File exists
leviathan2@gibson:~$ ls -l /tmp/tmp.xUXMnL6Ia1
total 0
lrwxrwxrwx 1 leviathan2 leviathan2 30 May 18 20:04 test -> /etc/leviathan_pass/leviathan3
-rw-rw-r-- 1 leviathan2 leviathan2  0 May 18 20:02 test file.txt
leviathan2@gibson:~$ chmod 777 /tmp/tmp.xUXMnL6Ia1
leviathan2@gibson:~$ ./printfile /tmp/tmp.xUXMnL6Ia1/"test file.txt"
Q0G8j4sakn
/bin/cat: file.txt: No such file or directory
```

## Level 3 -> 4

```
leviathan3@gibson:~$ ls
level3
leviathan3@gibson:~$ ./level3
Enter the password>
bzzzzzzzzap. WRONG
leviathan3@gibson:~$ man ltrace
leviathan3@gibson:~$ man strace
leviathan3@gibson:~$ ltrace ./level3
__libc_start_main(0x80492bf, 1, 0xffffd654, 0 <unfinished ...>
strcmp("h0no33", "kakaka")                       = -1
printf("Enter the password> ")                   = 20
fgets(Enter the password> asd
"asd\n", 256, 0xf7e2a620)                  = 0xffffd42c
strcmp("asd\n", "snlprintf\n")                   = -1
puts("bzzzzzzzzap. WRONG"bzzzzzzzzap. WRONG
)                       = 19
+++ exited (status 0) +++
leviathan3@gibson:~$ ./level3
Enter the password> snlprintf
[You've got shell]!
$ whoami
leviathan4
$ cat /etc/leviathan_pass/leviathan4
AgvropI4OA
```
