#MenuTitle: Activate All instances
# -*- coding: utf-8 -*-
__doc__="""
Activate All instances
"""

thisFont = Glyphs.font

Glyphs.clearLog()
Glyphs.showMacroWindow()

for instance in thisFont.instances:
		instance.active = True
	
		
		