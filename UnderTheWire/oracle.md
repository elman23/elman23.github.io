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

## Oracle 3 -> 4

### Task

The password for `oracle4` is the date that the system logs were last wiped as depicted in the event logs on the desktop.

NOTE:
– The format for the password is 2 digit month, 2 digit day, 4 digit year. Ex: 5 Jan 2015 would be 01/05/2015.

▼ HINT:
https://msdn.microsoft.com/en-us/powershell/reference/5.1/microsoft.powershell.diagnostics/get-winevent

### Solution

```
PS C:\users\Oracle3\desktop> Get-Childitem


    Directory: C:\users\Oracle3\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   5:52 AM        1118208 Oracle3_Security.evtx


PS C:\users\Oracle3\desktop> Get-WinEvent -Path '.\Oracle3_Security.evtx'


   ProviderName: Microsoft-Windows-Security-Auditing

TimeCreated                     Id LevelDisplayName Message
-----------                     -- ---------------- -------
5/18/2017 11:38:23 PM         4624 Information      An account was successfully logged on....
5/18/2017 11:38:23 PM         4672 Information      Special privileges assigned to new logon....
5/18/2017 11:38:23 PM         4634 Information      An account was logged off....
5/18/2017 11:37:38 PM         4624 Information      An account was successfully logged on....
5/18/2017 11:37:38 PM         4776 Information      The computer attempted to validate the credentials for an account....
5/18/2017 11:37:32 PM         4624 Information      An account was successfully logged on....
5/18/2017 11:37:32 PM         4672 Information      Special privileges assigned to new logon....
5/18/2017 11:37:32 PM         4634 Information      An account was logged off....
5/18/2017 11:37:31 PM         4624 Information      An account was successfully logged on....
5/18/2017 11:37:31 PM         4776 Information      The computer attempted to validate the credentials for an account....
5/18/2017 11:37:31 PM         4624 Information      An account was successfully logged on....
5/18/2017 11:37:31 PM         4776 Information      The computer attempted to validate the credentials for an account....
5/18/2017 11:37:31 PM         4634 Information      An account was logged off....
5/18/2017 11:37:31 PM         4624 Information      An account was successfully logged on....
5/18/2017 11:37:31 PM         4672 Information      Special privileges assigned to new logon....
5/18/2017 11:37:26 PM         4688 Information      A new process has been created....
5/18/2017 11:37:26 PM         4670 Information      Permissions on an object were changed....
5/18/2017 11:37:26 PM         4670 Information      Permissions on an object were changed....
5/18/2017 11:37:26 PM         4670 Information      Permissions on an object were changed....
5/18/2017 11:37:26 PM         4688 Information      A new process has been created....
5/18/2017 11:37:26 PM         4688 Information      A new process has been created....
5/18/2017 11:37:26 PM         4673 Information      A privileged service was called....
5/18/2017 11:37:26 PM         4611 Information      A trusted logon process has been registered with the Local Security Authority....
5/18/2017 11:37:25 PM         4673 Information      A privileged service was called....
5/18/2017 11:37:25 PM         4611 Information      A trusted logon process has been registered with the Local Security Authority....
5/18/2017 11:37:25 PM         4688 Information      A new process has been created....
5/18/2017 11:37:23 PM         4688 Information      A new process has been created....
5/18/2017 11:37:21 PM         4688 Information      A new process has been created....
5/18/2017 11:37:21 PM         4688 Information      A new process has been created....
5/18/2017 11:37:21 PM         4670 Information      Permissions on an object were changed....
5/18/2017 11:37:21 PM         4985 Information      The state of a transaction has changed....
5/18/2017 11:37:21 PM         4985 Information      The state of a transaction has changed....
5/18/2017 11:37:13 PM         4985 Information      The state of a transaction has changed....
5/18/2017 11:37:13 PM         4985 Information      The state of a transaction has changed....
5/18/2017 11:36:53 PM         4688 Information      A new process has been created....
5/18/2017 11:36:50 PM         4688 Information      A new process has been created....
5/18/2017 11:36:50 PM         4670 Information      Permissions on an object were changed....
5/18/2017 11:36:50 PM         4985 Information      The state of a transaction has changed....
5/18/2017 11:36:50 PM         4985 Information      The state of a transaction has changed....
5/18/2017 11:36:46 PM         4688 Information      A new process has been created....
5/18/2017 11:36:46 PM         4670 Information      Permissions on an object were changed....
5/18/2017 11:36:46 PM         4670 Information      Permissions on an object were changed....
5/18/2017 11:36:44 PM         4985 Information      The state of a transaction has changed....
5/18/2017 11:36:44 PM         4673 Information      A privileged service was called....
5/18/2017 11:36:44 PM         4688 Information      A new process has been created....
5/18/2017 11:36:44 PM         4688 Information      A new process has been created....
5/18/2017 11:36:44 PM         4985 Information      The state of a transaction has changed....
5/18/2017 11:36:43 PM         4688 Information      A new process has been created....
5/18/2017 11:36:43 PM         4985 Information      The state of a transaction has changed....
5/18/2017 11:36:43 PM         4634 Information      An account was logged off....
5/18/2017 11:36:43 PM         4634 Information      An account was logged off....
5/18/2017 11:36:43 PM         4624 Information      An account was successfully logged on....
5/18/2017 11:36:43 PM         4672 Information      Special privileges assigned to new logon....
5/18/2017 11:36:43 PM         4688 Information      A new process has been created....
5/18/2017 11:36:43 PM         4985 Information      The state of a transaction has changed....
5/18/2017 11:36:43 PM         4985 Information      The state of a transaction has changed....
5/18/2017 11:36:43 PM         4688 Information      A new process has been created....
5/18/2017 11:36:43 PM         4673 Information      A privileged service was called....
5/18/2017 11:36:43 PM         4688 Information      A new process has been created....
5/18/2017 11:36:43 PM         4985 Information      The state of a transaction has changed....
5/18/2017 11:36:43 PM         4673 Information      A privileged service was called....
5/18/2017 11:36:41 PM         4688 Information      A new process has been created....
5/18/2017 11:36:41 PM         4688 Information      A new process has been created....
5/18/2017 11:36:41 PM         4670 Information      Permissions on an object were changed....
5/18/2017 11:36:41 PM         4672 Information      Special privileges assigned to new logon....
5/18/2017 11:36:41 PM         4624 Information      An account was successfully logged on....
5/18/2017 11:36:41 PM         4670 Information      Permissions on an object were changed....
5/18/2017 11:36:41 PM         4673 Information      A privileged service was called....
5/18/2017 11:36:41 PM         4688 Information      A new process has been created....
5/18/2017 11:36:41 PM         4670 Information      Permissions on an object were changed....
5/18/2017 11:36:41 PM         4688 Information      A new process has been created....
5/18/2017 11:36:41 PM         4688 Information      A new process has been created....
5/18/2017 11:36:41 PM         4688 Information      A new process has been created....
5/18/2017 11:36:41 PM         4688 Information      A new process has been created....
5/18/2017 11:36:41 PM         4688 Information      A new process has been created....
5/18/2017 11:36:41 PM         4688 Information      A new process has been created....
5/18/2017 11:36:41 PM         4688 Information      A new process has been created....
5/18/2017 11:36:41 PM         4688 Information      A new process has been created....
5/18/2017 11:36:41 PM         4670 Information      Permissions on an object were changed....
5/18/2017 11:36:41 PM         4672 Information      Special privileges assigned to new logon....
5/18/2017 11:36:41 PM         4624 Information      An account was successfully logged on....
5/18/2017 11:36:41 PM         4688 Information      A new process has been created....
5/18/2017 11:36:41 PM         4670 Information      Permissions on an object were changed....
5/18/2017 11:36:41 PM         4688 Information      A new process has been created....
5/18/2017 11:36:41 PM         4688 Information      A new process has been created....
5/18/2017 11:36:40 PM         4688 Information      A new process has been created....
5/18/2017 11:36:40 PM         4688 Information      A new process has been created....
5/18/2017 11:36:40 PM         4688 Information      A new process has been created....
5/18/2017 11:36:40 PM         4670 Information      Permissions on an object were changed....
5/18/2017 11:36:40 PM         4985 Information      The state of a transaction has changed....
5/18/2017 11:36:40 PM         4985 Information      The state of a transaction has changed....
5/18/2017 11:36:40 PM         4985 Information      The state of a transaction has changed....
5/18/2017 11:36:40 PM         4634 Information      An account was logged off....
5/18/2017 11:36:40 PM         4634 Information      An account was logged off....
5/18/2017 11:36:40 PM         4634 Information      An account was logged off....
5/18/2017 11:36:40 PM         4624 Information      An account was successfully logged on....
5/18/2017 11:36:40 PM         4672 Information      Special privileges assigned to new logon....
5/18/2017 11:36:40 PM         4648 Information      A logon was attempted using explicit credentials....
5/18/2017 11:36:40 PM         4624 Information      An account was successfully logged on....
5/18/2017 11:36:40 PM         4672 Information      Special privileges assigned to new logon....
5/18/2017 11:36:40 PM         4634 Information      An account was logged off....
5/18/2017 11:36:40 PM         4634 Information      An account was logged off....
5/18/2017 11:36:40 PM         4624 Information      An account was successfully logged on....
5/18/2017 11:36:40 PM         4672 Information      Special privileges assigned to new logon....
5/18/2017 11:36:40 PM         4648 Information      A logon was attempted using explicit credentials....
5/18/2017 11:36:40 PM         4624 Information      An account was successfully logged on....
5/18/2017 11:36:40 PM         4672 Information      Special privileges assigned to new logon....
5/18/2017 11:36:40 PM         4624 Information      An account was successfully logged on....
5/18/2017 11:36:40 PM         4672 Information      Special privileges assigned to new logon....
5/18/2017 11:36:40 PM         4985 Information      The state of a transaction has changed....
5/18/2017 11:36:40 PM         4985 Information      The state of a transaction has changed....
5/18/2017 11:36:40 PM         4985 Information      The state of a transaction has changed....
5/18/2017 11:36:40 PM         4985 Information      The state of a transaction has changed....
5/18/2017 11:36:40 PM         4985 Information      The state of a transaction has changed....
5/18/2017 11:36:39 PM         4673 Information      A privileged service was called....
5/18/2017 11:36:39 PM         4985 Information      The state of a transaction has changed....
5/18/2017 11:36:39 PM         4673 Information      A privileged service was called....
5/18/2017 11:36:39 PM         4688 Information      A new process has been created....
5/18/2017 11:36:39 PM         4670 Information      Permissions on an object were changed....
5/18/2017 11:36:39 PM         4688 Information      A new process has been created....
5/18/2017 11:36:39 PM         4985 Information      The state of a transaction has changed....
5/18/2017 11:36:39 PM         4673 Information      A privileged service was called....
5/18/2017 11:36:39 PM         4688 Information      A new process has been created....
5/18/2017 11:36:39 PM         4688 Information      A new process has been created....
5/18/2017 11:36:39 PM         4985 Information      The state of a transaction has changed....
5/18/2017 11:36:39 PM         4985 Information      The state of a transaction has changed....
5/18/2017 11:36:39 PM         4985 Information      The state of a transaction has changed....
5/18/2017 11:36:39 PM         4985 Information      The state of a transaction has changed....
5/18/2017 11:36:39 PM         4688 Information      A new process has been created....
5/18/2017 11:36:39 PM         4670 Information      Permissions on an object were changed....
5/18/2017 11:36:39 PM         4688 Information      A new process has been created....
5/18/2017 11:36:39 PM         4670 Information      Permissions on an object were changed....
5/18/2017 11:36:39 PM         4688 Information      A new process has been created....
5/18/2017 11:36:39 PM         4688 Information      A new process has been created....
5/18/2017 11:36:39 PM         4688 Information      A new process has been created....
5/18/2017 11:36:39 PM         4688 Information      A new process has been created....
5/18/2017 11:36:39 PM         4688 Information      A new process has been created....
5/18/2017 11:36:39 PM         4688 Information      A new process has been created....
5/18/2017 11:36:38 PM         4616 Information      The system time was changed....
5/18/2017 11:36:38 PM         4616 Information      The system time was changed....
5/9/2017 11:36:38 PM          4624 Information      An account was successfully logged on....
5/9/2017 11:36:38 PM          4672 Information      Special privileges assigned to new logon....
5/9/2017 11:36:32 PM          4688 Information      A new process has been created....
5/9/2017 11:36:32 PM          4673 Information      A privileged service was called....
5/9/2017 11:36:32 PM          4611 Information      A trusted logon process has been registered with the Local Security Authority....
5/9/2017 11:36:32 PM          4634 Information      An account was logged off....
5/9/2017 11:36:32 PM          4624 Information      An account was successfully logged on....
5/9/2017 11:36:32 PM          4672 Information      Special privileges assigned to new logon....
5/9/2017 11:36:30 PM          4673 Information      A privileged service was called....
5/9/2017 11:36:30 PM          4673 Information      A privileged service was called....
5/9/2017 11:36:30 PM          4611 Information      A trusted logon process has been registered with the Local Security Authority....
5/9/2017 11:36:30 PM          4688 Information      A new process has been created....
5/9/2017 11:36:28 PM          4688 Information      A new process has been created....
5/9/2017 11:36:28 PM          4688 Information      A new process has been created....


   ProviderName: Microsoft-Windows-Eventlog

TimeCreated                     Id LevelDisplayName Message
-----------                     -- ---------------- -------
5/9/2017 11:36:05 PM          1102 Information      The audit log was cleared....


   ProviderName: Microsoft-Windows-Security-Auditing

TimeCreated                     Id LevelDisplayName Message
-----------                     -- ---------------- -------
5/9/2017 11:36:04 PM          4634 Information      An account was logged off....
5/9/2017 11:36:04 PM          4624 Information      An account was successfully logged on....
5/9/2017 11:36:04 PM          4672 Information      Special privileges assigned to new logon....
5/9/2017 11:36:04 PM          4688 Information      A new process has been created....
5/9/2017 11:36:04 PM          4670 Information      Permissions on an object were changed....
5/9/2017 11:36:04 PM          4670 Information      Permissions on an object were changed....
5/9/2017 11:36:04 PM          4670 Information      Permissions on an object were changed....
5/9/2017 11:36:04 PM          4688 Information      A new process has been created....
```

