from django import forms
from .models import Survey

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['student_id', 'question_1', 'question_2', 'question_3', 'question_4', 'question_5', 'question_6', 'question_7', 'question_8', 'question_9', 'question_10', 'question_11', 'fill_in_1', 'fill_in_2']
        widgets = {
            'question_1': forms.RadioSelect,
            'question_2': forms.RadioSelect,
            'question_3': forms.RadioSelect,
            'question_4': forms.RadioSelect,
            'question_5': forms.RadioSelect,
            'question_6': forms.RadioSelect,
            'question_7': forms.RadioSelect,
            'question_8': forms.RadioSelect,
            'question_9': forms.RadioSelect,
            'question_10': forms.RadioSelect,
            'question_11': forms.RadioSelect,

        }
