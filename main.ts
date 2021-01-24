input.onButtonPressed(Button.A, function () {
    led.plot(25, 1000)
    led.toggle(2, 15)
})
basic.showString("Paula")
basic.forever(function () {
    music.playTone(262, music.beat(BeatFraction.Whole))
})
