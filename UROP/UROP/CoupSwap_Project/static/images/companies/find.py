from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

def downloadimg(query):
	arguments = {"keywords": query,
				"format": "png",
				"limit":1,
				"print_urls":True,
				"size": "medium",}
	try:
		response.download(arguments)
	
	except:
		pass

downloadimg(input())
