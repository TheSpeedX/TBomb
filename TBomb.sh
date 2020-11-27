#!/bin/bash

detect_distro() {
    if [ -z "$distro" ]; then
        distro=$(ls /etc | awk 'match($0, "(.+?)[-_](?:release|version)", groups) {if(groups[1] != "os") {print groups[1]}}')
    fi

    if [ -z "$distro" ]; then
        if [[ "$OSTYPE" == linux-android* ]]; then
            distro="termux"
        elif [ -f "/etc/os-release" ]; then
            distro="$(source /etc/os-release && echo $ID)"
        elif [ "$OSTYPE" == "darwin" ]; then
            distro="darwin"
        else 
            distro="invalid"
        fi
    fi
}

pause() {
    read -n1 -r -p "Press any key to continue..." key
}
banner() {
    clear
    echo -e "\e[1;31m"
    if ! [ -x "$(command -v figlet)" ]; then
        echo 'Presenting The interesting project'
        echo """
     ████████╗   ██████╗  ██████╗  ██████╗ ███╗   ███╗
     ╚══██╔══╝   ██╔══██╗██╔═══██╗██╔═══██╗████╗ ████║
        ██║█████╗██████╔╝██║   ██║██║   ██║██╔████╔██║
        ██║╚════╝██╔══██╗██║   ██║██║   ██║██║╚██╔╝██║
        ██║      ██████╔╝╚██████╔╝╚██████╔╝██║ ╚═╝ ██║
        ╚═╝      ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝     ╚═╝
                                Made by :- SPEEDX
        """
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

}

init_environ(){
    declare -A backends; backends=(
        ["arch"]="pacman -S --noconfirm"
        ["debian"]="apt-get -y install"
        ["ubuntu"]="apt -y install"
        ["termux"]="apt -y install"
        ["fedora"]="yum -y install"
        ["redhat"]="yum -y install"
        ["SuSE"]="zypper -n install"
        ["sles"]="zypper -n install"
        ["darwin"]="brew install"
        ["alpine"]="apk add"
    )

    INSTALL="${backends[$distro]}"

    if [ "$distro" == "termux" ]; then
        PYTHON="python"
        SUDO=""
    else
        PYTHON="python3"
        SUDO="sudo"
    fi
    PIP="$PYTHON -m pip"
}

install_deps(){
    
    packages=(openssl git $PYTHON $PYTHON-pip figlet toilet)
    if [ -n "$INSTALL" ];then
        for package in ${packages[@]}; do
            $SUDO $INSTALL $package
        done
        $PIP install -r requirements.txt
    else
        echo "We could not install dependencies."
        echo "Please make sure you have git, python3, pip3 and requirements installed."
        echo "Then you can execute bomber.py ."
        exit
    fi
}

banner
pause
detect_distro
init_environ
if [ -f .update ];then
    echo "All Requirements Found...."
else
    echo 'Creating Environments....'
    echo 'Making the files ready....'
    echo 'Installing Requirements....'
    echo .
    echo .
    install_deps
    echo This Script Was Made By SpeedX > .update
    echo 'Environments is ready sir....'
    echo 'Requirements Installed....'
    pause
fi
while :
do
    banner
    echo " ✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭"
    echo -e "\e[4;31m Please Read Instruction Carefully !!! \e[0m"
    echo "✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭ "
    echo "  ✭✭ Press 1 To  Start SMS  Bomber                      ✭✭       "                       
    echo "  ✭✭ Press 2 To  Start CALL Bomber                      ✭✭"
    echo "  ✭✭ Press 3 To  Start MAIL Bomber                      ✭✭"
    echo "  ✭✭ Press 4 To  Get Latest Version                     ✭✭ "
    echo "  ✭✭ Press 5 To  Exit                                   ✭✭ "
    echo " ✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭ "
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
        echo -e "\e[1;34m Please Wait sir ..."
        echo -e "\e[1;34m Downloading Latest Files..."
        echo -e "\e[1;34m ︾︾︾︾︾︾︾︾︾︾︾︾︾︾"
        rm -f .update
        $PYTHON bomber.py --update
        echo -e "\e[1;34m Restating the T-Boom...."
        echo -e "\e[1;34m ︾︾︾︾︾︾︾︾︾︾︾"
        pause
        exit
    elif [ $ch -eq 5 ];then
        banner
        exit
    else
        echo -e "\e[4;32m Please choose the correct option.{invalid Input} !!! \e[0m"
        echo -e "\e[4;32m ︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾ \e[0m"
        pause
    fi
done
