from django import forms
from django.forms import formset_factory, modelformset_factory
from ratings.models import Rating


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['beer_name', 'score', 'brewer_name', 'notes']
