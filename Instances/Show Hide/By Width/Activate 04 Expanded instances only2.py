#MenuTitle: Activate Expanded instances Only 
# -*- coding: utf-8 -*-
__doc__="""
Activate Expanded instances (and deactivates all others)
Ignores instances where custom parameter "familyName" == "Master Condensed" or "Master Wide"
"""

thisFont = Glyphs.font

Glyphs.clearLog()
Glyphs.showMacroWindow()

for instance in thisFont.instances:

	if instance.active:
		instance.active = False
		
	if instance.width == "Expanded":
		instance.active = True
		
	if instance.familyName == "Master Condensed":
		instance.active = False

	if instance.familyName == "Master Wide":
		instance.active = False		