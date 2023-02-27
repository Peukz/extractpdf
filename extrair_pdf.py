!pip install PyPDF2

import PyPDF2

# abrir o arquivo PDF
pdf_file = open('ResultadoVale.pdf', 'rb')

# criar objeto PDFReader
pdf_reader = PyPDF2.PdfReader(pdf_file)

# extrair texto de todas as páginas
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    print(page.extract_text())