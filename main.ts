input.onButtonPressed(Button.A, function () {
    for (let index = 0; index < 4; index++) {
        I2C_LCD1602.clear()
        I2C_LCD1602.ShowString("Ampel An", 5, 0)
        strip.showColor(neopixel.colors(NeoPixelColors.Red))
        basic.pause(5000)
        strip.showColor(neopixel.colors(NeoPixelColors.Yellow))
        basic.pause(1000)
        strip.showColor(neopixel.colors(NeoPixelColors.Green))
        basic.pause(5000)
        strip.showColor(neopixel.colors(NeoPixelColors.Yellow))
        basic.pause(1000)
        basic.pause(5000)
    }
    I2C_LCD1602.clear()
    I2C_LCD1602.ShowString("Ampel aus", 0, 0)
})
input.onButtonPressed(Button.AB, function () {
    I2C_LCD1602.ShowString("Temperatur", 0, 0)
    I2C_LCD1602.ShowNumber(input.temperature(), 12, 0)
})
let strip: neopixel.Strip = null
strip.showRainbow(1, 4)
I2C_LCD1602.LcdInit(39)
basic.showIcon(IconNames.Yes)
I2C_LCD1602.ShowString("Hallo Max Und", 0, 0)
I2C_LCD1602.ShowString("Stefan", 0, 1)
basic.showLeds(`
    . . # . .
    . # . # .
    # # # # #
    # . # . #
    # . # # #
    `)
basic.pause(5000)
basic.showLeds(`
    . # . # .
    . . # . .
    # . . . #
    . # # # .
    . . . . .
    `)
basic.pause(2000)
music.playMelody("D E D C C5 C F G ", 120)
strip = neopixel.create(DigitalPin.P14, 4, NeoPixelMode.RGB)
strip.showRainbow(1, 360)
basic.pause(2000)
I2C_LCD1602.clear()
basic.pause(200)
basic.forever(function () {
    strip.rotate(1)
    basic.pause(100)
    strip.show()
})
