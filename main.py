from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
import webbrowser
from api_fetcher import get_word_data

class SplashScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        layout.add_widget(Image(source='assets/icon.png', size_hint=(1, 0.4)))
        layout.add_widget(Label(text="Word of the Day", font_size=32, bold=True))
        layout.add_widget(Label(text="Learn English easily", font_size=18))
        start_btn = Button(text="Get started", size_hint=(1, 0.2))
        start_btn.bind(on_press=self.go_to_main)
        layout.add_widget(start_btn)
        self.add_widget(layout)

    def go_to_main(self, instance):
        self.manager.current = 'main'

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        word = get_word_data()
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text=word["word"], font_size=32, bold=True))
        layout.add_widget(Label(text=word["transcription"], font_size=20))
        layout.add_widget(Label(text=word["example"], font_size=16))
        play_button = Button(text="🔊 Вимова", size_hint=(1, 0.2))
        play_button.bind(on_press=lambda x: webbrowser.open(word["audio"]))
        layout.add_widget(play_button)
        self.add_widget(layout)

class WordApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SplashScreen(name='splash'))
        sm.add_widget(MainScreen(name='main'))
        return sm

if __name__ == "__main__":
    WordApp().run()