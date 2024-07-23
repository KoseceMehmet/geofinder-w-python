import requests

def get_public_ip():
    response = requests.get('https://api.ipify.org?format=json')
    data = response.json()
    return data['ip']

print(f"Your public IP address is: {get_public_ip()}")
