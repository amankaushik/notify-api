def wiriteJSONToFile(self, filename, collection):
		print('Writing Stories to File ...')
		with open(filename, 'w', encoding='utf8') as outF:
			for item in collection:
				json.dump(item.__dict__, outF)
		print('Stories written to file')

@retry(uErr, tries=4, delay=3, backoff=2)
def getResponse(url):
	try:
		return uReq.urlopen(url)
	except HTTPError as err:
		print ('HTTPError: '.format(err))
	except URLError as err:
		print ('URLError: '.fromat(err))
