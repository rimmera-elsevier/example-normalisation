import unittest

from bs4 import BeautifulSoup
from pylatex import Document

from normalise_pdf import generate_normalised_html


class PDFNormalisationTest(unittest.TestCase):
    output_dir = "test_output"

    @staticmethod
    def strip_pdf_file_extension(file_name: str) -> str:
        return file_name.split(".")[0]

    def current_test_method_name(self):
        return self.id().split(".")[1]

    def setUp(self) -> None:

        output_stem = "{}/{}".format(
            self.output_dir,
            self.current_test_method_name()
        )

        self.output_pdf = "{}.pdf".format(output_stem)
        self.output_html = "{}.html".format(output_stem)

    def test_single_sentence_pdf_no_glyphs(self):
        content = "Hello, world."

        pdf_file = Document(
            default_filepath=self.strip_pdf_file_extension(self.output_pdf),
            page_numbers=False
        )

        pdf_file.append(content)
        pdf_file.generate_tex()
        pdf_file.generate_pdf(clean_tex=False)

        normalised_html = generate_normalised_html(self.output_pdf)
        soup = BeautifulSoup(normalised_html, 'html.parser')
        section = soup.section

        assert content in str(section.string)

    def test_single_sentence_pdf_with_fi_glyph(self):

        # LaTex font renders the fi in file as a single character
        content = "Hello, world. I am a PDF file"

        pdf_file = Document(
            default_filepath=self.strip_pdf_file_extension(self.output_pdf),
            page_numbers=False
        )

        pdf_file.append(content)
        pdf_file.generate_tex()
        pdf_file.generate_pdf(clean_tex=False)

        normalised_html = generate_normalised_html(self.output_pdf)
        soup = BeautifulSoup(normalised_html, 'html.parser')
        section = soup.section

        assert content in str(section.string)
