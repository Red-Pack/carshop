from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = CustomUser
        fields = ["email", "username", "phone", "address", "password1", "password2"]

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Имя пользователя"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Пароль"}))

class ProfileUpdateForm(forms.ModelForm):
    new_password1 = forms.CharField(
        label="Новый пароль",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        required=False,
        help_text="Оставьте пустым, если не хотите менять пароль"
    )
    new_password2 = forms.CharField(
        label="Подтверждение нового пароля",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        required=False
    )
    current_password = forms.CharField(
        label="Текущий пароль (для подтверждения изменений)",
        widget=forms.PasswordInput,
        required=False
    )

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'phone', 'address']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['readonly'] = True

    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')
        current_password = cleaned_data.get('current_password')

        if new_password1 or new_password2:
            if not current_password:
                raise ValidationError("Для изменения пароля введите текущий пароль")
            
            if not self.instance.check_password(current_password):
                raise ValidationError("Текущий пароль введен неверно")
            
            if new_password1 != new_password2:
                raise ValidationError("Новые пароли не совпадают")
            
            try:
                validate_password(new_password1, self.instance)
            except ValidationError as error:
                self.add_error('new_password1', error)

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        new_password = self.cleaned_data.get('new_password1')
        
        if new_password:
            user.set_password(new_password)
        
        if commit:
            user.save()
        return user
    
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'phone', 'address']
        widgets = {
            'address': forms.Textarea(attrs={
                'rows': 2,
                'cols': 50,
                'placeholder': 'Введите ваш адрес...',
                'class': 'form-control address-field'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': '+7 (XXX) XXX-XX-XX'
            })
        }


