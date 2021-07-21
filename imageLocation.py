#script to pull Exif location data from ImageFolder
from logging import error
import exifread
import os
from statistics import mean


#path to folder containing images
ImageFolder = '/Users/m./Documents/SOFTWARE DEV/THANDI/Exif pull/ImageFolder'

# inittialise array to store long/lat data
latDegData = []
latMinData = []
latSecondsData = []
longDegData = []
longMinData = []
longSecondsData = []

numProcessed = 0
numUnprocessed = 0

#iterate through dir containing IMG's
for image in os.listdir(ImageFolder):
    
    numProcessed = numProcessed + 1

    #check if image
    if image.endswith(".HEIC") or image.endswith(".jpg") or image.endswith(".png") or image.endswith(".tif") or image.endswith(".mov"):
        
        imageObject = open(ImageFolder +"/"+ image, 'rb')
        tags = exifread.process_file(imageObject)
        
        #pull data --> process data
        try: 
            data = tags['GPS GPSLatitude']
            data = str(data).split(",")
            latSeconds = data[2]
            latSeconds = latSeconds[:-1]
            latSeconds = latSeconds.split("/")
            latSeconds = float(latSeconds[0]) / float(latSeconds[1])
            latMin = data[1]
            latMin = latMin[1:]
            latDeg = data[0]
            latDeg = latDeg[1:]

            data = tags['GPS GPSLongitude']
            data = str(data).split(",")
            longSeconds = data[2]
            longSeconds = longSeconds[:-1]
            longSeconds = longSeconds.split("/")
            longSeconds = float(longSeconds[0]) / float(longSeconds[1])
            longMin = data[1]
            longMin = longMin[1:]
            longDeg = data[0]
            longDeg = longDeg[1:]

            #append data to array
            latDegData.append(int(latDeg)) 
            latMinData.append(int(latMin))
            latSecondsData.append(float(latSeconds))

            longDegData.append(int(longDeg))
            longMinData.append(int(longMin))
            longSecondsData.append(float(longSeconds))
        except:
            numUnprocessed = numUnprocessed + 1
        

# calcutae mean
meanLatDeg = str(int(round(mean(latDegData),0)))
meanLatMin = str(int(round(mean(latMinData),0)))
meanLatSeconds = str(round(mean(latSecondsData),2))

meanLongDeg = str(int(round(mean(longDegData),0)))
meanLongMin = str(int(round(mean(longMinData),0)))
meanLongSeconds = str(round(mean(longSecondsData),2))



#compile google maps friendly output
print(meanLatDeg+"°"+ meanLatMin+ "'" + meanLatSeconds+ '"S '+ meanLongDeg+"°"+ meanLongMin+ "'" + meanLongSeconds+ '"E')

#stat
print("Processed:" + str(numProcessed))
print("Unprocessd: " + str(numUnprocessed))
print("% missed: " + str(numUnprocessed/numProcessed))



