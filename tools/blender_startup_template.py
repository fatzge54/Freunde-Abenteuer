# Blender Start-Template Script

# Zweck: Dieses Python-Skript legt eine standardisierte Blender-Szene an: Kamera, Light-Rig, Render-Settings und grundlegende Sampler.
# Nutzung: blender --background --python tools/blender_startup_template.py -- <output_path>

import bpy
import sys

# Lösche Standardobjekte
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Szene Grundeinstellungen
scene = bpy.context.scene
scene.render.engine = 'CYCLES'
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
scene.render.film_transparent = False
scene.cycles.device = 'GPU'
scene.view_settings.view_transform = 'Filmic'

# Camera
cam_data = bpy.data.cameras.new('Cam')
cam = bpy.data.objects.new('Camera', cam_data)
scene.collection.objects.link(cam)
scene.camera = cam
cam.location = (0.0, -6.0, 2.0)
cam.rotation_euler = (1.2, 0.0, 0.0)

# Key Light (Sun)
light_data = bpy.data.lights.new(name='KeyLight', type='SUN')
light = bpy.data.objects.new(name='KeyLight', object_data=light_data)
scene.collection.objects.link(light)
light.rotation_euler = (0.9, 0.0, 0.6)
light.data.energy = 3.0

# Fill Light (Area)
fill_data = bpy.data.lights.new(name='Fill', type='AREA')
fill = bpy.data.objects.new('Fill', fill_data)
scene.collection.objects.link(fill)
fill.location = (3.0, -3.0, 2.0)
fill.data.size = 2.0
fill.data.energy = 200.0

# Add a ground plane
bpy.ops.mesh.primitive_plane_add(size=20, location=(0,0,0))
plane = bpy.context.active_object
plane.name = 'GroundPlane'

# Create render output directory if provided
argv = sys.argv
if '--' in argv:
    idx = argv.index('--')
    args = argv[idx+1:]
    if len(args) > 0:
        outpath = args[0]
        scene.render.filepath = outpath

print('Startup template created with Camera and Light rig.')
