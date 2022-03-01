from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):
    """Add question form for admin user"""
    class Meta:
        model = Question
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        questions = Question.objects.all()
