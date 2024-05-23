# Groot

## Groot 0 -> 1

The goal of this level is to log into the game. Do the following in order to achieve this goal.

1. Obtain the initial credentials via the **#StartHere** channel on our Slack. Once you are in the channel, scroll to the top to see the credentials.

2. After obtaining the credentials, connect to the server via SSH. You will need an SSH client such as Putty. The host that you will be connecting to is `groot.underthewire.tech`, on port 22.

3. When prompted, use the credentials for the applicable game found in the **#StartHere** Slack channel.

4. You have successfully connected to the game server when your path changes to `PS C:\Users\Groot1\desktop>`.

---

Following the procedure, we end up with the credentials `groot1:groot1`.

## Groot 1 -> 2

The password for `groot2` is the last five alphanumeric characters of the MD5 hash of this system’s hosts file.

**NOTE**: The password will be lowercase no matter how it appears on the screen.

**IMPORTANT**:
Once you feel you have completed the `groot1` challenge, start a new connection to the server, and log in with the username of `groot2` and this password will be the answer from `groot1`. If successful, close out the `groot1` connection and begin to solve the `groot2` challenge. This concept is repeated over and over until you reach the end of the game.

---

We can get the hash of a file with the commandlet `Get-FileHash`. We specify the filepath after the command and `-Algorithm` as `MD5`. The syntax is:

```powershell
Get-FileHash <filepath> -Algorithm MD5
```

The hosts file in Windows is:

```
C:\Windows\System32\drivers\etc\hosts
```

Thus:

```powershell
PS C:\users\Groot1\desktop> Get-FileHash C:\Windows\System32\drivers\etc\hosts -Algorithm MD5

Algorithm       Hash
---------       ----
MD5             6EEC08310BD5328FFC8FB72CD8E464C3
```

Therefore we get the credentials: `groot2:464c3`.

## Groot 2 -> 3

The password for `groot3` is the word that is made up from the letters in the range of 1,481,110 to 1,481,117 within the file on the desktop.

**NOTE**:
– The password will be lowercase no matter how it appears on the screen.

**HINT**:
Seems like a great time to explore using ranges within PowerShell...

---

Start by listing the files in the `desktop` folder:

```
PS C:\users\Groot2\desktop> ls


    Directory: C:\users\Groot2\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   5:52 AM        2357268 elements.txt
```

Now we get the content of the file `elements.txt` and we save it to a variable named `$content`; then, we list the specified indexes with the bracket syntax; it goes as follows:

```
PS C:\users\Groot2\desktop> $content = get-content .\elements.txt
PS C:\users\Groot2\desktop> $content[1481110..1481117]

h
i
d
i
n
g
```

Thus: `groot3:hiding`.

## Groot 3 -> 4

The password for `groot4` is the number of times the word `"beetle"` is listed in the file on the desktop.

---

