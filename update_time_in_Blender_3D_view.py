import bpy
import time


texttime = time.ctime()

bpy.context.selected_objects
bpy.ops.object.editmode_toggle()
bpy.ops.font.select_all()
bpy.ops.font.text_insert(text=texttime, accent=False)
bpy.ops.object.editmode_toggle()