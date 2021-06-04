from django.shortcuts import render,HttpResponse,redirect,reverse
from django.contrib.auth import authenticate, login,logout
from  . models import *
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect(reverse('login_page'))
    question_objects=Question.objects.all()
    # choices_object=question_object.choices.all()

    return render(request,'index.html',{'questions':question_objects})

def selected(request,choice_id):
    selected_choice=Choice.objects.get(id=choice_id)
    # selected_choice.votes=selected_choice.votes+1
    # selected_choice.save()
    question_object=selected_choice.question_set.all()[0]
    voted_list=question_object.voted_users.all()
    current_user=request.user
    for i in voted_list:
        if i.id == current_user.id:
            return HttpResponse('You are already voted')
    selected_choice.votes=selected_choice.votes+1
    selected_choice.save()
    question_object.voted_users.add(current_user)
    question_object.save()
    return HttpResponse('you selected '+ selected_choice.choice_text +' '+str(selected_choice.votes)) 

def login_page(request):
    if request.method=='GET':
        return render(request,'login.html')
    elif request.method=='POST':
        user_name=request.POST['username']
        pass_word=request.POST['password']
        user=authenticate(request,username=user_name,password=pass_word)
        if user is not None:
            login(request,user)
            return redirect(reverse('index'))
        else:
            return HttpResponse('Invalid username or password')     

def logout_user(request):
    logout(request)
    return redirect(reverse('login_page'))

def signup(request):
    if request.method=='GET':
        return render(request,'signup.html')
    elif request.method=='POST':
        user_name=request.POST['username']
        pass_word=request.POST['password']
        pass_word1=request.POST['password2']
        if pass_word != pass_word1:
            return HttpResponse("Password doesn't match")
        try:
            user  = User.objects.get(username=user_name)
        except ObjectDoesNotExist:
            user = None
        if user is not None:
            return HttpResponse('Username already exists')
        user=User.objects.create_user(username=user_name, password=pass_word)
        user.save()
        login(request, user)
        return redirect(reverse('index'))   


