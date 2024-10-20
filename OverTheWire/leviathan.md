# Leviathan

## Introduction

Dare you face the lord of the oceans?
Leviathan is a wargame that has been rescued from the demise of `intruded.net`, previously hosted on `leviathan.intruded.net`. Big thanks to adc, morla and reth for their help in resurrecting this game!

What follows below is the original description of `leviathan`, copied from `intruded.net`:

**Summary**:
Difficulty: 1/10
Levels: 8
Platform: Linux/x86

**Author**:
Anders Tonfeldt

**Special Thanks**:
We would like to thank AstroMonk for coming up with a replacement idea for the last level,
deadfood for finding a leveljump and Coi for finding a non-planned vulnerability.

**Description**:
This wargame doesn't require any knowledge about programming - just a bit of common
sense and some knowledge about basic \*nix commands. We had no idea that it'd be this
hard to make an interesting wargame that wouldn't require programming abilities from
the players. Hopefully we made an interesting challenge for the new ones.
Leviathan’s levels are called `leviathan0`, `leviathan1`, ... etc. and can be accessed on `leviathan.labs.overthewire.org` through SSH on port `2223`.

To login to the first level use:

Username: `leviathan0`
Password: `leviathan0`
Data for the levels can be found in the home directories. You can look at `/etc/leviathan_pass` for the various level passwords.

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

Interactively:

```
>>> bin_values = ["01000101", "01001011", "01001011", "01101100", "01010100", "01000110", "00110001", "01011000", "01110001", "01110011", "00001010"]
>>> s = binary_to_string(bin_values)
>>> print(s)
EKKlTF1Xqs
```

## Level 5 -> 6

```
leviathan5@gibson:~$ ls -la
total 36
drwxr-xr-x  2 root       root        4096 Oct  5  2023 .
drwxr-xr-x 83 root       root        4096 Oct  5  2023 ..
-rw-r--r--  1 root       root         220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root       root        3771 Jan  6  2022 .bashrc
-r-sr-x---  1 leviathan6 leviathan5 15132 Oct  5  2023 leviathan5
-rw-r--r--  1 root       root         807 Jan  6  2022 .profile
leviathan5@gibson:~$ ./leviathan5
Cannot find /tmp/file.log
leviathan5@gibson:~$ ls /tmp/file.log
ls: cannot access '/tmp/file.log': No such file or directory
leviathan5@gibson:~$ ln -s /etc/leviathan_pass/leviathan6 /tmp/file.log
leviathan5@gibson:~$ ./leviathan5
YZ55XPVk2l
```

## Leviathan 6 -> 7

