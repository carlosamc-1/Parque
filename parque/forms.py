from tkinter.messagebox import ABORTRETRYIGNORE
from django import forms
from .models import Parque, Zona, Lugar

# class ParqueForm(forms.ModelForm):
#     nome = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Your title'}))
#     morada = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Your address'}))
#     capacidade = forms.IntegerField(label='', widget=forms.TextInput(attrs={'placeholder':'Your capacity'}))
#     zonas = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Your fds'}))
#     class Meta:
#         model = Parque
#         fields = [
#             'nome'
#             'morada'
#             'capacidade'
#             'zonas'
#         ]

class ParqueModelForm(forms.ModelForm):
    nome = forms.CharField(
        max_length=60,
        help_text='60 characters max',
        widget=forms.TextInput(attrs={'placeholder':'Enter the name of the park','rows':1,'cols':120}),
        required=True
        )
    capacidade = forms.IntegerField(
        help_text='Must be at least 100',
        min_value=100,
        initial=100,
        required=True
        )
    zonas = forms.IntegerField(
        help_text='Must be at least 1',
        min_value=1,
        initial=1,
        required=True
        )
    morada = forms.CharField(
        max_length=120,
        widget=forms.TextInput(attrs={'placeholder':'Enter the address of the park','rows':1,'cols':120}),
        required=True
        )
    pais = forms.CharField(
        max_length=50,
        required=True
        )
    cidade = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder':'Enter the name of the city','rows':1,'cols':120}),
        required=True
        )
    distrito = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder':'Enter the name of the city','rows':1,'cols':120}),
        required=True
        )
    codigo_postal = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={'placeholder':'Enter the zip code','rows':1,'cols':120}),
        required=True
        )
    estado = forms.ChoiceField(
        choices=Parque.make_options(),
        required=True
        )

    class Meta:
        model = Parque
        fields = [
            'nome',
            'morada',
            'capacidade',
            'zonas',
            'cidade',
            'codigo_postal',
            'distrito',
            'pais',
            'estado'
        ]



class ZonaModelForm(forms.ModelForm):
    numero_da_zona = forms.IntegerField(
        required=True,
        initial=1,
        min_value=1,
        max_value=1000
        )
    lugares = forms.IntegerField(
        required=True,
        initial=1,
        min_value=1,
        max_value=1000
        )
    tipo_de_zona = forms.ChoiceField(
        choices=Zona.make_options(),
        required=True
        )

    class Meta:
        model = Zona
        fields = [
            'numero_da_zona',
            'lugares',
            'tipo_de_zona'
        ]



class LugarModelForm(forms.ModelForm):
    numero_do_lugar = forms.IntegerField(
        required=True,
        initial=1,
        min_value=1,
        max_value=1000
        )
    estado = forms.ChoiceField(
        choices=Lugar.make_options(),
        required=True
        )

    class Meta:
        model = Lugar
        fields = [
            'numero_do_lugar',
            'estado'
        ]

    # def clean_nome(self, *args, **kwargs):
    #     nome=self.cleaned_data.get("nome")
    #     if "@" in nome:
    #         raise forms.ValidationError("This is not a valid title")
    #     else:
    #         return nome

#    def clean_email(self, *args, **kwargs):
#        email=self.cleaned_data.get("email")
#        if not email.endswith("edu"):
#            raise forms.ValidationError("This is not a valid email")
#        return email