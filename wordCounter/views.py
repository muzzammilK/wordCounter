from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordslist = fulltext.split()
    count = len(wordslist)
    wordsfreq = {}
    for i in wordslist:
        if i in wordsfreq:
            wordsfreq[i] +=1
        else:
            wordsfreq[i] =1
    print(wordsfreq)
    sorted_wordsfreq = dict(sorted(wordsfreq.items(), key=lambda x: x[1], reverse=True))
    return render(request, 'count.html', {'fulltext':fulltext, 'count':count, 'wordsfreq':sorted_wordsfreq})

def info(request):
    return render(request, 'info.html')