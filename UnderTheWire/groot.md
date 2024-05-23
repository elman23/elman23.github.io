# Groot

## Groot 0 -> 1

The goal of this level is to log into the game. Do the following in order to achieve this goal.

1. Obtain the initial credentials via the **#StartHere** channel on our Slack. Once you are in the channel, scroll to the top to see the credentials.

2. After obtaining the credentials, connect to the server via SSH. You will need an SSH client such as Putty. The host that you will be connecting to is `groot.underthewire.tech`, on port 22.

3. When prompted, use the credentials for the applicable game found in the **#StartHere** Slack channel.

4. You have successfully connected to the game server when your path changes to `PS C:\Users\Groot1\desktop>`.

---

`groot1:groot1`

## Groot 1 -> 2

The password for `groot2` is the last five alphanumeric characters of the MD5 hash of this system’s hosts file.

**NOTE**: The password will be lowercase no matter how it appears on the screen.

**IMPORTANT**:
Once you feel you have completed the `groot1` challenge, start a new connection to the server, and log in with the username of `groot2` and this password will be the answer from `groot1`. If successful, close out the `groot1` connection and begin to solve the `groot2` challenge. This concept is repeated over and over until you reach the end of the game.

---

```powershell
Get-FileHash <filepath> -Algorithm MD5
```

The hosts file in Windows is:

```
C:\Windows\System32\drivers\etc\hosts
```

```powershell
PS C:\users\Groot1\desktop> Get-FileHash C:\Windows\System32\drivers\etc\hosts -
Algorithm MD5

Algorithm       Hash
---------       ----
MD5             6EEC08310BD5328FFC8FB72CD8E464C3
```

Therefore:

```
groot2:464c3
```

## Groot 2 -> 3

The password for groot3 is the word that is made up from the letters in the range of 1,481,110 to 1,481,117 within the file on the desktop.

NOTE:
– The password will be lowercase no matter how it appears on the screen.

▼HINT:

Seems like a great time to explore using ranges within PowerShell...

---

```
PS C:\users\Groot2\desktop> ls


    Directory: C:\users\Groot2\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   5:52 AM        2357268 elements.txt


PS C:\users\Groot2\desktop> $content = get-content .\elements.txt
PS C:\users\Groot2\desktop> $content[1481110..1481117]

h
i
d
i
n
g
```

`groot3:hiding`

## Groot 3 -> 4

The password for groot4 is the number of times the word “beetle” is listed in the file on the desktop.

---

