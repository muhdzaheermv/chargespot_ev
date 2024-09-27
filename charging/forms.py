from django import forms
from stationoperator.models import StationReview

class StationReviewform(forms.ModelForm):
    review = forms.CharField(widget=forms.Textarea(attrs={'placeholder':"Write review"}))
    
    class Meta:
        model = StationReview
        fields = ['review','rating']