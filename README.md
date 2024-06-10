<a id="top"></a>
<h1 align="center">
  <br>
  <a href="https://github.com/xpierroz/EZKey"><img src="assets/supergif.gif" width=300 weigth=400 alt="R"></a>
  <br>
 EZKey
</h1>

<div align="center">
    <strong>
        POC | FUD KeyLogger made with Python 
    </strong>
    <p>by <a href="https://github.com/xpierroz">pierro</a></p>
    <hr style="border-radius: 2%; margin-top: 60px; margin-bottom: 60px;" noshade="" size="20" width="100%">
    <br><br>
</div>

### Introduction

EZKey is a POC made to demonstrate how a simple Python program is able to steal the keyboard activity from someone while passing most of the antivirus protections. 

### Features

- FUD (fully undetectable)
- Encrypting the data
- Sending the data to your Discord Webhook

### How to use

- Download this repository and extract it.
- Start client.py and create the payload
- Then, the payload (ezkey.pyw) will be modified with your webhook
- Edit the payload's name, and compile it (not necessary)
- Send the payload to your victim


### How does it work

Once the victim executes the payload, it will start the keylogger in the background. Every keys will be recorded and saved to MatPlot.cache. Everytime the maxlen var (chosed by the user when creating the payload) is reached, the keylogger will send a file containing the data to the webhook. The data will be encrypted to integers, so it will be harder to detect it.


### Virus Total analyze

![VirusTotal](assets/virustotal.png)

### Warning

This program is made explicity for educational & research purposes only.
Do not use for malicious purposes.
I am not responsible for any of your actions!

<p align="center"><a href=#top>Back to Top</a></p>