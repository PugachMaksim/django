import logging

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accesed')
    return HttpResponse("<h1>Hello World</h1><br>"
                        "<p>Решил вот поменять работу</p>")


def about(request):
    logger.debug('About page accesed')
    return HttpResponse("Учусь новому делу")



# def about(request):
#     try:
#         result = 1 / 0
#     except Exception as e:
#         logger.exception(f'Error in about page: {e}')
#         return HttpResponse('Oops...')
#     else:
#         logger.debug('About page accesed')
#         return HttpResponse("Учусь новому делу")
