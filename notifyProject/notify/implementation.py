class HackerNewsAPIImpl:
	def __init__(self):
		pass

	def checkRedundantIDs(self, idList):
		try:
			fFile = open('ids.txt', 'r')
		except (IOError, OSError) as err:
			print ("Could not open file: " + format(err))
		else:
			oldIDList = []
			for idd in fFile:
				oldIDList.append(int(idd))
		finally:
			fFile.close()
		try:
			fFile = open('ids.txt', 'w')
		except (IOError, OSError) as err:
			print ("Could not open file: " + format(err))
		else:
			for idd in idList:
				fFile.write(str(idd) + '\n')
		finally:
			fFile.close()

		return [idd for idd in idList if idd not in oldIDList]

	def getStoryIDs(self, topStoriesBaseUrl, reponseFormat, limit):
		storyIDs = []

		topStoriesFinalUrl = topStoriesBaseUrl + reponseFormat
		response = getResponse(topStoriesFinalUrl)
		storyIDs = json.loads(response.read().decode("utf-8"))
		storyIDs = storyIDs[:int(limit)]
		return storyIDs

	def getStories(self, idList, storyBaseUrl, reponseFormat):
		hackerNewsItemList = []
		count = 1;
		for id in idList:
			storyFinalUrl = storyBaseUrl + str(id) + reponseFormat
			response = getResponse(storyFinalUrl)
			storyData = json.loads(response.read().decode("utf-8"))
			if storyData is not None and 'url' in list(storyData.keys()):
				hackerNewsItem = HackerNewsItem()
				# JSON response inconsistant, check if all keys exist for every response
				hackerNewsItem.id = storyData['id']
				hackerNewsItem.title = storyData['title']
				hackerNewsItem.url = storyData['url']
				hackerNewsItemList.append(hackerNewsItem)
				print('Story ' + str(count) + ' retrived.')
				count += 1
		return hackerNewsItemList
