from PIL import Image


def imgResize(file, maxWidth):
    """Reduce image dimensions and quality"""
    
    newFileName = imgRename(file)
    
    inputImage = Image.open(file)
    (inWidth, inHeight) = inputImage.size 
    
    
    if (maxWidth >= inWidth):
        inputImage.save(newFileName, optimize=True, quality=85)
        return newFileName
    
    imgRatio = float(inHeight)/inWidth
    
    outputImage = inputImage.resize((maxWidth, int(maxWidth*imgRatio)), Image.ANTIALIAS)
    outputImage.save(newFileName, optimize=True, quality=85)
        
    return newFileName

def imgRename(fileName):
    
    fileNameSplit = fileName.split('.')
    newFileName = fileNameSplit[0]+'_rez.'+fileNameSplit[1]
    
    return newFileName