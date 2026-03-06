from _ctypes import Structure, byref
from ctypes import c_long #, windll


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]


def queryMousePosition():
    pt = POINT()
    # windll.user32.GetCursorPos(byref(pt))
    return {"x": pt.x, "y": pt.y}
