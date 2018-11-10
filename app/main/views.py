from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news,get_headlines
from ..models import News,Headlines