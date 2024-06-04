from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off'  # 禁用自動填寫
            },
        )
    )
    password = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off'  # 禁用自動填寫
            }
        )
    )

# class signinForm(forms.Form):
#     username = forms.CharField(
#         max_length=20,
#         widget=forms.TextInput(
#             attrs={'class': 'form-control'}
#         )
#     )
#     password = forms.CharField(
#         max_length=20,
#         widget=forms.PasswordInput(
#             attrs={'class': 'form-control'}
#         )
#     )
