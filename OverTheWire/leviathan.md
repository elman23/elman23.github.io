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

## Level 4 -> 5

```
leviathan4@gibson:~$ ls
leviathan4@gibson:~$ ls -la
total 24
drwxr-xr-x  3 root root       4096 Oct  5  2023 .
drwxr-xr-x 83 root root       4096 Oct  5  2023 ..
-rw-r--r--  1 root root        220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root root       3771 Jan  6  2022 .bashrc
-rw-r--r--  1 root root        807 Jan  6  2022 .profile
dr-xr-x---  2 root leviathan4 4096 Oct  5  2023 .trash
leviathan4@gibson:~$ cd .trash/
leviathan4@gibson:~/.trash$ ls
bin
leviathan4@gibson:~/.trash$ ./bin
01000101 01001011 01001011 01101100 01010100 01000110 00110001 01011000 01110001 01110011 00001010
leviathan4@gibson:~/.trash$ ltrace bin
Can't execute `bin': Permission denied
failed to initialize process 795368: No such file or directory
couldn't open program 'bin': No such file or directory
leviathan4@gibson:~/.trash$ strace bin
strace: Can't stat 'bin': No such file or directory
leviathan4@gibson:~/.trash$ ltrace ./bin
__libc_start_main(0x80491a6, 1, 0xffffd644, 0 <unfinished ...>
fopen("/etc/leviathan_pass/leviathan5", "r")     = 0
+++ exited (status 255) +++
leviathan4@gibson:~/.trash$ file bin
bin: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=8a80a5de629bf55ff162e8110099b5c4e77a4bb1, for GNU/Linux 3.2.0, not stripped
```

From [here](https://www.geeksforgeeks.org/python-program-to-convert-binary-to-ascii/):

```
# Function to convert binary to ASCII value
def binary_to_string(bits):
    return ''.join([chr(int(i, 2)) for i in bits])

# Driver Code

# This is the binary equivalent of string "GFG"
bin_values = ['01000111', '01000110', '01000111']

# calling the function
# and storing the result in variable 's'
s = binary_to_string(bin_values)

# Printing the result
print("The string created from the binary parts : ",s)
```

Our case:

```
def binary_to_string(bits):
    return ''.join([chr(int(i, 2)) for i in bits])

bin_values = ["01000101", "01001011", "01001011", "01101100", "01010100", "01000110", "00110001", "01011000", "01110001", "01110011", "00001010"]
s = binary_to_string(bin_values)
print(s)
```

```
>>> bin_values = ["01000101", "01001011", "01001011", "01101100", "01010100", "01000110", "00110001", "01011000", "01110001", "01110011", "00001010"]
>>> s = binary_to_string(bin_values)
>>> print(s)
EKKlTF1Xqs
```
