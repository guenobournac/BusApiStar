import requests


def requete():
    r = requests.get("https://data.explore.star.fr/api/records/1.0/search/?dataset=tco-bus-circulation-passages-tr&facet=idligne&facet=nomcourtligne&facet=sens&facet=destination&facet=precision&refine.nomcourtligne=C4&refine.destination=Grand+Quartier&refine.precision=Temps+r%C3%A9el&refine.idarret=1292")
    return r