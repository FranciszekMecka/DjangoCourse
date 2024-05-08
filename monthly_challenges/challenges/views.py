from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

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
    # try:
        challenge_text = months_dict[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    # except:
        return HttpResponseNotFound("This month is not supported!")


def monthly_challenge_by_number(request, month):
    try:
        months_keys = list(months_dict.keys())
        redirect_month = months_keys[month - 1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except:
        # this looks for 404.html file in templates folder
        raise Http404()

def index(request):
    months_keys = list(months_dict.keys())
    body = ""
    return render(request, "challenges/index.html", {
        "months": months_keys
    })
