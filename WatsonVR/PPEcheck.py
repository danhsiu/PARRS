# This script uses Watson Visual Recognition to locate PPE on personnel

import json
from watson_developer_cloud import VisualRecognitionV3

# API Setup
vr = VisualRecognitionV3('2017-10-14', api_key='6f0aeb66590d3e711120fe2985dcf4ec7c186134')

# Detect Face in image
faceLocation = vr.detect_faces(images_file="@1.jpg")
print(json.dumps(faceLocation))