Candidate: `oracle4:05/09/2017`.

## Oracle 4 -> 5

### Task

The password for `oracle5` is the name of the GPO that was last created PLUS the name of the file on the user’s desktop.

NOTE:
– If the GPO name is `blob` and the file on the desktop is named `1234`, the password would be `blob1234`.
– The password will be lowercase no matter how it appears on the screen.

▼ HINT:
Good thing there is a module with cmdlets that can help with this…

### Solution

First thing, the file in `desktop`:

```
PS C:\users\Oracle4\desktop> Get-ChildItem


    Directory: C:\users\Oracle4\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:49 AM              0 83
```

Looking around in the Web, one finds that GPO means Group Policy Object.

There seem to be a GPO module for PowerShell: https://learn.microsoft.com/en-us/powershell/module/grouppolicy/?view=windowsserver2022-ps.

A useful resource: https://www.linkedin.com/pulse/use-powershell-find-all-gpos-updated-last-x-hours-james-sargent.

```
PS C:\users\Oracle4\desktop> Import-Module GroupPolicy
PS C:\users\Oracle4\desktop> $varHours = 48
PS C:\users\Oracle4\desktop> Get-GPO -All | Where {((Get-Date)-[datetime]$_.ModificationTime).Hours -lt $varHours}


DisplayName      : Default Domain Policy
DomainName       : underthewire.tech
Owner            : underthewire\Domain Admins
Id               : 31b2f340-016d-11d2-945f-00c04fb984f9
GpoStatus        : AllSettingsEnabled
Description      :
CreationTime     : 8/30/2018 2:51:10 AM
ModificationTime : 8/30/2018 10:45:42 AM
UserVersion      : AD Version: 0, SysVol Version: 0
ComputerVersion  : AD Version: 4, SysVol Version: 4
WmiFilter        :

DisplayName      : Charlie
DomainName       : underthewire.tech
Owner            : underthewire\Domain Admins
Id               : 44080cf1-1053-467d-b000-2ea3f27dbbfa
GpoStatus        : AllSettingsEnabled
Description      : I_am_Groot
CreationTime     : 11/20/2018 12:18:09 AM
ModificationTime : 11/20/2018 12:18:08 AM
UserVersion      : AD Version: 0, SysVol Version: 0
ComputerVersion  : AD Version: 0, SysVol Version: 0
WmiFilter        :

DisplayName      : Alpha
DomainName       : underthewire.tech
Owner            : underthewire\Domain Admins
Id               : 49401c32-4145-463f-b5e7-816926d4f78d
GpoStatus        : AllSettingsEnabled
Description      : Are you there?
CreationTime     : 1/13/2019 9:40:20 PM
ModificationTime : 1/13/2019 9:40:20 PM
UserVersion      : AD Version: 0, SysVol Version: 0
ComputerVersion  : AD Version: 0, SysVol Version: 0
WmiFilter        :

DisplayName      : Echo
DomainName       : underthewire.tech
Owner            : underthewire\Domain Admins
Id               : 5d91f4cf-3487-40ec-99ed-d219371c0a7c
GpoStatus        : AllSettingsEnabled
Description      : Phone Home
CreationTime     : 8/30/2018 10:49:44 AM
ModificationTime : 8/30/2018 10:49:44 AM
UserVersion      : AD Version: 0, SysVol Version: 0
ComputerVersion  : AD Version: 0, SysVol Version: 0
WmiFilter        :

DisplayName      : Default Domain Controllers Policy
DomainName       : underthewire.tech
Owner            : underthewire\Domain Admins
Id               : 6ac1786c-016f-11d2-945f-00c04fb984f9
GpoStatus        : AllSettingsEnabled
Description      :
CreationTime     : 8/30/2018 2:51:10 AM
ModificationTime : 12/9/2018 8:25:40 PM
UserVersion      : AD Version: 0, SysVol Version: 0
ComputerVersion  : AD Version: 9, SysVol Version: 9
WmiFilter        :

DisplayName      : Default
DomainName       : underthewire.tech
Owner            : underthewire\Domain Admins
Id               : ecb4a7c0-b4e1-41b1-9e89-161cfa679999
GpoStatus        : AllSettingsEnabled
Description      :
CreationTime     : 8/30/2018 3:07:39 AM
ModificationTime : 8/30/2018 3:07:40 AM
UserVersion      : AD Version: 1, SysVol Version: 1
ComputerVersion  : AD Version: 1, SysVol Version: 1
WmiFilter        :

DisplayName      : Delta
DomainName       : underthewire.tech
Owner            : underthewire\Domain Admins
Id               : fc6f3bf4-9239-4308-9956-a9d0d9569505
GpoStatus        : AllSettingsEnabled
Description      : I_am
CreationTime     : 8/30/2018 10:49:44 AM
ModificationTime : 8/30/2018 10:49:44 AM
UserVersion      : AD Version: 0, SysVol Version: 0
ComputerVersion  : AD Version: 0, SysVol Version: 0
WmiFilter        :
```

