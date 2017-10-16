# This script uses Watson Visual Recognition to determine the features in an uploaded image

import json

from watson_developer_cloud import VisualRecognitionV3

# API Setup
vr = VisualRecognitionV3('2017-10-14', api_key='6f0aeb66590d3e711120fe2985dcf4ec7c186134')

# Classify an Image by URL
results = vr.classify(images_url="http://bit.ly/2yLPOFb")
print(json.dumps(results))

