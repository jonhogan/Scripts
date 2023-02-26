import csv
import json
import copy
import pandas as pd

#df = pd.read_csv('cityList.csv', names=("City","Country","UN 2018 population estimates","Definition", "Population City", "Area City" , "Density City",
#                                        "Population Urban", "Area Urban", "Density Urban", "Population Metro", "Area Metro", "Density Metro","Total Density"), encoding='latin-1')

#with open('cityList.json', 'w') as f:
#    json.dump(df.to_dict(orient="records"), f, indent=4)


# df = pd.read_csv('usCityList.csv', names=("City","State","Land Area(sq mi)","Land Are(sq km)", "Water Area (sq mi)", "Water Area (sq km)" , "Total Area (sq mi)",
#                                         "Total Area (sq km)", "Population (2020)", "Density"), encoding='latin-1')

# with open('usCityList.json', 'w') as f:
#     json.dump(df.to_dict(orient="records"), f, indent=4)

# df = pd.read_csv('metroList.csv', names=("City", "Country Region", "Name", "Service Opened","Last Expanded","Stations",
#                 "System Length (km)", "Annual Ridership (millions)", "Rail Type"), encoding='latin-1')

# with open('metroList.json', 'w') as f:
#      json.dump(df.to_dict(orient="records"), f, indent=4)

df = pd.read_csv('worldCitiesLat.csv', names=("City", "State", "Country", "Latitude (D)","Latitude (C)","Longitude (D)",
                "Longitude (C)"), encoding='Latin-1')

with open('worldCitiesLat.json', 'w') as f:
     json.dump(df.to_dict(orient="records"), f, indent=4)