`oracle5:alpha83`

## Oracle 5 -> 6

### Task

The password for `oracle6` is the name of the GPO that contains a description of `I_AM_GROOT` PLUS the name of the file on the user’s desktop.

NOTE:
– If you are using SSH, you MUST do a Help on the cmdlet needed to solve this. For example, if the cmdlet is `get-something` type `help get-something` first, this will make the cmdlet available for you to use. This is a bug in the SSH software used.
– If the GPO description is `blob` and the file on the desktop is named `1234`, the password would be `blob1234`.
– The password will be lowercase no matter how it appears on the screen.

▼ HINT:
https://learn.microsoft.com/en-us/powershell/module/activedirectory/?view=windowsserver2016-ps

### Solution

```
PS C:\users\Oracle4\desktop> Import-Module GroupPolicy
```

```
PS C:\users\Oracle5\desktop> Help Get-GPO

NAME
    Get-GPO

SYNOPSIS
    Gets one GPO or all the GPOs in a domain.


SYNTAX
    Get-GPO [-Guid] <Guid> [[-Domain] <String>] [[-Server] <String>] [-All] [<CommonParameters>]

    Get-GPO [[-Domain] <String>] [[-Server] <String>] [-All] [<CommonParameters>]

    Get-GPO [-Name] <String> [[-Domain] <String>] [[-Server] <String>] [-All] [<CommonParameters>]


DESCRIPTION
    The Get-GPO cmdlet gets one Group Policy Object (GPO) or all the GPOs in a domain. You can specify a GPO by its display name or by its globally unique identifier (GUID) to get a single
    GPO, or you can get all the GPOs in the domain through the All parameter.

    This cmdlet returns one or more objects that represent the requested GPOs. By default, properties of the requested GPOs are printed to the display; however, you can also pipe the output
    of the Get-GPO cmdlet to other Group Policy cmdlets.


RELATED LINKS
    Online Version:
    Backup-GPO
    Copy-GPO
    Import-GPO
    New-GPO
    Remove-GPO
    Rename-GPO
    Restore-GPO

REMARKS
    To see the examples, type: "get-help Get-GPO -examples".
    For more information, type: "get-help Get-GPO -detailed".
    For technical information, type: "get-help Get-GPO -full".
    For online help, type: "get-help Get-GPO -online"
```

