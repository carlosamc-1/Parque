from django import forms
from .models import Cliente, Contrato, Dia, Parque, Periodicidade, Lugar        
import datetime

class ParqueModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.nome

class LugarModelChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.numero_do_lugar

class ContratoForm(forms.ModelForm):
    CHOICES_Dias = (('0', 'Segunda-Feira'),('1', 'Terça-Feira'), ('2', 'Quarta-Feira'), ('3', 'Quinta-Feira'), ('4', 'Sexta-Feira'), ('5', 'Sábado'), ('6', 'Domingo'))
    CHOICES_Periodicidade=(('diário', 'Todos os dias'), ('semanal', 'Escolher Dias: '))
    CHOICES_Horario=(('24H', '24H'), ('diurno', '8-20H'), ('noturno', '20-8H'))
    user=None
    OPTIONS_lugar = Lugar.makeOptions()
    parqueid = ParqueModelChoiceField(label="Parque", queryset=Parque.objects.all(), required=True)
    periodicidade = forms.ChoiceField(choices=CHOICES_Periodicidade, widget=forms.RadioSelect, required=True)
    dias = forms.MultipleChoiceField(choices=CHOICES_Dias, required=False)
    horario = forms.ChoiceField(choices=CHOICES_Horario, required=True)
    data_de_inicio = forms.DateField(required=True)
    data_de_termino = forms.DateField(required=True)
    lugar = LugarModelChoiceField(label="Lugar", queryset=Lugar.objects.filter(reservaid__isnull=True).filter(contratoid__isnull=True), required=True)
    class Meta:
        model = Contrato
        fields = [
            'parqueid',
            'data_de_inicio',
            'data_de_termino',
            'periodicidade',
            'dias',
            'horario',
            'lugar',
        ]

    def __init__(self, *args, **kwargs):
        if kwargs:
            self.user = kwargs.pop('current_user', None)
        super().__init__(*args, **kwargs)
	    
    def clean_data_de_inicio(self):
        data = self.cleaned_data.get('data_de_inicio')
        if data < datetime.date.today():
            raise forms.ValidationError("A data precisa de ser depois de hoje")
        return data

    def clean_data_de_termino(self):
        data_inicio = self.cleaned_data.get('data_de_inicio')
        if data_inicio == None:
            data_inicio = datetime.date.min
        data_fim = self.cleaned_data.get('data_de_termino')
        if data_fim <= data_inicio:
            raise forms.ValidationError("A data de fim precisa de ser maior que a de inicio")
        return data_fim

    def save(self, contratoID = None):
        if contratoID is not None:
            newContrato = Contrato.objects.get(id=contratoID)
        else:
            newContrato = Contrato()
		
        newContrato.parqueid = self.cleaned_data.get('parqueid')
        newContrato.clienteid = self.user
        newPeriodicidade = Periodicidade()
        newPeriodicidade.horario = self.cleaned_data.get('horario')
        newPeriodicidade.periodicidade = self.cleaned_data.get('periodicidade')
        newPeriodicidade.save()
        print(self.cleaned_data.get('periodicidade'))
        if self.cleaned_data.get('periodicidade') == "semanal":
            for i in range(len(self.cleaned_data.get('dias'))):
                newDia = Dia()
                newDia.periodicidadeid = newPeriodicidade
                newDia.nome = self.CHOICES_Dias[i][1]
                newDia.save()
        newContrato.periodicidadeid = newPeriodicidade
        newContrato.data_de_inicio = self.cleaned_data.get('data_de_inicio')
        newContrato.data_de_termino = self.cleaned_data.get('data_de_termino')
        newContrato.save()
        for i in self.cleaned_data.get('lugar'):
                i.contratoid = newContrato
                i.save()

