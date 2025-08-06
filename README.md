<h1>Python - Basic Keylogger</h1>

 <h2>DISCLAIMER</h2>
This tool is for educational and ethical cybersecurity research only. Do not use this software on any system you do not own or have explicit permission to test. The author is not responsible for any misuse of the code.
<br />

<h2>Description</h2>
Project consists of a simple Python script that records all keys the user inputs while it is running, this type of software is better known as a Keylogger. Once the script is run it will record all keys pressed, with the exceptions of certain special characters such as the arrow keys, and stores them in a string value called "log". The script will run until the esc key is pressed, after which all the data in "log" will be entered into the "KeyloggerOutput.txt" file.
<br />

<h2>Features</h2>
The script handles the input of specific special characters including: Space, Backspace, Enter, and Esc. All other special characters are ignored to reduce the clutter in the log file.
<br />
This Python script is not obfuscated and doesn't attempt to hide itself, as using a keylogger on someone's device without their knowledge or consent is illegal.
<br />

<h2>Installation/Usage</h2>
Download the Keylogger.py file from this repo
<br />
Install Python, Which can be done here: https://www.python.org/downloads/
<br />
Install the pynput library, which can be done with the command "pip install pynput"
<br />
