<h1 align="center">
  <br>
  <a href="https://github.com/TheSpeedX/TBomb"><img src="https://i.ibb.co/F4HBKqm/TBomb.png" alt="TBomb"></a>
  <br>
  TBomb v2.1b
  <br>
</h1>


<p align="center">A free and open-source SMS/Call bombing application</p>

## NOTE:


> **Due to the overuse of script, a bunch of APIs have been taken offline. It is okay if you do not receive all the messages.**


- The application requires active internet connection to contact the APIs
- You would not be charged for any SMS/calls dispatched as a consequence of this script
- For best performance, use single thread with considerable delay time
- Always ensure that you are using the latest version of TBomb and have Python 3
- This application must not be used to cause harm/discomfort/trouble to others
- By using this, you agree that you cannot hold the contributors responsible for any misuse

## Compatibility
Check your Python version by typing in
```shell script
$ python --version
```
If you get the following
```shell script
Python 3.8.3
```
or any version greater than or equal to 3.4, this script has been tested and confirmed to be supported. For obsolete versions of Python (eg 2.7), use discretion while executing the script as it has not been tested there.

## Features

- Over 15 integrated messaging and calling APIs included with JSON
- Unlimited (with abuse protection) and super-fast bombing with multithreading
- Possibility of international API support (APIs are offline)
- Flexible with addition of newer APIs with the help of JSON documents
- Actively supported by the developers with frequent updates and bug-fixes
- Intuitive auto-update feature and notification fetch feature included
- Recently made free and open-source for community contributions
- Modular codebase and snippets can be easily embedded in other program


## Usage:

### Install by PIP (Recommended)

Before continuing make sure following requirements are satisfied:

- Python version greater than or equal to 3.4 is installed
- pip is installed for Python 3

Install `tbomb` package by running:

```shell script
pip3 install tbomb
```

Run TBomb by just typing:
```shell script
tbomb
```

### Install from GIT

#### NOTE 

Git installation methods are not universal and are likely to differ between distributions so installing Git as per the given instructions below may not work. Please check out how to install Git for your Linux distribution [here](https://git-scm.com/). Commands below provide instructions for Debian-based systems.

>Running `TBomb.sh` as sudo miscofigures files ownership. It is recommended not to run it as sudo

Run these commands to clone and run TBomb.

#### For Termux

To use the bomber type the following commands in Termux:
```shell script
pkg install git -y 
pkg install python -y 
git clone https://github.com/TheSpeedX/TBomb.git
cd TBomb
./TBomb.sh
```

#### For iSH

To use the application, type in the following commands in iSH.
```shell script
apk add git
apk add python3
apk add py3-pip
apk add ruby
gem install toilet
git clone https://github.com/TheSpeedX/TBomb.git
cd TBomb
pip3 install -r requirements.txt
chmod +x TBomb.sh
./TBomb.sh
```

#### For Debian-based GNU/Linux distributions

To use the application, type in the following commands in GNU/Linux terminal.
```shell script
sudo apt install git
git clone https://github.com/TheSpeedX/TBomb.git
cd TBomb
bash TBomb.sh
```

#### For MacOS

To use the application, type in the following commands in MacOS terminal:

##### Install Brew

```shell script
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
````

##### Install dependencies:

```shell script
brew install git
brew install python3
sudo easy_install pip
sudo pip install --upgrade pip
git clone https://github.com/TheSpeedX/TBomb.git
cd TBomb
bash TBomb.sh
```


##### Missing Tools on MacOS

The package `toilet` cannot be installed yet on macOS. But TBomb does still work.

### Demonstrative Video:

- Watch Indian Bombing Method [here](https://youtu.be/9KWkwsr_QGw)  
- Watch International Bombing Method [here](https://youtu.be/JqsHkyIcnPM).  

## Contributors

- Catch **[t0xic0der](https://github.com/t0xic0der)** at https://atlasdoc.netlify.app
- Check **[Avinash](https://github.com/AvinashReddy3108)** at https://github.com/AvinashReddy3108
- Mail **[scpketer](https://github.com/scpketer)** at scpketer@protonmail.ch
- Mail **[0n1cOn3](https://github.com/0n1cOn3)** at 0n1cOn3@gmx.ch
- Ping **Rieltar** at https://t.me/RieltarReborn


### Donators:

- **[34D30Y](34db0y@protonmail.com)**
- **SC AMAN**

### TODO:

- [x] Make Code More Readable and Extensible
- [ ] Add More Mail Spam APIs
- [ ] Add More SMS Spam APIs
- [ ] Add More Call Spam APIs
- [ ] Resolve threading issue in some devices

## FAQ

**Q:** Is there any TBomb Website/App ?

**A:** There is no official website/app yet.The only official releases of TBomb are published in [Github](https://github.com/TheSpeedX/TBomb) and [PyPi](https://pypi.org/project/tbomb)
##
**Q:** Poor Internet Connection Detected:

**A:** Here are a few stuff you can try:
- Check your connection.
- Make sure `openssl` is installed.
- Try to `ping` any remote site/address to be sure.
- Try to reinstall if nothing works.
##
**Q:** Do you support "X" Country?

**A:** Most Countries are supported for SMS and only India for calls. The SMS delivery rate might be different for different countries.
##
**Q:** Can you add support for "X" Country?

**A:** We do what we can, but we cannot promise. Please stay tuned for future support. If you are ready to help then maybe we can do faster.
##
**Q:** Why is the limit so low?

**A:** Due the amount of requests, the APIs can die. To prevent a bigger outtake of TBomb, it has been limited. 
##
**Q:** Help, I got the error that the requirements aren't installed, even when the installer has successfully reached the main menu

**A:** First, make sure `python3` and `pip3` are installed. 
- The Easy Method:  
   `pip3 install tbomb`  
    Then execute by simply running `tbomb`
- The Git Method:  
    Clone the repo and Switch to the TBomb Directory and execute this command:  
    `pip3 install -r requirements.txt`
##
**Q:** Help, It says `command 'tbomb' not found` after installing PIP version!

**A:** Try running `sudo pip3 install tbomb`
##
**Q:** Help, I can't execute TBomb.sh!

**A:** Run TBomb Directly with `python3 bomber.py`
##
**Q:** Should I use VPN? 

**A:** No, If you are facing high fail rate as TBomb can fail due the high response time or API restrictions.
##
**Q:** How to get protection ?

**A:** Use OTP blockers and activate DND.
##
**Q:** Why does it fail?

**A:** Due to the overuse of script, a bunch of APIs have been taken offline. It is okay if you do not receive all the messages.
##
### Support

For Queries: [Telegram Group](https://t.me/TBombChat)  
Contributions, issues, and feature requests are welcome!  
Give a ★ if you like this project!

<p align="right"> Last FAQ Update: 08.08.2021 </p>
