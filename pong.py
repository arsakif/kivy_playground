from random import randint

from kivy.app import App
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.vector import Vector


class PongGame(Widget):

    def serve_ball(self):
        self.ball.center = self.center
        self.ball.velocity = Vector(dp(10), 0).rotate(randint(0, 360))

    def update(self, dt):
        self.ball.move_ball()

        # bounce off top and bottom
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1

        # bounce off left and right
        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.velocity_x *= -1

    def on_touch_down(self, touch):
        if self.width/2 - 5 < touch.x < self.width/2 + 5:
            self.serve_ball()

        if self.width/2 + 5 < touch.x:
            if self.height/2 < touch.y:
                self.move_racket_2_up()
            else:
                self.move_racket_2_down()

        if self.width/2 - 5 > touch.x:
            if self.height/2 < touch.y:
                self.racket1.move_racket_1_up()
            else:
                self.racket1.move_racket_1_down()


class PongBall(Widget):
    # velocity of the ball on x and y
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)


    # move fuction to move the ball
    def move_ball(self):
        self.pos = Vector(*self.velocity) + self.pos


class Racket_1(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # move fuction to move the ball
    def move_racket_1_up(self):
        self.velocity = Vector(0, 5)
        self.pos = Vector(*self.velocity) + self.pos

    def move_racket_1_down(self):
        self.velocity = Vector(0, -5)
        self.pos = Vector(*self.velocity) + self.pos



class Racket_2(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # move fuction to move the ball
    def move_racket_2_up(self):
        self.velocity = Vector(0, 5)
        self.pos = Vector(*self.velocity) + self.pos

    def move_racket_2_down(self):
        self.velocity = Vector(0, -5)
        self.pos = Vector(*self.velocity) + self.pos


class PongGameApp(App):
    def build(self):
        game = PongGame()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == "__main__":
    PongGameApp().run()
