import requests
import json
import datetime

def requete():
    r = requests.get("https://data.explore.star.fr/api/records/1.0/search/?dataset=tco-bus-circulation-passages-tr&sort=-arrivee&facet=idligne&facet=nomcourtligne&facet=sens&facet=destination&facet=precision&refine.nomcourtligne=C4&refine.destination=Grand+Quartier&refine.precision=Temps+r%C3%A9el&refine.idarret=1292")
    return r

def nextBuses():
    r = requete()
    jsonR = json.loads(r.text)
    res = []
    for rows in jsonR["records"][0:2]:
        strArrivee = rows["fields"]["arrivee"]
        arrive = datetime.datetime.strptime(strArrivee, '%Y-%m-%dT%H:%M:%S+00:00') + datetime.timedelta(hours = 1)
        res.append(arrive.strftime('%H:%M %d/%m/%Y'))
    return res
