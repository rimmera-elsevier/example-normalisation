import unittest
import generate_pdf
import normalise_pdf

from pdfminer.high_level import extract_text


def test_can_generate_single_sentence_pdf_file_and_convert_to_normalised_html5():
    file_name = "example_1"
    content = "Hello, world. I am a small and very uninteresting PDF file."

    generate_pdf.generate_pdf_file_with_simple_content(
        file_name,
        content
    )
