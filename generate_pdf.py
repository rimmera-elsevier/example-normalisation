from pylatex import Document, Section, Subsection, Command
from pylatex.utils import italic, NoEscape


def fill_document(doc):
    doc.append("hello world")
    # with doc.create(Section('A section')):
    #     doc.append('Some regular text and some ')
    #     doc.append(italic('italic text. '))
    #
    #     with doc.create(Subsection('A subsection')):
    #         doc.append('Also some crazy characters: $&#{}')


if __name__ == '__main__':
    doc = Document('basic')
    fill_document(doc)
    doc.generate_pdf(clean_tex=False)
    doc.generate_tex()

    # # Document with `\maketitle` command activated
    # doc = Document()
    #
    # doc.preamble.append(Command('title', 'Awesome Title'))
    # doc.preamble.append(Command('author', 'Anonymous author'))
    # doc.preamble.append(Command('date', NoEscape(r'\today')))
    # doc.append(NoEscape(r'\maketitle'))
    #
    # fill_document(doc)
    #
    # doc.generate_pdf('basic_maketitle', clean_tex=False)