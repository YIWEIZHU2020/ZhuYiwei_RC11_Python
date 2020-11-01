# Imports:
# use python --version to check what version of python your standard installation is
# if this is 2.x you will have to use pip3 install otherwise pip install
import csv
import requests
# pip install pillow
from PIL import Image
from io import BytesIO

# Define the ArtTate class, with all attributes that you find usefull
class ArtTate:
    # Define the initialise function accordingly
    def __init__(self,id, width, depth, height, imageUrl, artist):
        # delete pass when you start editing, this is a placeholder keyword to say that nothing happens
        self.id = id
        self.width = width
        self.depth = depth
        self.height = height
        self.imageUrl = imageUrl
        self.artist = artist
        self.imagePath = ''
# Define a function that prints a description
    def describe(self):
print("artist:" + self.artist, "id:" + self.id, "width:" + str(self.width), "depth:" + str(self.depth), "height:" + str(self.height))
        # delete pass when you start editing, this is a placeholder keyword to say that nothing happens


    # implement the get image function that saves the image to the specified folder
    def getImageFile(self):
            if self.imageUrl:
                response = requests.get(self.imageUrl)
                try:
                    im = Image.open(BytesIO(response.content))
                except OSError:
                    return None
                path = assignment1/resource/ArtImages/
                self.imagePath = path
                im.save(path, "JPEG")
        # delete pass when you start editing, this is a placeholder keyword to say that nothing happens
artPieces = []
with open(assignment1/resource/CSVfiles/artwork_data/, encoding = 'utf-8-sig') as artFile:
    artReader = csv.DictReader(artFile)

    for row in artReader:
        id = row['ObjectID']
        width = row['Width (cm)']
        height = row['Height (cm)']
        depth = row['Depth (cm)']
        imageUrl = row['ThumbnailURL']
        artist = row['Artist']
        if width or depth or height:
            artPiece = ArtMoMA(id, width, depth, height, imageUrl, artist)
            artPieces.append(artPiece)

for art in artPieces:
    if "Abakanowicz" in art.artist:
        art.getImageFile()


# Read in the rows of the artwork_data.csv file into a list of ArtTate objects

# write a loop that saves all artwork thumbnails of an artist to a specific folder
