# python manage.py flickr -a start 
# heroku run python flickr.py migration -a start 
from django.utils.encoding import smart_str, smart_unicode
from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
import urllib2
import json
from video.models import *

KEY='55b11c4fca4f090083ecfc1811ddc32c'
URL='https://api.flickr.com/services/rest/?method=flickr.groups.pools.getPhotos&api_key=%s&group_id=%s&format=json&nojsoncallback=1&page=%s'

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
        def get_image(_group,_page):
            current_url=URL % (KEY,_group.group_id,_page)
            handler=urllib2.urlopen(current_url)
            data=json.loads(handler.read())

            photos=data.get('photos')
            current_page=photos['pages']

            for item in photos['photo']:
                if len(Photo.objects.filter(photo_id=item['id'])) > 0:
                    _page=current_page
                else:
                    photo=Photo(photo_id=item['id'],owner=item['owner'],secret=item['secret'],server=item['server'],farm=item['farm'],title=item['title'],ownername=item['ownername'],group=_group)
                    try:
                        photo.save()
                    except Exception as e:
                        print 'URL: %s >>> %s (%s)' % (current_url,e.message, type(e))

            if(current_page!=_page):
                get_image(_group,_page+1)

        if options['action'] == 'start':
            groups = Group.objects.all()
            for group in groups:
                print 'Loading group: %s' % (group.name)
                get_image(group,1)

        elif options['action'] == 'update':
            print 'update'
        else:
            print 'No command'