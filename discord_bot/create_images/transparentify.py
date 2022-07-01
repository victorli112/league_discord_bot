from PIL import Image

"""
INPUT: Image object
OUTPUT: Transparent Image object
DESCRIPTION: Converts image object to RGBA tuple values. Creates a new list of pixel tuples by replacing black ones with transparent ones. Replaces original pixel tuples with new list.
"""
def transparentify(image) -> Image:
    rgba = image.convert("RGBA")
    datas = rgba.getdata()
    newData = []
    for item in datas:
        # finding black colour by its RGB value (0,0,0). If black found, append transparent (255,255,255)
        if item[0] == 0 and item[1] == 0 and item[2] == 0: 
            newData.append((255, 255, 255, 0))
        else:
            # other colours remain unchanged
            newData.append(item)  
    
    image.putdata(newData)
    return image