from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder
from plyer import filechooser

Builder.load_file('./stambilj.kv')
Window.size = (350,550)



class StambiljWidget(Widget):
    def ucitaj(self):
        path = filechooser.open_file(title="Izaberi prijavu",
                                     filters=[("PDf", "*.pdf")])
        print(path)

    def zavrsi(self):
        datum = self.ids.datum_prijave.text
        broj = self.ids.broj_prijave.text


class StambiljApp(App):
    def build(self):
        return StambiljWidget()

if __name__ == "__main__":
    StambiljApp().run()