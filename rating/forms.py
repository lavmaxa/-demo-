from .models import Statements,  Faculties,   Marks
from django.forms import ModelForm, TextInput,  Select,ModelChoiceField


class ChoiceStatement(ModelForm):
    class Meta:
        model = Faculties
        fields = ['name']
        widgets = {
            "name":  Select(attrs={
                'class': 'form-control'
            })
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ChoiceStatement, self).__init__(*args, **kwargs)
        user = self.request.user.email
        self.fields['name'] = ModelChoiceField(queryset=Statements.objects.filter(teacher=user).order_by('semester', 'date'))
        self.fields['name'].empty_label = '-- Список ведомостей -- '

class MarksForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(MarksForm, self).__init__(*args, **kwargs)


    class Meta:
        model = Marks
        fields = ['id', 'student', 'statement', 'mark']
        widgets = {
            "id":  TextInput(attrs={
                'class': 'form-control',
                'readonly': True,
                'hidden': True

            }),
            "student": Select(attrs={
                'class': 'form-control',

                # 'disabled': True
            }),
            "statement": Select(attrs={
                'class': 'form-control',
                'hidden': True
            }),
            "mark": Select(attrs={
                'class': 'form-control'
            }, choices=Marks.MARK),
        }

