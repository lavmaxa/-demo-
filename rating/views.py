from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404
from .models import Users, Marks, Statements, Group
from django.contrib.auth.models import User
from .forms import ChoiceStatement, MarksForm
from django.forms import modelformset_factory

def fillratings(request):
    error = ''
    count_student = 0
    stud_group = None
    get_group = None
    get_control = None
    ved = ''
    if request.method == 'GET':
        statem = request.GET.get('name', -1)
        if statem != -1:
            ved = get_object_or_404(Statements, id=statem)
            get_control = get_object_or_404(Statements, id=statem).control
            get_group = get_object_or_404(Statements, id=statem).group
            stud_group = Users.objects.filter(group=get_group).order_by('last_name')
            count_student = stud_group.count()

    MarksFormSet = modelformset_factory(Marks, fields=('id', 'student', 'statement', 'mark'), form=MarksForm,extra=count_student)

    if request.method == 'POST':
        formset = MarksFormSet(request.POST, queryset=Users.objects.filter(group=get_group))
        if formset.is_valid():
            formset.save()
            error = 'Ведомость успешно сохранена'
        else:
            error = 'Форма была не верной'


    formset = MarksFormSet(queryset=Users.objects.none())
    formFa = ChoiceStatement(request=request)

    count =0
    max_id = Marks.objects.values_list('id', flat=True)
    new_id = len(max_id) + 1
    for form in formset:
        if get_control == 'Экзамен':
            form.fields["mark"].choices = list(form.fields["mark"].choices)[:5]
        elif get_control == 'Зачёт':
            form.fields["mark"].choices = [("", "---------"), ] + list(form.fields["mark"].choices)[5:7]
        else:
            form.fields["mark"].choices = [("", "---------"), ] +list(form.fields["mark"].choices)[7:]
        form.fields['id'].initial = new_id + count
        form.fields['statement'].initial = get_object_or_404(Statements, id=statem)
        form.fields['student'].initial =stud_group[count]
        count+=1
    type_user = get_object_or_404(Users, email=request.user.email).type_user
    data = {
        'formset':formset,
        'formFa':formFa,
        'ved': ved,
        'error': error,
        'type_user': type_user
    }

    return render(request, 'rating/rating_for_teacher.html', data)




def index(request):
    tec_user = request.user.email
    get_mark = Marks.objects.filter(student=tec_user)
    mark = Marks.objects.all()
    use = get_object_or_404(Users, email=tec_user)
    type_user = get_object_or_404(Users, email=request.user.email).type_user
    return render(request, 'rating/rating.html', {'mark': mark, 'get_mark':get_mark, 'type_user': type_user,'use':use})

def all(request):
    tec_user = request.user.email
    get_mark = Marks.objects.filter(student=tec_user)
    get_sem = []
    for i in get_mark:
        s = i.statement.semester
        if s not in get_sem:
            get_sem.append(i.statement.semester)
    get_sem.sort(reverse=True)
    mark = Marks.objects.all()
    type_user = get_object_or_404(Users, email=request.user.email).type_user
    return render(request, 'rating/all.html', {'mark': mark, 'get_mark': get_mark, 'type_user': type_user,'get_sem':get_sem})

def sem1(request):
    tec_user = request.user.email
    get_mark = Marks.objects.filter(student=tec_user)
    mark = Marks.objects.all()
    type_user = get_object_or_404(Users, email=request.user.email).type_user
    return render(request, 'rating/1sem.html', {'mark': mark, 'get_mark': get_mark, 'type_user': type_user})
class ArtistView(ListView):
    model = Marks
    template_name = '1sem.html'
    context_object_name = 'mark'

def sem2(request):
    tec_user = request.user.email
    get_mark = Marks.objects.filter(student=tec_user)
    mark = Marks.objects.all()
    type_user = get_object_or_404(Users, email=request.user.email).type_user
    return render(request, 'rating/2sem.html', {'mark': mark, 'get_mark': get_mark, 'type_user': type_user})

def sem3(request):
    tec_user = request.user.email
    get_mark = Marks.objects.filter(student=tec_user)
    mark = Marks.objects.all()
    type_user = get_object_or_404(Users, email=request.user.email).type_user
    return render(request, 'rating/3sem.html', {'mark': mark, 'get_mark': get_mark, 'type_user': type_user})


def sem4(request):
    tec_user = request.user.email
    get_mark = Marks.objects.filter(student=tec_user)
    mark = Marks.objects.all()
    type_user = get_object_or_404(Users, email=request.user.email).type_user
    return render(request, 'rating/4sem.html', {'mark': mark, 'get_mark': get_mark, 'type_user': type_user})



def sem5(request):
    tec_user = request.user.email
    get_mark = Marks.objects.filter(student=tec_user)
    mark = Marks.objects.all()
    type_user = get_object_or_404(Users, email=request.user.email).type_user
    return render(request, 'rating/5sem.html', {'mark': mark, 'get_mark': get_mark, 'type_user': type_user})


def sem6(request):
    tec_user = request.user.email
    get_mark = Marks.objects.filter(student=tec_user)
    mark = Marks.objects.all()
    type_user = get_object_or_404(Users, email=request.user.email).type_user
    return render(request, 'rating/6sem.html', {'mark': mark, 'get_mark': get_mark, 'type_user': type_user})

def sem7(request):
    tec_user = request.user.email
    get_mark = Marks.objects.filter(student=tec_user)
    mark = Marks.objects.all()
    type_user = get_object_or_404(Users, email=request.user.email).type_user
    return render(request, 'rating/7sem.html', {'mark': mark, 'get_mark': get_mark, 'type_user': type_user})

def sem8(request):
    tec_user = request.user.email
    get_mark = Marks.objects.filter(student=tec_user)
    mark = Marks.objects.all()
    type_user = get_object_or_404(Users, email=request.user.email).type_user
    return render(request, 'rating/8sem.html', {'mark': mark, 'get_mark': get_mark, 'type_user': type_user})
