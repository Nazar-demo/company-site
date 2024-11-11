from django.shortcuts import render


def index(request):
    return render(request, 'company/index.html')


def news(request):
    return render(request, 'company/news.html')


def activity(request):
    return render(request, 'company/activity.html')


def contacts(request):
    return render(request, 'company/contacts.html')


def management(request):
    return render(request, 'company/management.html')


# Management urls
def gogol(request):
    return render(request, 'company/management/gogol.html')


def stus(request):
    return render(request, 'company/management/stus.html')


def smith(request):
    return render(request, 'company/management/smith.html')