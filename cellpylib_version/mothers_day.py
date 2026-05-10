import numpy as np
import cellpylib as cpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image, ImageDraw, ImageFont

ROWS = 80
COLS = 220

# empty grid
ca = np.zeros((1, ROWS, COLS), dtype=np.int32)

# text
img = Image.new('L', (COLS, ROWS), color=255)
draw = ImageDraw.Draw(img)

text = "HAPPY MOTHERS DAY"

font = ImageFont.load_default()

bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

x = (COLS - text_width) // 2
y = (ROWS - text_height) // 2

draw.text((x, y), text, font=font, fill=0)

text_array = np.array(img)

# text cells alive
text_cells = (text_array < 128).astype(int)

# random noise
noise = np.random.choice(
    [0, 1],
    size=(ROWS, COLS),
    p=[0.72, 0.28]
)

# text padding
padding = 8

clean_zone = np.zeros((ROWS, COLS), dtype=bool)

y1 = max(0, y - padding)
y2 = min(ROWS, y + text_height + padding)

x1 = max(0, x - padding)
x2 = min(COLS, x + text_width + padding)

clean_zone[y1:y2, x1:x2] = True

# remove noise near text
noise[clean_zone] = 0

# combine text & noise
ca[0] = np.maximum(text_cells, noise)

# evolution
ca = cpl.evolve2d(
    ca,
    timesteps=100,
    neighbourhood='Moore',
    apply_rule=cpl.game_of_life_rule,
    memoize='recursive'
)

# animation
fig, ax = plt.subplots(figsize=(16, 7))

img_plot = ax.imshow(
    ca[0],
    interpolation='nearest',
    cmap='Greys'
)

ax.axis('off')

def init():
    img_plot.set_data(ca[0])
    return [img_plot]

def animate(i):
    img_plot.set_data(ca[i])
    return [img_plot]

ani = animation.FuncAnimation(
    fig,
    animate,
    init_func=init,
    frames=100,
    interval=100,
    blit=True,
    repeat=False
)

plt.show()
