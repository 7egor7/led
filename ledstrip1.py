import machine 
from ws2812 import WS2812
import utime
import urandom

ws = WS2812(machine.Pin(0),8)

rot = 40
gruen = 0
blau = 0
richtung = +5
farbe = "rot"

while True:
    #for f in ["rot", "gruen", "blau"]:
    if farbe == "rot":
        rot = rot + richtung
        if rot == 0xFF and gruen == 0x00 and blau == 0x00:
            farbe = "gruen"
        elif rot == 0x00:
            farbe = "blau"
            richtung = +5
        elif rot == 0xFF and  blau == 0xFF:
            farbe = "gruen"
            richtung = +5
        
            
    elif farbe == "gruen":
        gruen = gruen + richtung
        if gruen == 0xFF and rot == 0xFF:
            farbe = "rot"
            richtung = -5
        elif gruen == 0x00 and blau == 0xFF:
            farbe = "rot"
            richtung = +5
        if rot == 0xFF and blau == 0xFF and gruen == 0xFF:
            farbe = "weiss"
            richtung = -5
    elif farbe == "weiss":
       rot = rot + richtung
       gruen = gruen + richtung
       blau = blau + richtung
       
       if rot == 0x00 and blau == 0x00 and gruen == 0x00:
           farbe = "rot"
           richtung = +5
       
          
    else:
        blau = blau + richtung
        if blau == 0xFF and gruen == 0xFF:
            farbe = "gruen"
            richtung = -5
           
       
    
    for i in range(0,8):
        ws[i]= (rot<<16) | (gruen<<8) | blau
    #print("farbe ", str(hex((rot<<16) | (gruen<<8) | blau)))
    ws.write()
    utime.sleep_ms(100)


