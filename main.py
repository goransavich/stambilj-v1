from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder
from plyer import filechooser
import pathlib

Builder.load_file('./stambilj.kv')
Window.size = (350,550)



class StambiljWidget(Widget):
    def ucitaj(self):
        imported_file = filechooser.open_file(title="Izaberi prijavu",
                                         filters=["*.pdf", "*.bmp", "*.jpg","*.jpeg", "*.png"])

        if len(imported_file) !=0:
            file_extension = pathlib.Path(imported_file[0]).suffix


    def zavrsi(self):
        datum = self.ids.datum_prijave.text
        broj = self.ids.broj_prijave.text


class StambiljApp(App):
    def build(self):
        return StambiljWidget()

if __name__ == "__main__":
    StambiljApp().run()