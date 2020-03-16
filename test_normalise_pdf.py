import normalise_pdf

from bs4 import BeautifulSoup
from pylatex import Document


def generate_pdf_file_with_simple_content(file_name: str, content: str) -> None:

    pdf_file = Document(
        default_filepath=file_name,
        page_numbers=False
    )

    pdf_file.append(content)
    pdf_file.generate_tex()
    pdf_file.generate_pdf(clean_tex=False)


def _generate_pdf_normalise_and_read_back_html_content(file_name: str, content: str):
    generate_pdf_file_with_simple_content(
        file_name,
        content
    )
    normalised_html = normalise_pdf.generate_normalised_html_from_pdf_file(file_name)
    return BeautifulSoup(normalised_html, 'html.parser')


def test_can_generate_single_sentence_pdf_file_and_convert_to_normalised_html5():
    file_name = "test_output/example_1"
    content = "Hello, world."
    soup = _generate_pdf_normalise_and_read_back_html_content(file_name, content)

    section = soup.section
    assert content in str(section.string)
