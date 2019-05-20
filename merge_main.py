from kivy.app import App

from kivy.uix.screenmanager import ScreenManager, NoTransition, Screen
from kivy.uix.popup import Popup

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import CoreImage
from io import BytesIO

from merge import Merge


class MergeModeChooser(Popup, Merge):
    def __init__(self, image_1_path, image_2_path, *args, **kwargs):
        super(MergeModeChooser, self).__init__(image_1_path=image_1_path, image_2_path=image_2_path,*args,**kwargs)
        self.image_1.save(f"{image_1_path}_draft.png")
        self.image_2.save(f"{image_2_path}_draft.png")
        self.first_image.texture = CoreImage(f"{image_1_path}_draft.png").texture
        self.second_image.texture = CoreImage(f"{image_2_path}_draft.png").texture
    
    def choose_mode(self, effect):
        if 'median':
            self.merge_1_median()
        if effect == 'concat':
            self.merge_2_concat()
        if effect == 'blend':
            self.merge_3_blend()
        self.image_merged.save('draft.png')

        self.final_image.texture = CoreImage('draft.png').texture
        self.final_image.source = 'draft.png'
        self.final_image.reload()

class FileChooser(Screen):
    def __init__(self, **kwargs):
        super(FileChooser, self).__init__(**kwargs)
    
    def load_images(self, image_1_path, image_2_path):
        try:
            self.popup = MergeModeChooser(image_1_path=image_1_path[0], image_2_path=image_2_path[0], title="Mode",
                                size_hint=(1,1))
            self.popup.open()
        except Exception as e:
            print(e)

class MainApp(App):
    def build(self):
        self.title = "Vaizdų suliejimo priemonė"
        manager = ScreenManager()
        manager.transition=NoTransition()
        manager.add_widget(FileChooser(name='FileChooser'))
        return manager

if __name__ == '__main__':
    try:
        app = MainApp()
        app.run()
    except Exception as e:
        print(e)
        app.get_running_app().stop()