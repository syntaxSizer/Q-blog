#!flask/bin/python 
import datetime
import functools
import os
import re
import urllib

from flask import (Flask, abort, flash, Markup, redirect, render_template,
                   request, Response, session, url_for)
from markdown import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.extra import ExtraExtension
from micawber import bootstrap_basic, parse_html
from micawber.cache import Cache as OEmbedCache
from peewee import *
from playhouse.flask_utils import FlaskDB, get_object_or_404, object_list
from playhouse.sqlite_ext import *
# one way hash to be used on admin_password before deploy

ADMIN_PASSWORD = 'secret'
APP_DIR = os.path.dirname(os.path.realpath(__file__))
DATABASE = 'sqliteext:///%s' % os.path.join(APP_DIR, 'blog.db')
DEBUG = False
SECRET_KEY = 'swaswa,secret!' #used by Flask to encrypt session cookies.
SITE_WIDTH = 800


app = Flask(__name__)
app.config.from_object(__name__)


flask_db = FlaskDB(app)
database = flask_db.database


oembed_providers = bootstrap_basic(OEmbedCache())



class Entry(flask_db.Model):
      title = CharField()
      slug = CharField(unique = True)
      content = TextField()
      published = BooleanField(index=True)
      timestamp = DateTimeField(default=datetime.datetime.now, index=True)


      def save(self,*args, **kwargs):
          if not self.slug:
             self.slug = re.sub('[^/w]+','-',self.title.lower())
          ret = super(Entry, self).save(*args, **kwargs)


         # store search content. 
          self.update_search_index()
          return ret

      def update_search_index(self):
          try:
              fts_entry = FTSEntry.get(FTSEntry.entry_id == self.id)
          except FTSEntry.DoesNotExist:
              fts_entry = FTSEntry(entry_id=self.id)
              force_insert = True
          else:
              force_entry = False
          fts_entry.content = '\n'.join((self.title, self.content))
          fts_entry.save(force_insert = force_insert)


class FTSEntry(FTSModel):
     entry_id = IntegerField()
     content = TextField()

class Meta:
      database = datatbase






#code  initlizer
@app.template_filter('clean_querystring')
def clean_querystring(request_args, *keys_to_remove,**new_values):
    querystring = dict((key,value) for key, value in request_args.items())
    for key in keys_to_remove:
        querystring.pop(key,None)
    querystring.update(new_values)
    return urllib.urlencode(querystring)



@app.errorhandler(404)
def not_found(exc):
    return Response('<h3>Not Found</h3>'), 404


def main():
    database.create_tables([Entry,FTSEntry],safe=True)
    app.run(debug = True)


if __name__ == '__main__':

   main()
