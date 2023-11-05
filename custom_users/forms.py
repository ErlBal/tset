from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

MALE = 1
FEMALE = 2

GENDER_TYPE = (
    (MALE, "Муж"),
    (FEMALE, "Жен")
)

class CustomRegForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True, label='Укажите ваш номер')
    date_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE, required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "phone_number",
            "date_birth",
            "gender",
        )

    def save(self, commit=True):
        user = super(CustomRegForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user