def loadfile():
    '''loads the file to be read''' 
    '''
    file = str(input("Please enter the name of the txt file to import.\nPlease remember to type .txt after the file\nDISCLAIMER:In order for the grapics mode to function properly, \nplease import a maximum of ten planets\nNow Please enter the filename: "))
    '''
    fileRef = open("planetsData1.txt","r")      ##remember to switch back to 'file'
    stringlist=[]
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
        print(dashplaces)
        dash=1
        for d in range(3):  ##d is an arbitraily assigned counter
            datalist[i].append(int(stringlist[i][dashplaces[dash-1]+1:dashplaces[dash]]))
            dash+=1
    if len(datalist) <= len(presetplanet):
        for q in range(len(datalist)):  ##q is an arbitraily assigned counter
            presetplanet[q][0].extend(datalist[q])
            planets.append(presetplanet[q])
    else:
        for q in range(len(datalist)):  ##q is an arbitraily assigned counter
            presetplanet[q][0].extend(datalist[q])
            datalist.remove(datalist[q])
            planets.append(presetplanet[q])
        for extra in datalist:
            planets.append(datalist[extra])
        
    print(datalist)
    
    
    
loadfile()