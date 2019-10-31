import requests
import json
import datetime
"""
Star Api Request for Real Time hours
"""
def requete(ligne = "C4", destination = "Grand+Quartier", idArret = "1292"):
    r = requests.get("https://data.explore.star.fr/api/records/1.0/search/?dataset=tco-bus-circulation-passages-tr&sort=-arrivee&facet=idligne&facet=nomcourtligne&facet=sens&facet=destination&" +
    "refine.nomcourtligne=" + ligne + "&refine.destination=" + destination + "&" +
    "&refine.idarret=" + idArret)
    return r

"""
This functiun gives the next hours for the buses
"""
def nextHoursBuses(ligne = "C4", destination = "Grand+Quartier", idArret = "1292" , nbResult = 2):
    r = requete(ligne, destination, idArret)
    jsonR = json.loads(r.text)
    res = []
    for rows in jsonR["records"][0:nbResult]:
        strArrivee = rows["fields"]["arrivee"]
        res.append(conversionDate(strArrivee))
    return res

def conversionDate(date):
    dateObject = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S+00:00') 
    dateObject = dateObject + datetime.timedelta(hours = 1)
    return dateObject.strftime('%H:%M %d/%m/%Y')

def Affichage(ligne = "C4", destination = "Grand+Quartier", idArret = "1292", nbResult = 2):
    r = nextHoursBuses(ligne, destination, idArret, nbResult)
    print("ligne : " + ligne)
    print("direction : " + destination.replace("+", " "))
    print("Arret : " + idArret)
    for l in r:
        print(" "+l)