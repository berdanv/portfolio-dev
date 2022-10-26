from django.forms import ModelForm
from app.models import Alunos


class AlunosForm(ModelForm):
    class Meta:
        model = Alunos
        fields = ['nome', 'cidade', 'idade']