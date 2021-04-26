from django import forms
from .models import Comment

class SearchForm(forms.Form):
    query = forms.CharField()

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']