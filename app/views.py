from django.conf import settings
import datetime
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse


CONTEXT = [str(i) for i in range(1000)]


def info_view(request):
    page = int(request.GET.get('page', 0))
    elements_per_page = 10

    paginator = Paginator(CONTEXT, elements_per_page)
    page_ = paginator.get_page(page)

    context = page_.object_list

    return HttpResponse('<br>'.join(context))

