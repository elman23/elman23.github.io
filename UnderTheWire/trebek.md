# Trebek

https://underthewire.tech/trebek

## Trebek 0 -> 1

### Task

The goal of this level is to log into the game. Do the following in order to achieve this goal.

1. Obtain the initial credentials via the #StartHere channel on our Slack (Link). Once you are in the channel, scroll to the top to see the credentials.

2. After obtaining the credentials, connect to the server via SSH. You will need an SSH client such as Putty. The host that you will be connecting to is trebek.underthewire.tech, on port 22.

3. When prompted, use the credentials for the applicable game found in the #StartHere Slack channel.

4. You have successfully connected to the game server when your path changes to “PS C:\Users\Trebek1\desktop>”.

### Solution

Simply use the credentials `trebek1:trebek1` to login via SSH into the server:

```bash
ssh trebek1@trebek.underthewire.tech
```

## Trebek 1 -> 2

### Task

The password for trebek2 is the name of the script referenced in a deleted task as depicted in the event logs on the desktop.

NOTE:
– Don’t include the file extension (i.e.- .vbs)
– The password will be lowercase no matter how it appears on the screen.

IMPORTANT:
Once you feel you have completed the Trebek1 challenge, start a new connection to the server, and log in with the username of Trebek2 and this password will be the answer from Trebek1. If successful, close out the Trebek1 connection and begin to solve the Trebek2 challenge. This concept is repeated over and over until you reach the end of the game.

▼ HINT:
https://msdn.microsoft.com/en-us/powershell/reference/5.1/microsoft.powershell.diagnostics/get-winevent

▼ HINT:
You may want to look at what data is available on a typical log containing this data…

### Solution

