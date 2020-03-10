import html

from pdfminer.high_level import extract_text


def extract_text_from_pdf(pdf_file_name):
    return extract_text(pdf_file_name)


def generate_normalised_html_from_pdf_file(pdf_file_name):
    text_content = extract_text_from_pdf(pdf_file_name)
