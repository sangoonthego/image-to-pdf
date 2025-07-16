from PIL import Image, ImageDraw, ImageFont

def add_watermark(image: Image.Image, text: str, position=(10, 10), opacity=128):
    watermark = Image.new("RGBA", image.size)
    draw = ImageDraw.Draw(watermark)

    try:
        font = ImageFont.truetype("arial.ttf", 36)
    except:
        font = ImageFont.load_default()

    draw.text(position, text, fill=(255, 255, 255, opacity), font=font)
    watermarked = Image.alpha_composite(image.convert("RGBA"), watermark)
    return watermarked.convert("RGB")