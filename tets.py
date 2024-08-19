import requests

def register():
    url = 'http://127.0.0.1:5000/api/register.php'
    data = {
        'username': 'unclem',
        'password': 'd7df09cd5ed94d4ad815c3fa5aef46fc',
        'deviceID': 'testdeviceid',
        'email': 'mannringyt11@gmail.com',
        'sign': 'testsign'
    }

    response = requests.post(url, data=data)

    if response.status_code == 200:
        print('Response:', response.text)
    else:
        print('Failed to register. Status code:', response.status_code)
def login():
    url = 'http://127.0.0.1:5000/api/login.php'
    data = {
        'username': 'unclem',
        'password': 'd7df09cd5ed94d4ad815c3fa5aef46fc',
        'version': '40'
    }

    response = requests.post(url, data=data)

    if response.status_code == 200:
        print('Response:', response.text)
        
        ssid = response.text.split(" ")[1]
        return ssid
    
    else:
        print('Failed to register. Status code:', response.status_code)
        
        
def presubmit(ssid):
    url = 'http://127.0.0.1:5000/api/submit.php'
    data = {
        'userID': '1',
        'ssid': f'{ssid}',
        'filename': 'Turbo - PADORU  PADORU (Sotarks) [Gift].osu',
        'hash': 'a53a591e8ee0e4cf66a20a070968b194',
        'songTitle': 'PADORU / PADORU',
        'songArtist': 'Turbo',
        'songCreator': 'Sotarks'}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print('Response:', response.text)
    else:
        print('Failed to register. Status code:', response.status_code)
        
def submit():
    url = 'http://127.0.0.1:5000/api/submit.php'
    data = {
        'userID': '1',
         'playID': '2',
        'data' : '| 473932 179 B 16 124 4 21 0 2 89115 1724083548144 0 unclem'
        
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print('Response:', response.text)
    else:
        print('Failed to register. Status code:', response.status_code)
        
# register()  
ssid = login()
presubmit(ssid)
submit()