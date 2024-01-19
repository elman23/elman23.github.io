# Cyborg

[https://underthewire.tech/cyborg](https://underthewire.tech/cyborg)

## Cyborg 0

The goal of this level is to log into the game. Do the following in order to achieve this goal.

1. Obtain the initial credentials via the **#StartHere** channel on our **Slack** ([link](https://join.slack.com/t/underthewire/shared_invite/zt-11xkgkxj5-VmAGL_ofeIAQ2hNXuu_irg)). Once you are in the channel, scroll to the top to see the credentials.

2. After obtaining the credentials, connect to the server via SSH. You will need an SSH client such as Putty. The host that you will be connecting to is **cyborg.underthewire.tech**, on port **22**.

3. When prompted, use the credentials for the applicable game found in the #StartHere Slack channel.

4. You have successfully connected to the game server when your path changes to “PS C:\Users\Cyborg1\desktop>”.

```bash
ssh cyborg1@cyborg.underthewire.tech
```

Use the password `cyborg1`.

## Cyborg 1

The password for cyborg2 is the state that the user Chris Rogers is from as stated within Active Directory.

**NOTE:**  
– The password will be lowercase no matter how it appears on the screen.  
– “State” refers to the location within the country and NOT the “state” of the account (enabled/ disabled).

**IMPORTANT:**  
Once you feel you have completed the Cyborg1 challenge, start a new connection to the server, and log in with the username of Cyborg2 and this password will be the answer from Cyborg1. If successful, close out the Cyborg1 connection and begin to solve the Cyborg2 challenge. This concept is repeated over and over until you reach the end of the game.

▼ **HINT:**

List the available modules, there may be a useful one available…

Here: https://www.itechtics.com/user-information-powershell-get-aduser/?expand_article=1 I find that the command I was looking for is:

```powershell
Get-ADUser -Filter *
```

I elaborate it into:

```powershell
Get-ADUser -Filter * | Select-String "Chris"
```

which gives me:

```
CN=Rogers\, Chris\ ,OU=T-65,OU=X-Wing,DC=underthewire,DC=tech
```

In particular, running the command without the `Select-String` part and analysing the output, I recognise:

```
DistinguishedName : CN=Rogers\, Chris\
                    ,OU=T-65,OU=X-Wing,DC=underthewire,DC=tech
Enabled           : False
GivenName         : Chris
Name              : Rogers, Chris
ObjectClass       : user
ObjectGUID        : ee6450f8-cf70-4b1d-b902-a837839632bd
SamAccountName    : chris.rogers
SID               : S-1-5-21-758131494-606461608-3556270690-2177
Surname           : Rogers
UserPrincipalName : chris.rogers
```

But here I cannot see anything about the state...
Here: https://social.technet.microsoft.com/Forums/en-US/c5b93b5f-a097-4094-888f-01c72dbba8dc/getting-detailed-user-account-status-in-active-directory I found the command:

```powershell
get-aduser chris.rogers -properties *
```

Which outputs:

```
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
CanonicalName                        : underthewire.tech/X-Wing/T-65/Rogers,
                                       Chris
Certificates                         : {}
City                                 :
CN                                   : Rogers, Chris
codePage                             : 0
Company                              :
CompoundIdentitySupported            : {}
Country                              :
countryCode                          : 0
Created                              : 8/30/2018 3:28:44 AM
createTimeStamp                      : 8/30/2018 3:28:44 AM
Deleted                              :
Department                           :
Description                          :
DisplayName                          : Rogers, Chris
DistinguishedName                    : CN=Rogers\, Chris\ ,OU=T-65,OU=X-Wing,DC
                                       =underthewire,DC=tech
Division                             :
DoesNotRequirePreAuth                : False
dSCorePropagationData                : {1/1/1601 12:00:00 AM}
EmailAddress                         : chris.rogers@underthewire.tech
EmployeeID                           :
EmployeeNumber                       :
Enabled                              : False
Fax                                  :
GivenName                            : Chris
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
LogonWorkstations                    :
mail                                 : chris.rogers@underthewire.tech
Manager                              :
MemberOf                             : {}
MNSLogonAccount                      : False
MobilePhone                          :
Modified                             : 11/18/2018 8:43:51 PM
modifyTimeStamp                      : 11/18/2018 8:43:51 PM
msDS-User-Account-Control-Computed   : 8388608
Name                                 : Rogers, Chris
nTSecurityDescriptor                 : System.DirectoryServices.ActiveDirectory
                                       Security
ObjectCategory                       : CN=Person,CN=Schema,CN=Configuration,DC=
                                       underthewire,DC=tech
ObjectClass                          : user
ObjectGUID                           : ee6450f8-cf70-4b1d-b902-a837839632bd
objectSid                            : S-1-5-21-758131494-606461608-3556270690-
                                       2177
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
PrimaryGroup                         : CN=Domain
                                       Users,CN=Users,DC=underthewire,DC=tech
primaryGroupID                       : 513
PrincipalsAllowedToDelegateToAccount : {}
ProfilePath                          :
ProtectedFromAccidentalDeletion      : False
pwdLastSet                           : 0
SamAccountName                       : chris.rogers
sAMAccountType                       : 805306368
ScriptPath                           :
sDRightsEffective                    : 0
ServicePrincipalNames                : {}
SID                                  : S-1-5-21-758131494-606461608-3556270690-
                                       2177
SIDHistory                           : {}
SmartcardLogonRequired               : False
sn                                   : Rogers
st                                   : kansas
State                                : kansas
StreetAddress                        :
Surname                              : Rogers
Title                                :
TrustedForDelegation                 : False
TrustedToAuthForDelegation           : False
UseDESKeyOnly                        : False
userAccountControl                   : 514
userCertificate                      : {}
UserPrincipalName                    : chris.rogers
uSNChanged                           : 38765
uSNCreated                           : 19675
whenChanged                          : 11/18/2018 8:43:51 PM
whenCreated                          : 8/30/2018 3:28:44 AM
```

Well, Chris is from Kansas.

Credentials: `cyborg2:kansas`.

## Cyborg 2

The password for cyborg3 is the host A record IP address for CYBORG718W100N **PLUS** the name of the file on the desktop.

**NOTE:**  
– If the IP is “10.10.1.5” and the file on the desktop is called “\_address”, then the password is “10.10.1.5_address”.  
– The password will be lowercase no matter how it appears on the screen.

▼ **HINT:**

WMI or cmdlets… choices, choices.

▼ **HINT:**

Each domain client has its own specific Zone Name.

The password for cyborg3 is the host A record IP address for CYBORG718W100N **PLUS** the name of the file on the desktop.

Idea: to ping CYBORG718W100N and see if the IP address is revealed.

```powershell
PS C:\users\cyborg2\desktop> ping CYBORG718W100N

Pinging CYBORG718W100N.underthewire.tech [172.31.45.167] with 32 bytes of data:
Request timed out.
Request timed out.
Request timed out.
Request timed out.

Ping statistics for 172.31.45.167:
    Packets: Sent = 4, Received = 0, Lost = 4 (100% loss),
```

On the other hand, it is easy to see what is there on the desktop:

```powershell
PS C:\users\cyborg2\desktop> get-childitem


    Directory: C:\users\cyborg2\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        2/26/2022   2:14 PM              0 _ipv4


PS C:\users\cyborg2\desktop>
```

The guess is for `172.31.45.167_ipv4`. It works.

## Cyborg 3

The password for cyborg4 is the number of users in the Cyborg group within Active Directory **PLUS** the name of the file on the desktop.

**NOTE:**  
– If the number of users is “20” and the file on the desktop is called “\_users”, then the password is “20_users”.  
– The password will be lowercase no matter how it appears on the screen.

▼ **HINT:**

[https://technet.microsoft.com/en-us/library/ee617195.aspx](https://technet.microsoft.com/en-us/library/ee617195.aspx)

```powershell
PS C:\users\cyborg3\desktop> get-adgroup cyborg


DistinguishedName : CN=cyborg,OU=Groups,DC=underthewire,DC=tech
GroupCategory     : Distribution
GroupScope        : Global
Name              : cyborg
ObjectClass       : group
ObjectGUID        : e9511d2f-b09b-40ef-a5b2-180e162ee4a7
SamAccountName    : cyborg
SID               : S-1-5-21-758131494-606461608-3556270690-2180
```

From: https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/ee617241(v=technet.10):
To get all objects of the type specified by the cmdlet, use the asterisk wildcard:  
 All user objects:  
 `Get-ADUser -Filter *`
-or-  
 All computer objects:  
 `Get-ADComputer -Filter *`

From: https://stackoverflow.com/questions/36222811/get-aduser-within-a-specific-ad-group#36223406:

```bash
Get-ADGroupMember 'groupname' |
  Get-ADUser -Properties EmailAddress |
  Where-Object { $_.Surname -eq 'foo' -and $_.GivenName -eq 'bar' } |
  Select-Object -Expand EmailAddress
```

Therefore, the number of users in the `'cyborg'` Active Directory group:

```powershell
PS C:\users\cyborg3\desktop> get-adgroupmember 'cyborg' | measure-object


Count    : 88
Average  :
Sum      :
Maximum  :
Minimum  :
Property :
```

The name of the file on the Desktop:

```powershell
PS C:\users\cyborg3\desktop> pwd

Path
----
C:\users\cyborg3\desktop


PS C:\users\cyborg3\desktop> get-childitem


    Directory: C:\users\cyborg3\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        2/26/2022   2:14 PM              0 _objects
```

So: `cyborg4:88_objects`.

## Cyborg 4

The password for cyborg5 is the PowerShell module name with a version number of 8.9.8.9 **PLUS** the name of the file on the desktop.

**NOTE:**  
– If the module name is “bob” and the file on the desktop is called “\_settings”, then the password is “bob_settings”.  
– The password will be lowercase no matter how it appears on the screen.

▼**HINT:**

List the modules…

List the modules imported in the current session or that can be imported from the PSModulePath. (See: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-module?view=powershell-7.3.)

```powershell
PS C:\users\cyborg4\desktop> get-module -all

ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Binary     3.0.0.0    Microsoft.PowerShell.Commands.Ma... {Add-Content, Clear-Content, Clear-ItemProperty, Join-Path...}
Binary     3.0.0.0    Microsoft.PowerShell.Commands.Ut... {New-Object, Measure-Object, Select-Object, Sort-Object...}
Manifest   3.1.0.0    Microsoft.PowerShell.Management     {Add-Computer, Add-Content, Checkpoint-Computer, Clear-Content...}
Script     0.0        Microsoft.PowerShell.Utility        {ConvertFrom-SddlString, Format-Hex, Get-FileHash, Import-PowerShellDataFile...}
Manifest   3.1.0.0    Microsoft.PowerShell.Utility        {Add-Member, Add-Type, Clear-Variable, Compare-Object...}
Binary     1.0.0.1    PackageManagement                   {Find-Package, Find-PackageProvider, Get-Package, Get-PackageProvider...}
Script     1.0.0.1    PowerShellGet                       {Find-Command, Find-DscResource, Find-Module, Find-RoleCapability...}
```

None has the desired version. Therefore the indications must refer to some other module...

We try with `-ListAvailable`:

```powershell
PS C:\users\cyborg4\desktop> Get-Module -ListAvailable


    Directory: C:\Program Files\WindowsPowerShell\Modules


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Script     1.0.1      Microsoft.PowerShell.Operation.V... {Get-OperationValidation, Invoke-OperationValidation}
Binary     1.0.0.1    PackageManagement                   {Find-Package, Get-Package, Get-PackageProvider, Get-PackageSource...}
Script     3.4.0      Pester                              {Describe, Context, It, Should...}
Script     1.0.0.1    PowerShellGet                       {Install-Module, Find-Module, Save-Module, Update-Module...}
Script     1.2        PSReadline                          {Get-PSReadlineKeyHandler, Set-PSReadlineKeyHandler, Remove-PSReadlineKeyHandler, Get-PSReadlineOption...}
Script     1.0.6      PSSlack                             {Find-SlackMessage, Get-PSSlackConfig, Get-SlackAuth, Get-SlackChannel...}
Script     1.0.0      PSSlack                             {Find-SlackMessage, Get-PSSlackConfig, Get-SlackAuth, Get-SlackChannel...}
Script     0.1.3      PSSlack                             {Find-SlackMessage, Get-PSSlackConfig, Get-SlackAuth, Get-SlackChannel...}
Script     0.1.0      PSSlack                             {Find-SlackMessage, Get-PSSlackConfig, Get-SlackAuth, Get-SlackChannel...}


    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Manifest   1.0.0.0    ActiveDirectory                     {Add-ADCentralAccessPolicyMember, Add-ADComputerServiceAccount, Add-ADDomainControllerPasswordReplication...
Manifest   1.0.0.0    ADDSDeployment                      {Add-ADDSReadOnlyDomainControllerAccount, Install-ADDSForest, Install-ADDSDomain, Install-ADDSDomainContr...
Manifest   1.0.0.0    AppBackgroundTask                   {Disable-AppBackgroundTaskDiagnosticLog, Enable-AppBackgroundTaskDiagnosticLog, Set-AppBackgroundTaskReso...
Manifest   2.0.0.0    AppLocker                           {Get-AppLockerFileInformation, Get-AppLockerPolicy, New-AppLockerPolicy, Set-AppLockerPolicy...}
Manifest   1.0.0.0    AppvClient                          {Add-AppvClientConnectionGroup, Add-AppvClientPackage, Add-AppvPublishingServer, Disable-Appv...}
Manifest   2.0.0.0    Appx                                {Add-AppxPackage, Get-AppxPackage, Get-AppxPackageManifest, Remove-AppxPackage...}
Script     1.0.0.0    AssignedAccess                      {Clear-AssignedAccess, Get-AssignedAccess, Set-AssignedAccess}
Manifest   8.9.8.9    bacon                               Get-bacon
Manifest   1.0        BestPractices                       {Get-BpaModel, Get-BpaResult, Invoke-BpaModel, Set-BpaResult}
Manifest   2.0.0.0    BitsTransfer                        {Add-BitsFile, Complete-BitsTransfer, Get-BitsTransfer, Remove-BitsTransfer...}
Manifest   1.0.0.0    BranchCache                         {Add-BCDataCacheExtension, Clear-BCCache, Disable-BC, Disable-BCDowngrading...}
Manifest   1.0.0.0    CimCmdlets                          {Get-CimAssociatedInstance, Get-CimClass, Get-CimInstance, Get-CimSession...}
Manifest   1.0        ConfigCI                            {Get-SystemDriver, New-CIPolicyRule, New-CIPolicy, Get-CIPolicy...}
Manifest   1.0        ConfigDefender                      {Get-MpPreference, Set-MpPreference, Add-MpPreference, Remove-MpPreference...}
Manifest   1.0        ConfigDefenderPerformance           {New-MpPerformanceRecording, Get-MpPerformanceReport}
Manifest   1.0        Defender                            {Get-MpPreference, Set-MpPreference, Add-MpPreference, Remove-MpPreference...}
Manifest   1.0        DFSN                                {Get-DfsnRoot, Remove-DfsnRoot, Set-DfsnRoot, New-DfsnRoot...}
Binary     2.0.0.0    DFSR                                {New-DfsReplicationGroup, Get-DfsReplicationGroup, Set-DfsReplicationGroup, Remove-DfsReplicationGroup...}
Manifest   1.0.0.0    DirectAccessClientComponents        {Disable-DAManualEntryPointSelection, Enable-DAManualEntryPointSelection, Get-DAClientExperienceConfigura...
Script     3.0        Dism                                {Add-AppxProvisionedPackage, Add-WindowsDriver, Add-WindowsCapability, Add-WindowsImage...}
Manifest   1.0.0.0    DnsClient                           {Resolve-DnsName, Clear-DnsClientCache, Get-DnsClient, Get-DnsClientCache...}
Manifest   2.0.0.0    DnsServer                           {Add-DnsServerConditionalForwarderZone, Add-DnsServerDirectoryPartition, Add-DnsServerForwarder, Add-DnsS...
Manifest   1.0.0.0    EventTracingManagement              {New-EtwTraceSession, Get-EtwTraceSession, Set-EtwTraceSession, Send-EtwTraceSession...}
Manifest   1.0.0.0    GroupPolicy                         {Backup-GPO, Block-GPInheritance, Copy-GPO, Get-GPInheritance...}
Script     1.0.0.0    IISAdministration                   {Get-IISAppPool, Start-IISCommitDelay, Stop-IISCommitDelay, Get-IISSite...}
Manifest   2.0.0.0    International                       {Get-WinDefaultInputMethodOverride, Set-WinDefaultInputMethodOverride, Get-WinHomeLocation, Set-WinHomeLo...
Manifest   1.0.0.0    iSCSI                               {Get-IscsiTargetPortal, New-IscsiTargetPortal, Remove-IscsiTargetPortal, Update-IscsiTargetPortal...}
Manifest   2.0.0.0    IscsiTarget                         {Add-ClusteriSCSITargetServerRole, Add-IscsiVirtualDiskTargetMapping, Checkpoint-IscsiVirtualDisk, Conver...
Script     1.0.0.0    ISE                                 {New-IseSnippet, Import-IseSnippet, Get-IseSnippet}
Manifest   1.0.0.0    Kds                                 {Add-KdsRootKey, Get-KdsRootKey, Test-KdsRootKey, Set-KdsConfiguration...}
Manifest   1.0.1.0    Microsoft.PowerShell.Archive        {Compress-Archive, Expand-Archive}
Manifest   3.0.0.0    Microsoft.PowerShell.Diagnostics    {Get-WinEvent, Get-Counter, Import-Counter, Export-Counter...}
Manifest   3.0.0.0    Microsoft.PowerShell.Host           {Start-Transcript, Stop-Transcript}
Manifest   1.0.0.0    Microsoft.PowerShell.LocalAccounts  {Add-LocalGroupMember, Disable-LocalUser, Enable-LocalUser, Get-LocalGroup...}
Manifest   3.1.0.0    Microsoft.PowerShell.Management     {Add-Content, Clear-Content, Clear-ItemProperty, Join-Path...}
Script     1.0        Microsoft.PowerShell.ODataUtils     Export-ODataEndpointProxy
Manifest   3.0.0.0    Microsoft.PowerShell.Security       {Get-Acl, Set-Acl, Get-PfxCertificate, Get-Credential...}
Manifest   3.1.0.0    Microsoft.PowerShell.Utility        {Format-List, Format-Custom, Format-Table, Format-Wide...}
Manifest   3.0.0.0    Microsoft.WSMan.Management          {Disable-WSManCredSSP, Enable-WSManCredSSP, Get-WSManCredSSP, Set-WSManQuickConfig...}
Manifest   1.0        MMAgent                             {Disable-MMAgent, Enable-MMAgent, Set-MMAgent, Get-MMAgent...}
Manifest   1.0.0.0    MsDtc                               {New-DtcDiagnosticTransaction, Complete-DtcDiagnosticTransaction, Join-DtcDiagnosticResourceManager, Rece...
Manifest   2.0.0.0    NetAdapter                          {Disable-NetAdapter, Disable-NetAdapterBinding, Disable-NetAdapterChecksumOffload, Disable-NetAdapterEnca...
Manifest   1.0.0.0    NetConnection                       {Get-NetConnectionProfile, Set-NetConnectionProfile}
Manifest   1.0.0.0    NetEventPacketCapture               {New-NetEventSession, Remove-NetEventSession, Get-NetEventSession, Set-NetEventSession...}
Manifest   2.0.0.0    NetLbfo                             {Add-NetLbfoTeamMember, Add-NetLbfoTeamNic, Get-NetLbfoTeam, Get-NetLbfoTeamMember...}
Manifest   1.0.0.0    NetNat                              {Get-NetNat, Get-NetNatExternalAddress, Get-NetNatStaticMapping, Get-NetNatSession...}
Manifest   2.0.0.0    NetQos                              {Get-NetQosPolicy, Set-NetQosPolicy, Remove-NetQosPolicy, New-NetQosPolicy}
Manifest   2.0.0.0    NetSecurity                         {Get-DAPolicyChange, New-NetIPsecAuthProposal, New-NetIPsecMainModeCryptoProposal, New-NetIPsecQuickModeC...
Manifest   1.0.0.0    NetSwitchTeam                       {New-NetSwitchTeam, Remove-NetSwitchTeam, Get-NetSwitchTeam, Rename-NetSwitchTeam...}
Manifest   1.0.0.0    NetTCPIP                            {Get-NetIPAddress, Get-NetIPInterface, Get-NetIPv4Protocol, Get-NetIPv6Protocol...}
Manifest   1.0.0.0    NetworkConnectivityStatus           {Get-DAConnectionStatus, Get-NCSIPolicyConfiguration, Reset-NCSIPolicyConfiguration, Set-NCSIPolicyConfig...
Manifest   1.0.0.0    NetworkSwitchManager                {Disable-NetworkSwitchEthernetPort, Enable-NetworkSwitchEthernetPort, Get-NetworkSwitchEthernetPort, Remo...
Manifest   1.0.0.0    NetworkTransition                   {Add-NetIPHttpsCertBinding, Disable-NetDnsTransitionConfiguration, Disable-NetIPHttpsProfile, Disable-Net...
Manifest   1.0        NFS                                 {Get-NfsMappedIdentity, Get-NfsNetgroup, Install-NfsMappingStore, New-NfsMappedIdentity...}
Manifest   1.0.0.0    PcsvDevice                          {Get-PcsvDevice, Start-PcsvDevice, Stop-PcsvDevice, Restart-PcsvDevice...}
Manifest   1.0.0.0    PKI                                 {Add-CertificateEnrollmentPolicyServer, Export-Certificate, Export-PfxCertificate, Get-CertificateAutoEnr...
Manifest   1.0.0.0    PlatformIdentifier                  Get-PlatformIdentifier
Manifest   1.0.0.0    PnpDevice                           {Get-PnpDevice, Get-PnpDeviceProperty, Enable-PnpDevice, Disable-PnpDevice}
Manifest   1.1.0.0    PowerShellWebAccess                 {Get-PswaAuthorizationRule, Add-PswaAuthorizationRule, Remove-PswaAuthorizationRule, Test-PswaAuthorizati...
Manifest   1.1        PrintManagement                     {Add-Printer, Add-PrinterDriver, Add-PrinterPort, Get-PrintConfiguration...}
Manifest   1.1        PSDesiredStateConfiguration         {Set-DscLocalConfigurationManager, Start-DscConfiguration, Test-DscConfiguration, Publish-DscConfiguratio...
Script     1.0.0.0    PSDiagnostics                       {Disable-PSTrace, Disable-PSWSManCombinedTrace, Disable-WSManTrace, Enable-PSTrace...}
Binary     1.1.0.0    PSScheduledJob                      {New-JobTrigger, Add-JobTrigger, Remove-JobTrigger, Get-JobTrigger...}
Manifest   2.0.0.0    PSWorkflow                          {New-PSWorkflowExecutionOption, New-PSWorkflowSession, nwsn}
Manifest   1.0.0.0    PSWorkflowUtility                   Invoke-AsWorkflow
Manifest   2.0.0.0    RemoteDesktop                       {Get-RDCertificate, Set-RDCertificate, New-RDCertificate, New-RDVirtualDesktopDeployment...}
Manifest   1.0.0.0    ScheduledTasks                      {Get-ScheduledTask, Set-ScheduledTask, Register-ScheduledTask, Unregister-ScheduledTask...}
Manifest   2.0.0.0    SecureBoot                          {Confirm-SecureBootUEFI, Set-SecureBootUEFI, Get-SecureBootUEFI, Format-SecureBootUEFI...}
Manifest   1.0.0.0    SecurityCmdlets                     {Backup-SecurityPolicy, Restore-SecurityPolicy, Backup-AuditPolicy, Restore-AuditPolicy}
Script     1.0.0.0    ServerCore                          {Get-DisplayResolution, Set-DisplayResolution}
Script     2.0.0.0    ServerManager                       {Get-WindowsFeature, Install-WindowsFeature, Uninstall-WindowsFeature, Enable-ServerManagerStandardUserRe...
Cim        1.0.0.0    ServerManagerTasks                  {Get-SMCounterSample, Get-SMPerformanceCollector, Start-SMPerformanceCollector, Stop-SMPerformanceCollect...
Manifest   2.0.0.0    SmbShare                            {Get-SmbShare, Remove-SmbShare, Set-SmbShare, Block-SmbShareAccess...}
Manifest   2.0.0.0    SmbWitness                          {Get-SmbWitnessClient, Move-SmbWitnessClient, gsmbw, msmbw...}
Manifest   2.0.0.0    SoftwareInventoryLogging            {Get-SilComputer, Get-SilComputerIdentity, Get-SilSoftware, Get-SilWindowsUpdate...}
Manifest   1.0.0.0    StartLayout                         {Export-StartLayout, Import-StartLayout, Get-StartApps}
Manifest   2.0.0.0    Storage                             {Add-InitiatorIdToMaskingSet, Add-PartitionAccessPath, Add-PhysicalDisk, Add-TargetPortToMaskingSet...}
Manifest   2.0.0.0    TLS                                 {New-TlsSessionTicketKey, Enable-TlsSessionTicketKey, Disable-TlsSessionTicketKey, Export-TlsSessionTicke...
Manifest   1.0.0.0    TroubleshootingPack                 {Get-TroubleshootingPack, Invoke-TroubleshootingPack}
Manifest   2.0.0.0    TrustedPlatformModule               {Get-Tpm, Initialize-Tpm, Clear-Tpm, Unblock-Tpm...}
Binary     2.1.639.0  UEV                                 {Clear-UevConfiguration, Clear-UevAppxPackage, Restore-UevBackup, Set-UevTemplateProfile...}
Manifest   1.0.0.0    UserAccessLogging                   {Enable-Ual, Disable-Ual, Get-Ual, Get-UalDns...}
Manifest   2.0.0.0    VpnClient                           {Add-VpnConnection, Set-VpnConnection, Remove-VpnConnection, Get-VpnConnection...}
Manifest   1.0.0.0    Wdac                                {Get-OdbcDriver, Set-OdbcDriver, Get-OdbcDsn, Add-OdbcDsn...}
Manifest   1.0.0.0    WebAdministration                   {Start-WebCommitDelay, Stop-WebCommitDelay, Get-WebConfigurationLock, Remove-WebConfigurationLock...}
Manifest   2.0.0.0    Whea                                {Get-WheaMemoryPolicy, Set-WheaMemoryPolicy}
Manifest   1.0.0.0    WindowsDeveloperLicense             {Get-WindowsDeveloperLicense, Unregister-WindowsDeveloperLicense, Show-WindowsDeveloperLicenseRegistration}
Script     1.0        WindowsErrorReporting               {Enable-WindowsErrorReporting, Disable-WindowsErrorReporting, Get-WindowsErrorReporting}
Manifest   1.0.0.0    WindowsSearch                       {Get-WindowsSearchSetting, Set-WindowsSearchSetting}
Manifest   1.0.0.0    WindowsUpdate                       Get-WindowsUpdateLog
```

Definitely more stuff...
Try with:

```powershell
PS C:\users\cyborg4\desktop> Get-Module -ListAvailable | Select-String "8.9.8.9"
```

Nothing. But reading the output of the command without the `Select-String` we see:

```powershell
Manifest   8.9.8.9    bacon                               Get-bacon
```

And the file on the desktop?

```powershell
PS C:\users\cyborg4\desktop> get-childitem


    Directory: C:\users\cyborg4\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:45 AM              0 _eggs
```

Therefore: `cyborg5:bacon_eggs`.

**NB**: Maybe `Get-Module -ListAvailable | ?{$_.Version -like '8.9.8.9'}` was better...

## Cyborg 5

The password for cyborg6 is the last name of the user who has logon hours set on their account **PLUS** the name of the file on the desktop.

**NOTE:**  
– If the last name is “fields” and the file on the desktop is called “\_address”, then the password is “fields_address”.  
– The password will be lowercase no matter how it appears on the screen.

**▼ HINT:**

[https://technet.microsoft.com/en-us/library/ee617195.aspx](https://technet.microsoft.com/en-us/library/ee617195.aspx)

We start with the file on the Desktop:

```powershell
PS C:\users\cyborg5\desktop> Get-ChildItem


    Directory: C:\users\cyborg5\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:45 AM              0 _timer
```

From a previous level, the command

```powershell
PS C:\users\cyborg5\desktop> get-aduser -filter * -properties lastLogon
```

seems promising, but the output is simply overwhelming.
The command:

```powershell
get-aduser -filter * -properties lastLogon | where-object lastLogon -gt 0
```

Seems to improve the output.
The answer:

```powersell
PS C:\users\cyborg5\desktop> Get-ADUser -Filter 'logonHours -like "*"'


DistinguishedName : CN=Administrator,CN=Users,DC=underthewire,DC=tech
Enabled           : True
GivenName         :
Name              : Administrator
ObjectClass       : user
ObjectGUID        : 427058c2-1d57-4e49-a23d-204865b502ae
SamAccountName    : Administrator
SID               : S-1-5-21-758131494-606461608-3556270690-500
Surname           :
UserPrincipalName :

DistinguishedName : CN=Rowray\, Benny  \ ,OU=T-85,OU=X-Wing,DC=underthewire,DC=tech
Enabled           : False
GivenName         : Benny
Name              : Rowray, Benny
ObjectClass       : user
ObjectGUID        : c9aad4f3-3e4f-46b5-84db-2bb7105796dd
SamAccountName    : Benny.Rowray
SID               : S-1-5-21-758131494-606461608-3556270690-1647
Surname           : Rowray
UserPrincipalName : Benny.Rowray
```

Therefore: `cyborg6:rowray_timer`.

## Cyborg 6

The password for cyborg7 is the decoded text of the string within the file on the desktop.

**NOTE:**  
– The password is the last word of the string. For example, if it is “I like PowerShell”, the password would be “powershell”.  
– The password will be lowercase no matter how it appears on the screen.  
– There are no spaces in the answer.

**▼ HINT:**

PowerShell has access to the .Net Framework which can convert text encoding between formats. Find the right system call and you will be able to convert text strings.

```powershell
PS C:\users\cyborg6\desktop> ls


    Directory: C:\users\cyborg6\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----         2/8/2022  10:47 PM             32 cypher.txt


PS C:\users\cyborg6\desktop> cat .\cypher.txt
YwB5AGIAZQByAGcAZQBkAGQAbwBuAA==
```

I suspect that this is Base64 encoding, therefore I look online to decode Base64 strings in PowerShell. Here is what I found:

```powershell
PS C:\users\cyborg6\desktop> $x = cat .\cypher.txt
PS C:\users\cyborg6\desktop> $x
YwB5AGIAZQByAGcAZQBkAGQAbwBuAA==
PS C:\users\cyborg6\desktop> $y = [System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String($x))
PS C:\users\cyborg6\desktop> $y
cybergeddon
```

## Cyborg 7

The password for cyborg8 is the executable name of a program that will start automatically when cyborg7 logs in.

**NOTE:**  
– The password will be lowercase no matter how it appears on the screen.

**▼** **HINT:**

The Run key in the registry seems like a good place to look…

Learn about the registry keys: https://learn.microsoft.com/en-us/powershell/scripting/samples/working-with-registry-keys?view=powershell-7.3.
Still better: https://learn.microsoft.com/en-us/windows/win32/setupapi/run-and-runonce-registry-keys.

The Windows registry includes the following four `Run` and `RunOnce` keys:

- **HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run**
- **HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce**
- **HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run**
- **HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce**

The command

```powershell
Get-ChildItem 'HKLM:\Software\Microsoft\Windows\CurrentVersion'
```

gives an output with

```powershell
...
RADAR                          CLResolutionInterval : 5
                               DisplayInterval      : 1440
run                            SKYNET : C:\program files\SkyNet\skynet.exe
Screensavers
...
```

I guess: `cyborg8:skynet`.

## Cyborg 8

The password for cyborg9 is the Internet zone that the picture on the desktop was downloaded from.

**NOTE:**  
– The password will be lowercase no matter how it appears on the screen.

**▼** **HINT:**

Alternate NTFS data streams contain valuable information. Get information for the item with appropriate parameter to solve this level.

Alternate NTFS data streams:

```powershell
PS C:\users\cyborg8\desktop> Get-Item .\1_qs5nwlcl7f_-SwNlQvOrAw.png -Stream *


PSPath        : Microsoft.PowerShell.Core\FileSystem::C:\users\cyborg8\desktop\1_qs5nwlcl7f_-SwNlQvOrAw.png::$DATA
PSParentPath  : Microsoft.PowerShell.Core\FileSystem::C:\users\cyborg8\desktop
PSChildName   : 1_qs5nwlcl7f_-SwNlQvOrAw.png::$DATA
PSDrive       : C
PSProvider    : Microsoft.PowerShell.Core\FileSystem
PSIsContainer : False
FileName      : C:\users\cyborg8\desktop\1_qs5nwlcl7f_-SwNlQvOrAw.png
Stream        : :$DATA
Length        : 60113

PSPath        : Microsoft.PowerShell.Core\FileSystem::C:\users\cyborg8\desktop\1_qs5nwlcl7f_-SwNlQvOrAw.png:Zone.Identifier
PSParentPath  : Microsoft.PowerShell.Core\FileSystem::C:\users\cyborg8\desktop
PSChildName   : 1_qs5nwlcl7f_-SwNlQvOrAw.png:Zone.Identifier
PSDrive       : C
PSProvider    : Microsoft.PowerShell.Core\FileSystem
PSIsContainer : False
FileName      : C:\users\cyborg8\desktop\1_qs5nwlcl7f_-SwNlQvOrAw.png
Stream        : Zone.Identifier
Length        : 26
```

Read:

```powershell
PS C:\users\cyborg8\desktop> Get-Content .\1_qs5nwlcl7f_-SwNlQvOrAw.png -Stream Zone.Identifier
[ZoneTransfer]
	ZoneId=4
```

Also:

```powershell
PS C:\users\cyborg8\desktop> Get-Content .\1_qs5nwlcl7f_-SwNlQvOrAw.png:Zone.Identifier
[ZoneTransfer]
ZoneId=4
```

Will it be: `cyborg9:4`?

## Cyborg 9

The password for cyborg10 is the first name of the user with the phone number of 876-5309 listed in Active Directory **PLUS** the name of the file on the desktop.

**NOTE:**  
– If the first name “chris” and the file on the desktop is called “23”, then the password is “chris23”.  
– The password will be lowercase no matter how it appears on the screen.

▼ HINT:

https://learn.microsoft.com/en-us/powershell/module/activedirectory/?view=windowsserver2016-ps

```powershell
PS C:\users\cyborg9\desktop> Get-ADUser -Filter * -Properties Name, OfficePhone | Where-Object { $_.OfficePhone -eq '876-5309' }


DistinguishedName : CN=Garick\, Onita  \ ,OU=T-65,OU=X-Wing,DC=underthewire,DC=tech
Enabled           : False
GivenName         : Onita
Name              : Garick, Onita
ObjectClass       : user
ObjectGUID        : 5fc5bb5b-272a-4b70-877a-ed774029e247
OfficePhone       : 876-5309
SamAccountName    : Onita.Garick
SID               : S-1-5-21-758131494-606461608-3556270690-2124
Surname           : Garick
UserPrincipalName : Onita.Garick
```

File on the Desktop:

```powershell
PS C:\users\cyborg9\desktop> Get-ChildItem


    Directory: C:\users\cyborg9\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:45 AM              0 99
```

Then: `cyborg10:onita99`.

**NB**: Far better:

```powershell
Get-AdUser -Filter 'OfficePhone -eq "876-5309"'
```

## Cyborg 10

The password for cyborg11 is the description of the Applocker Executable deny policy for ill_be_back.exe **PLUS** the name of the file on the desktop.

**NOTE:**  
– If the description is “green$” and the file on the desktop is called “28”, then the password is “green$28”.  
– The password will be lowercase no matter how it appears on the screen.

**▼ **HINT:\*\*\*\*

Powershell is a great applockerpolicy tool just go GET it.

```powershell
PS C:\users\cyborg10\desktop> ls


    Directory: C:\users\cyborg10\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:45 AM              0 99
```

Command:

```powershell
PS C:\users\cyborg10\desktop> Get-AppLockerPolicy -Effective -Xml
<AppLockerPolicy Version="1"><RuleCollection Type="Appx" EnforcementMode="NotConfigured" /><RuleCollection Type="Dll" EnforcementMode="NotConfi
gured" /><RuleCollection Type="Exe" EnforcementMode="NotConfigured"><FilePathRule Id="cf7f9744-e5de-4189-8499-236666a32796" Name="C:\Users\cybo
rg10\Documents\ill_be_back.exe" Description="terminated!" UserOrGroupSid="S-1-1-0" Action="Deny"><Conditions><FilePathCondition Path="C:\Users\
cyborg10\Documents\ill_be_back.exe" /></Conditions></FilePathRule></RuleCollection><RuleCollection Type="Msi" EnforcementMode="NotConfigured" /
><RuleCollection Type="Script" EnforcementMode="NotConfigured" /></AppLockerPolicy>
```

Useful, too:

```powershell
PS C:\users\cyborg10\desktop> Get-ChildItem -Path c:\ -Recurse *.exe -ErrorAction SilentlyContinue |  ?{$_.name -eq "ill_be_back.exe"}


    Directory: C:\Users\cyborg10\Documents


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   5:52 AM           4532 ill_be_back.exe
```

Finally:

```powershell
PS C:\users\cyborg10\Desktop> ls


    Directory: C:\users\cyborg10\Desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:45 AM              0 99
```

Therefore: `cyborg11:terminated!99`.

## Cyborg 11

The password for cyborg12 is located in the IIS log. The password is not Mozilla or Opera.

NOTE:
– The password will be lowercase no matter how it appears on the screen.

▼ HINT:
A log is just a file, load the content then search what you are looking for or not what you looking for. Sometimes extra noise is a good thing.

---

Generally, IIS log files are stored in this default path:
`%SystemDrive%\inetpub\logs\LogFiles`

```
PS C:\inetpub\logs\logfiles\w3svc1> pwd

Path
----
C:\inetpub\logs\logfiles\w3svc1

PS C:\inetpub\logs\logfiles\w3svc1> ls


    Directory: C:\inetpub\logs\logfiles\w3svc1


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   5:52 AM        1099641 u_ex160413.log

PS C:\inetpub\logs\logfiles\w3svc1> Get-Content .\u_ex160413.log | Select-String "password"

2016-04-13 04:14:12 W3SVC1 Century 172.31.45.65 GET / - 80 - 172.31.45.65 HTTP/1.1 LordHelmet/5.0+(CombTheDesert)+Password+is:spaceballs - -
century.underthewire.tech 200 0 0 925 118 0
```

`cyborg12:spaceballs`

## Cyborg12

The password for cyborg13 is the first four characters of the base64 encoded full path to the file that started the i_heart_robots service PLUS the name of the file on the desktop.

NOTE:
– An example of a full path would be ‘c:\some_folder\test.exe’.
– Be sure to use ‘unicode’ in your encoding.
– If the encoded base64 is “rwmed2fdreewrt34t” and the file on the desktop is called “_address”, then the password is “rwme_address”.
– The password will be lowercase no matter how it appears on the screen.

▼ HINT:
Remember there are two steps to base64 decode.

---

```
PS C:\users\cyborg12\desktop> Get-ChildItem


    Directory: C:\users\cyborg12\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:45 AM              0 _heart
```

```
PS C:\users\cyborg12\desktop> Get-WmiObject win32_service | ?{$_.Name -like "i_heart_robots"}


ExitCode  : 1077
Name      : i_heart_robots
ProcessId : 0
StartMode : Disabled
State     : Stopped
Status    : OK
```

```
PS C:\users\cyborg12\desktop> Get-WmiObject win32_service | ?{$_.Name -like "i_heart_robots"} | Select-Object *


PSComputerName          : UTW
Name                    : i_heart_robots
Status                  : OK
ExitCode                : 1077
DesktopInteract         : False
ErrorControl            : Normal
PathName                : c:\windows\system32\cmd.exe
ServiceType             : Own Process
StartMode               : Disabled
__GENUS                 : 2
__CLASS                 : Win32_Service
__SUPERCLASS            : Win32_BaseService
__DYNASTY               : CIM_ManagedSystemElement
__RELPATH               : Win32_Service.Name="i_heart_robots"
__PROPERTY_COUNT        : 26
__DERIVATION            : {Win32_BaseService, CIM_Service, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                : UTW
__NAMESPACE             : root\cimv2
__PATH                  : \\UTW\root\cimv2:Win32_Service.Name="i_heart_robots"
AcceptPause             : False
AcceptStop              : False
Caption                 : i_heart_robots
CheckPoint              : 0
CreationClassName       : Win32_Service
DelayedAutoStart        : False
Description             : I be lovin some metal bots!
DisplayName             : i_heart_robots
InstallDate             :
ProcessId               : 0
ServiceSpecificExitCode : 0
Started                 : False
StartName               : LocalSystem
State                   : Stopped
SystemCreationClassName : Win32_ComputerSystem
SystemName              : UTW
TagId                   : 0
WaitHint                : 0
Scope                   : System.Management.ManagementScope
Path                    : \\UTW\root\cimv2:Win32_Service.Name="i_heart_robots"
Options                 : System.Management.ObjectGetOptions
ClassPath               : \\UTW\root\cimv2:Win32_Service
Properties              : {AcceptPause, AcceptStop, Caption, CheckPoint...}
SystemProperties        : {__GENUS, __CLASS, __SUPERCLASS, __DYNASTY...}
Qualifiers              : {dynamic, Locale, provider, UUID}
Site                    :
Container               :
```

```
PS C:\users\cyborg12\desktop> Get-WmiObject win32_service | ?{$_.Name -like "i_heart_robots"} | Select-Object PathName

PathName
--------
c:\windows\system32\cmd.exe
```

Base64 encode & decode in PowerShell: https://adsecurity.org/?p=478

Encoding:
```
$Text = 'This is a secret and should be hidden'
$Bytes = [System.Text.Encoding]::Unicode.GetBytes($Text)
$EncodedText =[Convert]::ToBase64String($Bytes)
$EncodedText
```

Decoding:
```
$EncodedText = "VABoAGkAcwAgAGkAcwAgAGEAIABzAGUAYwByAGUAdAAgAGEAbgBkACAAcwBoAG8AdQBsAGQAIABiAGUAIABoAGkAZABlAG4A"
$DecodedText = [System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String($EncodedText))
$DecodedText
```

Therefore:
```
PS C:\users\cyborg12\desktop> Get-WmiObject win32_service | ?{$_.Name -like "i_heart_robots"} | Select-Object PathName

PathName
--------
c:\windows\system32\cmd.exe


PS C:\users\cyborg12\desktop> $Bytes = [System.Text.Encoding]::Unicode.GetBytes("c:\windows\system32\cmd.exe")
PS C:\users\cyborg12\desktop> $EncodedText =[Convert]::ToBase64String($Bytes)
PS C:\users\cyborg12\desktop> $EncodedText
YwA6AFwAdwBpAG4AZABvAHcAcwBcAHMAeQBzAHQAZQBtADMAMgBcAGMAbQBkAC4AZQB4AGUA
```

The guess:
`cyborg13:ywa6_heart`

## Cyborg13

The password cyborg14 is the number of days the refresh interval is set to for DNS aging for the underthewire.tech zone PLUS the name of the file on the desktop.

NOTE:
– If the days are set to “08:00:00:00” and the file on the desktop is called “_tuesday”, then the password is “8_tuesday”.
– The password will be lowercase no matter how it appears on the screen.

▼ HINT:
WMI or cmdlets… choices, choices.

---

```
PS C:\users\cyborg13\desktop> Get-ChildItem


    Directory: C:\users\cyborg13\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:45 AM              0 _days
```

```
PS C:\users\cyborg13\desktop> Get-DnsServerZoneAging

cmdlet Get-DnsServerZoneAging at command pipeline position 1
Supply values for the following parameters:
Name[0]:
PS C:\users\cyborg13\desktop> Get-DnsServerZoneAging underthewire.tech


ZoneName             : underthewire.tech
AgingEnabled         : True
AvailForScavengeTime : 9/21/2018 10:00:00 AM
RefreshInterval      : 22.00:00:00
NoRefreshInterval    : 7.00:00:00
ScavengeServers      :


PS C:\users\cyborg13\desktop> Get-DnsServerZoneAging underthewire.tech | Select-Object *


ScavengeServers       :
AgingEnabled          : True
AvailForScavengeTime  : 9/21/2018 10:00:00 AM
NoRefreshInterval     : 7.00:00:00
RefreshInterval       : 22.00:00:00
ZoneName              : underthewire.tech
PSComputerName        :
CimClass              : root/Microsoft/Windows/DNS:DnsServerZoneAging
CimInstanceProperties : {AgingEnabled, AvailForScavengeTime, NoRefreshInterval, RefreshInterval...}
CimSystemProperties   : Microsoft.Management.Infrastructure.CimSystemProperties
```

`cyborg14:22_days`

## Cyborg14

The password for cyborg15 is the caption for the DCOM application setting for application ID {59B8AFA0-229E-46D9-B980-DDA2C817EC7E} PLUS the name of the file on the desktop.

NOTE:
– If the caption is “dcom” and the file on the desktop is called “_address”, then the password is “dcom_address”.
– The password will be lowercase no matter how it appears on screen.

▼ HINT:
win32_DCOMApplicationSetting

---

```
PS C:\users\cyborg14\desktop> Get-ChildItem


    Directory: C:\users\cyborg14\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:45 AM              0 _objects
```

```
PS C:\users\cyborg14\desktop> Get-WmiObject Win32_DCOMApplicationSetting | ?{$_.AppID -like "{59B8AFA0-229E-46D9-B980-DDA2C817EC7E}"}


__GENUS                   : 2
__CLASS                   : Win32_DCOMApplicationSetting
__SUPERCLASS              : Win32_COMSetting
__DYNASTY                 : CIM_Setting
__RELPATH                 : Win32_DCOMApplicationSetting.AppID="{59B8AFA0-229E-46d9-B980-DDA2C817EC7E}"
__PROPERTY_COUNT          : 12
__DERIVATION              : {Win32_COMSetting, CIM_Setting}
__SERVER                  : UTW
__NAMESPACE               : root\cimv2
__PATH                    : \\UTW\root\cimv2:Win32_DCOMApplicationSetting.AppID="{59B8AFA0-229E-46d9-B980-DDA2C817EC7E}"
AppID                     : {59B8AFA0-229E-46d9-B980-DDA2C817EC7E}
AuthenticationLevel       :
Caption                   : propshts
CustomSurrogate           :
Description               : propshts
EnableAtStorageActivation : False
LocalService              :
RemoteServerName          :
RunAsUser                 :
ServiceParameters         :
SettingID                 :
UseSurrogate              : False
PSComputerName            : UTW
```

```
PS C:\users\cyborg14\desktop> Get-WmiObject Win32_DCOMApplicationSetting | ?{$_.AppID -like "{59B8AFA0-229E-46D9-B980-DDA2C817EC7E}"} | Select-O
bject Caption

Caption
-------
propshts
```

`cyborg15:propshts_objects`

## Cyborg15

Congratulations!

You have successfully made it to the end!

Try your luck with other games brought to you by the Under The Wire team.

Thanks for playing!

## Links

- For extreme help: [https://cybertuna.gitbook.io/underthewire/cyborg/cyborg-10-greater-than-15](https://cybertuna.gitbook.io/underthewire/cyborg/cyborg-10-greater-than-15).
