import math
def findTrekantOmkreds(): #Made by Yusuf, Hadi
    return 0

def findTrekantSidelaengder(x1,x2,x3,y1,y2,y3): #Made by Bjørn, Rasmus E, Nick
    a = math.sqrt((x1-x2)**2+(y1-y2)**2)
    return [a,b,c]

def findTrekantAreal(): #Made by Jakob, Rasmus W
    return 0

def findTrekantVinkler(): #Made by Said, Omar
    return 0

def findTrekantOmskrevneCirkelsRadius(): #Made by Gwion, Frederik L
    return 0

def findTrekantOmskrevneCirkelsKordinater(): #Made by Oliver, Mads, Liam
    return 0

def findTrekantIndskrevneCirkelsRadius(): #Made by Michael, Alexander
    return 0

def findTrekantIndskrevneCirkelsKordinater(x1, x2, x3, y1, y2, y3): #Made by Allan, Gabriel, Daniel
    # udregner vinkel mellem x-aksen og linjerne
    a1 = (y2-y1)/(x2-x1)
    a2 = (y3-y2)/(x3-x2)
    a3 = (y3-y1)/(x3-x1)
    vinkel1 = math.atan(math.radians(a1))
    vinkel2 = math.atan(math.radians(a2))
    vinkel3 = math.atan(math.radians(a3))

    # Vinkel for vinkelhalveringslinje 1
    helVinkel1 = vinkel1 - vinkel2
    if helVinkel1 < 0:
        helVinkel1 = helVinkel1 * -1
    halvVinkel1 = helVinkel1 / 2
    halva1 = math.tan(math.radians(halvVinkel1))

    # Vinkel for vinjelhalveringslinje 2
    helvinkel2 = vinkel1 - vinkel3
    halvVinkel2 = helvinkel2 / 2
    halva2 = math.tan(math.radians(halvVinkel2))

    # Udregner b for begge linjer
    b1 = y2 - halvVinkel1 * x2
    b2 = y1 - halvVinkel2 * x1

    # udregn x og y
    x = (b2 - b1) / (halva1 - halva2)
    y = halva1 * x + b1
    # return [x, y]
    # !VIRKER IKKE ENDNU!

def findTrekantVinkelHalveringsLinjer(): #Made by
    return 0

def tegnTrekant(): #Made by Yusuf, Hadi
    return 0

def skrivResultater():
    return 0
