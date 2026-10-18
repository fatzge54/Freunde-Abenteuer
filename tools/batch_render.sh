# Batch Render Helper (Blender CLI wrapper)

#!/bin/bash
# Usage: ./batch_render.sh <blendfile> <scene_name> <output_path>

BLENDFILE="$1"
SCENE="$2"
OUTPUT="$3"

if [ -z "$BLENDFILE" ] || [ -z "$OUTPUT" ]; then
  echo "Usage: $0 <blendfile> <scene_name> <output_path>"
  exit 1
fi

blender --background "$BLENDFILE" --scene "$SCENE" --render-output "$OUTPUT" --render-frame 1..250 --engine CYCLES -- --cycles-device GPU
