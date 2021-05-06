import json
from pathlib import Path

from django.shortcuts import render

booksReader = open(Path(__file__).parent.joinpath('data/books.json'))
data = json.loads(booksReader.read())
booksReader.close()


def index(request):
    return render(request, 'books/index.html', {
        'name': 'John',
        'books': data[:10]
    })
