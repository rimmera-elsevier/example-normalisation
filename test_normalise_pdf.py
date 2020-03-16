from bs4 import BeautifulSoup
import generate_pdf
import normalise_pdf


def test_can_generate_single_sentence_pdf_file_and_convert_to_normalised_html5():
    file_name = "test_output/example_1.pdf"
    content = "Hello, world. I am a small and very uninteresting PDF."

    generate_pdf.generate_pdf_file_with_simple_content(
        file_name,
        content
    )

    normalised_html = normalise_pdf.generate_normalised_html_from_pdf_file(file_name)

    # print(normalised_html)
    soup = BeautifulSoup(normalised_html, 'html.parser')
    section = soup.section
    print(section.string)
    print(type(section.string))
    assert content in str(section.string)
