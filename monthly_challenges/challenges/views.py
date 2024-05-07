from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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
        return HttpResponseRedirect(f"/challenges/{months_keys[month - 1]}")
    except:
        return HttpResponseNotFound("This month is not supported!")
