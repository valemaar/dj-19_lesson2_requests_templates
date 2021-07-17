from django.conf import settings
import datetime
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse


CONTEXT = [str(i) for i in range(1000)]


def info_view(request):
    page = int(request.GET.get('page', 0))
    elements_per_page = 10

    paginator = Paginator(CONTEXT, elements_per_page)
    page_ = paginator.get_page(page)

    # context = page_.object_list

    # if page_.has_next():
    #     n = page_.next_page_number()
    #     print(f'След.страница - {n}')
    #
    # return HttpResponse('<br>'.join(context))

    context = {
        'data': page_.object_list,
        'page': page_.number,
        'next': page_.next_page_number() if page_.has_next() else paginator.num_pages,
        'prev': page_.previous_page_number() if page_.has_previous() else 1,
        'pages': paginator.num_pages
    }

    return JsonResponse(context)
