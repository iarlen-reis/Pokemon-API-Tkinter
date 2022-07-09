from tkinter import Label
from tela import Tela
from pathlib import Path
from redimecionar import resize_image
from PIL import Image, ImageTk
import requests


class GetPokemon(Tela):
    def __init__(self) -> None:
        super().__init__()

    def get_id_pokemon(self):
        self.id = super().get_id_pokemon()
        self.get_200_or_404()

    def get_200_or_404(self):
        self.request = requests.get(f'https://pokeapi.co/api/v2/pokemon/{self.id}')
        if self.request.status_code == 200:
            self.get_pokemon_name()
            self.get_image_pokemon()
        else:
            self.erro_404()

    def get_pokemon_name(self):
        self.request = requests.get(f'https://pokeapi.co/api/v2/pokemon/{self.id}')
        self.response = self.request.json()
        self.name_pokemon = self.response['forms'][0]['name']
        self.get_label_loading()

    def get_image_pokemon(self):
        self.image = self.response['sprites']['other']['home']['front_default']
        self.image_content = requests.get(self.image).content
        self.create_image_and_dir()
        self.set_image()

    def get_label_loading(self):
        self.set_text = super().get_label_loading()
        self.set_text['text'] = f'{self.name_pokemon}!'.title()

    def erro_404(self):
        self.set_text = super().get_label_loading()
        self.set_text['text'] = 'No found =|'.title()

    def create_image_and_dir(self):
        image_path = Path('pokemon_image.png')
        try:
            if image_path.exists:
                image_path.unlink()
        except:
            image_path.touch()

        with open('pokemon_image.png', 'wb') as file:
            file.write(self.image_content)
        resize_image()

    def set_image(self):
        image = Image.open('pokemon_image.png')
        photo = ImageTk.PhotoImage(image)
        self.imagem = Label(text='teste')
        self.imagem.config(image=photo)
        self.imagem.image = photo
        self.imagem.place(x=10, y=140, relwidth=0.95, relheight=0.5, width=0.5)

