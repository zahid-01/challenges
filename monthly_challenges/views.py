from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": "Learn Django for at least 20 minutes every day!"
}

# Create your views here.


def challenges_by_number(request, month):
    months = list(monthly_challenges.keys())
    if (month > len(months)):
        return HttpResponseNotFound('No page found!')

    redirect_path = reverse("challenges_by_name", args=[months[month-1]])
    return HttpResponseRedirect(redirect_path)


def challenges(request, month):
    if (monthly_challenges[month]):
        response_data = f"<h1>{monthly_challenges[month]}</h1>"
        return HttpResponse(response_data)

    return HttpResponseNotFound('No page found')


def challenges_list(request):
    months = list(monthly_challenges.keys())

    list_data = ""

    for month in months:
        path = reverse("challenges_by_name", args=[month])
        list_data += f'<li><a href="{path}">{month.capitalize()}</a></li>'

    return HttpResponse(f"<ul>{ list_data}</ul>")
