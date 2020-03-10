from pylatex import Document


def generate_pdf_file_with_simple_content(file_name: str, content: str) -> None:
    pdf_file = Document(file_name)
    pdf_file.append(content)
    pdf_file.generate_tex()
    pdf_file.generate_pdf(clean_tex=False)
