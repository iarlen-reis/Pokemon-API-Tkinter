from PIL import Image


def resize_image():
    image = Image.open('pokemon_image.png')
    tamanho = (250, 250)
    image.thumbnail(tamanho)
    image.save("pokemon_image.png")
