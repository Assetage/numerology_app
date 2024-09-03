import os
import tarfile
import urllib.request

# Directory to store the fonts
font_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")

# Ensure the directory exists
os.makedirs(font_dir, exist_ok=True)

# URL to download the DejaVu Sans fonts archive
font_archive_url = "http://sourceforge.net/projects/dejavu/files/dejavu/2.37/dejavu-fonts-ttf-2.37.tar.bz2"
font_archive_path = os.path.join(font_dir, "dejavu-fonts-ttf-2.37.tar.bz2")

# Download the font archive if it doesn't exist
if not os.path.isfile(font_archive_path):
    print(f"Downloading DejaVu fonts archive...")
    urllib.request.urlretrieve(font_archive_url, font_archive_path)
else:
    print(f"DejaVu fonts archive already exists, skipping download.")

# Extract the fonts from the archive
with tarfile.open(font_archive_path, "r:bz2") as tar:
    tar.extractall(path=font_dir)

# Paths to the specific font files
font_files = {
    "DejaVuSans.ttf": os.path.join(
        font_dir, "dejavu-fonts-ttf-2.37/ttf/DejaVuSans.ttf"
    ),
    "DejaVuSans-Bold.ttf": os.path.join(
        font_dir, "dejavu-fonts-ttf-2.37/ttf/DejaVuSans-Bold.ttf"
    ),
    "DejaVuSans-Oblique.ttf": os.path.join(
        font_dir, "dejavu-fonts-ttf-2.37/ttf/DejaVuSans-Oblique.ttf"
    ),
}

# Check if the specific font files exist
for font_name, font_path in font_files.items():
    if not os.path.isfile(font_path):
        raise FileNotFoundError(
            f"Font file {font_name} not found in the extracted archive."
        )
    print(f"Font file {font_name} is ready.")


# Example usage of adding the font to FPDF
def add_fonts_to_fpdf(pdf):
    pdf.add_font("DejaVu", "", font_files["DejaVuSans.ttf"], uni=True)
    pdf.add_font("DejaVu", "B", font_files["DejaVuSans-Bold.ttf"], uni=True)
    pdf.add_font("DejaVu", "I", font_files["DejaVuSans-Oblique.ttf"], uni=True)


# Test the font addition with a sample PDF
def create_sample_pdf():
    pdf = FPDF()
    add_fonts_to_fpdf(pdf)
    pdf.add_page()
    pdf.set_font("DejaVu", "", 14)
    pdf.cell(0, 10, "This is a test PDF with DejaVu Sans font.", 0, 1)
    pdf.output("sample.pdf")


if __name__ == "__main__":
    create_sample_pdf()
