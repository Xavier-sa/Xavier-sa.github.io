from pdf2image import convert_from_path

# Converte PDF para imagens
pages = convert_from_path('aulasdefigma.pdf', dpi=300)

# Salva cada página como imagem
for i, page in enumerate(pages):
    page.save(f'pagina_{i + 1}.jpg', 'JPEG')