```
PS C:\users\Oracle5\desktop> Get-GPO -All


DisplayName      : Default Domain Policy
DomainName       : underthewire.tech
Owner            : underthewire\Domain Admins
Id               : 31b2f340-016d-11d2-945f-00c04fb984f9
GpoStatus        : AllSettingsEnabled
Description      :
CreationTime     : 8/30/2018 2:51:10 AM
ModificationTime : 8/30/2018 10:45:42 AM
UserVersion      : AD Version: 0, SysVol Version: 0
ComputerVersion  : AD Version: 4, SysVol Version: 4
WmiFilter        :

DisplayName      : Charlie
DomainName       : underthewire.tech
Owner            : underthewire\Domain Admins
Id               : 44080cf1-1053-467d-b000-2ea3f27dbbfa
GpoStatus        : AllSettingsEnabled
Description      : I_am_Groot
CreationTime     : 11/20/2018 12:18:09 AM
ModificationTime : 11/20/2018 12:18:08 AM
UserVersion      : AD Version: 0, SysVol Version: 0
ComputerVersion  : AD Version: 0, SysVol Version: 0
WmiFilter        :

DisplayName      : Alpha
DomainName       : underthewire.tech
Owner            : underthewire\Domain Admins
Id               : 49401c32-4145-463f-b5e7-816926d4f78d
GpoStatus        : AllSettingsEnabled
Description      : Are you there?
CreationTime     : 1/13/2019 9:40:20 PM
ModificationTime : 1/13/2019 9:40:20 PM
UserVersion      : AD Version: 0, SysVol Version: 0
ComputerVersion  : AD Version: 0, SysVol Version: 0
WmiFilter        :

DisplayName      : Echo
DomainName       : underthewire.tech
Owner            : underthewire\Domain Admins
Id               : 5d91f4cf-3487-40ec-99ed-d219371c0a7c
GpoStatus        : AllSettingsEnabled
Description      : Phone Home
CreationTime     : 8/30/2018 10:49:44 AM
ModificationTime : 8/30/2018 10:49:44 AM
UserVersion      : AD Version: 0, SysVol Version: 0
ComputerVersion  : AD Version: 0, SysVol Version: 0
WmiFilter        :

DisplayName      : Default Domain Controllers Policy
DomainName       : underthewire.tech
Owner            : underthewire\Domain Admins
Id               : 6ac1786c-016f-11d2-945f-00c04fb984f9
GpoStatus        : AllSettingsEnabled
Description      :
CreationTime     : 8/30/2018 2:51:10 AM
ModificationTime : 12/9/2018 8:25:40 PM
UserVersion      : AD Version: 0, SysVol Version: 0
ComputerVersion  : AD Version: 9, SysVol Version: 9
WmiFilter        :

DisplayName      : Default
DomainName       : underthewire.tech
Owner            : underthewire\Domain Admins
Id               : ecb4a7c0-b4e1-41b1-9e89-161cfa679999
GpoStatus        : AllSettingsEnabled
Description      :
CreationTime     : 8/30/2018 3:07:39 AM
ModificationTime : 8/30/2018 3:07:40 AM
UserVersion      : AD Version: 1, SysVol Version: 1
ComputerVersion  : AD Version: 1, SysVol Version: 1
WmiFilter        :

DisplayName      : Delta
DomainName       : underthewire.tech
Owner            : underthewire\Domain Admins
Id               : fc6f3bf4-9239-4308-9956-a9d0d9569505
GpoStatus        : AllSettingsEnabled
Description      : I_am
CreationTime     : 8/30/2018 10:49:44 AM
ModificationTime : 8/30/2018 10:49:44 AM
UserVersion      : AD Version: 0, SysVol Version: 0
ComputerVersion  : AD Version: 0, SysVol Version: 0
WmiFilter        :
```

