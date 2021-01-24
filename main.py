def on_button_pressed_a():
    led.plot(25, 1000)
input.on_button_pressed(Button.A, on_button_pressed_a)

basic.show_string("Hello!")

def on_forever():
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
basic.forever(on_forever)
