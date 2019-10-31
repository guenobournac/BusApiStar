#!/usr/bin/python

from Api import *
import sys
import getopt
"""
Default Constant
"""

defaultNbResult = 2
defaultLigne = "C4"
defaultDestination = "Grand+Quartier"
defaultIdArret = "1292"

#====================================================================
def main(argv):
    nbResult = defaultNbResult
    ligne = defaultLigne
    destination = defaultDestination
    idArret = defaultIdArret

    try:                                
        opts, args = getopt.getopt(argv, "hn:s:d:l:", ["help", "nbResult=", "station=", "destination=", "line="])
    except getopt.GetoptError:
        usage()                         
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ("-h, --help"):
            usage()
            sys.exit()
        if opt in ("-n", "--nbResult"):
            try:
                nbResult = int(arg)
            except ValueError:
                usage()
                sys.exit()
        if opt in ("-s","--station"):
            idArret = arg
        if opt in ("-d","--destination"):
            destination = arg
        if opt in ("-l","--line"):
            ligne = arg

        
    Affichage(ligne = ligne, destination = destination,idArret = idArret, nbResult = nbResult)

def usage():
    print("""usage : ./main.py [OPTION]
[OPTION] : 
    -h, --help  help
    -n, --nbResult [nb] with nb an integer
    -s, --station [stationNumber] with stationNumber the number of the station
    -d, --destination [busDestination] with busDestination the destination of the bus
    -l, --line [busLineName] with busLineName the name of the bus Lane""")


if __name__ == "__main__":
    # execute only if run as a script
    main(sys.argv[1:])
