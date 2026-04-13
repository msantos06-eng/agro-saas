import requests
import numpy as np

def get_token(client_id, client_secret):
    return "FAKE_TOKEN"

def fetch_sentinel(token, bbox):
    return {"data": "sentinel_raw"}

# =========================
# TOKEN SENTINEL
# =========================
def get_token(client_id, client_secret):

    url = "https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token"

    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }

    r = requests.post(url, data=data)
    return r.json().get("access_token")


# =========================
# BUSCAR IMAGEM SENTINEL-2
# =========================
def search_sentinel(token, bbox, date_from, date_to):

    url = "https://catalogue.dataspace.copernicus.eu/odata/v1/Products"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    query = (
        f"SENTINEL-2 AND "
        f"OData.CSC.Intersects(area=geography'SRID=4326;{bbox}')"
    )

    params = {
        "$filter": query
    }

    r = requests.get(url, headers=headers, params=params)

    return r.json()