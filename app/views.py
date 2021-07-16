from django.conf import settings
import datetime
from django.shortcuts import render
from django.http import HttpResponse


CONTEXT = [str(i) for i in range(1000)]


def info_view(request):
    page = int(request.GET.get('page', 0))
    elements_per_page = 10

    context = CONTEXT[page * elements_per_page: elements_per_page * (page + 1)]

    return HttpResponse('<br>'.join(context))

