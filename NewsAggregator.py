# Import libraries

import feedparser as f
import html2text as h
from ebooklib import epub
from lxml import etree
import bs4 as bs4

# Define Functions

def ArticleParser(feed, excludeTags):
    # ArticleParser grabs elements from the RSS feed using feedparser.
    # Elements are passed into a temporarly list that is passed into a permanent list then cleared each loop.
    # Elements with tags that are not desired are excluded.
    aList = []
    for entry in feed.entries:
        if CheckExclude(excludeTag, tagParser(entry.tags)):
            bList = []
            bList.append(r.feed.title)
            bList.append(entry.title)
            bList.append(entry.author)
            bList.append(
                    tagParser(entry.tags))
            # bList.append(ContentParser(entry.content))
            aList.append(bList)
        else:
            pass # Skip results that have tags that should be excluded
    return aList

def tagParser(tags):
    tagList =[]
    for i in tags:
        tagList.append(i.term)
    return tagList

def ContentParser(content):
    for i in content:
        output = i.value
    return output

def CheckExclude(excludeTags, articleTags):
    for i in articleTags:
        if i not in excludeTags:
            result = True
        else:
            result = False
            break
    return result


feedList = ['https://fivethirtyeight.com/contributors/nate-silver/feed/', 'https://fivethirtyeight.com/features/feed/']
excludeTag = ['FiveThirtyEight Podcasts', 'Video']
results = []
# b = f.parse('https://fivethirtyeight.com/contributors/nate-silver/feed/')

for i in feedList:
    results.append(f.parse(i))

for r in results:
    a_details = ArticleParser(r,excludeTag)