```
leviathan6@gibson:~$ ls -la
total 36
drwxr-xr-x  2 root       root        4096 Oct  5  2023 .
drwxr-xr-x 83 root       root        4096 Oct  5  2023 ..
-rw-r--r--  1 root       root         220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root       root        3771 Jan  6  2022 .bashrc
-r-sr-x---  1 leviathan7 leviathan6 15024 Oct  5  2023 leviathan6
-rw-r--r--  1 root       root         807 Jan  6  2022 .profile
leviathan6@gibson:~$ ./leviathan6
usage: ./leviathan6 <4 digit code>
leviathan6@gibson:~$ ./leviathan6 0000
Wrong
leviathan6@gibson:~$ ltrace ./leviathan6 0000
__libc_start_main(0x80491d6, 2, 0xffffd644, 0 <unfinished ...>
atoi(0xffffd79c, 0xf7fd6f90, 0xf7c184be, 0xf7fbe4a0) = 0
puts("Wrong"Wrong
)                                    = 6
+++ exited (status 0) +++
leviathan6@gibson:~$ strace ./leviathan6 0000
execve("./leviathan6", ["./leviathan6", "0000"], 0x7fffffffe558 /* 23 vars */) = 0
[ Process PID=800529 runs in 32 bit mode. ]
access("/etc/suid-debug", F_OK)         = -1 ENOENT (No such file or directory)
brk(NULL)                               = 0x804d000
arch_prctl(0x3001 /* ARCH_??? */, 0xffffd4e8) = -1 EINVAL (Invalid argument)
fcntl64(0, F_GETFD)                     = 0
fcntl64(1, F_GETFD)                     = 0
fcntl64(2, F_GETFD)                     = 0
access("/etc/suid-debug", F_OK)         = -1 ENOENT (No such file or directory)
mmap2(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xf7fbe000
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_LARGEFILE|O_CLOEXEC) = 3
statx(3, "", AT_STATX_SYNC_AS_STAT|AT_NO_AUTOMOUNT|AT_EMPTY_PATH, STATX_BASIC_STATS, {stx_mask=STATX_BASIC_STATS|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFREG|0644, stx_size=31595, ...}) = 0
mmap2(NULL, 31595, PROT_READ, MAP_PRIVATE, 3, 0) = 0xf7fb6000
close(3)                                = 0
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/i386-linux-gnu/libc.so.6", O_RDONLY|O_LARGEFILE|O_CLOEXEC) = 3
read(3, "\177ELF\1\1\1\3\0\0\0\0\0\0\0\0\3\0\3\0\1\0\0\0p\27\2\0004\0\0\0"..., 512) = 512
pread64(3, "\4\0\0\0\24\0\0\0\3\0\0\0GNU\0\326\250j\1=\233\37\350y\10\256\250\273\27r\340"..., 96, 468) = 96
statx(3, "", AT_STATX_SYNC_AS_STAT|AT_NO_AUTOMOUNT|AT_EMPTY_PATH, STATX_BASIC_STATS, {stx_mask=STATX_BASIC_STATS|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFREG|0755, stx_size=2280756, ...}) = 0
mmap2(NULL, 2312124, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0xf7c00000
mprotect(0xf7c20000, 2129920, PROT_NONE) = 0
mmap2(0xf7c20000, 1581056, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x20000) = 0xf7c20000
mmap2(0xf7da2000, 544768, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1a2000) = 0xf7da2000
mmap2(0xf7e28000, 12288, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x227000) = 0xf7e28000
mmap2(0xf7e2b000, 38844, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0xf7e2b000
close(3)                                = 0
set_thread_area({entry_number=-1, base_addr=0xf7fbf500, limit=0x0fffff, seg_32bit=1, contents=0, read_exec_only=0, limit_in_pages=1, seg_not_present=0, useable=1}) = 0 (entry_number=12)
set_tid_address(0xf7fbf568)             = 800529
set_robust_list(0xf7fbf570, 12)         = 0
rseq(0xf7fbfa20, 0x20, 0, 0x53053053)   = 0
mprotect(0xf7e28000, 8192, PROT_READ)   = 0
mprotect(0x804b000, 4096, PROT_READ)    = 0
mprotect(0xf7ffb000, 8192, PROT_READ)   = 0
ugetrlimit(RLIMIT_STACK, {rlim_cur=8192*1024, rlim_max=RLIM_INFINITY}) = 0
munmap(0xf7fb6000, 31595)               = 0
statx(1, "", AT_STATX_SYNC_AS_STAT|AT_NO_AUTOMOUNT|AT_EMPTY_PATH, STATX_BASIC_STATS, {stx_mask=STATX_BASIC_STATS|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFCHR|0620, stx_size=0, ...}) = 0
getrandom("\xc7\x5e\x99\xd9", 4, GRND_NONBLOCK) = 4
brk(NULL)                               = 0x804d000
brk(0x806e000)                          = 0x806e000
brk(0x806f000)                          = 0x806f000
write(1, "Wrong\n", 6Wrong
)                  = 6
exit_group(0)                           = ?
+++ exited with 0 +++
```

How to find the code needed? Use `gdb`.

