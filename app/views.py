from django.conf import settings
import datetime
from django.shortcuts import render
from django.http import HttpResponse

# def info_view(request, year, month, day):
#     # none_result = 'Данных по пользователю нет'
#     # data = {
#     #     'Ivan': 'Начальник отдела',
#     #     'Alex': 'Руководитель службы разработки',
#     #     'Не определен': 'Нет данных'
#     # }
#     #
#     # name = request.GET.get('name', 'Не определен')
#     # return HttpResponse(f'Пользователь {name} - {data.get(name, none_result)}')
#     #
#     # # admin_email = settings.ADMIN_EMAIL
#     # # return HttpResponse(f'Почта админа - {admin_email}')
#
#     date = datetime.datetime(year, month, day)
#
#     return HttpResponse(f'{date}')


# def info_view(request, value):
#     print('===>', type(value))
#
#     return HttpResponse(f'{value}')

def info_view(request):
    class User:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def info(self):
            return f'Пользователь {self.name} с возрастом {self.age}'

    user_1 = User('Ivan', '25')
    user_2 = User('Alex', '30')

    context = {
        'info': 'Данные о пользователях',
        'users': [user_1, user_2]
    }

    return render(request, 'app/index.html', context)
