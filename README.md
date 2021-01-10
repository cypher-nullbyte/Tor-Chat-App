# Tor Chat Application

A simple application that allows safe and private communication between a group of individuals through the Tor network.

The usage is simple clone this repository on the client and server machine. Then follow the Setup instruction:

# Usage

Watch the following youtube video with the tutorial on how to use the Tor Chat app:

[![Video Tutorial](https://i9.ytimg.com/vi/mcoticbMe_Q/mqdefault.jpg?time=1610307600000&sqp=CJCw7f8F&rs=AOn4CLDEG_f42KJ0AdfmILWpAf8F1mpYhA)](https://www.youtube.com/watch?v=mcoticbMe_Q)

Or access https://www.youtube.com/watch?v=mcoticbMe_Q

# Setup

## Requirements:

python3 is required in order to run this app.

it is also recommended the use of pip

## Installing requirements:

Install requirements:

```bash
pip install -r requirements.txt
```

### Install pycurl on ubuntu:

```bash
sudo apt install python3-pycurl
```

### Install tkinter on ubuntu:

```bash
sudo apt-get install python3-tk 
```

### Install pycurl on MacOS:

 - First you need to install OpenSSL via Homebrew:
 
```bash
$ brew install openssl
```

 - Curl is normally already installed in MacOs, but to be sure it uses OpenSSL, we need to install it using brew:
```bash
$ brew install curl-openssl
```
 - Curl is installed keg-only by brew. This means that is installed but not linked. Therefore, we need to instruct pip to use the recently installed curl before installing pycurl. We can do this permanently by changing our bash_profile:
```bash
$ echo 'export PATH="/usr/local/opt/curl-openssl/bin:$PATH"' >> ~/.bash_profile
```
 - Or temporary in the current shell:
```bash
$ export PATH="/usr/local/opt/curl-openssl/bin:$PATH"
```
 - Then, we need to install pycurl as follows:
```bash
$ PYCURL_SSL_LIBRARY=openssl LDFLAGS="-L/usr/local/opt/openssl/lib" CPPFLAGS="-I/usr/local/opt/openssl/include" pip install --no-cache-dir pycurl
```

## Install tor:

### Mac

```bash
brew install tor
```

### Ubuntu 

```bash
sudo apt-get install tor
```

### Configure the file torrc

On mac you might find it on '/usr/local/etc/tor/torrc', and on ubuntu '/etc/tor/torrc'.
Insert these lines on the file:

```
ControlPort 9051

CookieAuthentication 1

HashedControlPassword 16:E600ADC1B52C80BB6022A0E999A7734571A451EB6AE50FED489B72E3DF
```
 
 
# Running:

### Initiate Tor:

Kill any previously existing Tor instance:
```bash
sudo killall tor
```

Initiate tor:
```bash
tor
```

### On server side:

#### In order to initialize the chat app, you will need to set a hidden service.

To do that run:

```bash
python create_hidden_service.py
```

#### Now on the same machine running the hidden service run the message server:

```bash
python message_server.py
```

### On client side:

#### Now every machine that wants to join the chat just need to run the chat app and fill with the hidden service information:

```bash
python chat_app.py
```
