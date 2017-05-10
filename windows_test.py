#!/usr/bin/python
# -*- coding: latin-1 -*-

"""
Copyright (c) 2008 Canio Massimo "Keebus" Tristano

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.




THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
"""

import pygame
from pygame.locals import *
pygame.init()

import spg
from spg.core import *

#screen = pygame.display.set_mode((800,600), pygame.RESIZABLE)
screen = pygame.display.set_mode((800,600))
FPS = 25 
clock = pygame.time.Clock()
running = True

# *** TESTING HERE ***
artpath = "art/"
background = pygame.image.load(artpath + "back.png").convert()

#COMMON STYLES

SkinOK_icon = pygame.image.load(artpath + "ok.png").convert_alpha()
SkinCancel_icon = pygame.image.load(artpath + "cancel.png").convert_alpha()
SkinCloseButton  = pygame.image.load(artpath + "close.png").convert_alpha()
SkinShadeButton =  pygame.image.load(artpath + "shade.png").convert_alpha()

winStyle = {'font': spg.styles.titleFont,
			  'font-color': (255,255,255),
			  'offset-top-left': (14, 35),
			  'offset-bottom-right': (14,14),
			  'title-position': (10,10),
			  
			  'appearence': spg.styles.GRAPHICAL,
			  
			  'border-offset-top-left': (5,5),
			  'border-offset-bottom-right': (7,5),
			  
			  'image-top-left': pygame.image.load(artpath + "win_topleft.png").convert_alpha(),
			  'image-top': pygame.image.load(artpath + "win_top.png").convert_alpha(),
			  'image-top-right': pygame.image.load(artpath + "win_topright.png").convert_alpha(),
			  'image-right': pygame.image.load(artpath + "win_right.png").convert_alpha(),
			  'image-bottom-right': pygame.image.load(artpath + "win_bottomright.png").convert_alpha(),
			  'image-bottom': pygame.image.load(artpath + "win_bottom.png").convert_alpha(),
			  'image-bottom-left': pygame.image.load(artpath + "win_bottomleft.png").convert_alpha(),
			  'image-left': pygame.image.load(artpath + "win_left.png").convert_alpha(),
			  'image-middle': pygame.image.load(artpath + "win_middle.png").convert_alpha(),
			  
			  'close-button-skin':  SkinCloseButton,
			  'shade-button-skin': SkinShadeButton,
			  
			  'close-button-offset': (10,7),
			  'shade-button-offset': (32,7),
			  'shade-button-only-offset': (10,7)
			  }

graphicButtonStyle1 = {'font': spg.styles.defaultFont,
					  'antialias': True,
					  'autosize': True,
					  
					  'appearence': spg.styles.GRAPHICAL,
					  
					  'font-color':(0,0,0),
					  'font-color-over': (0,0,0),
					  'font-color-down': (0,0,0),
					  'font-color-disabled': (0,0,0), 
					  
					  'skin': pygame.image.load(artpath + "button.png").convert_alpha(),
					  'widths-normal': (4,1,4),
					  'widths-over': (4,1,4),
					  'widths-down': (4,1,4),
					  'widths-disabled': (4,1,4),
					  'widths-focused': (6,2,6)
					  }

CheckBoxStyle1 = {'font': spg.styles.defaultFont,
                        'font-color': (255,0,0),
                        'font-color-disabled':(150,150,150),
                        'wordwrap': True,
                        'antialias': True,
                        'spacing': 4,
                        
                        'appearence': spg.styles.VECTORIAL,
                        
                        'box-width': 15,
                        
                        'box-color': (50,50,100,100),
                        'box-color-over': (150,150,150,200),
                        'box-color-down': (50,50,50,100),
                        'box-color-disabled': (10,100,100,100),
                        
                        'border-color': (0,0,0),
                        'border-color-over': (0,0,0),
                        'border-color-down': (0,0,0),
                        'border-color-disabled': (0,0,0),
                        
                        'check-color': (0,0,255),
                        'check-color-over': (100,100,255),
                        'check-color-down': (225,225,225),
                        'check-color-disabled': (255,255,255)
                        }

desktop = spg.core.Desktop()

