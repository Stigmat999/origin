# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .nginx_log_parser import nginx_log_parser
from polls.models import LogString

def index(request):
    count_created = 0
    log_list = nginx_log_parser()
    for i in log_list:
        LogString.objects.create(ip = i[0], method = i[5].replace("\"",""), code = int(i[8]))
        count_created += 1
    return HttpResponse("LogString objects created: {}".format(count_created))
