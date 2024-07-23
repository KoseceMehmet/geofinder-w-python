import folium

def create_map(latitude, longitude):
    my_map = folium.Map(location=[latitude, longitude], zoom_start=12)
    folium.Marker([latitude, longitude], popup="I'm here!").add_to(my_map)
    my_map.save("map.html")

latitude = input("your latitude : ")
longitude = input("your longitude : ")

create_map(latitude, longitude)
