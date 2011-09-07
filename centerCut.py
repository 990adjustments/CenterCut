"""

centerCut.py

Copyright: Erwin Santacruz, www.990adjustments.com

Written for CINEMA 4D R12.016

Name-US: CenterCut

Description-US: Toggles the center-cut safe zones in 16:9 viewers.
This python script will show where cropping will occur on non-widescreen displays.
It will also toggle the viewer border opacity between 10% and 90%.

Script tested on OS X 10.6.4 and Cinema 4D versions:
CINEMA 4D R12.016
CINEMA 4D R12.032

Creation Date: 11/24/2010

"""

import c4d


def main():
    bd = doc.GetActiveBaseDraw()
    if bd is None:
        return

    if bd[c4d.BASEDRAW_DATA_TITLESAFE_CENTER] == 1:
        bd[c4d.BASEDRAW_DATA_TITLESAFE_CENTER] = 0
    else:
        bd[c4d.BASEDRAW_DATA_TITLESAFE_CENTER] = 1

    if bd[c4d.BASEDRAW_DATA_ACTIONSAFE_CENTER] == 1:
        bd[c4d.BASEDRAW_DATA_ACTIONSAFE_CENTER] = 0
    else:
        bd[c4d.BASEDRAW_DATA_ACTIONSAFE_CENTER] = 1

    #Uncomment the next line to change border color to taste. 
    #bd[c4d.BASEDRAW_DATA_TINTBORDER_COLOR] = c4d.Vector(0.0, 0.0, 0.0) 
    if bd.GetParameterData(c4d.BASEDRAW_DATA_TINTBORDER_OPACITY) == 0.9:
        bd[c4d.BASEDRAW_DATA_TINTBORDER_OPACITY] = 0.1
    else:
        bd[c4d.BASEDRAW_DATA_TINTBORDER_OPACITY] = 0.9;

    c4d.EventAdd()

if __name__=='__main__':
    main()
