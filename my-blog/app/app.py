# app.py

import datetime
import functools
import os
import re
import urllib

from flask import (Flask, abort, flash, Markup, redirect, render_template, request, Response, session, url_for)

from markdown import markdown
from markdown.extensions.codehilite import codeHiliteExtension
from markdown.extensions.extra import ExtraExtension
from micawber import bootstrap_basic, parse_html
from micawber.cache import Cache as OembedCache
from peewee import *
from playhouse.sqlite_ext import FlaskDB, get_object_or_404, object_list
from playhouse.sqlite_ext import *

# one way hash to be used on admin_password before deploy

ADMIN_PASSWORD = 'secret'
APP_DIR = os.psth.dirname(os.path.realpath(__file__))
DATABASE = 'sqliteext:///%' % os.path.join(APP_DIR, 'blog.db')
DEBUG = False
SECRET_KEY = 'swaswa,secret!' #used by Flask to encrypt session cookies.
SITE_WIDTH = 800


app = Flask(__name__)
app.config.from_object(__name__)


flask_db = FlaskDB(app)
database = flask_db.database


oembed_providers = bootstrap_basic(OEmbedCache())

