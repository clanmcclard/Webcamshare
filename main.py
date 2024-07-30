from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import time
from kivy.core.clipboard import Clipboard
from filesharer import Filesharer
import webbrowser

Builder.load_file('frontend.kv')


class CameraScreen(Screen):
    def start(self):
        self.ids.camera.play = True
        self.ids.camera.opacity = 1
        self.ids.camera_button.text = "Stop Camera"
        self.ids.camera.texture = self.ids.camera._camera.texture
        self.ids.camera.opacity = 1

    def stop(self):
        self.ids.camera.play = False
        self.ids.camera_button.text = "Start Camera"
        self.ids.camera.texture = None
        self.ids.camera.opacity = 0

    def capture(self):
        current_time = time.strftime('%m%d%Y-%H%M%S')
        self.filepath = f"images/{current_time}.png"
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.filepath

class ImageScreen(Screen):

    link_error_msg = "You must create the link first!"

    def create_link(self):
        file_path = App.get_running_app().root.ids.camera_screen.filepath
        filesharer = Filesharer(filepath=file_path)
        self.url = filesharer.share()
        self.ids.label.text = self.url

    def copy_link(self):
        try:
           Clipboard.copy(self.url)
        except:
            self.ids.label.text = self.link_error_msg

    def open_link(self):
        try:
            webbrowser.open(self.url)
        except:
            self.ids.label.text = self.link_error_msg
class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
