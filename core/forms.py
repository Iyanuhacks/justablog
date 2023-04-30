from django import forms
from .models import Comment
from ckeditor.widgets import CKEditorWidget

class MyForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
   
           


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')
