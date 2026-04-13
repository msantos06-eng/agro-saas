import folium
import numpy as np

def create_ndvi_colored_map(ndvi):

    m = folium.Map(location=[-12.5, -45.5], zoom_start=10)

    # simplificação visual
    for i in range(ndvi.shape[0]):
        for j in range(ndvi.shape[1]):

            value = ndvi[i][j]

            if value < 0.3:
                color = "red"
            elif value < 0.6:
                color = "yellow"
            else:
                color = "green"

            folium.CircleMarker(
                location=[-12.5 + i*0.01, -45.5 + j*0.01],
                radius=3,
                color=color,
                fill=True
            ).add_to(m)

    return m 