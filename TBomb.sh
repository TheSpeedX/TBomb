#!/bin/bash

detect_os() {
    if [ -e $PREFIX/bin/termux-info ]; then
        OS="TERMUX"
    else
        OS="LINUX"
    fi
}

pause() {
    read -n1 -r -p "Press any key to continue..." key
}
banner() {
    clear
    echo -e "\e[1;31m"
    if ! [ -x "$(command -v figlet)" ]; then
        echo 'Introducing TBomb'
    else
        figlet TBomb
    fi
    if ! [ -x "$(command -v toilet)" ]; then
        echo -e "\e[4;34m This Bomber Was Created By \e[1;32mSpeedX \e[0m"
    else
        echo -e "\e[1;34mCreated By \e[1;34m"
        toilet -f mono12 -F border SpeedX
    fi
    echo -e "\e[1;34m For Any Queries Mail Me!!!\e[0m"
    echo -e "\e[1;32m           Mail: ggspeedx29@gmail.com \e[0m"
    echo -e "\e[4;32m   YouTube: https://www.youtube.com/c/GyanaTech \e[0m"
    echo " "
    pause
}

init_environ(){
    if [ $OS = "TERMUX" ]; then
        PYTHON="python"
        PIP="python -m pip"
        PKG="pkg"
    elif [ $OS = "LINUX" ]; then
        PYTHON="python3"
        PIP="python3 -m pip"
        PKG="apt"
    fi
}

install_deps(){
    $PKG install -y figlet
    $PKG install -y curl
    $PKG install -y openssl
    $PKG install -y git
    $PKG install -y $PYTHON
    $PKG install -y $PYTHON-pip
    $PIP install -r requirements.txt    
}

banner
detect_os
init_environ
if [ -e .update ];then
    echo "All Requirements Found...."
else
    echo 'Installing Requirements....'
    echo .
    echo .
    install_deps
    echo This Script Was Made By SpeedX > .update
    echo 'Requirements Installed....'
    pause
fi
while :
do
    banner
    echo -e "\e[4;31m Please Read Instruction Carefully !!! \e[0m"
    echo " "
    echo "Press 1 To  Start SMS  Bomber "
    echo "Press 2 To  Start CALL Bomber "
    echo "Press 3 To  Start MAIL Bomber "
    echo "Press 4 To  Update (Works On Linux And Linux Emulators) "
    echo "Press 5 To  Exit "
    read ch
    clear
    if [ $ch -eq 1 ];then
        $PYTHON bomber.py --sms
        exit
    elif [ $ch -eq 2 ];then
        $PYTHON bomber.py --call
        exit
    elif [ $ch -eq 3 ];then
        $PYTHON bomber.py --mail
        exit
    elif [ $ch -eq 4 ];then
        echo -e "\e[1;34m Downloading Latest Files..."
        rm -f .update
        git reset --hard HEAD
        git pull --force
        echo -e "\e[1;32m TBomb Has Been Updated..."
        echo -e "\e[1;32m All The Required Packages Will Be Installed..."
        echo -e "\e[1;34m RUNNING TBomb Again..."
        pause
        ./TBomb.sh
        exit
    elif [ $ch -eq 5 ];then
        banner
        exit
    else
        echo -e "\e[4;32m Invalid Input !!! \e[0m"
        pause
    fi
done
