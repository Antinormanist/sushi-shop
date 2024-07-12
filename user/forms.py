from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from .models import Profile

class CreateUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2']
        
        
class ChangeProfileForm(forms.ModelForm):
    last_name = forms.CharField(max_length=128, label='Фамилия')
    first_name = forms.CharField(max_length=128, label='Имя')
    patronymic = forms.CharField(max_length=128, label='Отчество')
    phone = forms.CharField(max_length=24, label='Номер телефона')
    address = forms.CharField(max_length=255, label='Адрес')
    
    
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'patronymic', 'address', 'phone']
        
        
    # Do a phone validator
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if phone.strip('0123456789') != '':
            raise forms.ValidationError('Номер телефона должен состоять только из цифр! Даже без +')
        elif len(phone) < 11:
            raise forms.ValidationError('Номер телефона слишком короткий')
        return phone
    
    
class ChangeAvatar(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['image']