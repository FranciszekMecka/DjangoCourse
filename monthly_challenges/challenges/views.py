from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

months_dict = {
    "january": "Random string for January",
    "february": "Random string for February",
    "march": "Random string for March",
    "april": "Random string for April",
    "may": "Random string for May",
    "june": "Random string for June",
    "july": "Random string for July",
    "august": "Random string for August",
    "september": "Random string for September",
    "october": "Random string for October",
    "november": "Random string for November",
    "december": "Random string for December"
}


def monthly_challenge(request, month):
    try:
        return HttpResponse(months_dict[month])
    except:
        return HttpResponseNotFound("This month is not supported!")


def monthly_challenge_by_number(request, month):
    try:
        months_keys = list(months_dict.keys())
        redirect_month = months_keys[month - 1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("This month is not supported!")

def index(request):
    months_keys = list(months_dict.keys())
    body = ""
    for month in months_keys:
        body += f"<li><a href=\"{reverse('month-challenge', args=[month])}\">{month}</a></li>"
    body = f"<ul>{body}</ul>"
    return HttpResponse(body)
