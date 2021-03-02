import json

infile = open("US_fires_9_1.json", "r")

fire_data = json.load(infile)

lons, lats, brights = [], [], []

for fire in fire_data:
    if fire["brightness"] > 450:
        lon = fire["longitude"]
        lat = fire["latitude"]
        bright = fire["brightness"]
        lons.append(lon)
        lats.append(lat)
        brights.append(bright)

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "text": brights,
        "marker": {
            "size": [0.03 * bright for bright in brights],
            "color": brights,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Brightness"},
        },
    }
]

my_layout = Layout(title="US Fires 9-1-20 to 9-13-20")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="US_Fires.html")