import PyPDF2

# Path to the PDF file
# pdf_path = "/home/george/Downloads/Back-Up-As-Far-As-the-World-Stretches.pdf"
pdf_path = "/home/george/Downloads/The-Bible.pdf"
output_path = "text.txt"

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

# Extract text from the PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Split text after each period followed by a space (to avoid breaking numbers, etc.)
formatted_text = pdf_text.replace(". ", ".\n").strip()

# Save the formatted text to a new file
with open(output_path, "w", encoding="utf-8") as output_file:
    output_file.write(formatted_text)

print(f"Formatted text has been saved to {output_path}.")
