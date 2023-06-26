#! /usr/bin/python

import json
import matplotlib.pyplot as plt
import pandas as pd
import sys
import cartopy

def readJsonFile(path):
    with open(path) as f:
        jsonData = json.load(f)

    return jsonData["locations"]

def createDataFrame(rawData):
    return pd.DataFrame(rawData, columns=["timestamp", "latitudeE7", "longitudeE7"])

def plotAllData(locations):
    fig = plt.figure()
    ax = fig.add_subplot(projection=cartopy.crs.Mercator())
    ax.set_global()
    #ax.stock_img()
    #ax.coastlines()
    ax.add_feature(cartopy.feature.BORDERS, alpha=0.2)
    ax.add_feature(cartopy.feature.STATES, alpha=0.2)
    ax.add_feature(cartopy.feature.COASTLINE, alpha=0.2)
    ax.add_feature(cartopy.feature.LAKES, alpha=0.2)

    ax.plot(locations["longitudeE7"].div(10000000), locations["latitudeE7"].div(10000000), transform=cartopy.crs.Geodetic(), marker=',', markersize=4, linestyle='', linewidth=0.2)

    plt.show()

if __name__ == "__main__":
    # Read the JSON file into a json
    print("Reading Json File...")
    rawData = readJsonFile(sys.argv[1])

    # Extract 'latitudeE7', 'longitudeE7', 'timestamp'
    # Convert into pandas dataframe
    print("Converting dict to DataFrame...")
    locations = createDataFrame(rawData)

    # Plot using matplotlib
    print("Plotting data with matplotlib")
    plotAllData(locations)

    print("Done")
