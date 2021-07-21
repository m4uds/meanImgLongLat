#script to pull Exif location data from ImageFolder
from logging import error
import exifread
import os
from statistics import mean


#path to folder containing images
ImageFolder = "!path!"

# inittialise array to store long/lat data
latDegData = []
latMinData = []
latSecondsData = []
longDegData = []
longMinData = []
longSecondsData = []

#iterate through dir containing IMG's
for image in os.listdir(ImageFolder):
    
    #check if image or video file
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
            print(image + " |-----x---x-----| ERROR")
        

# calcutae mean
meanLatDeg = str(mean(latDegData))
meanLatMin = str(mean(latMinData))
meanLatSeconds = str(mean(latSecondsData))

meanLongDeg = str(mean(longDegData))
meanLongMin = str(mean(longMinData))
meanLongSeconds = str(mean(longSecondsData))

#compile google maps friendly output
print(meanLatDeg+"°"+ meanLatMin+ "'" + meanLatSeconds+ '"S '+ meanLongDeg+"°"+ meanLongMin+ "'" + meanLongSeconds+ '"E')






