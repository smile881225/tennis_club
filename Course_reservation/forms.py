# from django import forms
# from Course_reservation.models import Course_reservation
# from django.forms import SelectDateWidget, ValidationError
# from datetime import date

# class BookingForm(forms.ModelForm):
#     class Meta:
#         model = Course_reservation     # 對應的資料

#         # fields = '__all__'  # 呈現所有欄位
#         # 也可以用 list 來表達要呈現的欄位
#         fields = ['Period', 'Course_code', 'Time_start', 'week_choices']

#         widgets = {
#             'Period': forms.Select(attrs={'readonly': 'readonly'}),
#             # 'user': forms.TextInput(                
#             #     attrs={'readonly': 'readonly'}),    # 文字框
#             'Course_code': forms.Select(),                # 下拉式選單
#             'Time_start': SelectDateWidget(
#                 attrs={'initial': date.today()}),   # 日期選單
#             'week_choices': forms.Select(),
#         }

#         labels = {
#             'Period': '期別',
#             'Course_code': '課程代碼',
#             'Time_start': '開始日期',
#             'week_choices': '星期',
#         }

#     def clean_reason(self):
#         print ('clean_reason is called')
#         reason = self.cleaned_data.get('reason')
#         if len(reason) <= 10:
#             raise ValidationError(f'用途必須至少包含 10 個字元。目前只有 {len(reason)} 個字')
#         return reason        