from PIL import Image

def resize_images(image: Image.Image, mode="original", percent=100, width=None, height=None):
    if mode == "percent":
        image = image.resize((int(image.width * percent / 100), int(image.height * percent / 100)))
    elif mode == "pixel" and width and height:
        image = image.resize((int(width), int(height)))
    return image
    
