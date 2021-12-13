#!/usr/bin/python
# -*- coding: UTF-8 -*-
#import chardet
import os
import sys 
import time
import logging
import spidev as SPI
sys.path.append("..")
from lib import LCD_2inch
from PIL import Image,ImageDraw,ImageFont
import face

class Expression:
    # Raspberry Pi pin configuration:
    RST = 27
    DC = 25
    BL = 18
    bus = 0
    device = 0
    eye_width = 80
    eye_length = 120

    def __init__(self):
        # display with hardware SPI:
        ''' Warning!!!Don't  creation of multiple displayer objects!!! '''
        # display resolution 240 x 320
        #disp = LCD_2inch.LCD_2inch(spi=SPI.SpiDev(bus, device),spi_freq=10000000,rst=RST,dc=DC,bl=BL)
        self.disp = LCD_2inch.LCD_2inch()
        # Initialize library.
        self.disp.Init()
        # Clear display.
        self.disp.clear()
        
        # Create blank image for drawing.
        self.image1 = Image.new("RGB", (self.disp.height, self.disp.width ), "BLACK")
        self.draw = ImageDraw.Draw(self.image1)
        self.draw.ellipse((70,60,140,180), fill = (0,255,255))
        self.draw.ellipse((180,60,250,180), fill = (0,255,255))
        self.disp.ShowImage(self.image1)

    def left_eye_coor(self):
        pass
    
    def test(self):
        for i in range(2):
            self.image1 = Image.new("RGB", (self.disp.height, self.disp.width ), "BLACK")
            self.draw = ImageDraw.Draw(self.image1)
            self.draw.ellipse((70-25*i,60,140-25*i,180), fill = (0,255,255))
            self.draw.ellipse((180-25*i,60,250-25*i,180), fill = (0,255,255))
            self.disp.ShowImage(self.image1)
            #time.sleep(0.01);
        time.sleep(0.5)
        for i in range(4):
            self.image1 = Image.new("RGB", (self.disp.height, self.disp.width ), "BLACK")
            self.draw = ImageDraw.Draw(self.image1)
            self.draw.ellipse((20+25*i,60,90+25*i,180), fill = (0,255,255))
            self.draw.ellipse((130+25*i,60,200+25*i,180), fill = (0,255,255))
            self.disp.ShowImage(self.image1)
            #time.sleep(0.01);
        time.sleep(0.5)
        for i in range(2):
            self.image1 = Image.new("RGB", (self.disp.height, self.disp.width ), "BLACK")
            self.draw = ImageDraw.Draw(self.image1)
            self.draw.ellipse((120-25*i,60,190-25*i,180), fill = (0,255,255))
            self.draw.ellipse((230-25*i,60,300-25*i,180), fill = (0,255,255))
            self.disp.ShowImage(self.image1)
            #time.sleep(0.01);
        time.sleep(0.5)
        
        

#expression = Expression()
#time.sleep(1)

#expression.test()
#print('done')
    
    
    
    