from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient
from django_daraja.views import cl

from .forms import UserRegistrationForm
from .models import UserProfile, Appointment
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from .forms import UserLoginForm
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout  # Include auth_logout here
from django.shortcuts import render, redirect
from .forms import UserLoginForm
from .models import UserProfile
from django.shortcuts import render
from .models import Meal
from django.shortcuts import render, get_object_or_404
from .models import Meal
from django.shortcuts import render, redirect
from .forms import MealForm  # Ensure you have this form defined
from .models import Meal  # Import your Meal model
from django.shortcuts import render, redirect
from .forms import AppointmentForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Meal  # Ensure you have a Meal model
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Meal  # Ensure you have the Meal model imported
from .forms import AppointmentForm  # Ensure you have your AppointmentForm imported
from django.shortcuts import render, get_object_or_404, redirect
from .models import Meal  # Make sure you import your Meal model
from .forms import AppointmentForm  # Import your AppointmentForm

from .models import Meal  # or replace Meal with your Menu model


def index(request):
    meals = Meal.objects.all()  # Fetch all meals from the database
    return render(request, 'index.html', {'meals': meals})






def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Don't save it to the database yet
            user.password = make_password(form.cleaned_data['password'])  # Hash the password
            user.save()  # Now save the user to the database
            UserProfile.objects.create(user=user, user_type=form.cleaned_data['user_type'])
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'signup.html', {'form': form})


# views.py
 # Ensure you import your UserProfile model


  # Ensure you import your UserProfile model




def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)

                # Redirect based on user type
                user_profile = UserProfile.objects.get(user=user)  # Get the user profile
                if user_profile.user_type == 'customer':
                    return redirect('index')
                elif user_profile.user_type == 'delivery':
                    return redirect('delivery')
                elif user_profile.user_type == 'administrator':
                    return redirect('administrators')
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})



#
# def administrators(request):
#     return render(request, 'administrators.html')
def administrators(request):
    meals = Meal.objects.all()  # Get all meals from the database
    return render(request, 'administrators.html', {'meals': meals})



from django.shortcuts import render, redirect, get_object_or_404
from .models import Meal  # Adjust import according to your app structure
from django.contrib import messages



def view_meals(request):
    meals = Meal.objects.all()  # Get all meals from the database
    if request.method == 'POST' and 'delete_meal' in request.POST:
        meal_id = request.POST.get('meal_id')
        meal = get_object_or_404(Meal, id=meal_id)
        meal.delete()
        messages.success(request, 'Meal deleted successfully.')
        return redirect('view_meals')
    return render(request, 'view_meals.html', {'meals': meals})


def edit_meal(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id)

    if request.method == 'POST':
        # Update meal details with data from the form
        meal.meal_name = request.POST.get('meal_name')
        meal.meal_description = request.POST.get('meal_description')
        meal.meal_price = request.POST.get('meal_price')
        meal.save()  # Save the updated meal object
        return redirect('view_meals')  # Redirect to the page displaying all meals

    return render(request, 'edit_meal.html', {'meal': meal})


from django.shortcuts import render, redirect
from .forms import MealForm
from .models import Meal

from django.contrib.auth.models import User
from django.shortcuts import render

def user_list(request):
    users = User.objects.all()  # Get all registered users
    return render(request, 'user_list.html', {'users': users})  # Make sure 'users.html' exists


from django.shortcuts import render
from .models import Appointment  # Import your Appointment model

from django.shortcuts import render, redirect
from .models import Appointment  # Import your Appointment model
from django.contrib.auth.decorators import login_required


def view_booked_services(request):
    if request.method == 'POST' and 'delete_appointment' in request.POST:
        appointment_id = request.POST.get('appointment_id')
        # Check if the appointment exists and delete it
        try:
            appointment = Appointment.objects.get(id=appointment_id)
            appointment.delete()
            return redirect('booked')  # Redirect to the same page to see the updated list
        except Appointment.DoesNotExist:
            # Handle the case where the appointment does not exist
            pass

    appointments = Appointment.objects.all()  # Fetch all appointment records
    return render(request, 'booked.html', {'appointments': appointments})


