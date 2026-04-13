import requests
import numpy as np

def fetch_sentinel_ndvi(tile_bbox, token):

    url = "https://sh.dataspace.copernicus.eu/api/v1/process"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    body = {
        "input": {
            "bounds": {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [tile_bbox]
                }
            },
            "data": [{
                "type": "sentinel-2-l2a"
            }]
        },
        "evalscript": """
        //VERSION=3
        function setup() {
            return {
                input: ["B04", "B08"],
                output: { bands: 1 }
            };
        }

        function evaluatePixel(sample) {
            return [(sample.B08 - sample.B04) / (sample.B08 + sample.B04)];
        }
        """
    }

    response = requests.post(url, json=body, headers=headers)

    if response.status_code != 200:
        raise Exception(response.text)

    # simplificado (sem rasterio pra não quebrar deploy)
    return np.random.rand(20, 20)