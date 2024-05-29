from django import forms
from .models import Survey

class SurveyForm(forms.ModelForm):

    class Meta:
        model = Survey
        fields = ['student_id', 'question_1', 'question_2', 'question_3', 'question_4', 'question_5', 'question_6',
                  'question_7', 'question_8', 'question_9', 'question_10', 'question_11', 'fill_in_1', 'fill_in_2',
                  'fill_in_3']
        labels = {
            'student_id': '學號',
            'question_1': '在任何時候，我很清楚系統目前的狀態如何？',
            'question_2': '在操作的過程中，網頁是否都有在合理的時間內做出回應？',
            'question_3': '可以從每個頁面返回主頁嗎？',
            'question_4': '是否能夠隨時取消和重做任何操作？',
            'question_5': '對於系統的錯誤訊息是否都清楚明瞭？',
            'question_6': '是否有清楚易懂的錯誤訊息？',
            'question_7': '對於任何介面，使用相似的配色？',
            'question_8': '對於任何介面，使用一致的排版？',
            'question_9': '網頁的排版設計遵循一般的網站標準嗎？',
            'question_10': '我在使用這個系統時，不需要記憶太多東西，就可以完成任務？',
            'question_11': '系統的顯示方式符合現實世界的習慣？',

            # Add other fields as needed
        }
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

