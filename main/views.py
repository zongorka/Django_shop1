from django.shortcuts import render


def index(request):
    context = {
        'title': 'Main page',
        'content': 'Some text of shop',
        'list': ['12', 13],

    }


    return render(request, 'main/index.html', context)


def about(request):
    return render(request)