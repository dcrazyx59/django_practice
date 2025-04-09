from django.http import HttpResponse
import datetime


def hello(request):
    return HttpResponse("<h1> Hello world </h1>")

def give_date(request):
    date = datetime.datetime.now()
    document = f"""<h1> Hello world time: {date} </h1>"""
    return HttpResponse(document)

def calculate_age(request, age, year):
    period = year - 2025
    future_age = age + period
    document = f"""<h1> In the year {year} you will be {future_age} </h1>"""

    return HttpResponse(document)
    