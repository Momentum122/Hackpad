import board
import busio
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306

from kb import SmolPad
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

keyboard = SmolPad()

media_keys = MediaKeys()
keyboard.extensions.append(media_keys)

encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.D6, board.D7, board.D10),)
encoder_handler.map = (
    ((KC.AUDIO_VOL_UP, KC.AUDIO_VOL_DOWN, KC.AUDIO_MUTE),),
)
keyboard.modules.append(encoder_handler)


keyboard.keymap = [
    [
        KC.MEDIA_PLAY_PAUSE, KC.BRIU,       KC.BRID,
        KC.LGUI,             KC.AUDIO_MUTE, KC.LCTL(KC.C),
        KC.LCTL(KC.X),       KC.LCTL(KC.V), KC.LCTL(KC.Z),
    ]
]


displayio.release_displays()
i2c = busio.I2C(scl=board.D8, sda=board.D9)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)

splash = displayio.Group()
text_area = label.Label(
    terminalio.FONT,
    text="SmolPad Active",
    color=0xFFFFFF,
    x=10,
    y=16
)
splash.append(text_area)
display.root_group = splash

if __name__ == "__main__":
    keyboard.go()
