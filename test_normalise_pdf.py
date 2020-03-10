import generate_pdf
import normalise_pdf


def test_can_generate_single_sentence_pdf_file_and_convert_to_normalised_html5():
    file_name = "example_1.pdf"
    content = "Hello, world. I am a small and very uninteresting PDF file."

    generate_pdf.generate_pdf_file_with_simple_content(
        file_name,
        content
    )

    print(normalise_pdf.generate_normalised_html_from_pdf_file(file_name))
