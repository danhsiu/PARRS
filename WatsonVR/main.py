# This script uses Watson Visual Recognition to determine the features in an uploaded image

import json

from watson_developer_cloud import VisualRecognitionV3

# API Setup
vr = VisualRecognitionV3('2017-10-14', api_key='6f0aeb66590d3e711120fe2985dcf4ec7c186134')

# Classify an Image by URL
results = vr.classify(images_url="http://www.literarychicago.com/wp-content/uploads/2014/05/Dog-at-Computer.jpg")
print(json.dumps(results))

text = vr.recognize_text(images_url="https://capsafe.com.au/wp-content/uploads/2016/12/WARNING_SIGN_HIGH_VOLTAGE__78257.1362074621.1280.1280.jpg")
print(json.dumps(text))

faces = vr.detect_faces(images_url="https://ak4.picdn.net/shutterstock/videos/9000334/thumb/1.jpg")
print(json.dumps(faces))

faces = vr.detect_faces(images)