```powershell
PS C:\users\trebek1\desktop> Get-WinEvent -Path "security.evtx" | Where-Object -Property Message -Match 'deleted' | Format-Table Id, File


TimeCreated  : 5/11/2017 8:10:49 PM
ProviderName : Microsoft-Windows-Security-Auditing
Id           : 4699
Message      : A scheduled task was deleted.

               Subject:
                Security ID:            S-1-5-21-3968311752-1263969649-2303472966-500
                Account Name:           Administrator
                Account Domain:         UNDERTHEWIRE
                Logon ID:               0x338C9

               Task Information:
                Task Name:              \Bitvise\Persistent BvSshServer Control
               Panel\S-1-5-21-3968311752-1263969649-2303472966-500
                Task Content:           <?xml version="1.0" encoding="UTF-16"?>
               <Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
                 <RegistrationInfo />
                 <Triggers>
                   <LogonTrigger>
                     <Enabled>true</Enabled>
                     <UserId>UNDERTHEWIRE\Administrator</UserId>
                   </LogonTrigger>
                 </Triggers>
                 <Principals>
                   <Principal id="Author">
                     <RunLevel>HighestAvailable</RunLevel>
                     <UserId>UNDERTHEWIRE\Administrator</UserId>
                     <LogonType>InteractiveToken</LogonType>
                   </Principal>
                 </Principals>
                 <Settings>
                   <MultipleInstancesPolicy>Parallel</MultipleInstancesPolicy>
                   <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>
                   <StopIfGoingOnBatteries>false</StopIfGoingOnBatteries>
                   <AllowHardTerminate>false</AllowHardTerminate>
                   <StartWhenAvailable>true</StartWhenAvailable>
                   <RunOnlyIfNetworkAvailable>false</RunOnlyIfNetworkAvailable>
                   <IdleSettings>
                     <Duration>PT10M</Duration>
                     <WaitTimeout>PT1H</WaitTimeout>
                     <StopOnIdleEnd>true</StopOnIdleEnd>
                     <RestartOnIdle>false</RestartOnIdle>
                   </IdleSettings>
                   <AllowStartOnDemand>false</AllowStartOnDemand>
                   <Enabled>true</Enabled>
                   <Hidden>false</Hidden>
                   <RunOnlyIfIdle>false</RunOnlyIfIdle>
                   <WakeToRun>false</WakeToRun>
                   <ExecutionTimeLimit>PT0S</ExecutionTimeLimit>
                   <Priority>6</Priority>
                 </Settings>
                 <Actions Context="Author">
                   <Exec>
                     <Command>C:\Program Files\Bitvise SSH Server\BssCtrl.exe</Command>
                     <Arguments>-startMinimized</Arguments>
                   </Exec>
                 </Actions>
               </Task>


...

TimeCreated  : 5/10/2017 12:08:29 PM
ProviderName : Microsoft-Windows-Security-Auditing
Id           : 4699
Message      : A scheduled task was deleted.

               Subject:
                Security ID:            S-1-5-21-3968311752-1263969649-2303472966-1135
                Account Name:           trebek1
                Account Domain:         UNDERTHEWIRE
                Logon ID:               0x644A01

               Task Information:
                Task Name:              \cleanup mess
                Task Content:           <?xml version="1.0" encoding="UTF-16"?>
               <Task version="1.3" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
                 <RegistrationInfo />
                 <Triggers>
                   <CalendarTrigger>
                     <StartBoundary>2017-05-10T01:00:00</StartBoundary>
                     <Enabled>true</Enabled>
                     <RandomDelay>P0DT0H0M0S</RandomDelay>
                     <ScheduleByDay>
                       <DaysInterval>1</DaysInterval>
                     </ScheduleByDay>
                   </CalendarTrigger>
                 </Triggers>
                 <Settings>
                   <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy>
                   <DisallowStartIfOnBatteries>true</DisallowStartIfOnBatteries>
                   <StopIfGoingOnBatteries>true</StopIfGoingOnBatteries>
                   <AllowHardTerminate>true</AllowHardTerminate>
                   <StartWhenAvailable>false</StartWhenAvailable>
                   <RunOnlyIfNetworkAvailable>false</RunOnlyIfNetworkAvailable>
                   <IdleSettings>
                     <Duration>PT10M</Duration>
                     <WaitTimeout>PT1H</WaitTimeout>
                     <StopOnIdleEnd>true</StopOnIdleEnd>
                     <RestartOnIdle>false</RestartOnIdle>
                   </IdleSettings>
                   <AllowStartOnDemand>true</AllowStartOnDemand>
                   <Enabled>true</Enabled>
                   <Hidden>false</Hidden>
                   <RunOnlyIfIdle>false</RunOnlyIfIdle>
                   <DisallowStartOnRemoteAppSession>false</DisallowStartOnRemoteAppSession>
                   <UseUnifiedSchedulingEngine>true</UseUnifiedSchedulingEngine>
                   <WakeToRun>false</WakeToRun>
                   <ExecutionTimeLimit>PT72H</ExecutionTimeLimit>
                   <Priority>7</Priority>
                 </Settings>
                 <Actions Context="Author">
                   <Exec>
                     <Command>C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe</Command>
                     <Arguments>-NonInteractive -NoLogo -NoProfile -File
               'c:\users\trebek1\mess_cleaner.ps1'</Arguments>
                   </Exec>
                 </Actions>
                 <Principals>
                   <Principal id="Author">
                     <UserId>UNDERTHEWIRE\trebek1</UserId>
                     <LogonType>InteractiveToken</LogonType>
                     <RunLevel>LeastPrivilege</RunLevel>
                   </Principal>
                 </Principals>
               </Task>
```

Credentials: `trebek2:mess_cleaner`.

## Trebek 2 -> 3

## Trebek 3 -> 4

## Trebek 4 -> 5

## Trebek 5 -> 6

## Trebek 6 -> 7

## Trebek 7 -> 8

## Trebek 8 -> 9

## Trebek 9 -> 10

## Trebek 10 -> 11

## Trebek 11 -> 12

## Trebek 12 -> 13

## Trebek 13 -> 14

## Trebek 14 -> 15
