import dominate
from dominate.tags import *
from dominate.util import raw
from pdfminer.high_level import extract_text


def generate_normalised_html(pdf_file_name):
    text_content = extract_text(pdf_file_name)
    html_doc = dominate.document(title="")

    with html_doc.head:
        link(rel="schema.dct", href="http://purl.org/dc/terms/")
        meta(name="id", content="https://example.com/minimal")
        meta(name="dct:conformsTo", content="http://data.elsevier.com/schema/led/")
        script(
            raw("""{
            "@context": ["https://data.elsevier.com/schema/led/", {"doc": "https://example.com/minimal#"}],
            "@id": "https://example.com/minimal",
            "dct:conformsTo": ["https://data.elsevier.com/schema/led/", "https://data.elsevier.com/schema/edm/"]
            }"""),
            type="application/ld+json",
        )

    with html_doc:
        section(text_content)

    return html_doc.render(pretty=True)
