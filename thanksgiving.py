import board
import displayio
from adafruit_st7789 import ST7789
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.roundrect import RoundRect
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.polygon import Polygon
from adafruit_display_shapes.rect import Rect


BORDER = 20
BACKGROUND_COLOR = 0xa15512
displayio.release_displays()
spi = board.SPI()
tft_cs = board.D2
tft_dc = board.D3
dbus = displayio.FourWire(spi, command = tft_dc, chip_select = tft_cs)
display = ST7789(dbus, rotation = 270, width = 240, height = 135, rowstart = 40, colstart = 53)
thanksgiving = displayio.Group()
display.root_group = thanksgiving
color_bitmap = displayio.Bitmap(display.width, display.height, 1)
color_palette = displayio.Palette(1)
color_palette[0] = BACKGROUND_COLOR
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader = color_palette, x = 0, y=0)
thanksgiving.append(bg_sprite)

third = Circle(120, 87, 40, fill = 0xf19e22, outline = 0x926016, stroke = 3)
thanksgiving.append(third)

second = Circle(120, 82, 30, fill = 0xf19e22, outline = 0x926016, stroke = 3)
thanksgiving.append(second)

base = Circle(120, 77, 20, fill = 0xf19e22, outline = 0x926016, stroke = 3)
thanksgiving.append(base)

