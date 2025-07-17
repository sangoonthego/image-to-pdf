# Image to PDF Streamlit App

This is a simple and user-friendly web application that allows you to convert images to a single PDF file. The app is built using [Streamlit](https://streamlit.io/) and [Pillow](https://python-pillow.org/), and provides options for resizing images and adding watermarks before exporting to PDF.

## Features
- **Upload Multiple Images:** Supports PNG, JPEG, and JPG formats. You can upload and reorder multiple images.
- **Resize Options:** Choose to keep the original size, resize by percentage, or specify exact pixel dimensions.
- **Add Watermark:** Optionally add a custom watermark with adjustable text, position, opacity, font size, and color.
- **Preview:** Instantly preview your images with applied changes before exporting.
- **Export to PDF:** Convert your processed images into a single PDF file and download it.

## Live Demo
Try the app online: [Streamlit Deployment](https://sangoonthego-image-to-pdf-streamlit-app-tywwys.streamlit.app/)

## Getting Started

### Prerequisites
- Python 3.7+

### Installation
1. Clone this repository:
   ```bash
   git clone <your-repo-url>
   cd image-to-pdf
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running Locally
```bash
streamlit run streamlit_app.py
```

## Project Structure
```
image-to-pdf/
│
├── README.md
├── requirements.txt
├── streamlit_app.py
├── utils/
│   ├── order.py
│   ├── watermark.py
│   ├── resize.py
│   ├── pdf.py
```
## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Acknowledgements
- [Streamlit](https://streamlit.io/)
- [Pillow (PIL)](https://python-pillow.org/)
