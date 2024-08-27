def on_button_pressed_a():
    for index in range(4):
        I2C_LCD1602.clear()
        I2C_LCD1602.show_string("Ampel An", 5, 0)
        strip.show_color(neopixel.colors(NeoPixelColors.RED))
        basic.pause(5000)
        strip.show_color(neopixel.colors(NeoPixelColors.YELLOW))
        basic.pause(1000)
        strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
        basic.pause(5000)
        strip.show_color(neopixel.colors(NeoPixelColors.YELLOW))
        basic.pause(1000)
        basic.pause(5000)
    I2C_LCD1602.clear()
    I2C_LCD1602.show_string("Ampel aus", 0, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    I2C_LCD1602.show_string("Temperatur", 0, 0)
    I2C_LCD1602.show_number(input.temperature(), 12, 0)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

strip: neopixel.Strip = None
strip.show_rainbow(1, 4)
I2C_LCD1602.lcd_init(39)
basic.show_icon(IconNames.YES)
I2C_LCD1602.show_string("Hallo Max Und", 0, 0)
I2C_LCD1602.show_string("Stefan", 0, 1)
basic.show_leds("""
    . . # . .
    . # . # .
    # # # # #
    # . # . #
    # . # # #
    """)
basic.pause(5000)
basic.show_leds("""
    . # . # .
    . . # . .
    # . . . #
    . # # # .
    . . . . .
    """)
basic.pause(2000)
music.play_melody("D E D C C5 C F G ", 120)
strip = neopixel.create(DigitalPin.P14, 4, NeoPixelMode.RGB)
strip.show_rainbow(1, 360)
basic.pause(2000)
I2C_LCD1602.clear()
basic.pause(200)

def on_forever():
    strip.rotate(1)
    basic.pause(100)
    strip.show()
basic.forever(on_forever)
