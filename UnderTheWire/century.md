# Century

[https://underthewire.tech/century-2](https://underthewire.tech/century)

## Century0

The goal of this level is to log into the game. Do the following in order to achieve this goal.

1. Obtain the initial credentials via the #StartHere channel on our Slack (link). Once you are in the channel, scroll to the top to see the credentials.

2. After obtaining the credentials, connect to the server via SSH. You will need an SSH client such as Putty. The host that you will be connecting to is century.underthewire.tech, on port 22.

3. When prompted, use the credentials for the applicable game found in the #StartHere Slack channel.

4. You have successfully connected to the game server when your path changes to “PS C:\Users\Century1\desktop>”.

```
century1:century1
```

## Century1

The password for Century2 is the build version of the instance of PowerShell installed on this system.

NOTE:
– The format is as follows: `**.*.*****.****`
– Include all periods
– Be sure to look for build version and NOT PowerShell version

```
PS C:\users\century1\desktop> $PSVersionTable

Name                           Value
----                           -----
PSVersion                      5.1.14393.5582
PSEdition                      Desktop
PSCompatibleVersions           {1.0, 2.0, 3.0, 4.0...}
BuildVersion                   10.0.14393.5582
CLRVersion                     4.0.30319.42000
WSManStackVersion              3.0
PSRemotingProtocolVersion      2.3
SerializationVersion           1.1.0.1
```

`century2:10.0.14393.5582`

## Century2

The password for Century3 is the name of the built-in cmdlet that performs the wget like function within PowerShell PLUS the name of the file on the desktop.

NOTE:
– If the name of the cmdlet is “get-web” and the file on the desktop is named “1234”, the password would be “get-web1234”.
– The password will be lowercase no matter how it appears on the screen.

```
PS C:\users\century2\desktop> Get-ChildItem


    Directory: C:\users\century2\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   3:29 AM            693 443


PS C:\users\century2\desktop> Get-Alias wget

CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Alias           wget -> Invoke-WebRequest
```

`century3:invoke-webrequest443`

## Century3

The password for Century4 is the number of files on the desktop.

```
PS C:\users\century3\desktop> Get-ChildItem | Measure-Object


Count    : 123
Average  :
Sum      :
Maximum  :
Minimum  :
Property :
```

`century4:123`

## Century4

The password for Century5 is the name of the file within a directory on the desktop that has spaces in its name.

```
PS C:\users\century4\desktop> Get-ChildItem


    Directory: C:\users\century4\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----        6/23/2022  10:30 PM                Can you open me
d-----        2/27/2023   4:55 PM                file
d-----         2/8/2022  10:35 PM                Open.txt
-a----        6/17/2022   1:19 AM              0 FolderList
-a----        5/28/2023   5:44 PM              0 temp.text
-a----       12/20/2023   6:43 PM              8 test.txt
-a----        1/17/2023   3:35 PM              0 text
-a----        1/17/2023   3:35 PM              0 text.txt


PS C:\users\century4\desktop> tree
Folder PATH listing for volume Windows
Volume serial number is 000000BA 641F:3922
C:.
├───Can you open me
├───file
└───Open.txt
PS C:\users\century4\desktop> Get-ChildItem ".\Can you open me"


    Directory: C:\users\century4\desktop\Can you open me


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        6/23/2022  10:24 PM             24 49125
```

`century5:49125`

## Century5

The password for Century6 is the short name of the domain in which this system resides in PLUS the name of the file on the desktop.

NOTE:
– If the short name of the domain is “blob” and the file on the desktop is named “1234”, the password would be “blob1234”.
– The password will be lowercase no matter how it appears on the screen.

```
PS C:\users\century5\desktop> Get-ChildItem


    Directory: C:\users\century5\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   3:29 AM             54 3347


PS C:\users\century5\desktop> Get-ADDomain


AllowedDNSSuffixes                 : {}
ChildDomains                       : {}
ComputersContainer                 : CN=Computers,DC=underthewire,DC=tech
DeletedObjectsContainer            : CN=Deleted Objects,DC=underthewire,DC=tech
DistinguishedName                  : DC=underthewire,DC=tech
DNSRoot                            : underthewire.tech
DomainControllersContainer         : OU=Domain Controllers,DC=underthewire,DC=tech
DomainMode                         : Windows2016Domain
DomainSID                          : S-1-5-21-758131494-606461608-3556270690
ForeignSecurityPrincipalsContainer : CN=ForeignSecurityPrincipals,DC=underthewire,DC=tech
Forest                             : underthewire.tech
InfrastructureMaster               : utw.underthewire.tech
LastLogonReplicationInterval       :
LinkedGroupPolicyObjects           : {cn={ECB4A7C0-B4E1-41B1-9E89-161CFA679999},cn=policies,cn=system,DC=underthewire,DC=tech,
                                     CN={31B2F340-016D-11D2-945F-00C04FB984F9},CN=Policies,CN=System,DC=underthewire,DC=tech}
LostAndFoundContainer              : CN=LostAndFound,DC=underthewire,DC=tech
ManagedBy                          :
Name                               : underthewire
NetBIOSName                        : underthewire
ObjectClass                        : domainDNS
ObjectGUID                         : bdccf3ad-b495-4d86-a94c-60f0d832e6f0
ParentDomain                       :
PDCEmulator                        : utw.underthewire.tech
PublicKeyRequiredPasswordRolling   : True
QuotasContainer                    : CN=NTDS Quotas,DC=underthewire,DC=tech
ReadOnlyReplicaDirectoryServers    : {}
ReplicaDirectoryServers            : {utw.underthewire.tech}
RIDMaster                          : utw.underthewire.tech
SubordinateReferences              : {DC=ForestDnsZones,DC=underthewire,DC=tech, DC=DomainDnsZones,DC=underthewire,DC=tech, CN=Configuration,DC=underthewire,DC=tech}
SystemsContainer                   : CN=System,DC=underthewire,DC=tech
UsersContainer                     : CN=Users,DC=underthewire,DC=tech
```

Look for the `Name`.

`century6:underthewire3347`

## Century6

The password for Century7 is the number of folders on the desktop.

```
PS C:\users\century6\desktop> Get-ChildItem -Directory | Measure-Object


Count    : 197
Average  :
Sum      :
Maximum  :
Minimum  :
Property :
```

`century7:197`

## Century7

The password for Century8 is in a readme file somewhere within the contacts, desktop, documents, downloads, favorites, music, or videos folder in the user’s profile.

NOTE:
– The password will be lowercase no matter how it appears on the screen.

```
PS C:\users\century7> Get-ChildItem -Recurse


    Directory: C:\users\century7


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-r---        7/16/2016   1:23 PM                Desktop
d-r---        8/30/2018   3:10 AM                Documents
d-----         6/9/2023   4:04 AM                Downloads
d-r---        7/16/2016   1:23 PM                Favorites
d-r---        7/16/2016   1:23 PM                Links
d-r---        7/16/2016   1:23 PM                Music
d-r---        7/16/2016   1:23 PM                Pictures
d-----        7/16/2016   1:23 PM                Saved Games
d-r---        7/16/2016   1:23 PM                Videos


    Directory: C:\users\century7\Downloads


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        2/25/2022  10:18 PM             17 LineNumbers.txt
-a----        8/30/2018   3:29 AM              7 Readme.txt


PS C:\users\century7> Get-Content C:\Users\century7\Downloads\Readme.txt
7points
```

`century8:7points`

## Century8

The password for Century9 is the number of unique entries within the file on the desktop.

```
PS C:\users\century8\desktop> Get-ChildItem


    Directory: C:\users\century8\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   3:33 AM          15858 unique.txt


PS C:\users\century8\desktop> Get-Content .\unique.txt | Get-Unique | Measure-Object


Count    : 696
Average  :
Sum      :
Maximum  :
Minimum  :
Property :
```

`century9:696`

## Century9

The password for Century10 is the 161st word within the file on the desktop.

NOTE:
– The password will be lowercase no matter how it appears on the screen.

```
PS C:\users\century9\desktop> Get-ChildItem


    Directory: C:\users\century9\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   3:34 AM           2131 Word_File.txt


PS C:\users\century9\desktop> Get-Content .\Word_File.txt
larceny epibole ampliate trecentos psychotoxic sybarism shatterwit cartilaginification crenulation splenification freespac untragicalness renovater smirch historism tymbal nonobjectivist pr
otestive octobass crownal retrorenal activation ascocarp clawing unaccordingly strontianite refutatory reline unsubmersible unstuffy asynergia asha rejunction spiritrompe preestimates papab
ot postcoital forbearantly epistolize corkwood rasers logicized rearrange rectigraph signposts prothrombin headkerchief upholden oversocialize semiperimeter hackbuteer ticklish brachiated a
theneum naegait engrasp palaeoconcha deminudity tragions curteous stratal swandown succinylcholine swooners caskanet irrespectability flocculant palatefulness thalamocoele maleate tittivate
 eustachium etudes loppering fidos flayers murrion uninduced numbedness nincompoopish compressors cassoulet protura fagopyrismus sesquibasic paxwaxes grievous remonstrator fulvid rotatoria
ultraconservatives postcards hairdresser wagnerianism mistreats nefarious winberry usherance conductility yearner uranostaphylorrhaphy rehabilitator agrapha junglegym emanant coy gaelicist
parallelogram wealdsman objurgator tapeline amay psalterer eleostearate mainprise overdyeing dowly coronado localed weasellike scattergram tocological disproportionation archicerebrum glaze
ment zugtierlaster sleepwort yabber tenontodynia laevulose walkaway readept literally weinmannia englut caulopteris schellingian thiamid suberizes bistorta quinetum woolulose jaculiferous t
restlework unoriginativeness kua uncontemptibleness unconcernedly taryard escapologist traumata chlorochrous exocolitis dysgnosia steadfastness keratoleukoma inordinate sacahuiste trippler
intoxicatively pierid nonapplicabness patinas rabific scandaliser waggel reauthenticate sufeism lairds cookee bragget ledgering perceptual chomper obscurities merino ganguela unproposed epu
lis loppard ignoblesse carrotage heartbrokenly unfusibness degenerate lacunae cirrocumulus knightlike overwhelmingness oxyrrhyncha capitalizations dimethylamine uninucleate syndicship grasp
able tropophil telchines abaiser overclement pursive
PS C:\users\century9\desktop> Get-Content .\Word_File.txt | Measure-Object -Word

Lines Words Characters Property
----- ----- ---------- --------
        200
```

```
PS C:\users\century9\desktop> (Get-Content .\Word_File.txt) -Split '\s+' | Select-Object -Index 160
pierid
```

```
PS C:\users\century9\desktop> (gc .\Word_File.txt).split(" ")[160]
pierid
```

`century10:pierid`

## Century10

The password for Century11 is the 10th and 8th word of the Windows Update service description combined PLUS the name of the file on the desktop.

NOTE:
– The password will be lowercase no matter how it appears on the screen.
– If the 10th and 8th word of the service description is “apple” and “juice” and the name of the file on the desktop is “88”, the password would be “applejuice88”.

```
PS C:\users\century10\desktop> Get-Service -DisplayName "*update*"

Status   Name               DisplayName
------   ----               -----------
Stopped  tzautoupdate       Auto Time Zone Updater
Running  UsoSvc             Update Orchestrator Service for Win...
Stopped  wuauserv           Windows Update
```

```
PS C:\users\century10\desktop> Get-WmiObject win32_service | ?{$_.Name -like "wuauserv"} | Select-Object Description

Description
-----------
Enables the detection, download, and installation of updates for Windows and other programs. If this service is disabled, users of this computer will not be able to use Windows Update o...
```

```
PS C:\users\century10\desktop> Get-ChildItem


    Directory: C:\users\century10\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   3:34 AM             43 110
```

`century11:windowsupdates110`

## Century11

The password for Century12 is the name of the hidden file within the contacts, desktop, documents, downloads, favorites, music, or videos folder in the user’s profile.

NOTE:
– Exclude “desktop.ini”.
– The password will be lowercase no matter how it appears on the screen.

```
PS C:\users\century11> Get-ChildItem -Recurse -Hidden


    Directory: C:\users\century11


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d--hsl        8/30/2018   3:11 AM                Application Data
d--hsl        8/30/2018   3:11 AM                Cookies
d--hsl        8/30/2018   3:11 AM                Local Settings
d--hsl        8/30/2018   3:11 AM                My Documents
d--hsl        8/30/2018   3:11 AM                NetHood
d--hsl        8/30/2018   3:11 AM                PrintHood
d--hsl        8/30/2018   3:11 AM                Recent
d--hsl        8/30/2018   3:11 AM                SendTo
d--hsl        8/30/2018   3:11 AM                Start Menu
d--hsl        8/30/2018   3:11 AM                Templates
-a-h--        7/17/2023   2:37 PM         262144 NTUSER.DAT
-a-hs-        8/30/2018   3:11 AM          98304 ntuser.dat.LOG1
-a-hs-        8/30/2018   3:11 AM         126976 ntuser.dat.LOG2
-a-hs-        7/12/2020  10:55 PM          65536 NTUSER.DAT{0f893ee4-78e5-11e6-90dd-eefb07825ed9}.TM.blf
-a-hs-        6/14/2020   4:36 AM         524288 NTUSER.DAT{0f893ee4-78e5-11e6-90dd-eefb07825ed9}.TMContainer00000000000000000001.regtrans-ms
-a-hs-        7/12/2020  10:55 PM         524288 NTUSER.DAT{0f893ee4-78e5-11e6-90dd-eefb07825ed9}.TMContainer00000000000000000002.regtrans-ms
---hs-        8/30/2018   3:11 AM             20 ntuser.ini


    Directory: C:\users\century11\AppData\Local


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d--hsl        8/30/2018   3:11 AM                Application Data
d--hsl        8/30/2018   3:11 AM                History
d--hsl        8/30/2018   3:11 AM                Temporary Internet Files
Get-ChildItem : Access to the path 'C:\users\century11\AppData\Local\Application Data' is denied.
At line:1 char:1
+ Get-ChildItem -Recurse -Hidden
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : PermissionDenied: (C:\users\centur...pplication Data:String) [Get-ChildItem], UnauthorizedAccessException
    + FullyQualifiedErrorId : DirUnauthorizedAccessError,Microsoft.PowerShell.Commands.GetChildItemCommand

Get-ChildItem : Access to the path 'C:\users\century11\AppData\Local\History' is denied.
At line:1 char:1
+ Get-ChildItem -Recurse -Hidden
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : PermissionDenied: (C:\users\century11\AppData\Local\History:String) [Get-ChildItem], UnauthorizedAccessException
    + FullyQualifiedErrorId : DirUnauthorizedAccessError,Microsoft.PowerShell.Commands.GetChildItemCommand



    Directory: C:\users\century11\AppData\Local\Microsoft\Windows


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d--hsl        8/30/2018   3:11 AM                Temporary Internet Files
-a-h--        8/30/2018   3:11 AM           8192 UsrClass.dat
-a-hs-        8/30/2018   3:11 AM           8192 UsrClass.dat.LOG1
-a-hs-        8/30/2018   3:11 AM           8192 UsrClass.dat.LOG2
-a-hs-        8/30/2018   3:11 AM          65536 UsrClass.dat{d82669b3-abff-11e8-90ee-e14c26db97e8}.TM.blf
-a-hs-        8/30/2018   3:11 AM         524288 UsrClass.dat{d82669b3-abff-11e8-90ee-e14c26db97e8}.TMContainer00000000000000000001.regtrans-ms
-a-hs-        8/30/2018   3:11 AM         524288 UsrClass.dat{d82669b3-abff-11e8-90ee-e14c26db97e8}.TMContainer00000000000000000002.regtrans-ms
Get-ChildItem : Access to the path 'C:\users\century11\AppData\Local\Microsoft\Windows\Temporary Internet Files' is denied.
At line:1 char:1
+ Get-ChildItem -Recurse -Hidden
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : PermissionDenied: (C:\users\centur... Internet Files:String) [Get-ChildItem], UnauthorizedAccessException
    + FullyQualifiedErrorId : DirUnauthorizedAccessError,Microsoft.PowerShell.Commands.GetChildItemCommand



    Directory: C:\users\century11\AppData\Local\Microsoft\Windows\WinX\Group1


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a-hs-        7/16/2016   1:21 PM             75 desktop.ini


    Directory: C:\users\century11\AppData\Local\Microsoft\Windows\WinX\Group2


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a-hs-        7/16/2016   1:21 PM            325 desktop.ini


    Directory: C:\users\century11\AppData\Local\Microsoft\Windows\WinX\Group3


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a-hs-        7/16/2016   1:21 PM            948 desktop.ini
Get-ChildItem : Access to the path 'C:\users\century11\AppData\Local\Temporary Internet Files' is denied.
At line:1 char:1
+ Get-ChildItem -Recurse -Hidden
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : PermissionDenied: (C:\users\centur... Internet Files:String) [Get-ChildItem], UnauthorizedAccessException
    + FullyQualifiedErrorId : DirUnauthorizedAccessError,Microsoft.PowerShell.Commands.GetChildItemCommand

Get-ChildItem : Access to the path 'C:\users\century11\AppData\Roaming\Microsoft\Windows\Start Menu' is denied.
At line:1 char:1
+ Get-ChildItem -Recurse -Hidden
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : PermissionDenied: (C:\users\centur...dows\Start Menu:String) [Get-ChildItem], UnauthorizedAccessException
    + FullyQualifiedErrorId : DirUnauthorizedAccessError,Microsoft.PowerShell.Commands.GetChildItemCommand

Get-ChildItem : Access to the path 'C:\users\century11\Application Data' is denied.
At line:1 char:1
+ Get-ChildItem -Recurse -Hidden
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : PermissionDenied: (C:\users\century11\Application Data:String) [Get-ChildItem], UnauthorizedAccessException
    + FullyQualifiedErrorId : DirUnauthorizedAccessError,Microsoft.PowerShell.Commands.GetChildItemCommand

Get-ChildItem : Access to the path 'C:\users\century11\Cookies' is denied.
At line:1 char:1
+ Get-ChildItem -Recurse -Hidden
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : PermissionDenied: (C:\users\century11\Cookies:String) [Get-ChildItem], UnauthorizedAccessException
    + FullyQualifiedErrorId : DirUnauthorizedAccessError,Microsoft.PowerShell.Commands.GetChildItemCommand



    Directory: C:\users\century11\Documents


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d--hsl        8/30/2018   3:11 AM                My Music
d--hsl        8/30/2018   3:11 AM                My Pictures
d--hsl        8/30/2018   3:11 AM                My Videos
Get-ChildItem : Access to the path 'C:\users\century11\Documents\My Music' is denied.
At line:1 char:1
+ Get-ChildItem -Recurse -Hidden
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : PermissionDenied: (C:\users\century11\Documents\My Music:String) [Get-ChildItem], UnauthorizedAccessException
    + FullyQualifiedErrorId : DirUnauthorizedAccessError,Microsoft.PowerShell.Commands.GetChildItemCommand

Get-ChildItem : Access to the path 'C:\users\century11\Documents\My Pictures' is denied.
At line:1 char:1
+ Get-ChildItem -Recurse -Hidden
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : PermissionDenied: (C:\users\century11\Documents\My Pictures:String) [Get-ChildItem], UnauthorizedAccessException
    + FullyQualifiedErrorId : DirUnauthorizedAccessError,Microsoft.PowerShell.Commands.GetChildItemCommand

Get-ChildItem : Access to the path 'C:\users\century11\Documents\My Videos' is denied.
At line:1 char:1
+ Get-ChildItem -Recurse -Hidden
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : PermissionDenied: (C:\users\century11\Documents\My Videos:String) [Get-ChildItem], UnauthorizedAccessException
    + FullyQualifiedErrorId : DirUnauthorizedAccessError,Microsoft.PowerShell.Commands.GetChildItemCommand



    Directory: C:\users\century11\Downloads


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
--rh--        8/30/2018   3:34 AM             30 secret_sauce
Get-ChildItem : Access to the path 'C:\users\century11\Local Settings' is denied.
At line:1 char:1
+ Get-ChildItem -Recurse -Hidden
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : PermissionDenied: (C:\users\century11\Local Settings:String) [Get-ChildItem], UnauthorizedAccessException
    + FullyQualifiedErrorId : DirUnauthorizedAccessError,Microsoft.PowerShell.Commands.GetChildItemCommand

Get-ChildItem : Access to the path 'C:\users\century11\My Documents' is denied.
At line:1 char:1
+ Get-ChildItem -Recurse -Hidden
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : PermissionDenied: (C:\users\century11\My Documents:String) [Get-ChildItem], UnauthorizedAccessException
    + FullyQualifiedErrorId : DirUnauthorizedAccessError,Microsoft.PowerShell.Commands.GetChildItemCommand

Get-ChildItem : Access to the path 'C:\users\century11\NetHood' is denied.
At line:1 char:1
+ Get-ChildItem -Recurse -Hidden
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : PermissionDenied: (C:\users\century11\NetHood:String) [Get-ChildItem], UnauthorizedAccessException
    + FullyQualifiedErrorId : DirUnauthorizedAccessError,Microsoft.PowerShell.Commands.GetChildItemCommand

Get-ChildItem : Access to the path 'C:\users\century11\PrintHood' is denied.
At line:1 char:1
+ Get-ChildItem -Recurse -Hidden
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : PermissionDenied: (C:\users\century11\PrintHood:String) [Get-ChildItem], UnauthorizedAccessException
    + FullyQualifiedErrorId : DirUnauthorizedAccessError,Microsoft.PowerShell.Commands.GetChildItemCommand

Get-ChildItem : Access to the path 'C:\users\century11\Recent' is denied.
At line:1 char:1
+ Get-ChildItem -Recurse -Hidden
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : PermissionDenied: (C:\users\century11\Recent:String) [Get-ChildItem], UnauthorizedAccessException
    + FullyQualifiedErrorId : DirUnauthorizedAccessError,Microsoft.PowerShell.Commands.GetChildItemCommand

Get-ChildItem : Access to the path 'C:\users\century11\SendTo' is denied.
At line:1 char:1
+ Get-ChildItem -Recurse -Hidden
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : PermissionDenied: (C:\users\century11\SendTo:String) [Get-ChildItem], UnauthorizedAccessException
    + FullyQualifiedErrorId : DirUnauthorizedAccessError,Microsoft.PowerShell.Commands.GetChildItemCommand

Get-ChildItem : Access to the path 'C:\users\century11\Start Menu' is denied.
At line:1 char:1
+ Get-ChildItem -Recurse -Hidden
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : PermissionDenied: (C:\users\century11\Start Menu:String) [Get-ChildItem], UnauthorizedAccessException
    + FullyQualifiedErrorId : DirUnauthorizedAccessError,Microsoft.PowerShell.Commands.GetChildItemCommand

Get-ChildItem : Access to the path 'C:\users\century11\Templates' is denied.
At line:1 char:1
+ Get-ChildItem -Recurse -Hidden
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : PermissionDenied: (C:\users\century11\Templates:String) [Get-ChildItem], UnauthorizedAccessException
    + FullyQualifiedErrorId : DirUnauthorizedAccessError,Microsoft.PowerShell.Commands.GetChildItemCommand
```

`century12:secret_sauce`

## Century12

The password for Century13 is the description of the computer designated as a Domain Controller within this domain PLUS the name of the file on the desktop.

NOTE:
– The password will be lowercase no matter how it appears on the screen.
– If the description “today_is” and the file on the desktop is named “\_cool”, the password would be “today_is_cool”.

```
PS C:\users\century12\desktop> Get-ChildItem


    Directory: C:\users\century12\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   3:34 AM             30 _things
```

```
PS C:\users\century12\desktop> Get-ADDomainController


ComputerObjectDN           : CN=UTW,OU=Domain Controllers,DC=underthewire,DC=tech
DefaultPartition           : DC=underthewire,DC=tech
Domain                     : underthewire.tech
Enabled                    : True
Forest                     : underthewire.tech
HostName                   : utw.underthewire.tech
InvocationId               : 09ee1897-2210-4ac9-989d-e19b4241e9c6
IPv4Address                : 192.99.167.156
IPv6Address                :
IsGlobalCatalog            : True
IsReadOnly                 : False
LdapPort                   : 389
Name                       : UTW
NTDSSettingsObjectDN       : CN=NTDS Settings,CN=UTW,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=underthewire,DC=tech
OperatingSystem            : Windows Server 2016 Standard
OperatingSystemHotfix      :
OperatingSystemServicePack :
OperatingSystemVersion     : 10.0 (14393)
OperationMasterRoles       : {SchemaMaster, DomainNamingMaster, PDCEmulator, RIDMaster...}
Partitions                 : {DC=ForestDnsZones,DC=underthewire,DC=tech, DC=DomainDnsZones,DC=underthewire,DC=tech, CN=Schema,CN=Configuration,DC=underthewire,DC=tech,
                             CN=Configuration,DC=underthewire,DC=tech...}
ServerObjectDN             : CN=UTW,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=underthewire,DC=tech
ServerObjectGuid           : df17c8a3-dd76-438b-8ddf-b7ad3e624618
Site                       : Default-First-Site-Name
SslPort                    : 636



PS C:\users\century12\desktop> Get-ADDomainController | Select-Object Name

Name
----
UTW


PS C:\users\century12\desktop> Get-ADComputer UTW -Properties Description


Description       : i_authenticate
DistinguishedName : CN=UTW,OU=Domain Controllers,DC=underthewire,DC=tech
DNSHostName       : utw.underthewire.tech
Enabled           : True
Name              : UTW
ObjectClass       : computer
ObjectGUID        : 5ca56844-bb73-4234-ac85-eed2d0d01a2e
SamAccountName    : UTW$
SID               : S-1-5-21-758131494-606461608-3556270690-1000
UserPrincipalName :
```

`century13:i_authenticate_things`

## Century13

The password for Century14 is the number of words within the file on the desktop.

```
PS C:\users\century13\desktop> Get-Content .\countmywords | Measure-Object -Word

Lines Words Characters Property
----- ----- ---------- --------
        755
```

`century14:755`

## Century14

The password for Century15 is the number of times the word “polo” appears within the file on the desktop.

NOTE:
– You should count the instances of the whole word only..

```
PS C:\users\century14\desktop> -Split (Get-Content .\countpolos | Out-String) | Where-Object {$_ -eq "polo"} | Measure-Object


Count    : 153
Average  :
Sum      :
Maximum  :
Minimum  :
Property :
```

`centry15:153`

## Century15

Congratulations!

You have successfully made it to the end!

Try your luck with other games brought to you by the Under The Wire team.

Thanks for playing!
