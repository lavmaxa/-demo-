from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import auth
from rating.models import Users, Marks, Statements, Faculties, Group
from .forms import *


def index(request):
    type_user = get_object_or_404(Users, email=request.user.email).type_user
    data={
        'title':'Зачетка',
        'type_user': type_user
    }
    return render(request,'main/index.html', data)

def about(request):
    type_user = get_object_or_404(Users, email=request.user.email).type_user
    return render(request,'main/about.html',{'type_user': type_user})

def user_login(request):
    type_user = get_object_or_404(Users, email=request.user.email).type_user
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
          # ЧЕТ НЕ РАБОТАЕТ     if user.is_active:
                    login(request, user)
                    return render(request, 'main/index.html')
         #       else:
         #           return render(request, 'main/login.html', {'type_user': type_user, 'form': form,'login_error' : "Данный пользователь не активен"})
            else:
                return render(request, 'main/login.html', {'type_user': type_user, 'form': form,'login_error' : "Неверный логин или пароль "})
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'type_user': type_user, 'form': form})

def logout(request):
    auth.logout(request)
    return redirect("index")


def register(request):
    type_user = get_object_or_404(Users, email=request.user.email).type_user
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password2'])
            # Save the User object
            new_user.save()
            user_form.save()

            return render(request, 'main/register_done.html', {'new_user': new_user, 'type_user':type_user})
    else:
        user_form = RegisterUser()
    return render(request, 'main/register.html', {'user_form': user_form,'type_user':type_user})


def my_view(request):

    if not request.user.is_authenticated:
        return redirect( '%s?next=%s' %(settings.LOGIN_URL, request.path))
    else:
        type_user = get_object_or_404(Users, email=request.user.email).type_user
        return render(request,'main/index.html', {'title':'Зачетка', 'type_user':type_user})


def vedomost(request):
    error = ''
    tec_user = request.user.email#Получение почты текущего пользователя
    facul = request.GET.get('name')
    if request.method == 'POST':
        form = StatementsForm(request.POST, request=request)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма некорректна'

    else:
        form = StatementsForm(request.POST, request=request)

    tec_teacher = Users.objects.filter(type_user='Преподаватель')#список преподов
    formFa = FacultyForm()

    form = StatementsForm(request=request)
    student = Users.objects.all()
    student = Users.objects.get(email=request.user.email)
    type_user = get_object_or_404(Users, email=request.user.email).type_user
    data = {
        'type_user': type_user,
        'form': form,
        'student': student,
        'tec_user': tec_user,
        'tec_teacher':tec_teacher,
        'error': error
    }

    return render(request, 'main/vedomost.html', data)


def all_student_group(request):
    error = ''
    stud_group = None
    get_group = None
    ved = request.GET.get('name', -1)
    if request.method == 'GET':
        if ved != -1:
            get_ved = get_object_or_404(Statements, id=ved)
            stud_group = Marks.objects.filter(statement=get_ved)

    formGroup = FormGroup()
    type_user =get_object_or_404(Users, email=request.user.email).type_user
    data = {
        'type_user':type_user,
        'formGroup': formGroup,
        'stud_group':stud_group,
        'error': error
    }
    return render(request, 'main/all_student_group.html', data)

