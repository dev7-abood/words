import json
import PyPDF2

def extract_words_from_pdf(pdf_path):
    """
    Extract words from a PDF file line by line.
    """
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        words = []
        for page in pdf_reader.pages:
            text = page.extract_text()  # Extract text from the page
            for line in text.splitlines():  # Split text into lines
                words.extend(line.split())  # Split each line into words and add to the list
        return words

def write_words_to_json(words, output_path):
    """
    Write the list of words to a JSON file.
    """
    with open(output_path, 'w') as json_file:
        json.dump({"words": words}, json_file, indent=4)
    print(f"Words successfully written to {output_path}")

# Paths
pdf_file_path = "Unique_Long_Words.pdf"  # Input PDF file
json_output_path = "words.json"  # Output JSON file

# Extract words from the PDF
extracted_words = extract_words_from_pdf(pdf_file_path)

# Write the extracted words to a JSON file
write_words_to_json(extracted_words, json_output_path)
