from django import forms
from .models import Book
from django.core.exceptions import ValidationError

class BookForm(forms.ModelForm):

    class Meta:
       model   = Book
       fields  = "__all__"    
    
    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) > 10 and len(title) < 60:
            return title
        raise ValidationError("title should be at least 10 characters!")


    def clean(self):
        super(BookForm, self).clean()
        title = self.cleaned_data.get('title')
        return self.cleaned_data