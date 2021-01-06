from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate,logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from app_login.forms import signupForm , UserProfileChange,Profilepic
# Create your views here.
def signup(request):
    form = signupForm()
    registered = False
    if request.method =='POST':
        form = signupForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
    dict = {'form':form,'registered':registered}
    return render(request,'app_login/sign_up.html',context=dict)
def loginpage(request):
    form = AuthenticationForm()
    if request.method == 'POST':
       form = AuthenticationForm(data=request.POST)
       if form.is_valid():
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password')
           user = authenticate(username=username,password=password)
           if user is not None:
               login(request,user)
               return HttpResponseRedirect(reverse('index'))
    return render(request,'app_login/login.html', context={'form':form})
@login_required
def logoutpage(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
@login_required
def user_profile(request):
    return render(request,'app_login/profile.html',context={})
@login_required
def user_change(request):
    registered = False
    current_user = request.user
    form = UserProfileChange(instance=current_user)
    if request.method == 'POST':
        form = UserProfileChange(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = UserProfileChange(instance=current_user)
            registered = True
    return render(request,'app_login/profile_change.html' , context={'form':form ,'registered':registered })
@login_required
def change_password(request):
    current_user = request.user
    changed = False
    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
       form = PasswordChangeForm(current_user,data=request.POST)
       if form.is_valid():
           form.save()
           changed = True
    return render(request ,'app_login/change_password.html', context={'form':form,'changed':changed})
@login_required
def pro_pic_add(request):
    form = Profilepic()
    if request.method == 'POST':
        form = Profilepic(request.POST,request.FILES)
        if form.is_valid():
           user_obj = form.save(commit=False)
           user_obj.user = request.user
           user_obj.save()
           return HttpResponseRedirect(reverse('login_app:user_profile'))
    return render(request,'app_login/pro_pic_add.html',context={'form':form})

@login_required
def change_user_pic(request):
    current_user = request.user.user_profile
    form = Profilepic(instance=current_user)
    if request.method == 'POST':
       form = Profilepic(request.POST, request.FILES , instance=current_user)
       if form.is_valid():
          form.save()
          return HttpResponseRedirect(reverse('login_app:user_profile'))
    return render(request,'app_login/pro_pic_add.html',context={'form':form})
