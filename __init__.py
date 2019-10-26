import display
import leds
import htmlcolor
import utime
dis = display.open() 
dis.clear()  
dis.print("Jugend Hackt") 
dis.update() 

zeile1=[1,2,2,1,1,1,1,1,2,2,1]
zeile2=[2,2,2,2,1,1,1,2,2,2,2]

feld=[
    zeile1,
    zeile2,
    [2,2,2,2,2,2,2,2,2,2,2],
    [2,2,2,2,2,2,2,2,2,2,2],
    [2,2,3,3,3,3,3,3,3,2,2],
    [2,3,3,3,3,3,3,3,3,3,2],
    [2,3,4,3,3,3,3,3,4,3,2],
    [2,3,3,3,4,3,4,3,3,3,2],
    [2,2,3,3,4,4,4,3,3,2,2],
    [1,2,2,3,3,3,3,3,2,2,1],
    [1,1,2,2,2,2,2,2,2,1,1],
]

while True:
    for zeilenindex,zeile in enumerate(feld):
        for lama,colorcode in enumerate(zeile):
            if 1==colorcode:
                leds.prep(lama, htmlcolor.RED)
            if 2==colorcode:
                leds.prep(lama, htmlcolor.BLUE)
            if 3==colorcode:
                leds.prep(lama, htmlcolor.WHITE)
            if 4==colorcode:
                leds.prep(lama, htmlcolor.BLACK)
        leds.update()
        utime.sleep(0.004)
