'''
Utils module
'''
import json
import logging
import ConfigParser
from notify.implementation import HackerNewsAPIImpl
from notify.models import  NewsItem

logger = logging.getLogger(__name__)

def wirite_json_to_file(filename, collection):
    '''
    Write JSON data to file
    '''
    print 'Writing Stories to File ...'
    with open(filename, 'w', encoding='utf8') as out_f:
        for item in collection:
            json.dump(item.__dict__, out_f)
    print 'Stories written to file'


def refresh_news_data():
    '''
    Refresh db
    '''
    hacker_news_api_impl = HackerNewsAPIImpl()
    config_parser = ConfigParser.ConfigParser()
    config_parser.read('notify/config.ini')
    hn_config = dict(config_parser.items('hackernews'))
    limit = int(hn_config['limit']) 
    story_base_url = hn_config['storybaseurl'] 
    response_format = hn_config['format'] 
    top_stories_base_url = hn_config['topstoriesbaseurl'] 
    new_ids = set(hacker_news_api_impl.getStoryIDs(top_stories_base_url,
                                                   response_format, limit))
    old_ids = set(NewsItem.objects.all().values_list('itemId', flat=True))
    updates = new_ids.intersection(old_ids)
    inserts = new_ids.difference(updates)
    deletes = old_ids.difference(updates)

    NewsItem.objects.filter(itemId__in=list(deletes)).delete()
    all_stories = hacker_news_api_impl.getStories(list(inserts), story_base_url,
                                                  response_format)
    NewsItem.objects.bulk_create(all_stories)
    NewsItem.objects.filter(itemId__in=list(updates)).update(isNew=False)