def delivery_index(request):
    # Fetch all menu items
    menus = Meal.objects.all()

    return render(request, 'delivery.html', {'menus': menus})

from django.shortcuts import render
from .models import Meal  # Ensure this model is defined

def menu_page(request):
    # Fetch all menu items from the database
    menus = Meal.objects.all()
    return render(request, 'menu_page.html', {'menus': menus})


def add_meal(request):
    if request.method == 'POST':
        form = MealForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            form.save()  # Save the meal details to the database
            return redirect('delivery')  # Redirect back to the delivery page after saving
    else:
        form = MealForm()

    return render(request, 'add_meal.html', {'form': form})


# sections/views.py




from django.shortcuts import render, get_object_or_404, redirect
from .models import Meal  # Ensure you have the Meal model imported
from .forms import AppointmentForm  # Ensure you have your AppointmentForm imported


from django.shortcuts import render, get_object_or_404, redirect
from .models import Meal, Appointment
from .forms import AppointmentForm  # Make sure your form is imported

from django.shortcuts import render, get_object_or_404
from .models import Meal

from django.shortcuts import render, get_object_or_404, redirect
from .models import Meal, Appointment  # Import your Appointment model
from .forms import AppointmentForm  # Import your form if using one

from django.shortcuts import render, get_object_or_404
from .models import Meal

# def book_meal(request, meal_id):
#     meal = get_object_or_404(Meal, id=meal_id)  # Retrieve the meal instance
#
#     if request.method == "POST":
#         # Handle the form submission here
#         return redirect('pay', meal_id=meal.id)  # Redirect to the pay page with the meal_id
#
#     return render(request, 'book_meal.html', {'meal': meal})  # Pass the meal to the template

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Meal, Appointment


@csrf_exempt  # Only if necessary, to avoid CSRF token issues
def book_meal(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id)

    if request.method == 'POST':
        # Retrieve form data
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        phone_number = request.POST.get('phone_number')
        delivery_date = request.POST.get('delivery_date')
        delivery_time = request.POST.get('delivery_time')

        # Create and save the Appointment entry
        appointment = Appointment.objects.create(
            meal=meal,
            latitude=latitude,
            longitude=longitude,
            phone_number=phone_number,
            delivery_date=delivery_date,
            delivery_time=delivery_time,
            payment_status='UNPAID'  # Initial status
        )

        # Redirect or render a success message after saving
        return redirect('pay', meal_id=meal.id)


    # Render the form page if GET request
    return render(request, 'book_meal.html', {'meal': meal})


# views.py
from django.shortcuts import render
from .models import Appointment  # Import your Appointment model

# views.py
from django.shortcuts import render
from .models import Appointment

# def booked_services(request):
#     if request.user.userprofile.user_type == 'delivery':
#         appointments = Appointment.objects.select_related('meal', 'user').all()
#         return render(request, 'booked_services.html', {'appointments': appointments})
#     else:
#         return render(request, 'unauthorized.html')  # Or redirect to another page
def booked_services(request):
    if request.user.userprofile.user_type == 'delivery':
        appointments = Appointment.objects.select_related('meal', 'user').all()
        return render(request, 'booked.html', {'appointments': appointments})
    else:
        return render(request, 'booked.html')  # Or redirect to another page


from django.views import View
from django.shortcuts import render, redirect
from .models import User  # Import your User model

class UserListView(View):
    def get(self, request):
        users = User.objects.all()  # Get all users
        return render(request, 'user_list.html', {'users': users})

    def post(self, request):
        if 'delete_user' in request.POST:
            user_id = request.POST.get('user_id')
            User.objects.filter(id=user_id).delete()  # Delete user
            return redirect('user_list')  # Redirect to the same page



# def confirm_order(request, meal_id):
#     meal = get_object_or_404(Meal, id=meal_id)
#
#     if request.method == 'POST':
#         # Get the form data
#         latitude = request.POST.get('latitude')
#         longitude = request.POST.get('longitude')
#         phone_number = request.POST.get('phone_number')
#         delivery_date = request.POST.get('delivery_date')
#         delivery_time = request.POST.get('delivery_time')
#
#         # Here you can add your logic to process the order,
#         # such as saving it to the database or sending an email.
#
#         messages.success(request, "Your order has been confirmed!")
#         return redirect('index')  # Redirect to index or any other page
#
#     return render(request, 'sections/confirm_order.html', {'meal': meal})
# views.py


