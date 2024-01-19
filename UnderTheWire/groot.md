# Groot

## Groot0

The goal of this level is to log into the game. Do the following in order to achieve this goal.

1. Obtain the initial credentials via the #StartHere channel on our Slack (link). Once you are in the channel, scroll to the top to see the credentials.

2. After obtaining the credentials, connect to the server via SSH. You will need an SSH client such as Putty. The host that you will be connecting to is groot.underthewire.tech, on port 22.

3. When prompted, use the credentials for the applicable game found in the #StartHere Slack channel.

4. You have successfully connected to the game server when your path changes to “PS C:\Users\Groot1\desktop>”.

---

`groot1:groot1`

## Groot1

The password for groot2 is the last five alphanumeric characters of the MD5 hash of this system’s hosts file.

NOTE:
– The password will be lowercase no matter how it appears on the screen.

IMPORTANT:
Once you feel you have completed the Groot1 challenge, start a new connection to the server, and log in with the username of Groot2 and this password will be the answer from Groot1. If successful, close out the Groot1 connection and begin to solve the Groot2 challenge. This concept is repeated over and over until you reach the end of the game.

---

```
Get-FileHash <filepath> -Algorithm MD5
```

The hosts file in Windows is

```
C:\Windows\System32\drivers\etc\hosts
```

```
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
