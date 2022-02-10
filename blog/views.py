from django.shortcuts import render
from django.http import HttpResponse
from.models import blog,Profile,news
from django.contrib import auth
from.forms import SignUpForm
from django.contrib.auth.decorators import login_required
from.forms import InputForm,blogform
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserUpdateForm, ProfileUpdateForm
from django.shortcuts import render, redirect
def home(request):
    blogs=blog.objects.all().order_by("created_on")
    context={
    "blogs": blogs
    }
    return render(request, 'blog/home.html', context)
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            user=u_form.save()
            profile=p_form.save(commit=False)
            profile.user=user
            profile.save()
            auth.login(request, user)
            messages.success(request, f'Your account has been updated!')
            return redirect('blog-profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'blog/profile.html', context)
def contactus(request):
    newses=news.objects.all().order_by("created_on")
    context={
    "newses": newses
    }
    return render(request, 'blog/contactus.html', context)
def logout(request):
    auth.logout(request)
    return render(request, 'blog/logout.html', {'title': 'logout'})
def about(request): 
    if request.method=='POST' and 'btnform1' in request.POST:
     yourForm= request.POST.dict()
     itemValue = yourForm.get("Text")
     kk=""
     for i in range(0,len(itemValue)):
        if(ord(itemValue[i])!=32):
         t=97+122-ord(itemValue[i])-32
         kk=kk+(chr)(t)
        else:
         kk=kk+itemValue[i]
     return HttpResponse(kk)
    elif request.method=='POST' and 'btnform2' in request.POST:
     yourForm= request.POST.dict()
     itemValue = yourForm.get("Text")
     kk=""
     for i in range(0,len(itemValue)):
        if(ord(itemValue[i])!=32):
         t=65+90-ord(itemValue[i])+32
         kk=kk+(chr)(t)
        else:
         kk=kk+itemValue[i]
     return HttpResponse(kk)
    else:
     context= InputForm() 
     return render(request, "blog/about.html", {'form':context,'form1':context}) 
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            User._meta.get_field('email')._unique = True
            user = authenticate(username=username, password=raw_password)
            profile=Profile.objects.create(user=user)
            profile.Mobile=form.cleaned_data.get('Mobile')
            profile.save()
            auth.login(request, user)
            return render(request, 'blog/response.html', {'title': 'response'})
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form':form})
def Login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                Profile(request,user)
                return redirect('/profile')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "blog/login.html",
                    context={"form":form})
