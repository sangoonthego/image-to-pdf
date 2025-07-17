from PIL import Image, ImageDraw, ImageFont

def add_watermark(image: Image.Image, text: str, position="center", opacity=128, font_size=None, font_color=(255,255,255)):
    watermark = Image.new("RGBA", image.size)
    draw = ImageDraw.Draw(watermark)

    font_size = font_size or int(min(image.size) * 0.05)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()

    text_size = draw.textsize(text, font)
    if position == "center":
        position = ((image.width - text_size[0]) // 2, (image.height - text_size[1]) // 2)

    draw.text(position, text, fill=(*font_color, opacity), font=font)
    watermarked = Image.alpha_composite(image.convert("RGBA"), watermark)
    return watermarked.convert("RGB")