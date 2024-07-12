from django import forms

from books.models import Booksclassification


class Booksform(forms.ModelForm):
    class Meta:
        model = Booksclassification
        fields = ['tittle', 'author', 'published_date', 'isbn']
