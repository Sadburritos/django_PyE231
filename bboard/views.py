from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from bboard.models import Bb


def index(requst):
    bbs = Bb.objects.order_by("-published")
    context = {"bbs": bbs}
    return render(requst, 'index.html', context)


def index_old(requst):
    template = loader.get_template('index.html')
    bbs = Bb.objects.order_by("-published")
    context = {"bbs": bbs}
    return HttpResponse(template.render(context, requst))
