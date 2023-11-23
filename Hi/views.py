from django.shortcuts import render, redirect

# Dummy user data (replace with a database in a real scenario)
users = {
    'Karti': {'password': 'password'},
    'Jaya': {'password': 'pass'},
}


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username in users and users[username]['password'] == password:
            return redirect('success')
        else:
            return redirect('fail')

    return render(request, 'login.html')


def success_view(request):
    return render(request, 'success.html')


def fail_view(request):
    return render(request, 'fail.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the username is already taken
        if username in users:
            return redirect('fail')  # You might want to render a specific fail template for registration

        # Register the new user
        users[username] = {'password': password}
        return redirect('successregister')  # Redirect to a success page or login page

    return render(request, 'register.html')

def success_register(request):
    return render(request, 'successregister.html')
