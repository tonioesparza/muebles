__author__ = "Bruger"
__version__ = "2020.05.25"

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import ghpythonlib.components as gh

tagList = list()

pointList = list()

i=0

for line in listOfLines:
    
    endPoints = gh.EndPoints(line)
    
    start = endPoints[0]
    end = endPoints [1]
    
    coorsStart = gh.Deconstruct(start)
    coorsEnd = gh.Deconstruct(end)
    
    "nota, z y x puede que esten invertidos"
    
    xcomp = [coorsStart[0],coorsEnd[0]]
    ycomp = [coorsStart[1],coorsEnd[1]]    
    zcomp = [coorsStart[2],coorsEnd[2]]  
    
    xcomp.sort()
    ycomp.sort()
    zcomp.sort()
    
    xBank = list()
    yBank = list()
    zBank = list()
    
    "Comparacion y obtencion de valores validos"
    
    #print "xrange",xcomp, 
    
    #print xcomp, xcomp[0]-layerThickness/2, xcomp[1]+layerThickness/2
    #print ycomp, ycomp[0]-layerThickness/2, ycomp[1]+layerThickness/2
    #print zcomp, zcomp[0]-layerThickness/2, zcomp[1]+layerThickness/2
    
    xcomp[0]= xcomp[0]-layerThickness/2
    xcomp[1]=xcomp[1]+layerThickness/2
    
    ycomp[0]= ycomp[0]-layerThickness/2
    ycomp[1]= ycomp[1]+layerThickness/2 
    
    zcomp[0]= zcomp[0]-layerThickness/2
    zcomp[1]= zcomp[1]+layerThickness/2
    
    #print xcomp
    #print ycomp
    #print zcomp
    
    
    for num in totalRangeX:
        
        if num >= xcomp[0]:
            if num <= xcomp[1]:
                if num not in xBank:
                    xBank.append(num)
                    
    for num in totalRangeY:
        if num >= ycomp[0]:
            if num <= ycomp[1]:
                if num not in yBank:
                    yBank.append(num)
    
    for num in totalRangeZ:
        if num >= zcomp[0]:
            if num <= zcomp[1]:
                if num not in zBank:
                    zBank.append(num)
    
    #print "zbank",zBank
    
    #print listOfLenghts[i], layerThickness
    
    
    
    extra = int(listOfLenghts[i]/layerThickness)
    
    #print extra
    
    if len(xBank) <= 0:
        for j in range(extra):
            print "X", xBank, extra
            ex = xBank[0]-layerThickness
            ex2 = xBank[-1] + layerThickness
            xBank.append(ex)
            xBank.append(ex2)
            xBank.sort()
    
    #print "xrange", xcomp,"finalxbank", xBank
    
    if len(yBank) <= 0:
        for k in range(extra):
            #print "Y", yBank, extra
            ey = yBank[0]-layerThickness
            ey2 = yBank[-1] + layerThickness
            yBank.append(ex)
            yBank.append(ex2)
            yBank.sort()
    
    #print "yrange", ycomp,"finalybank", yBank
    
    "Matriz de puntos"
    #print "lenx", len(xBank)
    if len(xBank)>0:
        #print "leny", len(yBank)
        if len(yBank)>0:
            #print "lenz", len(zBank)
            if len(zBank)>0:
                for co in xBank:
                    for coo in yBank:
                        for coor in zBank:
                            tag = str(co)+' X '+str(coo)+' Y '+str(coor)+' Z '
                            if tag not in tagList:
                                tagList.append(tag)
                                poi = gh.ConstructPoint(co,coo,coor)
                                pointList.append(poi)
    
                                #print zBank, tag
    
    
    i+=1
    
    
    
    #print " line ", i