```
PS C:\users\Oracle5\desktop> Get-ChildItem


    Directory: C:\users\Oracle5\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:50 AM              0 1337
```

`oracle6:charlie1337`

## Oracle 6 -> 7

### Task

The password for `oracle7` is the name of the OU that doesn’t have a GPO linked to it PLUS the name of the file on the user’s desktop.
NOTE:
– The password will be lowercase no matter how it appears on the screen.
– Exclude the `Groups` OU.

▼ HINT:
You may find you want to look in Group Policy however, maybe Active Directory is a better choice...

### Solution

First of all, OU stands for Organizational Unit.

[Here](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adorganizationalunit?view=windowsserver2022-ps) we find: `Get-ADOrganizationalUnit`. Let's give it a try.

```
PS C:\users\Oracle6\desktop> Get-ADOrganizationalUnit -Filter 'Name -like "*"' | Format-Table Name, LinkedGroupPolicyObjects

Name               LinkedGroupPolicyObjects
----               ------------------------
Domain Controllers {CN={6AC1786C-016F-11D2-945F-00C04fB984F9},CN=Policies,CN=System,DC=underthewire,DC=tech}
Games              {cn={49401C32-4145-463F-B5E7-816926D4F78D},cn=policies,cn=system,DC=underthewire,DC=tech}
X-Wing             {cn={49401C32-4145-463F-B5E7-816926D4F78D},cn=policies,cn=system,DC=underthewire,DC=tech}
T-65               {cn={49401C32-4145-463F-B5E7-816926D4F78D},cn=policies,cn=system,DC=underthewire,DC=tech}
T-70               {cn={49401C32-4145-463F-B5E7-816926D4F78D},cn=policies,cn=system,DC=underthewire,DC=tech}
T-85               {cn={49401C32-4145-463F-B5E7-816926D4F78D},cn=policies,cn=system,DC=underthewire,DC=tech}
T-15               {cn={49401C32-4145-463F-B5E7-816926D4F78D},cn=policies,cn=system,DC=underthewire,DC=tech}
T-25               {cn={49401C32-4145-463F-B5E7-816926D4F78D},cn=policies,cn=system,DC=underthewire,DC=tech}
T-35               {cn={49401C32-4145-463F-B5E7-816926D4F78D},cn=policies,cn=system,DC=underthewire,DC=tech}
T-40               {cn={49401C32-4145-463F-B5E7-816926D4F78D},cn=policies,cn=system,DC=underthewire,DC=tech}
T-50               {}
T-60               {cn={49401C32-4145-463F-B5E7-816926D4F78D},cn=policies,cn=system,DC=underthewire,DC=tech}
T-75               {cn={49401C32-4145-463F-B5E7-816926D4F78D},cn=policies,cn=system,DC=underthewire,DC=tech}
T-80               {cn={49401C32-4145-463F-B5E7-816926D4F78D},cn=policies,cn=system,DC=underthewire,DC=tech}
Groups             {}
```