```
leviathan6@gibson:~$ gdb --args ./leviathan6 0000
GNU gdb (Ubuntu 12.1-0ubuntu1~22.04) 12.1
Copyright (C) 2022 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./leviathan6...
(No debugging symbols found in ./leviathan6)
(gdb) disassemble main
Dump of assembler code for function main:
   0x080491d6 <+0>:	lea    0x4(%esp),%ecx
   0x080491da <+4>:	and    $0xfffffff0,%esp
   0x080491dd <+7>:	push   -0x4(%ecx)
   0x080491e0 <+10>:	push   %ebp
   0x080491e1 <+11>:	mov    %esp,%ebp
   0x080491e3 <+13>:	push   %ebx
   0x080491e4 <+14>:	push   %ecx
   0x080491e5 <+15>:	sub    $0x10,%esp
   0x080491e8 <+18>:	mov    %ecx,%eax
   0x080491ea <+20>:	movl   $0x1bd3,-0xc(%ebp)
   0x080491f1 <+27>:	cmpl   $0x2,(%eax)
   0x080491f4 <+30>:	je     0x8049216 <main+64>
   0x080491f6 <+32>:	mov    0x4(%eax),%eax
   0x080491f9 <+35>:	mov    (%eax),%eax
   0x080491fb <+37>:	sub    $0x8,%esp
   0x080491fe <+40>:	push   %eax
   0x080491ff <+41>:	push   $0x804a008
   0x08049204 <+46>:	call   0x8049050 <printf@plt>
   0x08049209 <+51>:	add    $0x10,%esp
   0x0804920c <+54>:	sub    $0xc,%esp
   0x0804920f <+57>:	push   $0xffffffff
   0x08049211 <+59>:	call   0x8049090 <exit@plt>
   0x08049216 <+64>:	mov    0x4(%eax),%eax
   0x08049219 <+67>:	add    $0x4,%eax
   0x0804921c <+70>:	mov    (%eax),%eax
   0x0804921e <+72>:	sub    $0xc,%esp
   0x08049221 <+75>:	push   %eax
   0x08049222 <+76>:	call   0x80490b0 <atoi@plt>
   0x08049227 <+81>:	add    $0x10,%esp
   0x0804922a <+84>:	cmp    %eax,-0xc(%ebp)
   0x0804922d <+87>:	jne    0x804925a <main+132>
   0x0804922f <+89>:	call   0x8049060 <geteuid@plt>
   0x08049234 <+94>:	mov    %eax,%ebx
   0x08049236 <+96>:	call   0x8049060 <geteuid@plt>
   0x0804923b <+101>:	sub    $0x8,%esp
   0x0804923e <+104>:	push   %ebx
   0x0804923f <+105>:	push   %eax
   0x08049240 <+106>:	call   0x80490a0 <setreuid@plt>
   0x08049245 <+111>:	add    $0x10,%esp
   0x08049248 <+114>:	sub    $0xc,%esp
   0x0804924b <+117>:	push   $0x804a022
   0x08049250 <+122>:	call   0x8049080 <system@plt>
   0x08049255 <+127>:	add    $0x10,%esp
   0x08049258 <+130>:	jmp    0x804926a <main+148>
   0x0804925a <+132>:	sub    $0xc,%esp
   0x0804925d <+135>:	push   $0x804a02a
   0x08049262 <+140>:	call   0x8049070 <puts@plt>
   0x08049267 <+145>:	add    $0x10,%esp
   0x0804926a <+148>:	mov    $0x0,%eax
   0x0804926f <+153>:	lea    -0x8(%ebp),%esp
   0x08049272 <+156>:	pop    %ecx
   0x08049273 <+157>:	pop    %ebx
   0x08049274 <+158>:	pop    %ebp
   0x08049275 <+159>:	lea    -0x4(%ecx),%esp
   0x08049278 <+162>:	ret
End of assembler dump.
(gdb) break *0x0804922a
Breakpoint 1 at 0x804922a
(gdb) run
Starting program: /home/leviathan6/leviathan6 0000
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, 0x0804922a in main ()
(gdb) info registers
eax            0x0                 0
ecx            0x0                 0
edx            0xffffd77e          -10370
ebx            0xf7e2a000          -136142848
esp            0xffffd530          0xffffd530
ebp            0xffffd548          0xffffd548
esi            0xffffd614          -10732
edi            0xf7ffcb80          -134231168
eip            0x804922a           0x804922a <main+84>
eflags         0x286               [ PF SF IF ]
cs             0x23                35
ss             0x2b                43
ds             0x2b                43
es             0x2b                43
fs             0x0                 0
gs             0x63                99
k0             0x0                 0
k1             0x0                 0
k2             0x0                 0
k3             0x0                 0
k4             0x0                 0
k5             0x0                 0
k6             0x0                 0
k7             0x0                 0
(gdb) print $ebp-0xc
$1 = (void *) 0xffffd53c
(gdb) x 0xffffd53c
0xffffd53c:	0x00001bd3
(gdb) print/d 0x00001bd3
$2 = 7123
```

Essential:

```
   0x0804922a <+84>:	cmp    %eax,-0xc(%ebp)
   0x0804922d <+87>:	jne    0x804925a <main+132>
```

Thus, print the address `%eax` is compared to:

```
(gdb) print $ebp-0xc
$1 = (void *) 0xffffd53c
```

Examine the memory there:

```
(gdb) x 0xffffd53c
0xffffd53c:	0x00001bd3
```

Print the number as decimal:

```
(gdb) print/d 0x00001bd3
$2 = 7123
```

Finally:

```
leviathan6@gibson:~$ ls
leviathan6
leviathan6@gibson:~$ ./leviathan6 7123
$ whoami
leviathan7
$ cat /etc/leviathan_pass/leviathan7
8GpZ5f8Hze
```

## Level 7

```
leviathan7@gibson:~$ ls
CONGRATULATIONS
leviathan7@gibson:~$ cat CONGRATULATIONS
Well Done, you seem to have used a *nix system before, now try something more serious.
(Please don't post writeups, solutions or spoilers about the games on the web. Thank you!)
```

Ooops...
