import numpy as np
from bar import AudioBar
from sound_process import get_decibel


def setup_bars(screen_w):
    bars = []
    frequencies = np.arange(100, 8000, 100)
    r = len(frequencies)
    width = screen_w / r
    x = (screen_w - width * r) / 2

    for freq in frequencies:
        bars.append(AudioBar(x, 300, freq, (255, 0, 0), max_height=400, width=width))
        x += width

    return bars


def update_bars(bars, screen, delta_time, pos):
    for b in bars:
        b.update(delta_time, get_decibel(pos/1000.0, b.freq))
        b.render(screen)
