from PIL import Image
ASCII_CHARS = ['#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']


def pegar_imagem(imagem_local):
    img = None
    # processo de pegar a imagem
    try:
        img = Image.open(imagem_local)
    except:
        print('IMAGEM N ENCONTRADA!')
        return
    return img


def converter_cinza(img):
    n_img = img.convert('L')
    return n_img


def converter_px_para_char(img, intervalo_largura=25):
    pixels_img = list(img.getdata())
    pixels_char = []
    print(pixels_img)
    for px_valor in pixels_img:
        aux = ASCII_CHARS[int(px_valor/intervalo_largura)]
        pixels_char.append(aux)

    return "".join(pixels_char)


def converter_imagem_ascii(img, n_largura=50):
    # TENHO: img => IMAGEM CINZA REDIMENSIONADA
    # QUERO: img-> IMGASCII > TEXTO >STRING
    pixels_chars = converter_px_para_char(img)
    tamanho_pixels_chars = len(pixels_chars)
    img_ascii = []
    for indexI in range(0, tamanho_pixels_chars, n_largura):
        aux = pixels_chars[indexI:indexI+n_largura]
        img_ascii.append(aux)
    #img_ascii = [pixels_chars[index:index+n_largura] for index in range(0, tamanho_pixels_chars, n_largura)]
    return "\n".join(img_ascii)


def redimencionar_imagem(img, n_largura=50):
    (orig_largura, orig_altura) = img.size
    aspect_ratio = float(orig_altura/orig_largura)
    n_altura = int(aspect_ratio * n_largura)
    n_img = img.resize((n_largura, n_altura))
    return n_img


def main():
    import sys
    imagem_local = sys.argv[1]
    imagem = pegar_imagem(imagem_local)
    imagem_redimensionada = redimencionar_imagem(imagem)
    imagem_cinza = converter_cinza(imagem_redimensionada)
    imagem_ascii = converter_imagem_ascii(imagem_cinza)
    print(imagem_ascii)
    return


main()
