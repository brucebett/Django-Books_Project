from django.contrib import messages
from django.shortcuts import render, redirect

from books.forms import Booksform


# Create your views here.

def booksrecord(request):
    if request.method == 'POST':
        form = Booksform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book Details Submitted Successfully')
            return redirect('booksrecord')
    else:
        form = Booksform()

    return render(request, 'booksrecord.html', {'form': form})


def booksform(request):
    return render(request, 'booksform.html')
