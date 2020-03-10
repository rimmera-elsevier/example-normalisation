import dominate
from dominate.tags import *
from dominate.util import raw
from pdfminer.high_level import extract_text


def extract_text_from_pdf(pdf_file_name):
    return extract_text(pdf_file_name)


def generate_normalised_html_from_pdf_file(pdf_file_name):
    """
    <!DOCTYPE html>
    <html xmlns="http://www.w3.org/1999/xhtml" xml:base="https://example.com/minimal">
      <head>
        <link rel="schema.dct" href="http://purl.org/dc/terms/" />
        <meta name="id" content="https://example.com/minimal"></meta>
        <meta name="dct:conformsTo" content="http://data.elsevier.com/schema/led/" />
        <script type="application/ld+json">
          {
            "@context": ["https://data.elsevier.com/schema/led/", {"doc": "https://example.com/minimal#"}],
            "@id": "https://example.com/minimal",
            "dct:conformsTo": ["https://data.elsevier.com/schema/led/", "https://data.elsevier.com/schema/edm/"]
          }
        </script>
      </head>
      <body>
      </body>
    </html>
    """
    text_content = extract_text_from_pdf(pdf_file_name)
    print(text_content)
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

    return html_doc.render(pretty=True).replace("<title></title>\n", "")  # Hack to remove unwanted title
