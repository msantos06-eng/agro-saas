import numpy as np
import pandas as pd

def generate_vra_map(ndvi):

    zones = np.zeros_like(ndvi)

    zones[ndvi < 0.3] = 1   # baixo vigor
    zones[(ndvi >= 0.3) & (ndvi < 0.6)] = 2
    zones[ndvi >= 0.6] = 3  # alto vigor

    return zones


def export_vra_csv(zones):

    unique, counts = np.unique(zones, return_counts=True)

    df = pd.DataFrame({
        "zone": unique,
        "area_pixels": counts
    })

    return df