```
PS C:\users\Oracle6\desktop> Get-ChildItem


    Directory: C:\users\Oracle6\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:50 AM              0 _97
```

Therefore: `oracle7:t-50_97`.

## Oracle 7 -> 8

### Task

The password for `oracle8` is the name of the domain that a trust is built with PLUS the name of the file on the user’s desktop.
NOTE:
– The password will be lowercase no matter how it appears on the screen.
– If the name of the trust is `blob` and the file on the desktop is named `1234`, the password would be `blob1234`.

### Solution

```
PS C:\users\Oracle7\desktop> Get-ChildItem


    Directory: C:\users\Oracle7\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:50 AM              0 111
```

Give a look [here](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adtrust?view=windowsserver2022-ps).

```
PS C:\users\Oracle7\desktop> Get-ADTrust -Filter *


Direction               : Outbound
DisallowTransivity      : True
DistinguishedName       : CN=multiverse,CN=System,DC=underthewire,DC=tech
ForestTransitive        : False
IntraForest             : False
IsTreeParent            : False
IsTreeRoot              : False
Name                    : multiverse
ObjectClass             : trustedDomain
ObjectGUID              : bbfcc0ca-e586-4058-9aef-c6b4a6b32708
SelectiveAuthentication : False
SIDFilteringForestAware : False
SIDFilteringQuarantined : False
Source                  : DC=underthewire,DC=tech
Target                  : multiverse
TGTDelegation           : False
TrustAttributes         : 1
TrustedPolicy           :
TrustingPolicy          :
TrustType               : MIT
UplevelOnly             : False
UsesAESKeys             : False
UsesRC4Encryption       : False
```

`oracle8:multiverse111`

## Oracle 8 -> 9

### Task

The password for `oracle9` is the name of the file in the GET Request from `www.guardian.galaxy.com` within the log file on the desktop.

NOTE:
– Don’t include the extension.
– The password will be lowercase no matter how it appears on the screen.

### Solution

```
PS C:\users\Oracle8\desktop> Get-ChildItem


    Directory: C:\users\Oracle8\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   5:52 AM         405295 logs.txt
```

```
PS C:\users\Oracle8\desktop> Get-Content .\logs.txt | Select-String -Pattern 'guardian.galaxy'

guardian.galaxy.com - - [28/Jul/1995:13:03:55 -0400] "GET /images/star-lord.gif HTTP/1.0" 200 786
```

`oracle9:star-lord`

## Oracle 9 -> 10

### Task

The password for `oracle10` is the computer name of the DNS record of the mail server listed in the `UnderTheWire.tech` zone PLUS the name of the file on the user’s desktop.

NOTE:
– If the server name is `some_blob` and the file on the desktop is named `1234`, the password would be `some_blob1234`.
– Only submit the computer name and not the fully qualified domain name.
– The password will be lowercase no matter how it appears on the screen.

### Solution

```
PS C:\users\Oracle9\desktop> Get-ChildItem


    Directory: C:\users\Oracle9\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:51 AM              0 9229
```

```
PS C:\users\Oracle9\desktop> Get-DnsServerResourceRecord -ZoneName underthewire.tech -RRType Mx

HostName                  RecordType Type       Timestamp            TimeToLive      RecordData
--------                  ---------- ----       ---------            ----------      ----------
utw_exch                  MX         15         0                    01:00:00        [10][mail.utw_exch.]
```

`oracle10:utw_exch9229`

