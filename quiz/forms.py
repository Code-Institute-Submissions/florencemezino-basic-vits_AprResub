from django import forms
from .models import Question

class addQuestionform(forms.ModelForm):
    """ Add question form for admin user """

    class Meta:
        model = Question
        fields = "__all__"

