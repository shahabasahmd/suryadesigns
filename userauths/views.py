from django.shortcuts import render,redirect,HttpResponse
from userauths.forms import UserRegisterForm
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.conf import settings



# Create your views here.
def register_view(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
           new_user= form.save()
           username = form.cleaned_data.get("username")
           fullname = form.cleaned_data.get("fullname")
           messages.success(request, f"Hey {username},Your account was created successfully")
           new_user = authenticate(username=form.cleaned_data['email'],name = form.cleaned_data.get("name"),
                                   password=form.cleaned_data['password1']
                                   )
           login(request,new_user)
           return redirect('userauths:sign-in')
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
    }
    return render(request, "userauths/sign-up.html",context)



def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Authenticate user
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            # Log in the user
            login(request, user)
            return redirect('index') 
        else:
            # Invalid login credentials, handle error
            return render(request, 'userauths/login.html', {'error_message': 'Invalid email or password'})

    return render(request,"userauths/login.html")