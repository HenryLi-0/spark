# Center your stuffs

def center(name:str, endstop:int|float, min:int|float, max:int|float, center:int|float):
    # all current config values
    print("\n" + name)
    nEndstop = endstop-center
    nMin = min-center
    nMax = max-center
    print("position_endstop: {} # {}".format(nEndstop, endstop))
    print("position_min: {} # {}".format(nMin, min))
    print("position_max: {} # {}".format(nMax, max))
    return (nEndstop, nMin, nMax)

center("x", 0, -12, 190, 50.00)
center("y", 0,   0, 145, 77.50)