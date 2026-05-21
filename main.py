def on_button_pressed_a():
    global slope
    if x2 == x1:
        basic.show_string("Undefined")
    else:
        slope = (y2 - y1) / (x2 - x1)
        basic.show_string("m=")
        basic.show_number(slope)
input.on_button_pressed(Button.A, on_button_pressed_a)

slope = 0
y2 = 0
x2 = 0
y1 = 0
x1 = 0
x1 = 3
y1 = 1
x2 = 3
y2 = 2

def on_forever():
    pass
basic.forever(on_forever)
