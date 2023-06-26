#! /usr/bin/python

import json
import matplotlib.pyplot as plt
import pandas as pd
import sys
import cartopy

def readJsonFile(path):
    with open(path, "r") as f:
        return json.load(f)["locations"]


def createDataFrame(rawData):
    return pd.DataFrame(rawData, columns=["timestamp", "latitudeE7", "longitudeE7"])

# This isn't really faster, and it's certainly harder to understand!
# def createDataFrameFromPath(path):
#     return pd.DataFrame.from_records(pd.read_json(path)["locations"],
#         columns=["timestamp", "latitudeE7", "longitudeE7"])

def plotAllData(locations):
    fig = plt.figure()
    ax = fig.add_subplot(projection=cartopy.crs.Mercator())

    ax.set_global()
    ax.add_feature(cartopy.feature.BORDERS, alpha=0.2)
    ax.add_feature(cartopy.feature.STATES, alpha=0.2)
    ax.add_feature(cartopy.feature.COASTLINE, alpha=0.2)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.2)

    ax.plot(locations["longitudeE7"].div(10**7),
            locations["latitudeE7"].div(10**7),
            transform=cartopy.crs.Geodetic(),
            marker=',',
            markersize=4,
            linestyle='',
            linewidth=0.2)

    plt.show()


if __name__ == "__main__":
    # Read the JSON file into a python dict
    print("Reading Json File...")
    rawData = readJsonFile(sys.argv[1])

    # Extract 'latitudeE7', 'longitudeE7', 'timestamp'
    # Convert python dict into pandas DataFrame
    print("Converting dict to DataFrame...")
    locations = createDataFrame(rawData)

    # Plot using matplotlib
    print("Plotting data with matplotlib...")
    plotAllData(locations)

    print("Done")
