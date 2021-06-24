from django.db import models
# from django.contrib.auth.models import User

class Faculties(models.Model):
    id = models.CharField(verbose_name='id', primary_key=True, max_length=100)
    name = models.CharField(verbose_name='Название', max_length=150)
    abbreviation = models.CharField(verbose_name='Аббревиатура', max_length=50)

    def __str__(self):
        return f' {self.name} ({self.abbreviation})'

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'


class Group(models.Model):
    id = models.CharField(verbose_name='id', primary_key=True, max_length=100)
    faculty = models.ForeignKey(Faculties, verbose_name='Факультет', on_delete=models.PROTECT)
    number = models.CharField(verbose_name='Группа', max_length=15)
    field_of_study = models.CharField(verbose_name='Направление', max_length=120)
    profile_of_study = models.CharField(verbose_name='Профиль/Направленность', max_length=150)

    def __str__(self):
        return f' {self.number} '

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Users(models.Model):
    email = models.EmailField(verbose_name='Почта', primary_key=True)
    first_name = models.CharField( verbose_name='Имя', max_length=140)
    last_name = models.CharField( verbose_name='Фамилия', max_length=200)
    second_name = models.CharField( verbose_name='Отчество', max_length=140, blank=True)
    TYPE_USER = (
        ('Студент', 'Студент'),
        ('Преподаватель', 'Преподаватель'),
        ('Сотрудник деканата', 'Сотрудник деканата'),
    )
    type_user = models.CharField(max_length=20, choices=TYPE_USER)
    faculty = models.ForeignKey(Faculties, verbose_name='Факультет', null=True, blank=True, on_delete=models.PROTECT)
    group = models.ForeignKey(Group, verbose_name='Группа', null=True, blank=True,  on_delete=models.PROTECT)
    number_zachetka = models.CharField(verbose_name='Номер зачетки', max_length=50, blank=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.second_name} ({self.type_user}) '

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"



class Disciplines(models.Model):
    id = models.CharField(verbose_name='id', primary_key=True, max_length=100)
    faculty = models.ForeignKey(Faculties, verbose_name='Факультет',null=True, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Дисциплина',null=True, max_length=150)


    def __str__(self):
        return f' {self.name} '

    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'


class Statements(models.Model):
    id = models.CharField(verbose_name='id', primary_key=True, max_length=100)
    # id = models.AutoField(verbose_name='id',primary_key=True)
    semester = models.IntegerField(verbose_name='Семестр')
    date = models.DateTimeField('Дата экзамена/зачета')
    CONTROL = (
            ('Экзамен', 'Экзамен'),
            ('Зачёт', 'Зачёт'),
            ('Зачёт c оценкой', 'Зачёт c оценкой'),
        )
    control = models.CharField(max_length=20, verbose_name='Экзамен/зачет', choices=CONTROL)
    disciplines = models.ForeignKey(Disciplines, verbose_name='Дисциплина', null=True, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, verbose_name='Группа', null=True, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Users, verbose_name='ФИО преподавателя', null=True, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.semester} семестр,  {self.date} {self.control} по дисциплине {self.disciplines}, {self.group}, {self.teacher}'

    class Meta:
        verbose_name = 'Ведомость'
        verbose_name_plural = 'Ведомости'


class Marks(models.Model):
    id = models.CharField(verbose_name='id',primary_key=True, max_length=100)
    student = models.ForeignKey(Users, verbose_name='Студент', on_delete=models.CASCADE)
    statement = models.ForeignKey(Statements, verbose_name='Ведомость', on_delete=models.CASCADE, null=True)
    MARK = (
        ('2', 'неуд'),
        ('3', 'удовл'),
        ('4', 'хор'),
        ('5', 'отл'),
        ('зач', 'зач'),
        ('незач', 'незач'),
        ('незач(2)', 'незач(неуд)'),
        ('зач(3)', 'зач(удовл)'),
        ('зач(4)', 'зач(хор)'),
        ('зач(5)', 'зач(отл)'),
    )
    mark = models.CharField(max_length=12,verbose_name='Оценка', choices=MARK)

    def __str__(self):
        return f'{self.student} получил(а) оценку {self.mark}'

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
