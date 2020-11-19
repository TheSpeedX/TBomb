<h1 align="center">
  <br>
  <a href="https://github.com/TheSpeedX/TBomb"><img src="https://i.ibb.co/F4HBKqm/TBomb.png" alt="TBomb"></a>
  <br>
  TBomb v2.0b
  <br>
</h1>


<p align="center">A free and open-source SMS/Call bombing application for GNU/Linux And Termux</p>

## Note:


> ## Deprecation Warning:
> **All TBomb versions below v2.0 will no longer work after 14-11-2020.**  
**All TBomb users need to update to v2.0 ASAP**

**Due to overuse of script, a bunch APIs have been taken offline. It is okay if you do not receive all the messages.**


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

### NOTE 

Git installation methods are not universal and are likely to differ between distributions so installing Git as per the given instructions below may not work. Please check out how to install Git for your Linux distribution [here](https://git-scm.com/). Commands below provide instructions for Debian-based systems.

>Ruuning `TBomb.sh` as sudo miscofigures files ownership. It is recommended not to run it as sudo

Run these commands to clone and run TBomb.

### For Termux

To use the bomber type the following commands in Termux:
```shell script
pkg install git -y 
pkg install python -y 
git clone https://github.com/TheSpeedX/TBomb.git
cd TBomb
./TBomb.sh
```

### For iSH

To use the application, type in the following commands in iSH.
```shell script
apk add git
apk add python3
apk add py3-pip
git clone https://github.com/TheSpeedX/TBomb.git
cd TBomb
pip3 install -r requirements.txt
chmod +x TBomb.sh
./TBomb.sh
```

### For Debian-based GNU/Linux distributions

To use the application, type in the following commands in GNU/Linux terminal.
```shell script
sudo apt install git
git clone https://github.com/TheSpeedX/TBomb.git
cd TBomb
bash TBomb.sh
```

### For MacOS

To use the application, type in the following commands in MacOS terminal:

#### Install Brew

```shell script
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
````

#### Install dependencies:

```shell script
brew install git
brew install python3
sudo easy_install pip
sudo pip install --upgrade pip
git clone https://github.com/TheSpeedX/TBomb.git
cd TBomb
```

#### Run TBomb

```shell script
bash TBomb.sh
```

#### Missing Tools on MacOS & iSH App

The package `toilet` cannot be installed yet. But TBomb does still work.

## Demonstrative Video:

- Watch Indian Bombing Method [here](https://youtu.be/9KWkwsr_QGw)  
- Watch International Bombing Method [here](https://youtu.be/JqsHkyIcnPM).  

## Contributors

- **[SpeedX](https://github.com/TheSpeedX)**<br>
[X] Join at: https://t.me/TBombChat

- **[t0xic0der](https://github.com/t0xic0der)**<br>
[X] Catch at: https://atlasdoc.netlify.app

- **[Avinash](https://github.com/AvinashReddy3108)**<br>
[X] Check at: https://github.com/AvinashReddy3108

- **[scpketer](https://github.com/scpketer)**<br>
[X] Mail At: scpketer@protonmail.ch

- **[Stefan](https://github.com/0n1cOn3)**<br>
[X] Mail at: 0n1cOn3@gmx.ch

- **Rieltar**<br>
[X] Ping at: https://t.me/RieltarReborn


## Donators:

* **[@] 34D30Y (34db0y@protonmail.com)**
* **[@] SC AMAN**

## TODO:

- [x] Make Code More Readable and Extensible
- [ ] Add Mail Spam Module
- [x] Add Update Feature using git
- [ ] Add Update Feature without git (download tarball and extract)
- [ ] Split code into multiple files (after Deprecation)


## Contact me

Feel free to open an issue  


For Queries: [Telegram Group](https://t.me/TBombChat)  
[Check Out My YouTube Channel](https://www.youtube.com/c/GyanaTech)

