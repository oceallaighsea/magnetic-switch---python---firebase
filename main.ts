input.onButtonPressed(Button.A, function () {
    basic.showNumber(input.magneticForce(Dimension.X))
})
basic.showLeds(`
    # # . . .
    . # # . .
    . . # # .
    . . . # #
    . . . . #
    `)
serial.redirect(
SerialPin.P0,
SerialPin.P1,
BaudRate.BaudRate115200
)
serial.redirectToUSB()
basic.forever(function () {
    if (input.magneticForce(Dimension.X) < 100) {
        serial.writeLine("1")
        basic.showNumber(input.magneticForce(Dimension.X))
        basic.showLeds(`
            # . . . #
            # . . # .
            # . # . .
            # # . . .
            # . . . .
            `)
        basic.pause(5000)
    } else {
        serial.writeLine("0")
        basic.showLeds(`
            # . . . .
            # . . . .
            # . . . .
            # . . . .
            # . . . .
            `)
        basic.pause(5000)
    }
})
