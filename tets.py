import requests

url = 'https://droid-atmosphere-72bfd8ea821e.herokuapp.com/api/register.php'
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