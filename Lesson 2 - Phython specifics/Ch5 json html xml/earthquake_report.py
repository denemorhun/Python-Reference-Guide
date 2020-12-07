# 
# Example file for parsing and processing JSON
#
import urllib.request 
import json

def printResults(data):
    # Use the json module to load the string data into a dictionary
    quake_json = json.loads(data)

    print(quake_json)

    # now we can access the contents of the JSON like any other Python object

    # title of quake in json feed
    if "title" in quake_json["metadata"]:
        print(quake_json["metadata"]["title"])

    # output the number of quakes, plus the magnitude and each event name

    count = quake_json["metadata"]["count"]
    print("Incidents recorded are: " + str(count))

    # for each event, print the place where it occurred
    # print the events that only have a magnitude greater than 4
    # where at least 1 person reported feeling something
    for quake in quake_json["features"]:
        mag = quake["properties"]["mag"]
        felt = quake["properties"]["felt"]
        place = quake["properties"]["place"]
        if mag >= 4.0 and felt is not None and felt > 0:
            print("Magnitude: %2.1f" % mag, str(place))

        if "Turkey" in str(place) or "Greece" in str(place) and felt is not None and felt > 0:
            print("Turkey had strength " + str(mag) + 
                  " earthquake nearby at: " + str(place), ",reported by " + str(felt))

        if "Spain" in str(place) and felt is not None:
            print("Spain had strength " + str(mag) + 
                  "earthquake nearby at: " + str(place))


def main():
    # define a variable to hold the source URL
    # In this case we'll use the free data feed from the USGS
    # This feed lists all earthquakes for the last day larger than Mag 2.5
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    data = get_url_data(urlData)

    printResults(data)

def get_url_data(urlData):
    # Open the URL and read the data
    webUrl = urllib.request.urlopen(urlData)
    result_code = webUrl.getcode()

    print("result code: " + str(result_code))

    # 200 is success
    if (result_code == 200):
        data = webUrl.read()
    else:
        print("ERROR: cannot parse results")
    return data


if __name__ == "__main__":
  main()
