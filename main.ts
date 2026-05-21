input.onButtonPressed(Button.A, function () {
    if (x2 == x1) {
        basic.showString("Undefined")
    } else {
        slope = (y2 - y1) / (x2 - x1)
        basic.showString("m=")
        basic.showNumber(slope)
    }
})
let slope = 0
let y2 = 0
let x2 = 0
let y1 = 0
let x1 = 0
x1 = 3
y1 = 1
x2 = 3
y2 = 2
basic.forever(function () {
	
})
