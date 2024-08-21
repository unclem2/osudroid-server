import requests

test = True
if test is True:
    endp = 'http://0.0.0.0:5001'
if test is False:
    endp = 'https://droid-atmosphere-72bfd8ea821e.herokuapp.com/'
def register():
    url = f'{endp}/api/register.php'
    data = {
        'username': 'lnh',
        'password': '14120a3fc517841862049bb4066843fe',
        'deviceID': 'testdeviceid',
        'email': 'bwadoasdjd@afasf.com',
        'sign': 'testsign'
    }

    response = requests.post(url, data=data)

    if response.status_code == 200:
        print('Response:', response.text)
    else:
        print('Failed to register. Status code:', response.status_code)
def login():
    url = f'{endp}/api/login.php'
    data = {
        'username': 'lnh',
        'password': '14120a3fc517841862049bb4066843fe',
        'version': '40'
    }

    response = requests.post(url, data=data)

    if response.status_code == 200:
        print('Response:', response.text)
        
        ssid = response.text.split(" ")[1]
        return ssid
    
    else:
        print('Failed to register. Status code:', response.status_code)
        
        
def padoru_presubmit(ssid):
    url = f'{endp}/api/submit.php'
    data = {
        'userID': '2',
        'ssid': f'{ssid}',
        'filename': 'Turbo - PADORU  PADORU (Sotarks) [Gift].osu',
        'hash': 'a53a591e8ee0e4cf66a20a070968b194',
        'songTitle': 'PADORU / PADORU',
        'songArtist': 'Turbo',
        'songCreator': 'Sotarks'}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print('Response:', response.text)
        play_id = response.text.split(" ")[1]
    else:
        print('Failed to register. Status code:', response.status_code)
        
def padoru_submit():
    url = f'{endp}/api/submit.php'
    data = {
        'userID': '2',
        'playID': '1',
        'data' : 'xs| 4739302 179 B 16 124 4 21 0 2 89115 1724083548144 0 lnh'
        
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print('Response:', response.text)
    else:
        print('Failed to register. Status code:', response.status_code)
        
def presubmit_second(ssid):
    url = f'{endp}/api/submit.php'

    data = {
    'userID': '2',
    'ssid': f'{ssid}',
    'filename': 'goreshit - looming shadow of a tree long gone (grumd) [Insane].osu',
    'hash': '4a7d699238f84bf0880f836c1fac1b11',
    'songTitle': 'looming shadow of a tree long gone',
    'songArtist': 'goreshit',
    'songCreator': 'grumd',
    'songID': '90803'
}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print('Response:', response.text)
        play_id = response.text.split(" ")[1]
    else:
        print('Failed to register. Status code:', response.status_code)
    
def submit_second():
    url = f'{endp}/api/submit.php'
    data = {
        "userID": "1",
        "playID": "1",
        "data": "| 382922 173 A 10 114 3 14 0 0 92708 1724161796400 0 unclem3"
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print('Response:', response.text)
    else:
        print('Failed', response.status_code)
    
def gettop(i):
    url = f"{endp}/api/gettop.php"
    data = {
        "playID": f"{i}"
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print('Response:', response.text)
    else:
        print('Failed', response.status_code)

def getrank():
    url = f"{endp}/api/getrank.php"
    data = {
        "filename": "goreshit - looming shadow of a tree long gone (grumd) [Insane].osu",
        "hash": "4a7d699238f84bf0880f836c1fac1b11",
        "uid": "1"
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print('Response:', response.text)
    else:
        print('Failed', response.status_code)
# register()  
ssid = login()
padoru_presubmit(ssid)
padoru_submit()
# presubmit_second(ssid)
# submit_second()
# for i in range(1, 6):
#     gettop(i)
# getrank()