## Oracle 10 -> 11

### Task

The password for `oracle11` is the `.biz` site the user has previously navigated to.
NOTE:
– Don’t include the extension.
– The password will be lowercase no matter how it appears on the screen.

▼ HINT:
The registry is awesome!

### Solution

```
PS C:\users\Oracle10\desktop> Get-Item 'HKCU:\Software\Microsoft\Internet Explorer\TypedURLs'


    Hive: HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer


Name                           Property
----                           --------
TypedURLs                      url1 : http://go.microsoft.com/fwlink/p/?LinkId=255141
                               url2 : http://google.com
                               url3 : http://underthewire.tech
                               url4 : http://bimmerfest.com
                               url5 : http://nba.com
                               url6 : http://yondu.biz
                               url7 : http://hardknocks.edu
                               url8 : http://installation.org                                 AAAA   NoRecords
```

`oracle11:yondu`

## Oracle 11 -> 12

### Task

The password for `oracle12` is the drive letter associated with the mapped drive that this user has.

NOTE:
– Submission should be one letter and lowercase.

▼ HINT:
The registry is awesome!

### Solution

```
PS C:\users\Oracle11\desktop> Get-ChildItem 'HKCU:\Network'


    Hive: HKEY_CURRENT_USER\Network


Name                           Property
----                           --------
M                              RemotePath     : \\127.0.0.1\WsusContent
                               UserName       : 0
                               ProviderName   : Microsoft Windows Network
                               ProviderType   : 131072
                               ConnectionType : 1
                               DeferFlags     : 4
```

`oracle12:m`

## Oracle 12 -> 13

### Task

The password for `oracle13` is the IP of the system that this user has previously established a remote desktop with.

▼ HINT:
The registry is awesome!

### Solution

```
PS C:\users\oracle12\desktop> Get-ChildItem 'HKCU:\Software\Microsoft\Terminal Server Client'


    Hive: HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client


Name                           Property
----                           --------
192.168.2.3                    UsernameHint : MyServer\raccoon
```

`oracle13:192.168.2.3`

## Oracle 13 -> 14

### Task

The password for `oracle14` is the name of the user who created the Galaxy security group as depicted in the event logs on the desktop PLUS the name of the text file on the user’s desktop.

NOTE:
– If the user’s name is `randy` and the file on the desktop is named `1234`, the password would be `randy1234`.
– The password will be lowercase no matter how it appears on the screen.

▼ HINT:
https://msdn.microsoft.com/en-us/powershell/reference/5.1/microsoft.powershell.diagnostics/get-winevent

### Solution

```
PS C:\users\Oracle13\desktop> Get-ChildItem


    Directory: C:\users\Oracle13\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:51 AM              0 88
-a----        8/30/2018   5:52 AM        2166784 security.evtx
```

```
PS C:\users\Oracle13\desktop> Get-WinEvent -Path '.\security.evtx' | Where-Object -Property Message -Match 'Galaxy'


   ProviderName: Microsoft-Windows-Security-Auditing

TimeCreated                     Id LevelDisplayName Message
-----------                     -- ---------------- -------
5/19/2017 1:19:28 AM          4728 Information      A member was added to a security-enabled global group....
5/19/2017 1:19:28 AM          4737 Information      A security-enabled global group was changed....
5/19/2017 1:18:26 AM          4727 Information      A security-enabled global group was created....
```

```
PS C:\users\Oracle13\desktop> Get-WinEvent -Path .\security.evtx | Where-Object -Property Message -Match 'Galaxy' | Format-List


TimeCreated  : 5/19/2017 1:19:28 AM
ProviderName : Microsoft-Windows-Security-Auditing
Id           : 4728
Message      : A member was added to a security-enabled global group.

               Subject:
                Security ID:            S-1-5-21-2268727836-2773903800-2952248001-1622
                Account Name:           nebula
                Account Domain:         UNDERTHEWIRE
                Logon ID:               0xBD8CC7

               Member:
                Security ID:            S-1-5-21-2268727836-2773903800-2952248001-1623
                Account Name:           CN=Bereet,OU=Morag,DC=UNDERTHEWIRE,DC=TECH

               Group:
                Security ID:            S-1-5-21-2268727836-2773903800-2952248001-1626
                Group Name:             Galaxy
                Group Domain:           UNDERTHEWIRE

               Additional Information:
                Privileges:             -

TimeCreated  : 5/19/2017 1:19:28 AM
ProviderName : Microsoft-Windows-Security-Auditing
Id           : 4737
Message      : A security-enabled global group was changed.

               Subject:
                Security ID:            S-1-5-21-2268727836-2773903800-2952248001-1622
                Account Name:           nebula
                Account Domain:         UNDERTHEWIRE
                Logon ID:               0xBD8CC7

               Group:
                Security ID:            S-1-5-21-2268727836-2773903800-2952248001-1626
                Group Name:             Galaxy
                Group Domain:           UNDERTHEWIRE

               Changed Attributes:
                SAM Account Name:       -
                SID History:            -

               Additional Information:
                Privileges:             -

TimeCreated  : 5/19/2017 1:18:26 AM
ProviderName : Microsoft-Windows-Security-Auditing
Id           : 4727
Message      : A security-enabled global group was created.

               Subject:
                Security ID:            S-1-5-21-2268727836-2773903800-2952248001-1621
                Account Name:           gamora
                Account Domain:         UNDERTHEWIRE
                Logon ID:               0xBC24FF

               New Group:
                Security ID:            S-1-5-21-2268727836-2773903800-2952248001-1626
                Group Name:             Galaxy
                Group Domain:           UNDERTHEWIRE

               Attributes:
                SAM Account Name:       Galaxy
                SID History:            -

               Additional Information:
                Privileges:             -
```

