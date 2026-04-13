# map.py
import folium

def generate_map(farms):
    m = folium.Map(location=[-12.5, -45], zoom_start=5)

    for farm in farms:
        _, name, area, lat, lon = farm
        folium.Marker(
            location=[lat, lon],
            popup=f"{name} - {area} ha"
        ).add_to(m)

    return m