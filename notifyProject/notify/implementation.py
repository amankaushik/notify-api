import json
from urllib2 import urlopen
from models import NewsItem
import datetime as dt

class HackerNewsAPIImpl:
	def __init__(self):
		pass

	def checkRedundantIDs(self, newIdList, oldIdList):
		return [idd for idd in newIdList if idd not in oldIdList]


	def getStoryIDs(self, topStoriesBaseUrl, reponseFormat, limit):
		storyIDs = []

		topStoriesFinalUrl = topStoriesBaseUrl + reponseFormat
		response = urlopen(topStoriesFinalUrl)
		storyIDs = json.loads(response.read().decode("utf-8"))
		storyIDs = storyIDs[:int(limit)]
		return storyIDs


	def getStories(self, idList, storyBaseUrl, reponseFormat):
		hackerNewsItemList = []
		count = 1;
		for id in idList:
			storyFinalUrl = storyBaseUrl + str(id) + reponseFormat
			response = urlopen(storyFinalUrl)
			storyData = json.loads(response.read().decode("utf-8"))
			if storyData is not None and 'url' in list(storyData.keys()):
				# JSON response inconsistant(not all keys are compulsory),
				# check if all keys exist for every response
				hackerNewsItemList.append(NewsItem(itemId=storyData['id'],
				                                   itemUrl=storyData['url'],
				                                   itemTitle=storyData['title'],
                                                   itemScore=storyData['score'],
                                                   itemTime=((dt.datetime.today()-\
                                                           dt.datetime.fromtimestamp(storyData['time'])\
                                                       ).seconds / 3600),
												   isNew=True))
				print('Story ' + str(count) + ' retrived.')
				count += 1
		return hackerNewsItemList
