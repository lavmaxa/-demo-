from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from rating.models import Users
from rating.models import Statements , Faculties, Group, Disciplines
from django.forms import ModelForm, TextInput, DateTimeInput, Select, NumberInput,ModelChoiceField,RadioSelect
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.db import models
import random

class LoginForm(forms.Form):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class RegisterUser(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



class FacultyForm(ModelForm):
    class Meta:
        model = Faculties
        fields = ['name']
        widgets = {
            "name":  Select(attrs={
                'class': 'form-control'
            })
        }

    def __init__(self, *args, **kwargs):
        super(FacultyForm, self).__init__(*args, **kwargs)
        self.fields['name'] = ModelChoiceField(queryset=Faculties.objects.all())
        # self.fields['name']= ModelChoiceField(queryset=Faculties.objects.all(),empty_label="(Nothing)")

class StatementsForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(StatementsForm, self).__init__(*args, **kwargs)
        user = self.request.user.email
        decanat = Users.objects.get(email=user).faculty

        max_id = Statements.objects.values_list('id', flat=True)
        new_id = len(max_id)+1
        self.fields['id'].initial = new_id
        self.fields['teacher'].queryset = Users.objects.filter(type_user='Преподаватель')
        self.fields['group'].queryset = Group.objects.filter(faculty=decanat).order_by('number')
        self.fields['group'].empty_label = '-- Список групп -- '
        self.fields['disciplines'].empty_label = '-- Список дисциплин -- '
        self.fields['teacher'].empty_label = '-- Список преподавателей -- '
        self.fields['disciplines'].queryset = Disciplines.objects.filter(faculty=decanat).order_by('name')

        self.fields["control"].choices =list(
            self.fields["control"].choices)[1:]

    class Meta:
        model = Statements
        fields = ['id','semester', 'date', 'control', 'disciplines', 'group', 'teacher']

        widgets ={
            "id": TextInput(attrs={
                'class': 'form-control',
                 # 'value': new_id, # значение по умолчанию
                'readonly': True,
                'hidden': True
        }),
            "semester": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Семестр',
                'min': 1,
                'max': 10

            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control datetimepicker-input',
                'placeholder': 'Дата контроля',
                'type': 'datetime-local'
            }),
            "control": RadioSelect(attrs={
                'class': 'from-radio',
                'type': 'checkbox'
            }, choices=Statements.CONTROL
            ),

            "disciplines": Select(attrs={
                'class': 'form-control',

            }),
            "group": Select(attrs={
                'class': 'form-control',
            })
            ,
            "teacher": Select(attrs={
                'class': 'form-control',
        })
        }


class FormGroup(ModelForm):
    class Meta:
        model = Faculties
        fields = ['name']
        widgets = {
            "name": Select(attrs={
                'class': 'form-control'
            })
        }

    def __init__(self, *args, **kwargs):
        super(FormGroup, self).__init__(*args, **kwargs)
        self.fields['name'] = ModelChoiceField(
            queryset=Statements.objects.all().order_by('semester', 'date'))
        self.fields['name'].empty_label = '-- Список ведомостей -- '
