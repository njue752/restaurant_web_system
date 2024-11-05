from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Choices for user type
USER_TYPE_CHOICES = [
    ('customer', 'Customer'),
    ('administrator', 'Administrator'),
    ('delivery', 'Delivery'),
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='customer')

    def __str__(self):
        return f"{self.user.username} - {self.user_type}"


class Meal(models.Model):
    meal_name = models.CharField(max_length=100)
    meal_description = models.TextField()
    meal_price = models.DecimalField(max_digits=10, decimal_places=2)
    meal_image = models.ImageField(upload_to='meal_images/')

    def __str__(self):
        return self.meal_name

class Appointment(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='appointments')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    # appointment_date = models.DateTimeField(auto_now_add=True)
    appointment_date = models.DateTimeField(default=timezone.now)
    phone_number = models.CharField(max_length=15)
    payment_status = models.CharField(max_length=20, default='UNPAID')
    latitude = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)
    delivery_date = models.DateField(null=True, blank=True)  # Add delivery_date field
    delivery_time = models.TimeField(null=True, blank=True)  # Add delivery_time field

    def __str__(self):
        return f"Appointment for {self.meal} by {self.user.username} on {self.appointment_date}"