[Here](https://stackoverflow.com/questions/29889495/count-specific-string-in-text-file-using-powershell) we find a useful hint (where the word is `/export` and the file is `YourFile.txt`):

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

Hence: `groot4:5`.

## Groot 4 -> 5

The password for `groot5` is the name of the `Drax` subkey within the `HKEY_CURRENT_USER` (`HKCU`) registry hive.

**NOTE**:
– The password will be lowercase no matter how it appears on the screen.

---

We use `Get-ChildItem`:

```
PS C:\users\Groot4\desktop> Get-ChildItem -Path HKCU:\ -Recurse | Select-String Drax

HKEY_CURRENT_USER\Software\Microsoft\Assistance\Drax
HKEY_CURRENT_USER\Software\Microsoft\Assistance\Drax\destroyer
...
```

Therefore: `groot5:destroyer`.

## Groot 5 -> 6

The password for `groot6` is the name of the workstation that the user with a username of `"baby.groot"` can log into as depicted in Active Directory PLUS the name of the file on the desktop.

**NOTE**:
– If the workstation is `"system1"` and the file on the desktop is named `"\_log"`, the password would be `"system1_log"`.
– The password will be lowercase no matter how it appears on the screen.

---

List the files in `desktop`:

```
PS C:\users\Groot5\desktop> ls


    Directory: C:\users\Groot5\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        9/20/2020   3:38 PM              0 _enterprise
```

Then we use `Get-ADUser` specifying `-Properties *`:

```
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

Shortly, since the property we are interested in is `userWorkstations`:

```
PS C:\users\Groot5\desktop> (Get-ADUser baby.groot -Properties *).userWorkstations
wk11
```

Thus: `groot6:wk11_enterprise`.

## Groot 6 -> 7

The password for `groot7` is the name of the program that is set to start when this user logs in PLUS the name of the file on the desktop.

**NOTE**:
– Omit the executable extension.
– If the program is `"mspaint"` and the file on the desktop is named `"_log"`, the password would be `"mspaint_log"`.
– The password will be lowercase no matter how it appears on the screen.

**HINT**:
https://blog.cylance.com/windows-registry-persistence-part-2-the-run-keys-and-search-order

---

The commandlet `Get-WmiObject` gives us some information about the services:

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
```

Now we can list the files in `desktop`:

```
PS C:\users\Groot6\desktop> ls


    Directory: C:\users\Groot6\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/21/2020   1:24 PM              0 _rules
```

The credentials for the next level are hence: `groot7:star-lord_rules`.

## Groot 7 -> 8

The password for `groot8` is the name of the DLL, as depicted in the registry, associated with the `"applockerfltr"` service PLUS the name of the file on the desktop.

**NOTE**:
– The password will be lowercase no matter how it appears on the screen.
– If the name of the dll is `"abc.dll"` and the file on the desktop is named `"_1234"`, the password would be `"abc_1234"`.

---

We first try with `Get-Service`:

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
```

It doesn't seem that useful. Try with `Get-Item`:

```
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
```

The file in `desktop` is:

```
PS C:\users\Groot7\desktop> ls


    Directory: C:\users\Groot7\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        5/31/2021   5:13 PM              0 _home
```

Therefore, the credentials: `groot8:srpapi_home`.

## Groot 8 -> 9

The password for `groot9` is the description of the firewall rule blocking MySQL PLUS the name of the file on the desktop.

**NOTE**:
– If the description of the rule is `"blue"` and the file on the desktop is named `"_bob"`, the password would be `"blue_bob"`.
– The password will be lowercase no matter how it appears on the screen.

---

The base is to use the commandlet `Get-NetFirewallRule`.

```
PS C:\users\Groot8\desktop> Get-NetFirewallRule -Action Block -Enabled True -Direction Outbound


Name                  : {0149D9BD-51BD-412E-BCD2-57E943981745}
DisplayName           : Block TCP 389 CLDAP - OVH
Description           :
DisplayGroup          :
Group                 :
Enabled               : True
Profile               : Any
Platform              : {}
Direction             : Outbound
Action                : Block
EdgeTraversalPolicy   : Block
LooseSourceMapping    : False
LocalOnlyMapping      : False
Owner                 :
PrimaryStatus         : OK
Status                : The rule was parsed successfully from the store. (65536)
EnforcementStatus     : NotApplicable
PolicyStoreSource     : PersistentStore
PolicyStoreSourceType : Local

Name                  : {ABB9FC80-F9F5-4FE0-A22D-DA88F84CF51D}
DisplayName           : Block UDP 389 CLDAP - OVH
Description           :
DisplayGroup          :
Group                 :
Enabled               : True
Profile               : Any
Platform              : {}
Direction             : Outbound
Action                : Block
EdgeTraversalPolicy   : Block
LooseSourceMapping    : False
LocalOnlyMapping      : False
Owner                 :
PrimaryStatus         : OK
Status                : The rule was parsed successfully from the store. (65536)
EnforcementStatus     : NotApplicable
PolicyStoreSource     : PersistentStore
PolicyStoreSourceType : Local



PS C:\users\Groot8\desktop> Get-NetFirewallRule -Action Block -Enabled True -Direction Inbound


Name                  : FPS-SMB-In-TCP
DisplayName           : File and Printer Sharing (SMB-In)
Description           : Inbound rule for File and Printer Sharing to allow Server Message Block
                        transmission and reception via Named Pipes. [TCP 445]
DisplayGroup          : File and Printer Sharing
Group                 : @FirewallAPI.dll,-28502
Enabled               : True
Profile               : Domain, Private, Public
Platform              : {}
Direction             : Inbound
Action                : Block
EdgeTraversalPolicy   : Block
LooseSourceMapping    : False
LocalOnlyMapping      : False
Owner                 :
PrimaryStatus         : OK
Status                : The rule was parsed successfully from the store. (65536)
EnforcementStatus     : NotApplicable
PolicyStoreSource     : PersistentStore
PolicyStoreSourceType : Local

Name                  : {8ce6b97d-5c1d-4347-a7fd-1792feb42355}
DisplayName           : MySQL
Description           : call_me
DisplayGroup          :
Group                 :
Enabled               : True
Profile               : Any
Platform              : {}
Direction             : Inbound
Action                : Block
EdgeTraversalPolicy   : Block
LooseSourceMapping    : False
LocalOnlyMapping      : False
Owner                 :
PrimaryStatus         : OK
Status                : The rule was parsed successfully from the store. (65536)
EnforcementStatus     : NotApplicable
PolicyStoreSource     : PersistentStore
PolicyStoreSourceType : Local

Name                  : {9D3BF213-672F-4928-BDD9-55ABA0A87780}
DisplayName           : Bad User Block (SSH)
Description           :
DisplayGroup          :
Group                 :
Enabled               : True
Profile               : Any
Platform              : {}
Direction             : Inbound
Action                : Block
EdgeTraversalPolicy   : Block
LooseSourceMapping    : False
LocalOnlyMapping      : False
Owner                 :
PrimaryStatus         : OK
Status                : The rule was parsed successfully from the store. (65536)
EnforcementStatus     : NotApplicable
PolicyStoreSource     : PersistentStore
PolicyStoreSourceType : Local

Name                  : {F8722F04-C14A-4D66-BAE7-B5E7C95C8188}
DisplayName           : Block TCP 389 CLDAP - OVH
Description           :
DisplayGroup          :
Group                 :
Enabled               : True
Profile               : Any
Platform              : {}
Direction             : Inbound
Action                : Block
EdgeTraversalPolicy   : Block
LooseSourceMapping    : False
LocalOnlyMapping      : False
Owner                 :
PrimaryStatus         : OK
Status                : The rule was parsed successfully from the store. (65536)
EnforcementStatus     : NotApplicable
PolicyStoreSource     : PersistentStore
PolicyStoreSourceType : Local

Name                  : {ACAE0DCD-7B5A-4FD0-B79A-BBED72049335}
DisplayName           : Block UDP 389 CLDAP - OVH
Description           :
DisplayGroup          :
Group                 :
Enabled               : True
Profile               : Any
Platform              : {}
Direction             : Inbound
Action                : Block
EdgeTraversalPolicy   : Block
LooseSourceMapping    : False
LocalOnlyMapping      : False
Owner                 :
PrimaryStatus         : OK
Status                : The rule was parsed successfully from the store. (65536)
EnforcementStatus     : NotApplicable
PolicyStoreSource     : PersistentStore
PolicyStoreSourceType : Local

Name                  : {71CBE4A5-A8F5-4B73-841C-B288C6E32199}
DisplayName           : Bad User Block (All communication)
Description           :
DisplayGroup          :
Group                 :
Enabled               : True
Profile               : Any
Platform              : {}
Direction             : Inbound
Action                : Block
EdgeTraversalPolicy   : Block
LooseSourceMapping    : False
LocalOnlyMapping      : False
Owner                 :
PrimaryStatus         : OK
Status                : The rule was parsed successfully from the store. (65536)
EnforcementStatus     : NotApplicable
PolicyStoreSource     : PersistentStore
PolicyStoreSourceType : Local
```

Moreover, get tie file name:

```
PS C:\users\Groot8\desktop> ls


    Directory: C:\users\Groot8\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:51 AM              0 _starlord
```

Credentials for the next level: `groot9:call_me_starlord`.

## Groot 9 -> 10

The password for `groot10` is the name of the OU that doesn’t have accidental deletion protection enabled PLUS the name of the file on the desktop.

**NOTE**:
– If the name of the OU is called `"blue"` and the file on the desktop is named `"_bob"`, the password would be `"blue_bob"`.
– The password will be lowercase no matter how it appears on the screen.

---

For those who may not know, an OU is an OrganizationalUnit in Active Directory.

The commandlet: `Get-ADOrganizationalUnit`.

The basic usage is the following (`-Filter` is mandatory):

```
PS C:\users\Groot9\desktop> Get-ADOrganizationalUnit -Filter *


City                     :
Country                  :
DistinguishedName        : OU=Domain Controllers,DC=underthewire,DC=tech
LinkedGroupPolicyObjects : {CN={6AC1786C-016F-11D2-945F-00C04fB984F9},CN=Policies,CN=System,DC=underthewi
                           re,DC=tech}
ManagedBy                :
Name                     : Domain Controllers
ObjectClass              : organizationalUnit
ObjectGUID               : 8d2b6653-bcbc-49fa-836a-2cacf5dec238
PostalCode               :
State                    :
StreetAddress            :

City                     :
Country                  :
DistinguishedName        : OU=Games,DC=underthewire,DC=tech
LinkedGroupPolicyObjects : {cn={49401C32-4145-463F-B5E7-816926D4F78D},cn=policies,cn=system,DC=underthewi
                           re,DC=tech}
ManagedBy                :
Name                     : Games
ObjectClass              : organizationalUnit
ObjectGUID               : ec46a25b-1ece-4044-86fb-b042c58956e6
PostalCode               :
State                    :
StreetAddress            :

City                     :
Country                  :
DistinguishedName        : OU=X-Wing,DC=underthewire,DC=tech
LinkedGroupPolicyObjects : {cn={49401C32-4145-463F-B5E7-816926D4F78D},cn=policies,cn=system,DC=underthewi
                           re,DC=tech}
ManagedBy                :
Name                     : X-Wing
ObjectClass              : organizationalUnit
ObjectGUID               : 845a64e6-447d-477b-bb82-2da49e35d5fd
PostalCode               :
State                    :
StreetAddress            :

City                     :
Country                  :
DistinguishedName        : OU=T-65,OU=X-Wing,DC=underthewire,DC=tech
LinkedGroupPolicyObjects : {cn={49401C32-4145-463F-B5E7-816926D4F78D},cn=policies,cn=system,DC=underthewi
                           re,DC=tech}
ManagedBy                :
Name                     : T-65
ObjectClass              : organizationalUnit
ObjectGUID               : f5d70e37-d26c-4d3d-b12f-70828d14399d
PostalCode               :
State                    :
StreetAddress            :

City                     :
Country                  :
DistinguishedName        : OU=T-70,OU=X-Wing,DC=underthewire,DC=tech
LinkedGroupPolicyObjects : {cn={49401C32-4145-463F-B5E7-816926D4F78D},cn=policies,cn=system,DC=underthewi
                           re,DC=tech}
ManagedBy                :
Name                     : T-70
ObjectClass              : organizationalUnit
ObjectGUID               : 6bb0dbca-fd1a-4399-95f1-eccec969e128
PostalCode               :
State                    :
StreetAddress            :

City                     :
Country                  :
DistinguishedName        : OU=T-85,OU=X-Wing,DC=underthewire,DC=tech
LinkedGroupPolicyObjects : {cn={49401C32-4145-463F-B5E7-816926D4F78D},cn=policies,cn=system,DC=underthewi
                           re,DC=tech}
ManagedBy                :
Name                     : T-85
ObjectClass              : organizationalUnit
ObjectGUID               : 8b097925-3cd7-4bc4-9299-ca58223ce439
PostalCode               :
State                    :
StreetAddress            :

City                     :
Country                  :
DistinguishedName        : OU=T-15,OU=X-Wing,DC=underthewire,DC=tech
LinkedGroupPolicyObjects : {cn={49401C32-4145-463F-B5E7-816926D4F78D},cn=policies,cn=system,DC=underthewi
                           re,DC=tech}
ManagedBy                :
Name                     : T-15
ObjectClass              : organizationalUnit
ObjectGUID               : 7d9b7bb9-6d95-4a65-b305-a76781be80ba
PostalCode               :
State                    :
StreetAddress            :

City                     :
Country                  :
DistinguishedName        : OU=T-25,OU=X-Wing,DC=underthewire,DC=tech
LinkedGroupPolicyObjects : {cn={49401C32-4145-463F-B5E7-816926D4F78D},cn=policies,cn=system,DC=underthewi
                           re,DC=tech}
ManagedBy                :
Name                     : T-25
ObjectClass              : organizationalUnit
ObjectGUID               : fc15c303-dd9a-4c44-a941-314cc6fdd394
PostalCode               :
State                    :
StreetAddress            :

City                     :
Country                  :
DistinguishedName        : OU=T-35,OU=X-Wing,DC=underthewire,DC=tech
LinkedGroupPolicyObjects : {cn={49401C32-4145-463F-B5E7-816926D4F78D},cn=policies,cn=system,DC=underthewi
                           re,DC=tech}
ManagedBy                :
Name                     : T-35
ObjectClass              : organizationalUnit
ObjectGUID               : f7581473-9e32-4659-a5af-2d2d0eb5d86d
PostalCode               :
State                    :
StreetAddress            :

City                     :
Country                  :
DistinguishedName        : OU=T-40,OU=X-Wing,DC=underthewire,DC=tech
LinkedGroupPolicyObjects : {cn={49401C32-4145-463F-B5E7-816926D4F78D},cn=policies,cn=system,DC=underthewi
                           re,DC=tech}
ManagedBy                :
Name                     : T-40
ObjectClass              : organizationalUnit
ObjectGUID               : eaf9473c-a7fd-41d0-9464-5684b5707242
PostalCode               :
State                    :
StreetAddress            :

City                     :
Country                  :
DistinguishedName        : OU=T-50,OU=X-Wing,DC=underthewire,DC=tech
LinkedGroupPolicyObjects : {}
ManagedBy                :
Name                     : T-50
ObjectClass              : organizationalUnit
ObjectGUID               : 5ace8bef-c00e-4f58-a543-3fd45436f1d4
PostalCode               :
State                    :
StreetAddress            :

City                     :
Country                  :
DistinguishedName        : OU=T-60,OU=X-Wing,DC=underthewire,DC=tech
LinkedGroupPolicyObjects : {cn={49401C32-4145-463F-B5E7-816926D4F78D},cn=policies,cn=system,DC=underthewi
                           re,DC=tech}
ManagedBy                :
Name                     : T-60
ObjectClass              : organizationalUnit
ObjectGUID               : 89c91b6a-6f3b-4811-95ac-051be76d368b
PostalCode               :
State                    :
StreetAddress            :

City                     :
Country                  :
DistinguishedName        : OU=T-75,OU=X-Wing,DC=underthewire,DC=tech
LinkedGroupPolicyObjects : {cn={49401C32-4145-463F-B5E7-816926D4F78D},cn=policies,cn=system,DC=underthewi
                           re,DC=tech}
ManagedBy                :
Name                     : T-75
ObjectClass              : organizationalUnit
ObjectGUID               : 91015ef3-039e-4ca6-a967-f953833bc8e3
PostalCode               :
State                    :
StreetAddress            :

City                     :
Country                  :
DistinguishedName        : OU=T-80,OU=X-Wing,DC=underthewire,DC=tech
LinkedGroupPolicyObjects : {cn={49401C32-4145-463F-B5E7-816926D4F78D},cn=policies,cn=system,DC=underthewi
                           re,DC=tech}
ManagedBy                :
Name                     : T-80
ObjectClass              : organizationalUnit
ObjectGUID               : 4b90b6fc-619f-481f-a153-528f90c2cc10
PostalCode               :
State                    :
StreetAddress            :

City                     :
Country                  :
DistinguishedName        : OU=Groups,DC=underthewire,DC=tech
LinkedGroupPolicyObjects : {}
ManagedBy                :
Name                     : Groups
ObjectClass              : organizationalUnit
ObjectGUID               : bf366f71-f291-43ca-8334-cdb18890e332
PostalCode               :
State                    :
StreetAddress            :



```

Usefil resource: https://theitbros.com/active-directory-organizational-unit-ou/.

```
PS C:\users\Groot9\desktop> Get-ADOrganizationalUnit -Properties ProtectedFromAccidentalDeletion -Filter *
 | Format-Table Name, ProtectedFromAccidentalDeletion

Name               ProtectedFromAccidentalDeletion
----               -------------------------------
Domain Controllers                            True
Games                                         True
X-Wing                                        True
T-65                                          True
T-70                                          True
T-85                                          True
T-15                                          True
T-25                                         False
T-35                                          True
T-40                                          True
T-50                                          True
T-60                                          True
T-75                                          True
T-80                                          True
Groups                                        True
```

Moreover:

```
PS C:\users\Groot9\desktop> ls


    Directory: C:\users\Groot9\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:51 AM              0 _tester
```

Thus: `groot10:t-25_tester`.

## Groot 10 -> 11

The password for `groot11` is the one word that makes the two files on the desktop different.

**NOTE**:
– The password will be lowercase no matter how it appears on the screen.

---

In Linux we can use `diff`... Let's give it a try:

```
PS C:\users\Groot10\desktop> ls


    Directory: C:\users\Groot10\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   5:52 AM          17324 new.txt
-a----        8/30/2018   5:52 AM          17313 old.txt


PS C:\users\Groot10\desktop> diff .\new.txt .\old.txt

InputObject SideIndicator
----------- -------------
.\old.txt   =>
.\new.txt   <=
```

Not working as expected... We find the commandlet `Compare-Object`:

```
PS C:\users\Groot10\desktop> Compare-Object (Get-Content new.txt) (Get-Content old.txt)

InputObject SideIndicator
----------- -------------
taserface   <=
```

Alternatively, we can use `diff`, but reading the files with `cat`!

```
PS C:\users\Groot10\desktop> diff (cat new.txt) (cat old.txt)

InputObject SideIndicator
----------- -------------
taserface   <=
```

## Groot 11 -> 12

The password for `groot12` is within an alternate data stream (ADS) somewhere on the desktop.

**NOTE**:
– The password will be lowercase no matter how it appears on the screen.

---

[Here](https://stackoverflow.com/questions/53380498/powershell-list-all-alternate-data-stream-information-from-one-directory) we find some information about Alternate Data Streams in Powershell.

```
PS C:\users\Groot11\desktop> $files = gci -recurse | % { gi $_.FullName -stream * } | where stream -ne ':$Data' | select filename,stream,@{'name'='identifier';"e"={"$($_.filename)$($_.stream)"}}
PS C:\users\Groot11\desktop> $files

FileName                                   Stream identifier
--------                                   ------ ----------
C:\users\Groot11\desktop\TPS_Reports04.pdf secret C:\users\Groot11\desktop\TPS_Reports04.pdfsecret
```

[Here](http://powershellcookbook.com/recipe/XilI/interact-with-alternate-data-streams) we find something interesting, too: we can specify the data stream after the file name, separating them with `:`, as follows:

```
Get-Content C:\users\Groot11\desktop\TPS_Reports04.pdf:secret
```

Hence:

```
PS C:\users\Groot11\desktop> Get-Content C:\users\Groot11\desktop\TPS_Reports04.pdf:secret
spaceships
```

Therefore: `groot13:spaceships`.

## Groot 12 -> 13

The password for `groot13` is the owner of the `Nine Realms` folder on the desktop.

**NOTE**:
– Exclude the `Administrator`, the `Administrators` group, and System.
– The password will be lowercase with no punctuation no matter how it appears on the screen. For example, if the owner is `"john.doe"`, it would be `"johndoe"`.

---

Simply list what is in `desktop`:

```
PS C:\users\Groot12\desktop> Get-ChildItem .


    Directory: C:\users\Groot12\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----        8/30/2018  10:51 AM                Nine Realms
```

Now `Get-Acl` comes to help:

```
PS C:\users\Groot12\desktop> Get-Acl '.\Nine Realms'


    Directory: C:\users\Groot12\desktop


Path        Owner                Access
----        -----                ------
Nine Realms underthewire\Airwolf NT AUTHORITY\SYSTEM Allow  FullControl...
```

The credentials: `groot13:airwolf`.

## Groot 13 -> 14

The password for `groot14` is the name of the Registered Owner of this system as depicted in the Registry PLUS the name of the file on the desktop.

**NOTE**:
– If the Registered Owner is `"Elroy"` and the file on the desktop is named `"_bob"`, the password would be `"elroy_bob"`.
– The password will be lowercase no matter how it appears on the screen.

---

We can find the desired information with `Get-ComputerInfo`:

```
PS C:\users\Groot13\desktop> Get-ComputerInfo | Select WindowsRegisteredOwner

WindowsRegisteredOwner
----------------------
UTW_Team


PS C:\users\Groot13\desktop> ls


    Directory: C:\users\Groot13\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:51 AM              0 _ned
```

The credentials are thus: `groot14:utw_team_ned`.

## Groot 14 -> 15

The password for `groot15` is the description of the share whose name contains `"task"` in it PLUS the name of the file on the desktop.

**NOTE**:
– If the description is `"frozen_pizza"` and the file on the desktop is named `"_sucks"`, the password would be `"frozen_pizza_sucks"`.
– The password will be lowercase no matter how it appears on the screen.

---

Use `Get-SmbShare`:

```
PS C:\users\Groot14\desktop> Get-SmbShare

Name           ScopeName Path Description
----           --------- ---- -----------
ADMIN$         *              Remote Admin
C$             *              Default share
IPC$           *              Remote IPC
NETLOGON       *              Logon server share
shoretroopers$ *              Nothing to see here
SYSVOL         *              Logon server share
Tasker         *              scheduled_things


PS C:\users\Groot14\desktop> ls


    Directory: C:\users\Groot14\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:51 AM              0 _8
```

Final credentials: `groot15:scheduled_things_8`.

## Groot 15

Congratulations!

You have successfully made it to the end!

Try your luck with other games brought to you by the Under The Wire team.

Thanks for playing!
