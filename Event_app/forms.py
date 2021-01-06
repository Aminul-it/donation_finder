from django import forms
from Event_app.models import Comment,event


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
