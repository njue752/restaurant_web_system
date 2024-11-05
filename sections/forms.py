
from django.contrib.auth.models import User
from .models import Meal
from django import forms
from .models import Appointment




USER_TYPE_CHOICES = [
    ('customer', 'Customer'),
    ('administrator', 'Administrator'),
    ('delivery', 'Delivery'),
]

class UserRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True, label="First Name")
    last_name = forms.CharField(max_length=30, required=True, label="Last Name")
    username = forms.CharField(max_length=30, required=True, label="Username")
    email = forms.EmailField(max_length=50, required=True, label="Email")
    password = forms.CharField(widget=forms.PasswordInput, required=True, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True, label="Confirm Password")
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, label="User Type")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match")

        return cleaned_data





class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, required=True, label='Password')







class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['meal_name', 'meal_image', 'meal_description', 'meal_price']

        widgets = {
            'meal_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter meal name'}),
            'meal_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'meal_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter meal description'}),
            'meal_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter meal price'}),
        }





from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['latitude', 'longitude', 'phone_number', 'delivery_date', 'delivery_time']
