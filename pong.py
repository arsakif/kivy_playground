from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout


class PongGame(Widget):
    pass


class PongGameApp(App):
    def build(self):
        return PongGame()


if __name__ == "__main__":
    PongGameApp().run()

