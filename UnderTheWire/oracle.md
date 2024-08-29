# Oracle

https://underthewire.tech/oracle

## Oracle 0 -> 1

### Task

The goal of this level is to log into the game. Do the following in order to achieve this goal.

1. Obtain the initial credentials via the `#StartHere` channel on our Slack ([link](https://communityinviter.com/apps/underthewire/under-the-wire)). Once you are in the channel, scroll to the top to see the credentials.

2. After obtaining the credentials, connect to the server via SSH. You will need an SSH client such as Putty. The host that you will be connecting to is `oracle.underthewire.tech`, on port `22`.

3. When prompted, use the credentials for the applicable game found in the `#StartHere` Slack channel.

4. You have successfully connected to the game server when your path changes to `PS C:\Users\Oracle1\desktop>`.

### Solution

The username is `oracle1`, the password is the same as the username.

You can guess that after some games from UnderTheWire and from the directory `C:\Users\Oracle1\desktop>`, which one could expect to be owned by `Oracle1`.

Credentials: `oracle1:oracle1`.

## Oracle 1 -> 2

### Task

The password for `oracle2` is the timezone in which this system is set to.

NOTE:
– The password is the abbreviation of the timezone. For example, if it is listed as being in the Eastern timezone, the answer is `est`.
– The password will be lowercase no matter how it appears on the screen.

IMPORTANT:
Once you feel you have completed the `Oracle1` challenge, start a new connection to the server, and log in with the username of `Oracle2` and this password will be the answer from `Oracle1`. If successful, close out the `Oracle1` connection and begin to solve the `Oracle2` challenge. This concept is repeated over and over until you reach the end of the game.

▼ HINT:

https://docs.microsoft.com/en-us/powershell/scripting/samples/working-with-registry-keys?view=powershell-7.1

### Solution

```
PS C:\users\Oracle1\desktop> Get-TimeZone


Id                         : UTC
DisplayName                : (UTC) Coordinated Universal Time
StandardName               : Coordinated Universal Time
DaylightName               : Coordinated Universal Time
BaseUtcOffset              : 00:00:00
SupportsDaylightSavingTime : False
```

Credentials: `oracle2:utc`.

## Oracle 2 -> 3

### Task

The password for `oracle3` is the last five digits of the MD5 hash, from the hashes of files on the desktop that appears twice.

NOTE:
– The password will be lowercase no matter how it appears on the screen.

▼ HINT:

After getting the hashes of all the files on the desktop, there will be two hashes that are the same, submit the last 5 digits of them.

▼ HINT:

A way to do this is to do one command and pipe it to another...

### Solution

Great resource I happened to use once: [here](https://4sysops.com/archives/find-and-remove-duplicate-files-with-powershell/).

```
PS C:\users\Oracle2\desktop> Get-ChildItem | Get-FileHash -Algorithm MD5 | Group -Property Has
h | Where {$_.Count -gt 1} | ForEach {$_.Group | Select Hash}

Hash
----
5BE11FF0037EED156F77213658C2F5C4
5BE11FF0037EED156F77213658C2F5C4
```

Credentials: `oracle3:2f5c4`.
