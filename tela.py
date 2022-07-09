from tkinter import Tk, Button, Label, Entry


class Tela:
    def __init__(self) -> None:
        self.tela = Tk()
        self.tela.title('Pokemon API')
        self.tela.resizable(False, False)
        #self.tela.configure(background='#F1EBB4')
        self.tela.geometry('400x400')
        self.widgets()
        self.tela.mainloop()

    def get_id_pokemon(self):
        return self.id_pokemon.get()

    def get_label_loading(self):
        return self.nome_pokemon

    def widgets(self):
        self.label('POKEMON API', 1, 10, 1, '#79d5b5')
        self.label('POKEMON ID:', 3, 60, 0.40, '#f1fdf5')
        self.id_pokemon = Entry(font='10')
        self.id_pokemon.place(x=165, y=60, relwidth=0.58, relheight=0.072)
        self.nome_pokemon = Label(
            text='AGUARDANDO',
            font='Courier',
            bg='#79d5b5'
        )
        self.nome_pokemon.place(x=1, y=105, relwidth=1)
        self.button('GET POKEMON', 1, 355, 1, '#79d5b5', self.get_id_pokemon)

    def button(self, text, localx, localy, relwidth, bg, command):
        Button(text=text, bg=bg, font='Comic', command=lambda: command()) \
            .place(x=localx, y=localy, relwidth=relwidth)

    def label(self, text, localx, localy, wid, bg):
        Label(text=text, font='Courier', bg=bg) \
            .place(x=localx, y=localy, relwidth=wid)