[Here](https://stackoverflow.com/questions/29889495/count-specific-string-in-text-file-using-powershell) we find (where the word is `/export` and the file is `YourFile.txt`):

```
$FileContent = Get-Content "YourFile.txt"
$Matches = Select-String -InputObject $FileContent -Pattern "/export" -AllMatches
$Matches.Matches.Count
```

We adapt it to our case:

```
$FileContent = Get-Content "words.txt"
$Matches = Select-String -InputObject $FileContent -Pattern "beetle" -AllMatches
$Matches.Matches.Count
```

Thus:

```
PS C:\users\Groot3\desktop> ls


    Directory: C:\users\Groot3\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   5:52 AM        2357296 words.txt


PS C:\users\Groot3\desktop> $FileContent = Get-Content "words.txt"
PS C:\users\Groot3\desktop> $Matches = Select-String -InputObject $FileContent -Pattern "beetle" -AllMatches
PS C:\users\Groot3\desktop> $Matches.Matches.Count
5
```

## Groot 4 -> 5

The password for groot5 is the name of the Drax subkey within the HKEY_CURRENT_USER (HKCU) registry hive.

NOTE:
– The password will be lowercase no matter how it appears on the screen.

---

```
PS C:\users\Groot4\desktop> Get-ChildItem -Path HKCU:\ -Recurse | Select-String Drax

HKEY_CURRENT_USER\Software\Microsoft\Assistance\Drax
HKEY_CURRENT_USER\Software\Microsoft\Assistance\Drax\destroyer
```

## Groot 5 -> 6

The password for groot6 is the name of the workstation that the user with a username of “baby.groot” can log into as depicted in Active Directory PLUS the name of the file on the desktop

NOTE:
– If the workstation is “system1” and the file on the desktop is named “\_log”, the password would be “system1_log”.
– The password will be lowercase no matter how it appears on the screen.

---

```
PS C:\users\Groot5\desktop> ls


    Directory: C:\users\Groot5\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        9/20/2020   3:38 PM              0 _enterprise


PS C:\users\Groot5\desktop> Get-ADUser baby.groot -Properties *


AccountExpirationDate                :
accountExpires                       : 9223372036854775807
AccountLockoutTime                   :
AccountNotDelegated                  : False
AllowReversiblePasswordEncryption    : False
AuthenticationPolicy                 : {}
AuthenticationPolicySilo             : {}
BadLogonCount                        : 0
badPasswordTime                      : 0
badPwdCount                          : 0
CannotChangePassword                 : False
CanonicalName                        : underthewire.tech/X-Wing/T-65/Groot
Certificates                         : {}
City                                 :
CN                                   : Groot
codePage                             : 0
Company                              :
CompoundIdentitySupported            : {}
Country                              :
countryCode                          : 0
Created                              : 8/30/2018 3:28:43 AM
createTimeStamp                      : 8/30/2018 3:28:43 AM
Deleted                              :
Department                           :
Description                          :
DisplayName                          : Groot
DistinguishedName                    : CN=Groot \ ,OU=T-65,OU=X-Wing,DC=underthewire,DC=tech
Division                             :
DoesNotRequirePreAuth                : False
dSCorePropagationData                : {1/1/1601 12:00:00 AM}
EmailAddress                         : baby.groot@underthewire.tech
EmployeeID                           :
EmployeeNumber                       :
Enabled                              : False
Fax                                  :
GivenName                            : Baby
HomeDirectory                        :
HomedirRequired                      : False
HomeDrive                            :
HomePage                             :
HomePhone                            :
Initials                             :
instanceType                         : 4
isDeleted                            :
KerberosEncryptionType               : {}
LastBadPasswordAttempt               :
LastKnownParent                      :
lastLogoff                           : 0
lastLogon                            : 0
LastLogonDate                        :
LockedOut                            : False
logonCount                           : 0
LogonWorkstations                    : wk11
mail                                 : baby.groot@underthewire.tech
Manager                              :
MemberOf                             : {}
MNSLogonAccount                      : False
MobilePhone                          :
Modified                             : 8/30/2018 10:51:10 AM
modifyTimeStamp                      : 8/30/2018 10:51:10 AM
msDS-User-Account-Control-Computed   : 8388608
Name                                 : Groot
nTSecurityDescriptor                 : System.DirectoryServices.ActiveDirectorySecurity
ObjectCategory                       : CN=Person,CN=Schema,CN=Configuration,DC=underthewire,DC=tech
ObjectClass                          : user
ObjectGUID                           : c938286d-f672-45b7-97ee-b371f0e39836
objectSid                            : S-1-5-21-758131494-606461608-3556270690-2175
Office                               :
OfficePhone                          :
Organization                         :
OtherName                            :
PasswordExpired                      : True
PasswordLastSet                      :
PasswordNeverExpires                 : False
PasswordNotRequired                  : False
POBox                                :
PostalCode                           :
PrimaryGroup                         : CN=Domain Users,CN=Users,DC=underthewire,DC=tech
primaryGroupID                       : 513
PrincipalsAllowedToDelegateToAccount : {}
ProfilePath                          :
ProtectedFromAccidentalDeletion      : False
pwdLastSet                           : 0
SamAccountName                       : baby.groot
sAMAccountType                       : 805306368
ScriptPath                           :
sDRightsEffective                    : 0
ServicePrincipalNames                : {}
SID                                  : S-1-5-21-758131494-606461608-3556270690-2175
SIDHistory                           : {}
SmartcardLogonRequired               : False
sn                                   : Groot
State                                :
StreetAddress                        :
Surname                              : Groot
Title                                :
TrustedForDelegation                 : False
TrustedToAuthForDelegation           : False
UseDESKeyOnly                        : False
userAccountControl                   : 514
userCertificate                      : {}
UserPrincipalName                    : baby.groot
userWorkstations                     : wk11
uSNChanged                           : 20021
uSNCreated                           : 19663
whenChanged                          : 8/30/2018 10:51:10 AM
whenCreated                          : 8/30/2018 3:28:43 AM
```

Shortly:

```
PS C:\users\Groot5\desktop> (Get-ADUser baby.groot -Properties *).userWorkstations
wk11
PS C:\users\Groot5\desktop> ls


    Directory: C:\users\Groot5\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        9/20/2020   3:38 PM              0 _enterprise


```

## Groot 6 -> 7

The password for groot7 is the name of the program that is set to start when this user logs in PLUS the name of the file on the desktop.

NOTE:
– Omit the executable extension.
– If the program is “mspaint” and the file on the desktop is named “\_log”, the password would be “mspaint_log”.
– The password will be lowercase no matter how it appears on the screen.

▼ HINT :

https://blog.cylance.com/windows-registry-persistence-part-2-the-run-keys-and-search-order

---

```
PS C:\users\Groot6\desktop> Get-WmiObject Win32_StartupCommand | Select-Object Name, command, Location, User  | Format-List


Name     : New Value #1
command  :
Location : HKU\S-1-5-21-758131494-606461608-3556270690-1169\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
User     : underthewire\Groot6

Name     : New Value #2
command  :
Location : HKU\S-1-5-21-758131494-606461608-3556270690-1169\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
User     : underthewire\Groot6

Name     : New Value #3
command  :
Location : HKU\S-1-5-21-758131494-606461608-3556270690-1169\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
User     : underthewire\Groot6

Name     : New Value #4
command  :
Location : HKU\S-1-5-21-758131494-606461608-3556270690-1169\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
User     : underthewire\Groot6

Name     : star-lord
command  : C:\star-lord.exe
Location : HKU\S-1-5-21-758131494-606461608-3556270690-1169\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
User     : underthewire\Groot6



PS C:\users\Groot6\desktop> ls


    Directory: C:\users\Groot6\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/21/2020   1:24 PM              0 _rules


```

`groot7:star-lord_rules`

## Groot 7 -> 8

The password for groot8 is the name of the dll, as depicted in the registry, associated with the “applockerfltr” service PLUS the name of the file on the desktop.

NOTE:
– The password will be lowercase no matter how it appears on the screen.
– If the name of the dll is “abc.dll” and the file on the desktop is named “\_1234”, the password would be “abc_1234”.

---

```
PS C:\users\Groot7\desktop> get-service applockerfltr | select -property *


Name                : applockerfltr
RequiredServices    : {AppIDSvc, AppID, FltMgr}
CanPauseAndContinue : False
CanShutdown         : False
CanStop             : False
DisplayName         : Smartlocker Filter Driver
DependentServices   : {}
MachineName         : .
ServiceName         : applockerfltr
ServicesDependedOn  : {AppIDSvc, AppID, FltMgr}
ServiceHandle       :
Status              : Stopped
ServiceType         : KernelDriver
StartType           : Manual
Site                :
Container           :



PS C:\users\Groot7\desktop> Get-Item HKLM:\SYSTEM\CurrentControlSet\Services\applockerfltr


    Hive: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services


Name                           Property
----                           --------
applockerfltr                  DisplayName     : @%systemroot%\system32\srpapi.dll,-102
                               ErrorControl    : 1
                               ImagePath       : system32\drivers\applockerfltr.sys
                               Start           : 3
                               Type            : 1
                               Description     : @%systemroot%\system32\srpapi.dll,-103
                               DependOnService : {FltMgr, AppID, AppIDSvc}


PS C:\users\Groot7\desktop> ls


    Directory: C:\users\Groot7\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        5/31/2021   5:13 PM              0 _home


```

`groot8:srpapi_home`