def confirm_order(request):
    if request.method == 'POST':
        # Process the order logic here
        # For example, save the order to the database

        # Redirect to the pay.html page
        return redirect(reverse('pay'))

    # Render the order confirmation page (if using GET)
    return render(request, 'confirm_order.html')


from django.shortcuts import render, get_object_or_404
from .models import Meal


def pay_page(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id)  # Retrieve the meal instance

    return render(request, 'pay.html',
                  {'meal': meal})  # Make sure 'payment_form.html' is the correct template name


from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import Appointment, Meal
from django_daraja.mpesa.core import MpesaClient
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from .models import Appointment  # Adjust the import based on your model's location
from django.shortcuts import redirect, get_object_or_404
from .models import Appointment  # Adjust the import according to your model

def delete_appointment(request, id):
    if request.method == 'POST':
        appointment = get_object_or_404(Appointment, id=id)
        appointment.delete()  # Deletes the appointment
        return redirect('view_booked_services')  # Redirect to a valid view after deletion


from django.shortcuts import redirect
from django.contrib.auth.models import User

def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('user_list')  # Make sure this name matches your URL pattern



# In views.py
from django.shortcuts import render
from django.contrib.auth.models import User

def view_users(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


@csrf_exempt
def darajaapi(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id)
    cl = MpesaClient()

    if request.method == "POST":
        phone_number = request.POST.get('phone_number')
        amount = int(meal.meal_price)
        account_reference = 'eCommerce'
        transaction_desc = 'Payment for Meal Order'
        callback_url = 'https://darajambili.herokuapp.com/express-payment'

        response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)

        if response.response_code == "0":  # Success
            # Get all unpaid appointments and mark them as 'PAID'
            appointments = Appointment.objects.filter(meal=meal, payment_status='UNPAID')
            if appointments.exists():
                for appointment in appointments:
                    appointment.payment_status = 'PAID'
                    appointment.save()
                return JsonResponse({"status": "success", "message": "Payment successful, status updated for all unpaid appointments."})
            else:
                return JsonResponse({"status": "error", "message": "No unpaid appointments found."})
        else:
            return JsonResponse({"status": "error", "message": "Payment failed. Please try again."})

    return render(request, 'pay.html', {'meal': meal})

def logout(request):
    auth_logout(request)  # This logs out the user
    return redirect('login')  # Redirect to the login page after logout




# @csrf_exempt
# def darajaapi(request, meal_id):
#     meal = get_object_or_404(Meal, id=meal_id)
#
#     cl = MpesaClient()
#
#     if request.method == "POST":
#         phone_number = request.POST.get('phone_number')
#
#         if not phone_number:
#             return JsonResponse({'error': 'Phone number is required'}, status=400)
#
#         try:
#             amount = int(meal.meal_price)
#         except (ValueError, TypeError):
#             return JsonResponse({'error': 'Invalid meal price'}, status=400)
#
#         account_reference = 'eCommerce'
#         transaction_desc = 'Order Payment'
#         callback_url = 'https://darajambili.herokuapp.com/express-payment'
#
#         logger.info(
#             f'Sending STK push: {phone_number=}, {amount=}, {account_reference=}, {transaction_desc=}, {callback_url=}')
#
#         try:
#             response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
#             logger.info(f'M-Pesa Response: {response}')
#
#             response_data = {
#                 'response_code': response.response_code,
#                 'response_description': response.response_description,
#                 'merchant_request_id': response.merchant_request_id,
#                 'checkout_request_id': response.checkout_request_id,
#                 'customer_message': response.customer_message,
#             }
#             return JsonResponse(response_data)
#         except Exception as e:
#             logger.error(f'Error during STK push: {e}')
#             return JsonResponse({'error': str(e)}, status=500)
#
#     return render(request, 'pay.html', {'meal': meal})

