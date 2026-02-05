from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

# view function


def index(request):

    list_months = list(mc_dict.keys())
    return render(request, "challenges\index.html", {
        "months": list_months,


    })


mc_dict = {
    "january": "Work",
    "february": "Sleep",
    "march": "Eat",
    "april": "Run",
    "may": "Make",
    "june": "Jump",
    "july": "Joy",
    "august": "Acc",
    "september": "Step",
    "october": "Official",
    "november": "Need",
    "december": None,
}


def month_by_number(request, aaa):

    mc_dict_keys = list(mc_dict.keys())

    if aaa > len(mc_dict_keys):
        return HttpResponseNotFound("enter a valid month number")
    redirect_month = mc_dict_keys[aaa-1]
    redirect_path = reverse("url_month", args=[redirect_month])

    return HttpResponseRedirect(redirect_path)


def month(request, aaa):

    # try:
    challenge_text = mc_dict[aaa]
    title_text = aaa
    return render(request, "challenges/challenge.html", {
        "text": challenge_text,
        "title": title_text

    })

    # except:
    #     return HttpResponseNotFound ("<h1>Enter a valid month</h1>")


# def janview(request):
#     return HttpResponse("1st month")


# def febview(request):
#     return HttpResponse("2nd month")


# def marview(request):
#     return HttpResponse("3rd month")


# def aprview(request):
#     return HttpResponse("4th month")


# def mayview(request):
#     return HttpResponse("5th month")


# def junview(request):
#     return HttpResponse("6th month")


# def julview(request):
#     return HttpResponse("7th month")


# def augview(request):
#     return HttpResponse("8th month")


# def sepview(request):
#     return HttpResponse("9th month")


# def octview(request):
#     return HttpResponse("10th month")


# def novview(request):
#     return HttpResponse("11th month")


# def decview(request):
#     return HttpResponse("12th month yay")
