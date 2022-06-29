from pickle import NONE
from pyexpat import model
from django import forms
from django.core.validators import validate_integer
from django.forms import ModelForm
from main.models import Parque, Reserva, Lugar, TabelaPrecos, Viatura
from django.forms import MultiWidget, TextInput
import datetime
from datetime import date

class ParqueModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.nome

class LugarModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.numero_do_lugar
    
class ViaturaModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.matricula

class CreateReserve(ModelForm):
    OPTIONS_parque = Reserva.makeOptions()
    # parqueid = forms.CharField(widget=forms.Select(choices=OPTIONS_parque, attrs={'class' : 'input'}), label='Parque', required=True)
    parqueid = ParqueModelChoiceField(label="Parque", queryset=Parque.objects.all(), required=True)
    data_de_inicio = forms.DateField(label="Data de Início", widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    data_de_termino = forms.DateField(label="Data de Término", widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    hora_de_inicio = forms.TimeField(label="Hora de Início", widget=forms.widgets.TimeInput(attrs={'type': 'time'}))
    hora_de_termino = forms.TimeField(label="Hora de Término", widget=forms.widgets.TimeInput(attrs={'type': 'time'}))
    lugar = LugarModelChoiceField(label="Lugar", queryset=Lugar.objects.filter(reservaid__isnull = True).filter(contratoid__isnull = True), required=True)
    viaturaid = ViaturaModelChoiceField(label="Matrícula", queryset=Viatura.objects.all(), required=True)

    class Meta:
        model = Reserva
        fields = ['parqueid', 'data_de_inicio', 'data_de_termino', 'hora_de_inicio', 'hora_de_termino', 'lugar', 'viaturaid']
    

    def clean_data_de_termino(self):
        data_inicio = self.cleaned_data.get('data_de_inicio')
        data_termino = self.cleaned_data.get('data_de_termino')
        if data_inicio < datetime.date.today():
            raise forms.ValidationError("A data precisa de ser depois de hoje")
        if data_termino < data_inicio:
            raise forms.ValidationError("A data de término tem que ser depois da data de início")
        return data_termino

    def clean_hora_de_termino(self):
        hora_inicio = self.cleaned_data.get('hora_de_inicio')
        hora_termino = self.cleaned_data.get('hora_de_termino')
        data_inicio = self.cleaned_data.get('data_de_inicio')
        data_termino = self.cleaned_data.get('data_de_termino')
        if  data_inicio == data_termino and hora_termino < hora_inicio:
            raise forms.ValidationError("A hora de término precisa ser maior que a hora de início")
        return hora_termino

class CreateTable(ModelForm):
    parqueid = ParqueModelChoiceField(label="Parque", queryset=Parque.objects.all(), required=True)
    preco_por_hora = forms.FloatField()
    taxa_por_hora = forms.FloatField()
    taxa_noturna = forms.FloatField()
    taxa_da_multa = forms.FloatField()

    class Meta:
        model = TabelaPrecos
        fields = ['parqueid', 'preco_por_hora', 'taxa_por_hora', 'taxa_noturna', 'taxa_da_multa']

    def clean_parqueid(self):
        parqueid = self.cleaned_data.get('parqueid')
        for instance in TabelaPrecos.objects.all():
            if instance.parqueid == parqueid:
                raise forms.ValidationError("Este parque já possuí uma tabela de preços. Selecione outro")
        return parqueid

    def clean_preco_por_hora(self):
        data = self.cleaned_data.get('preco_por_hora')
        if data < 0:
            raise forms.ValidationError("O valor necessita ser positivo")
        return data

    def clean_taxa_por_hora(self):
        data = self.cleaned_data.get('taxa_por_hora')
        if data < 0:
            raise forms.ValidationError("O valor necessita ser positivo")
        return data

    def clean_taxa_noturna(self):
        data = self.cleaned_data.get('taxa_noturna')
        if data < 0:
            raise forms.ValidationError("O valor necessita ser positivo")
        return data

    def clean_taxa_da_multa(self):
        data = self.cleaned_data.get('taxa_da_multa')
        if data < 0:
            raise forms.ValidationError("O valor necessita ser positivo")
        return data

class UpdateTable(ModelForm):
    preco_por_hora = forms.FloatField()
    taxa_por_hora = forms.FloatField()
    taxa_noturna = forms.FloatField()
    taxa_da_multa = forms.FloatField()

    class Meta:
        model = TabelaPrecos
        fields = ['preco_por_hora', 'taxa_por_hora', 'taxa_noturna', 'taxa_da_multa']

    def clean_parqueid(self):
        parqueid = self.cleaned_data.get('parqueid')
        for instance in TabelaPrecos.objects.all():
            if instance.parqueid == parqueid:
                raise forms.ValidationError("Este parque já possuí uma tabela de preços. Selecione outro")
        return parqueid

    def clean_preco_por_hora(self):
        data = self.cleaned_data.get('preco_por_hora')
        if data < 0:
            raise forms.ValidationError("O valor necessita ser positivo")
        return data

    def clean_taxa_por_hora(self):
        data = self.cleaned_data.get('taxa_por_hora')
        if data < 0:
            raise forms.ValidationError("O valor necessita ser positivo")
        return data

    def clean_taxa_noturna(self):
        data = self.cleaned_data.get('taxa_noturna')
        if data < 0:
            raise forms.ValidationError("O valor necessita ser positivo")
        return data

    def clean_taxa_da_multa(self):
        data = self.cleaned_data.get('taxa_da_multa')
        if data < 0:
            raise forms.ValidationError("O valor necessita ser positivo")
        return data