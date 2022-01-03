from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang.builder import Builder
from plyer import filechooser
import pathlib

Builder.load_file('./stambilj.kv')
Window.size = (350,550)



class StambiljWidget(Widget):
    def ucitaj(self):
        imported_file = filechooser.open_file(title="Izaberi prijavu")


        ##preventing crashing app if user not load any file
        if len(imported_file) !=0:
            file_extension = pathlib.Path(imported_file[0]).suffix
            list_of_extensions = [".pdf", ".bmp", ".jpg", ".jpeg", ".png"]
            if (file_extension not in list_of_extensions):
                # create content and add to the popup
                content = Button(text='Zatvori!')
                popup = Popup(title="Nije dobar format fajla.",
                              content=content, auto_dismiss=False,

                              size_hint=(None, None), size=(300, 200)
                              )

                # bind the on_press event of the button to the dismiss function
                content.bind(on_press=popup.dismiss)

                # open the popup
                popup.open()

    def zavrsi(self):
        datum = self.ids.datum_prijave.text
        broj = self.ids.broj_prijave.text


class StambiljApp(App):
    def build(self):
        return StambiljWidget()

if __name__ == "__main__":
    StambiljApp().run()