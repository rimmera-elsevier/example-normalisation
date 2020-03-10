from pylatex import Document


def remove_file_extension(file_name: str) -> str:
    return file_name.split(".")[0]


def generate_pdf_file_with_simple_content(file_name: str, content: str) -> None:

    pdf_file = Document(
        default_filepath=remove_file_extension(file_name),
        page_numbers=False
    )

    pdf_file.append(content)
    pdf_file.generate_tex()
    pdf_file.generate_pdf(clean_tex=False)
