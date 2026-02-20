from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from datetime import date
from django import forms

User = get_user_model()

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "birth_date")

    def clean_birth_date(self):
        today_year = float(date.today().year)
        birth_date = self.cleaned_data.get("birth_date")
        if birth_date and birth_date > today_year:
            raise forms.ValidationError("未来の日付は指定できません。")
        return birth_date
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get("email")
        user.birth_date = self.cleaned_data.get("birth_date")
        if commit:
            user.save()
        return user
     
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)