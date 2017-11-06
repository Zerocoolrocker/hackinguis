# Hackinguis
Hackinguis is a Python library that allows to develop scripts for interact with user graphical interfaces. It is formed by a series of modules that meet the following characteristics:
- Human aspect of behavior.
- Robust, fast and effective.
- Easy to develop.
- Multiplatform.

## Requirements
You need to install [autopy's requirements](https://github.com/msanders/autopy).

## Installation
```
git clone https://github.com/mondeja/hackinguis.git
cd hackinguis
pip install -r requirements.txt
python setup.py install
```
__________________________________________________________

## Modules:

### human_mouse
Human mouse is a library to performs human inputs mouse movements. It's built on top of [autopy's mouse module](https://github.com/mondeja/autopy_mouse).

_________________________________________________________

## Documentation

### Human Mouse
```python
from hackinguis import HumanMouse

hm = HumanMouse()

"""
This class has the following optional parameters:

    :param mouse_speed: Mouse velocity
        (optional, default == 18)
    :type mouse_speed: int/float

    :param gravity: If the number is larger, 
        grater uniformity of movement
        (optional, default == 60)
    :type gravity: inf/float

    :param wind: aleatority of movement
        (optional, default == 60)
    :type wind: int/float

    :param target_error: Error in target
        objetive (optional, default == 500)
        before achieve it without error
    :type target_error: int/float
"""

hm.move(<x>, <y>)          # Human-like movement
hm.click(<x>, <y>)         # Human-like movement and click
hm.double_click(<x>, <y>)  # Human-like movement and double click
```

### Virtual mouse
These are the fastest functions tested for working with machine-like mouse behavior ([autopy mouse reference](http://www.autopy.org/documentation/api-reference/mouse.html)).

```python
from autopy_mouse import mouse

mouse.click(<x>, <y>)       # Click without previous movement
mouse.move(<x>, <y>)        # Mouse teleportation
mouse.get_pos()             # Get current mouse position
mouse.toggle(<bool>)        # Holds down (True) or releases (False) mouse
mouse.smooth_move(<x>, <y>) # Mouse movement in a straight line

# ==========================================================

from pymouse import PyMouse
m = PyMouse()

m.scroll(vertical=<int>,   # Mouse scroll a number of times, 
         horizontal=<int>) # parameters are None by default

m.screen_size() # Gets (width, height) of your screen
```


