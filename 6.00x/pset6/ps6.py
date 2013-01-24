# 6.00x Problem Set 6
# RSS Feed Filter

import feedparser
import string
import time
import sys
from project_util import translate_html
from Tkinter import *


#-----------------------------------------------------------------------
#
# Problem Set 6

#======================
# Code for retrieving and parsing RSS feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret
#======================

#======================
# Part 1
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    """Organize the news items"""

    def __init__(self, guid, title, subject, summary, link):
        self.guid, self.title, self.subject, self.summary, self.link = guid, title, subject, summary, link
        
    def getGuid(self):
        """Returns GUID"""
        return self.guid

    def get_guid(self):
        return self.getGuid()
    
    def getTitle(self):
        """Returns Title"""
        return self.title

    def get_title(self):
        return self.getTitle()
    
    def getSubject(self):
        """Returns Subject"""
        return self.subject

    def get_subject(self):
        return self.getSubject()
    
    def getSummary(self):
        """Returns Summary"""
        return self.summary

    def get_summary(self):
        return self.getSummary()
    
    def getLink(self):
        """Returns Link"""
        return self.link

    def get_link(self):
        return self.getLink()
    
#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5

class WordTrigger(Trigger):

    def __init__(self, word):
        self.word = word.lower()
        
    def isWordIn(self, text):

        def prepareString(text):
            newText = text.lower()
            for x in string.punctuation:
                newText = newText.replace(x," ")
            return newText

        if self.word in prepareString(text).split():
            return True
        else:
            return False

class TitleTrigger(WordTrigger):

    def evaluate(self, story):
        return self.isWordIn(story.getTitle())

class SubjectTrigger(WordTrigger):

    def evaluate(self, story):
        return self.isWordIn(story.getSubject())

class SummaryTrigger(WordTrigger):

    def evaluate(self, story):
        return self.isWordIn(story.getSummary())

# Composite Triggers
# Problems 6-8

class NotTrigger(Trigger):

    def __init__(self, trig):
        self.trig = trig
        
    def evaluate(self, story):
        return not self.trig.evaluate(story)

class AndTrigger(Trigger):

    def __init__(self, trig1, trig2):
        self.trig1, self.trig2 = trig1, trig2

    def evaluate(self, story):
        return self.trig1.evaluate(story) and self.trig2.evaluate(story)
        
class OrTrigger(Trigger):

    def __init__(self, trig1, trig2):
        self.trig1, self.trig2 = trig1, trig2

    def evaluate(self, story):
        return self.trig1.evaluate(story) or self.trig2.evaluate(story)


# Phrase Trigger
# Question 9

class PhraseTrigger(Trigger):
    """Returns True if Text matchs Story Title, Summary or Subject"""

    def __init__(self, text):
        self.text = text

    def evaluate(self, story):
        return self.text in story.getTitle() or self.text in story.getSubject() or self.text in story.getSummary()


#======================
# Part 3
# Filtering
#======================

def filterStories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    matchedStories = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                matchedStories.append(story)
    
    return matchedStories

#======================
# Part 4
# User-Specified Triggers
#======================

def makeTrigger(triggerMap, triggerType, params, name):
    """
    Takes in a map of names to trigger instance, the type of trigger to make,
    and the list of parameters to the constructor, and adds a new trigger
    to the trigger map dictionary.

    triggerMap: dictionary with names as keys (strings) and triggers as values
    triggerType: string indicating the type of trigger to make (ex: "TITLE")
    params: list of strings with the inputs to the trigger constructor (ex: ["world"])
    name: a string representing the name of the new trigger (ex: "t1")

    Modifies triggerMap, adding a new key-value pair for this trigger.

    Returns: None
    """
    if triggerType == 'TITLE':
        triggerMap[name] = TitleTrigger(params[0])
    elif triggerType == 'SUBJECT':
        triggerMap[name] = SubjectTrigger(params[0])
    elif triggerType == 'SUMMARY':
        triggerMap[name] = SummaryTrigger(params[0])
    elif triggerType == 'PHRASE':
        triggerMap[name] = PhraseTrigger(' '.join(params))
    elif triggerType == 'NOT':
        triggerMap[name] = NotTrigger(triggerMap[params[0]])
    elif triggerType == 'AND':
        triggerMap[name] = AndTrigger(triggerMap[params[0]],triggerMap[params[1]])
    elif triggerType == 'OR':
        triggerMap[name] = OrTrigger(triggerMap[params[0]],triggerMap[params[1]])
    else:
        raise Exception('Invalid Trigger Type')

    return triggerMap[name]


def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """

    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    triggers = []
    triggerMap = {}

    # Be sure you understand this code - we've written it for you,
    # but it's code you should be able to write yourself
    for line in lines:

        linesplit = line.split(" ")

        # Making a new trigger
        if linesplit[0] != "ADD":
            trigger = makeTrigger(triggerMap, linesplit[1],
                                  linesplit[2:], linesplit[0])

        # Add the triggers to the list
        else:
            for name in linesplit[1:]:
                triggers.append(triggerMap[name])

    return triggers
    
import thread

SLEEPTIME = 60 #seconds -- how often we poll


def main_thread(master):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    try:
        # These will probably generate a few hits...
        t1 = TitleTrigger("Obama")
        t2 = SubjectTrigger("Romney")
        t3 = PhraseTrigger("Election")
        t4 = OrTrigger(t2, t3)
        triggerlist = [t1, t4]
        
        # TODO: Problem 11
        # After implementing makeTrigger, uncomment the line below:
        triggerlist = readTriggerConfig("triggers.txt")

        # from here is about drawing
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_summary())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print "Polling . . .",
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

            stories = filterStories(stories, triggerlist)

            map(get_cont, stories)
            scrollbar.config(command=cont.yview)


            print "Sleeping..."
            time.sleep(SLEEPTIME)

    except Exception as e:
        print e


if __name__ == '__main__':

    root = Tk()
    root.title("Some RSS parser")
    thread.start_new_thread(main_thread, (root,))
    root.mainloop()

