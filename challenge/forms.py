from django import forms
from django.forms import ModelForm

from .models import Answer, Challenge, Hint, Quizz


class DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"


class ChallengeForm(ModelForm):
    class Meta:
        model = Challenge
        fields = "__all__"
        exclude = ["owner"]
        widgets = {"date_start": DateTimeInput(), "date_end": DateTimeInput()}


class QuizzForm(ModelForm):
    class Meta:
        model = Quizz
        fields = ("challenge_id", "name", "question", "point", "file_content")
        exclude = ["challenge_id"]


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ["answer"]
