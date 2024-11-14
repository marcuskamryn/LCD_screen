import board
import displayio
from adafruit_st7789 import ST7789
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.roundrect import RoundRect
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.polygon import Polygon
from adafruit_display_shapes.rect import Rect
import time


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

ground = Rect(0, 100, 240, 135, fill = 0x4c8a33, outline = None, stroke = 0)
thanksgiving.append(ground)

third = Circle(120, 87, 40, fill = 0xf19e22, outline = 0x926016, stroke = 3)
thanksgiving.append(third)

overlay = Rect(80, 110, 100, 20, fill = 0x4c8a33, outline = None, stroke = 0)
thanksgiving.append(overlay)

bottom1 = Circle(108, 97, 23, fill = 0xf19e22, outline = None, stroke = 3)
thanksgiving.append(bottom1)

bottom2 = Circle(132, 97, 23, fill = 0xf19e22, outline = None, stroke = 3)
thanksgiving.append(bottom2)

second = Circle(120, 82, 30, fill = 0xf19e22, outline = 0x926016, stroke = 3)
thanksgiving.append(second)

base = Circle(120, 77, 20, fill = 0xf19e22, outline = 0x926016, stroke = 3)
thanksgiving.append(base)

stem = RoundRect(115, 40, 10, 20, 5, fill = 0x30860e, outline = None, stroke = 0)
thanksgiving.append(stem)

i = 5
r = 2
while True:
    third.x -= i
    overlay.x -= i
    bottom1.x -= i
    bottom2.x -= i
    second.x -= i
    base.x -= i
    stem.x-= i
    time.sleep(0.05)
        
    if stem.x < 0 or stem.x > 240:
        i *= -1
        
    if stem.x == 0:
        ground.fill = 0x4c8a33
        overlay.fill = 0x4c8a33
        color_palette[0] = BACKGROUND_COLOR
    
    if stem.x == 240:
        ground.fill = 0x314e32
        overlay.fill = 0x314e32
        color_palette[0] = 0x333361
    
    third.y += r
    overlay.y += r
    bottom1.y += r
    bottom2.y += r
    second.y += r
    base.y += r
    stem.y += r
    time.sleep(0.0005)
    if base.y > 135 or base.y < 77:
        r *= -1
