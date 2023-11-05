from django import forms
from . import models

class GamesForm(forms.ModelForm):
    class Meta:
        model = models.Games
        fields = "__all__"


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.ReviewGame
        fields = "__all__"