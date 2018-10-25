import requests
import json
# Given an image with human readable characters. Detect input language & extract text content from there.
# https://pixlab.io/#/cmd?id=ocr for additional information.

req = requests.get('https://api.pixlab.io/ocr',params={
	'img':'http://www.mwpvl.com/assets/images/autogen/Amazon-Delivery-Station-Network-in-USA_1.png',
	'orientation':True, # Correct text orientation
	'nl':True, # Output new lines if any
	'key':'api_key'
})
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
else:
	print ("Input language: " + reply['lang'])
	print ("Text Output: " + reply['output'])
	# Iterate over all extracted words
	for box in reply['bbox']:
		print ("Word: " + box['word'])
		print ("Bounding box - X: " + str(box['x']) + " Y: " + str(box['y']) + " Width: " + str(box['w']) + " Height: " + str(box['h']))
