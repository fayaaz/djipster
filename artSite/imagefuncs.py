from PIL import Image

def resize(file, maxWidth):
    """Reduce image dimensions and quality"""
    
    fileNameSplit = file.split('.')
    newFileName = fileNameSplit[0]+'rez.'+fileNameSplit[1]
    
    inputImage = Image.open(file)
    (inWidth, inHeight) = inputImage.size 
    
    if (maxWidth >= inWidth):
        outputImage.save(newFileName, optimize=True, quality=85)
        return newFileName
    
    imgRatio = float(inHeight)/inWidth
    
    outputImage = inputImage.resize((maxWidth, int(maxWidth*imgRatio)), Image.ANTIALIAS)
    outputImage.save(newFileName, optimize=True, quality=85)
        
    return newFileName