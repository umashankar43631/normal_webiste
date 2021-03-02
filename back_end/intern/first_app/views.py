from django.shortcuts import render
#from first_app.models import NewUserForm 
from first_app.forms import FormN,SignupForm,LoginForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout
# formname for contact us

# Create your views here.
def home(request):
    return render(request,'first_app/Home.html')
def about(request):
    return render(request,'first_app/About.html')
# def buynow(request):
#     return render(request, 'first_app/Buynow.html')
def cart(request):
    return render(request, 'first_app/cart.html')

def blog(request):
    return render(request,'first_app/blog.html')
def contactUs(request):
    form = FormN()
    if request.method == 'POST':
        form = FormN(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return home(request)
        else:
            print("Fill out Form correctly!")
    return render(request, 'first_app/contactUs.html', {'form': form})
def index(request):
    return render(request,'first_app/index.html')

def post_1(request):
    return render(request, 'first_app/post-1.html')

def post_2(request):
    return render(request, 'first_app/post-2.html')

def post_3(request):
    return render(request, 'first_app/post-3.html')

def post_4(request):
    return render(request, 'first_app/post-4.html')

def post_5(request):
    return render(request, 'first_app/post-5.html')

def post(request):
    return render(request, 'first_app/post.html')

def product(request):
    return render(request, 'first_app/Product.html')

def services(request):
    return render(request, 'first_app/services.html')

def cart(request):
    return render(request, 'first_app/cart.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def special(request):
    return HttpResponse("You are logged in")

# def login(request):
#     pass
#     # form = Login()
#     # if request.method == 'POST':
#     #     form = Login(request.POST)
#     #     if form.is_valid():
#     #         form.save(commit = True)
#     #         return home(request)
#     #     else:
#     #         return "Form is invalid"

def user_login(self, request):
    
    if request.method=='POST':
        register_status = False
        if request.POST.get('submit') == 'checkform1':
            user_form = SignupForm(data = request.POST)
            if user_form.is_valid():
                user = user_form.save()
                user.set_password(user.up)
                user.save()
                register_status = True
            else:
                print(user_form.errors)
        else:
            user_form = SignupForm()
        return render(request, 'first_app/Login.html', {'user_form':user_form,'register_status': register_status})
    elif request.POST.get('submit') == 'checkform2':
        pass

        ## do what ever you want to do for first function ####
    
            ## do what ever you want to do for second function ####
        ## return def post###  
    return render(request, 'first_app/Login.html', {'user_form':user_form,})