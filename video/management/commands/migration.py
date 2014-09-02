# python manage.py migration -a start 
# heroku run python manage.py migration -a start 
from django.utils.encoding import smart_str, smart_unicode
from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
import urllib2
import json
from video.models import *

KEY='AIzaSyA1A0iNtiAFf_ZgLdwifWH24WVR9BKvcQw'
URL='https://www.googleapis.com/youtube/v3/search?part=%s&channelId=%s&maxResults=10&key=%s'
URL_NEXT='https://www.googleapis.com/youtube/v3/search?part=%s&channelId=%s&maxResults=10&key=%s&pageToken=%s'

# Class MUST be named 'Command'
class Command(BaseCommand):

    # Displayed from 'manage.py help mycommand'
    help = "That's Your help message"

    option_list = BaseCommand.option_list + (
        make_option(
            "-a", 
            "--action", 
            dest = "action",
            help = "specify the option { start | update }", 
            metavar = "FILE"
        ),
    )

    def handle(self, *app_labels, **options):
        """
        app_labels - app labels (eg. myapp in "manage.py reset myapp")
        options - configurable command line options
        """
        def get_video(_channel,nextPage=None):

            if nextPage is None:
                print URL % ('id%2C+snippet',_channel.channel,KEY)
                handler=urllib2.urlopen(URL % ('id%2C+snippet',_channel.channel,KEY))
            else:
                print URL_NEXT % ('id%2C+snippet',_channel.channel,KEY,nextPage)
                handler=urllib2.urlopen(URL_NEXT % ('id%2C+snippet',_channel.channel,KEY,nextPage))

            data=json.loads(handler.read())

            for item in data.get('items'):
                if 'videoId' in item['id']:
                    video = Video(name=item['snippet']['title'],description=item['snippet']['description'],url=item['id']['videoId'],image=item['snippet']['thumbnails']['medium']['url'],channel=_channel,publishedAt=item['snippet']['publishedAt'])
                    if len(Video.objects.filter(url=video.url)) > 0:
                        if len(Video.objects.filter(name=video.name,description=video.description,url=video.url,image=video.image,channel=video.channel,publishedAt=video.publishedAt)) == 0 :
                            current_video = Video.objects.get(url=video.url)
                            current_video.name=video.name
                            current_video.description=video.description
                            current_video.image=video.image
                            current_video.channel=video.channel
                            current_video.publishedAt=video.publishedAt
                            current_video.save()
                            print smart_str('[UPDATE] - Row exist video: %s in channel %s' % (video.name,_channel.name))
                        else:
                            print smart_str('[EXIST] - Row exist video: %s in channel %s' % (video.name,_channel.name))
                    else:                       
                        video.save()
                        print smart_str('[INSERT] - Insert row video: %s in channel %s' % (video.name,_channel.name))
            if 'nextPageToken' in data:
                print 'nextPageToken >>>>>>>>>>>>> %s' % data['nextPageToken']
                get_video(_channel,data['nextPageToken'])
            else:
                print '============= Finish load channel: %s================' % (_channel.name)


        if options['action'] == 'start':
            channels = Channel.objects.all()
            for channel in channels:
                get_video(channel)

        elif options['action'] == 'update':
            print 'update'
        else:
            print 'No command'