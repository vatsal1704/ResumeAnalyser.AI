from pypdf import PdfReader


def process_pdf(pdf_doc):
    pdf= PdfReader(pdf_doc) # ojective is to extract the text and save it in a variable.
    raw_text = ""
    # index of the pdf page and page content
    for index, page in enumerate(pdf.pages):
        content= page.extract_text()
        if content:
            raw_text += content
    return raw_text