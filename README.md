<h1 align="center">
  Python P2P Crypt Chat App
</h1>

<h4 align="center">Chat over <a href="https://en.wikipedia.org/wiki/Berkeley_sockets">Berkeley Sockets</a> with encryption, p2p and over internet (needs port fowarding).</h4>

<p align="center">
  <a href="#about">About</a> •
  <a href="#features">Features</a> •
  <a href="#usage">Usage</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>

![cefet](https://i.imgur.com/K0E5iFC.jpg)

## About

This is a simple python program made for university work. It uses python socket, threads and a encryption package. This program uses P2P and client-server architecture.

## Features

* Interactive Chat
  * Send and view replies.
* Multi-client
  * Create a lobby with your friends
* P2P
  * Run your own server and client to make a direct connection with another clients
* Encryption
  * Make your messages safe with [fernet](https://github.com/pyca/cryptography).

## Usage

To run this program you will need [git](https://git-scm.com/), [python](https://www.python.org/), [request](https://github.com/psf/requests), [cryptography](https://github.com/pyca/cryptography). On your console:

```bash
# Clone the repository
git clone https://github.com/cassiofb-dev/python-p2p-crypt-chat

# Go inside
cd python-p2p-crypt-chat

# Install dependencies
pip install requests
pip install cryptography

# run application
py p2p.py
```

![usage](https://i.imgur.com/9nBRiJe.gif)

## Credits

This app uses the following open source projects:

* [Git](https://github.com/git/git)
* [Python](https://www.python.org/)
* [Requests](https://github.com/psf/requests)
* [Cryptography](https://github.com/pyca/cryptography)

## License

MIT

---

> [Acesse meu site](https://cassiofernando.netlify.app/) &nbsp;&middot;&nbsp;
> GitHub [@cassiofb-dev](https://github.com/cassiofb-dev) &nbsp;&middot;&nbsp;
> Twitter [@cassiofb_dev](https://twitter.com/cassiofb_dev)
