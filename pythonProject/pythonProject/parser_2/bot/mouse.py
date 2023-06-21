import matplotlib.pyplot as plt
import pyautogui as pag
import numpy as np
from pyHM import mouse

pag.drag(600, 500, 2, button='left', pag.easeInQuad)
pag.moveTo(600, 500, 2, pag.easeInQuad)     # начни медленно, закончи быстро
pag.moveTo(200, 100, 2, pag.easeOutQuad)    # начнем быстро, закончим медленно
#pag.moveTo(300, 100, 3, pag.easeInOutQuad)  # начать и закончить быстро, медленно в середине
#pag.moveTo(500, 100, 2, pag.easeInBounce)    # подпрыгнуть в конце
#pag.moveTo(100, 150, 2, pag.easeInElastic)   # резинка в конце

