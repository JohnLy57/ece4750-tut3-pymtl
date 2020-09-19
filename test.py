from pymtl import *

class Point( BitStructDefinition):
    def __init__(s):
        s.x = BitField(4)
        s.y = BitField(4)

pt1 = Point()
pt1.x = 3
pt1.y = 4
# print(pt1)
# print(pt1.x)
# print(pt1.y)
# print(pt1 & Bits( 8, 0xf0 ))
# print(pt1[0:4])

class PointN( BitStructDefinition ):
    def __init__( s, nbits ):
        s.x = BitField(nbits)
        s.y = BitField(nbits)

class RGBbasic():
    def __init__(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b

class RGB24(BitStructDefinition):
    def __init__(s,r,g,b):
        s.r = BitField(8)
        s.g = BitField(8)
        s.b = BitField(8)