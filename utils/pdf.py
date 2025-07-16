import io

def pdf_convert(images: list) -> bytes:
    pdf_bytes = io.BytesIO()
    images[0].save(pdf_bytes, format="PDF", save_all=True, append_images=images[1:])
    return pdf_bytes.getvalue()