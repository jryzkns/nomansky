#!/usr/bin/python3

##CMPT 120 D100; 16-3
##Jack 'Jryzkns' Zhou
##Brian Fu
##Daniel Lee
##Final Assignment - Planets, Aliens, and Explosions

#Mildly spaghettied cause jack is a pleb
def loadfile():
    '''loads the file to be read''' 
    file = str(input("Please enter the name of the txt file to import.\nPlease remember to type .txt after the file\nDISCLAIMER:In order for the grapics mode to function properly, \nplease import a maximum of ten planets\nNow Please enter the filename: "))
    ##needs validation to get the right file
    fileRef = open(file,"r")
    stringlist=[]
    ## <My intense dumbassery>
    for line in fileRef:
        string = "-"+line[0:len(line)-1]+"-"
        stringlist.append(string)
    fileRef.close()
    datalist=[]
    for i in range(len(stringlist)):
        datalist.append([])
        dashplaces=[]
        for e in range(len(stringlist[i])): ##e is an arbitraily assigned counter
            if stringlist[i][e] == "-":
                dashplaces.append(e)
        dash=1
        for d in range(3):  ##d is an arbitraily assigned counter
            datalist[i].append(int(stringlist[i][dashplaces[dash-1]+1:dashplaces[dash]]))
            dash+=1
    ## </My intense dumbassery>
    if len(datalist) <= len(presetplanet):
        for q in range(len(datalist)):  ##q is an arbitraily assigned counter
            presetplanet[q][0].extend(datalist[q])
            planets.append(presetplanet[q])
    else:   ##needs to be fixed when the list is longer than 10
        for q in range(len(datalist)):  ##q is an arbitraily assigned counter
            presetplanet[q][0].extend(datalist[q])
            datalist.remove(datalist[q])
            planets.append(presetplanet[q])
        for extra in datalist:
            planets.append(datalist[extra])


