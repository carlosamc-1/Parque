# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.urls import reverse
from datetime import datetime
from django.db import connection, models


class Parque(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.
    morada = models.CharField(db_column='Morada', max_length=255, blank=True, null=True)  # Field name made lowercase.
    capacidade = models.IntegerField(db_column='Capacidade')  # Field name made lowercase.
    zonas = models.IntegerField(db_column='Zonas')  # Field name made lowercase.

    def get_nome():
        return Parque.nome


class Administrador(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    parqueid = models.ForeignKey(Parque, models.CASCADE, db_column='ParqueID')  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.
    permissao = models.IntegerField(db_column='Permissao')  # Field name made lowercase.


class Cliente(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nib = models.IntegerField(db_column='NIB', blank=True, null=True)  # Field name made lowercase.
    morada = models.CharField(db_column='Morada', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data_de_nascimento = models.DateTimeField(auto_now=False, auto_now_add=False, db_column='Data de nascimento', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    telemovel = models.CharField(db_column='Telemovel', max_length=255, blank=True, null=True)  # Field name made lowercase.


class Contrato(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    parqueid = models.ForeignKey(Parque, models.CASCADE, db_column='ParqueID', default=1)  # Field name made lowercase.
    clienteid = models.ForeignKey(Cliente, models.CASCADE, db_column='ClienteID')  # Field name made lowercase.
    data_de_inicio = models.DateTimeField(auto_now=False, auto_now_add=False, db_column='Data de inicio', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    data_de_termino = models.DateTimeField(auto_now=False, auto_now_add=False, db_column='Data de termino', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.


class Dia(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dia = models.IntegerField(db_column='Dia')  # Field name made lowercase.
    mes = models.IntegerField(db_column='Mes')  # Field name made lowercase.
    ano = models.IntegerField(db_column='Ano')  # Field name made lowercase.


class Funcionario(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    parqueid = models.ForeignKey(Parque, models.CASCADE, db_column='ParqueID')  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.
    funcao = models.CharField(db_column='Funcao', max_length=255, blank=True, null=True)  # Field name made lowercase.
    permissao = models.IntegerField(db_column='Permissao')  # Field name made lowercase.


class RegistoMovimento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    parqueid = models.ForeignKey(Parque, models.CASCADE, db_column='ParqueID', default=1)  # Field name made lowercase.
    data_de_entrada = models.DateTimeField(default=datetime.now, db_column='Data de entrada', blank=False, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    data_de_saida = models.DateTimeField(auto_now=False, auto_now_add=False, db_column='Data de saida', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    provas = models.CharField(db_column='Provas', max_length=255, blank=True, null=True)  # Field name made lowercase.


class Viatura(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    contratoid = models.ForeignKey(Contrato, models.CASCADE, db_column='ContratoID')  # Field name made lowercase.
    registo_movimentoid = models.ForeignKey(RegistoMovimento, models.CASCADE, db_column='Registo-movimentoID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    marca = models.CharField(db_column='Marca', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modelo = models.CharField(db_column='Modelo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    matricula = models.CharField(db_column='Matricula', max_length=255, blank=True, null=True)  # Field name made lowercase.


class Zona(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    parqueid = models.ForeignKey(Parque, models.CASCADE, db_column='ParqueID')  # Field name made lowercase.
    numero_da_zona = models.IntegerField(db_column='Numero da zona')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lugares = models.IntegerField(db_column='Lugares')  # Field name made lowercase.


class Reserva(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    parqueid = models.ForeignKey(Parque, models.CASCADE, db_column='ParqueID', default=1)  # Field name made lowercase.
    viaturaid = models.ForeignKey(Viatura, models.CASCADE, db_column='ViaturaID', default=1)  # Field name made lowercase.
    data_de_inicio = models.DateField(auto_now=False, auto_now_add=False, db_column='Data de inicio', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    data_de_termino = models.DateField(auto_now=False, auto_now_add=False, db_column='Data de termino', blank=True, null=True)
    hora_de_inicio = models.TimeField(db_column='Hora de inicio', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hora_de_termino = models.TimeField(db_column='Hora de termino', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    @staticmethod
    def makeOptions():
        if "main_reserva" in connection.introspection.table_names():
            parques = Parque.objects.all()
            options=([(parque.nome) for parque in parques])
            return options
        else:
            return (("1", "No Database created"),)
    
    @staticmethod
    def makeOptions1():
        if "main_reserva" in connection.introspection.table_names():
            lugar = Lugar.objects.all()
            options=([(lugar.nome) for l in lugar])
            return options
        else:
            return (("1", "No Database created"),)

    def makeOptions2():
        if "main_reserva" in connection.introspection.table_names():
            viatura = Viatura.objects.all()
            options=([(viatura.matricula) for v in viatura])
            return options
        else:
            return (("1", "No Database created"),)


class Lugar(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    zonaid = models.ForeignKey(Zona, models.CASCADE, db_column='ZonaID')  # Field name made lowercase.
    contratoid = models.ForeignKey(Contrato, models.CASCADE, db_column='ContratoID')  # Field name made lowercase.
    viaturaid = models.ForeignKey(Viatura, models.CASCADE, db_column='ViaturaID')  # Field name made lowercase.
    reservaid = models.ForeignKey(Reserva, models.CASCADE, db_column='ReservaID')  # Field name made lowercase.
    numero_do_lugar = models.IntegerField(db_column='Numero do lugar')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    estado = models.CharField(db_column='Estado', max_length=255, blank=True, null=True)  # Field name made lowercase.

    def get_lugar_nome():
        return Lugar.nome_do_lugar
    

class Pagamento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    contratoid = models.ForeignKey(Contrato, models.CASCADE, db_column='ContratoID')  # Field name made lowercase.
    montante = models.FloatField(db_column='Montante')  # Field name made lowercase.
    estado_do_pagamento = models.TextField(db_column='Estado do pagamento')  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    data_de_vencimento = models.DateTimeField(auto_now=False, auto_now_add=False, db_column='Data de vencimento', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.


class Periodicidade(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    periodicidade = models.CharField(db_column='Periodicidade', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hora_de_inicio = models.TimeField(db_column='Hora de inicio', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hora_de_termino = models.TimeField(db_column='Hora de termino', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.


class TabelaPrecos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    parqueid = models.ForeignKey(Parque, models.CASCADE, db_column='ParqueID')  # Field name made lowercase.
    preco_por_hora = models.FloatField(db_column='Preco por hora')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    taxa_por_hora = models.FloatField(db_column='Taxa por hora')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    taxa_noturna = models.FloatField(db_column='Taxa noturna')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    taxa_da_multa = models.FloatField(db_column='Taxa da multa')  # Field name made lowercase. Field renamed to remove unsuitable characters.


    def get_absolute_url(self):
        return reverse("parque:parque-detail", kwargs={"id": self.id})
