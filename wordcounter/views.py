from json import dumps

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'hithere': 'This is me!'})


def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    worddict = {}

    for word in wordlist:
        if word in worddict:
            # Increase
            worddict[word] += 1
        else:
            # add to the dictionary
            worddict[word] = 1

    sorted_words = sorted(worddict.items(), key=lambda x: x[1], reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext,
                                          'count': len(wordlist),
                                          'sorted_words': sorted_words})


def about(request):
    text = 'This is inform page of Word Count web app.'

    return render(request, 'about.html', {'text': text})
