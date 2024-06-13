from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.conf import settings

def login(request):
    print('function calling')
    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('password')
        print(username)
        print(password)
        
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            auth_login(request, user)
            print('checking for user type:', user.user_type)

            
            
            # Determine the URL to redirect based on user type
            print('checking for user type')
            
            if user.user_type == 'employee':
                print('this is the  employee')
                return redirect('employee_dashboard')  # Replace with the URL for employee dashboard
            elif user.user_type == 'owner':
                print('this is the gym owner')
                return redirect('/gymfrontend')  # Replace with the URL for software owner dashboard
            elif user.user_type == 'trainer':
                print('this is the trianer ')
                return redirect('trainer_dashboard')  # Replace with the URL for trainer dashboard
            elif user.user_type == 'Software Owner':
                print('member tis is ')
                return redirect('/developerfrontend')  # Replace with the URL for member dashboard
            elif user.user_type == 'staff':
                print('this is the staff')
                return redirect('staff_dashboard')  # Replace with the URL for software staff dashboard

        else:
            # Return an 'invalid login' error message
            return render(request, 'login.html', {'error_message': 'Invalid email or password'})
    else:
        return render(request, 'login.html')