def show_dialog(widget):
	windlg1 = Window(parent = desktop, 
			size = (300,140),
			mode = MODE_DIALOG, 
			style = winStyle, 
			title = "wingdlg1 -- Dialog Window : P", 
			shadeable = False, 
			closeable = False)
	
	Label(parent = windlg1, 
		anchor = ANCHOR_TOP | ANCHOR_LEFT | ANCHOR_RIGHT, 
		autosize = AUTOSIZE_VERTICAL_ONLY, 
		text = 
'''This is a Dialog Window. 
While there's one or more pending dialog windows, 
only the last one gets the input while the others are frozen 
until the last Dialog Window is closed.''')
	
	Button(parent = windlg1, 
		position = (0,0), 
		text = "OK", 
		anchor =  ANCHOR_BOTTOM | ANCHOR_RIGHT,  
		style = graphicButtonStyle1, 
		image = SkinOK_icon).connect('onClick', lambda widget: windlg1.destroy())
	
	Button(parent = windlg1, 
		position = (60,0), 
		text = "Open Another One!", 
		style = graphicButtonStyle1, 
		anchor =  ANCHOR_BOTTOM | ANCHOR_RIGHT).connect('onClick', show_dialog)

def loadwin1():
#--win1
	win1 = Window(position = (100,100), 
		title = "win1 -- Window Always On Back", 
		size = (320,120), 
		parent = desktop, 
		style = winStyle, 
		mode = MODE_ALWAYS_BACK, 
		closeable = False)

	win1.shade()

	Label(text = 
'''This window will always be behind all the others. 
And this is very easy to do, just set the mode window property 
to MODE_ALWAYS_BACK while creating it.''',
		parent = win1, 
		size = (300,70), 
		autosize = 0)

def loadwin2():
#--win2
	win2 =  Window(title = "win2 -- Graphic Window", 
		size = (440,300), 
		parent = desktop, 
		style = winStyle, 
		resizable = True)

	win2.min_size = (360,210)

	Button(parent = win2, 
		text = "OK", 
		anchor =  ANCHOR_BOTTOM | ANCHOR_RIGHT,  
		style = graphicButtonStyle1, 
		image = SkinOK_icon)

	Button(parent = win2, 
		text = "Cancel", 
		position = (50,0), 
		anchor =  ANCHOR_BOTTOM | ANCHOR_RIGHT,  
		style = graphicButtonStyle1,  
		image = SkinCancel_icon)

	Button(parent = win2, 
		position = 10, 
		anchor = ANCHOR_BOTTOM| ANCHOR_LEFT | ANCHOR_RIGHT, 
		style = graphicButtonStyle1, 
		text = "Open a Dialog Window", 
		autosize =  0).connect('onClick', show_dialog)

	CheckBox(text = "Check me! ;)", 
		parent = win2, 
		style = CheckBoxStyle1,
		position = (0,0))

	Label(position = (0,20), 
		text = 
'''Welcome to Simple-Pygame-GUI 2 ! 
This is a very first version of the definitive game-focused GUI system for pygame. 
This is a basic demonstration of the new Window widget with its new features 
such as skinning, resizing, front windows, back windows, dialog windows, and so on. 
Hope you'll enjoy and please stay tuned for further updates and demos on http://www.keebus.net.''',
		parent = win2, 
		anchor = ANCHOR_TOP | ANCHOR_LEFT | ANCHOR_RIGHT, 
		autosize  = AUTOSIZE_VERTICAL_ONLY)

def loadmisc():
	CheckBox(text = "Check me! ;)", 
		parent = desktop, 
		style = CheckBoxStyle1,
		position = (5,5))


# *** END TESTING AREA ***
loadwin1()
loadwin2()
loadmisc()

pygame.display.set_caption("Simple-Pygame-GUI Ver " + spg.__version__)

while running:
	tick = clock.tick(FPS)
	pygame.display.set_caption("%d" % clock.get_fps())
	
	'''
	events = pygame.event.get()
	for event in events:
			#event quit
			if event.type == QUIT:
				running = False
			elif event.type == KEYDOWN and event.key == K_q:
				running = False
			elif event.type == KEYDOWN and event.key == K_F1:
				show_dialog
	'''
	
	for e in spg.setEvents():
		if e.type == pygame.QUIT:
			running = 0
		elif e.type == KEYDOWN and e.key == K_F1:
			running = 0
		
		if e.type == pygame.VIDEORESIZE:
			screen = pygame.display.set_mode(e.size, pygame.RESIZABLE)
		
	screen.blit(background, (0,0))
	desktop.update()
	desktop.draw()
	pygame.display.update()
	
pygame.quit()
