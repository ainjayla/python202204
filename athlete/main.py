from Athlete import *

athletes = []

peeter = Skydiver('Peeter', 'Suur', 35, 'M', 180, 85)
peeter.muudparameetrid = {'kinganumber': 43}
athletes.append(peeter)
kaie = Runner('Kaie', 'Roomus', 25, 'N', 170, 65)
kaie.muudparameetrid = {'juustevarv': 'pruun', 'silmavarv': 'roheline'}

athletes.append(kaie)

for athlete in athletes:
    print(athlete, end = '')
    if len(athlete.muudparameetrid) > 0:
        for parameeter in athlete.muudparameetrid:
            print(', ' + parameeter + ': ' + str(athlete.muudparameetrid[parameeter]), end = '')
        print()
    else:
        print()