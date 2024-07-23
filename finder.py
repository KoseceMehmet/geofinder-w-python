import requests

def get_location(ip):
    # ip-api.com kullanarak IP adresinden konum bilgisi alıyoruz
    response = requests.get(f"http://ip-api.com/json/{ip}")
    data = response.json()
    
    if data['status'] == 'success':
        print(f"IP Address: {data['query']}")
        print(f"Location: {data['city']}, {data['regionName']}, {data['country']}")
        print(f"Coordinates: (Lat: {data['lat']}, Lng: {data['lon']})")
        print(f"ISP: {data['isp']}")
    else:
        print("Location information could not be retrieved.")

if __name__ == "__main__":
    ip_address = input("Enter IP Address: ")
    get_location(ip_address)

