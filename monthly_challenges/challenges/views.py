from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

# view function


def month_by_number(request, aaa):
    return HttpResponse(aaa)


def month(request, aaa):
    challenge_text = None,
    if aaa == 'january':
        challenge_text = '1st month'
    elif aaa == 'february':
        challenge_text = '2nd Month'
    elif aaa == 'march':
        challenge_text = '3rd Month'
    elif aaa == 'april':
        challenge_text = '4th Month'
    elif aaa == 'may':
        challenge_text = '5th Month'
    elif aaa == 'june':
        challenge_text = '6th Month'
    elif aaa == 'july':
        challenge_text = '7th Month'
    elif aaa == 'august':
        challenge_text = '8th Month'
    elif aaa == 'september':
        challenge_text = '9th Month'
    elif aaa == 'october':
        challenge_text = '10th Month'
    elif aaa == 'november':
        challenge_text = '11th Month'
    elif aaa == 'december':
        challenge_text = '12th Month'
    else:
        return HttpResponseNotFound('enter a valid month plz')

    return HttpResponse(challenge_text)


def index(request):
    return HttpResponse("This works!")


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