`oracle14:gamora88`

## Oracle 14 -> 15

### Task

The password for `oracle15` is the name of the user who added the user `Bereet` to the `Galaxy` security group as depicted in the event logs on the desktop PLUS the name of the text file on the user’s desktop.

NOTE:
– If the script name is `randy` and the file on the desktop is named `1234`, the password would be `randy1234`.
– The password will be lowercase no matter how it appears on the screen.
▼ HINT:

https://msdn.microsoft.com/en-us/powershell/reference/5.1/microsoft.powershell.diagnostics/get-winevent

### Solution

```
PS C:\users\Oracle14\desktop> Get-ChildItem


    Directory: C:\users\Oracle14\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:51 AM              0 2112
-a----        8/30/2018   5:52 AM        2166784 security.evtx


PS C:\users\Oracle14\desktop> Get-WinEvent -Path '.\security.evtx' | Where-Object -Property Message -Match 'Galaxy'


   ProviderName: Microsoft-Windows-Security-Auditing

TimeCreated                     Id LevelDisplayName Message
-----------                     -- ---------------- -------
5/19/2017 1:19:28 AM          4728 Information      A member was added to a security-enabled global group....
5/19/2017 1:19:28 AM          4737 Information      A security-enabled global group was changed....
5/19/2017 1:18:26 AM          4727 Information      A security-enabled global group was created....
```

Then:

```
PS C:\users\Oracle14\desktop> Get-WinEvent -Path .\security.evtx | Where-Object -Property Message -Match 'Galaxy' | Format-List


TimeCreated  : 5/19/2017 1:19:28 AM
ProviderName : Microsoft-Windows-Security-Auditing
Id           : 4728
Message      : A member was added to a security-enabled global group.

               Subject:
                Security ID:            S-1-5-21-2268727836-2773903800-2952248001-1622
                Account Name:           nebula
                Account Domain:         UNDERTHEWIRE
                Logon ID:               0xBD8CC7

               Member:
                Security ID:            S-1-5-21-2268727836-2773903800-2952248001-1623
                Account Name:           CN=Bereet,OU=Morag,DC=UNDERTHEWIRE,DC=TECH

               Group:
                Security ID:            S-1-5-21-2268727836-2773903800-2952248001-1626
                Group Name:             Galaxy
                Group Domain:           UNDERTHEWIRE

               Additional Information:
                Privileges:             -

TimeCreated  : 5/19/2017 1:19:28 AM
ProviderName : Microsoft-Windows-Security-Auditing
Id           : 4737
Message      : A security-enabled global group was changed.

               Subject:
                Security ID:            S-1-5-21-2268727836-2773903800-2952248001-1622
                Account Name:           nebula
                Account Domain:         UNDERTHEWIRE
                Logon ID:               0xBD8CC7

               Group:
                Security ID:            S-1-5-21-2268727836-2773903800-2952248001-1626
                Group Name:             Galaxy
                Group Domain:           UNDERTHEWIRE

               Changed Attributes:
                SAM Account Name:       -
                SID History:            -

               Additional Information:
                Privileges:             -

TimeCreated  : 5/19/2017 1:18:26 AM
ProviderName : Microsoft-Windows-Security-Auditing
Id           : 4727
Message      : A security-enabled global group was created.

               Subject:
                Security ID:            S-1-5-21-2268727836-2773903800-2952248001-1621
                Account Name:           gamora
                Account Domain:         UNDERTHEWIRE
                Logon ID:               0xBC24FF

               New Group:
                Security ID:            S-1-5-21-2268727836-2773903800-2952248001-1626
                Group Name:             Galaxy
                Group Domain:           UNDERTHEWIRE

               Attributes:
                SAM Account Name:       Galaxy
                SID History:            -

               Additional Information:
                Privileges:             -
```

Thus:

```
Get-WinEvent -Path .\security.evtx | Where-Object -Property Message -Match 'Bereet' | Format-List


TimeCreated  : 5/19/2017 1:19:28 AM
ProviderName : Microsoft-Windows-Security-Auditing
Id           : 4728
Message      : A member was added to a security-enabled global group.

               Subject:
                Security ID:            S-1-5-21-2268727836-2773903800-2952248001-1622
                Account Name:           nebula
                Account Domain:         UNDERTHEWIRE
                Logon ID:               0xBD8CC7

               Member:
                Security ID:            S-1-5-21-2268727836-2773903800-2952248001-1623
                Account Name:           CN=Bereet,OU=Morag,DC=UNDERTHEWIRE,DC=TECH

               Group:
                Security ID:            S-1-5-21-2268727836-2773903800-2952248001-1626
                Group Name:             Galaxy
                Group Domain:           UNDERTHEWIRE

               Additional Information:
                Privileges:             -
```

`oracle15:nebula2112`

## Oracle 15

Congratulations!

You have successfully made it to the end!

Try your luck with other games brought to you by the Under The Wire team.

Thanks for playing!
