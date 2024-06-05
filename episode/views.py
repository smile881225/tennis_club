from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from .models import *
from .models import Episode  # 确保你有一个 Episode 模型

def seasons(request):
    seasons = Season.objects.all().values()
    template = loader.get_template('all_seasons.html')
    context = {
        'seasons': seasons,
    }
    return HttpResponse(template.render(context, request))


def episodes(request):
    episodes = Episode.objects.all()
    template = loader.get_template('all_episodes.html')
    context = {
        'episodes': episodes,
    }
    return HttpResponse(template.render(context, request))


def episode(request, id):
    ep = Episode.objects.get(id=id)
    template = loader.get_template('episode.html')
    context = {
        'ep': ep
    }
    return HttpResponse(template.render(context, request))


def casts(request):
    casts = Cast.objects.all().values()
    template = loader.get_template('all_casts.html')
    context = {
        'casts': casts,
    }
    return HttpResponse(template.render(context, request))
