# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrador(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    parqueid = models.ForeignKey('Parque', models.DO_NOTHING, db_column='ParqueID')  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.
    permiss�o = models.IntegerField(db_column='Permiss�o')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Administrador'


class Cliente(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nib = models.CharField(db_column='NIB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    morada = models.CharField(db_column='Morada', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data_de_nascimento = models.DateField(db_column='Data de nascimento', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    telem�vel = models.CharField(db_column='Telem�vel', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cliente'


class Contrato(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    clienteid = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='ClienteID')  # Field name made lowercase.
    data_de_in�cio = models.DateField(db_column='Data de in�cio', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    data_de_t�rmino = models.DateField(db_column='Data de t�rmino', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Contrato'


class Dia(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dia = models.IntegerField(db_column='Dia')  # Field name made lowercase.
    m�s = models.IntegerField(db_column='M�s')  # Field name made lowercase.
    ano = models.IntegerField(db_column='Ano')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Dia'


class Funcionrio(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    parqueid = models.ForeignKey('Parque', models.DO_NOTHING, db_column='ParqueID')  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fun��o = models.CharField(db_column='Fun��o', max_length=255, blank=True, null=True)  # Field name made lowercase.
    permiss�o = models.IntegerField(db_column='Permiss�o')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Funcion�rio'


class Lugar(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    zonaid = models.ForeignKey('Zona', models.DO_NOTHING, db_column='ZonaID')  # Field name made lowercase.
    contratoid = models.ForeignKey(Contrato, models.DO_NOTHING, db_column='ContratoID')  # Field name made lowercase.
    viaturaid = models.ForeignKey('Viatura', models.DO_NOTHING, db_column='ViaturaID')  # Field name made lowercase.
    reservaid = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='ReservaID')  # Field name made lowercase.
    n�mero_do_lugar = models.IntegerField(db_column='N�mero do lugar')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    estado = models.CharField(db_column='Estado', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Lugar'


class Pagamento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    contratoid = models.ForeignKey(Contrato, models.DO_NOTHING, db_column='ContratoID')  # Field name made lowercase.
    montante = models.FloatField(db_column='Montante')  # Field name made lowercase.
    estado_do_pagamento = models.TextField(db_column='Estado do pagamento')  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    data_de_vencimento = models.DateField(db_column='Data de vencimento', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Pagamento'


class Parque(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.
    morada = models.CharField(db_column='Morada', max_length=255, blank=True, null=True)  # Field name made lowercase.
    capacidade = models.IntegerField(db_column='Capacidade')  # Field name made lowercase.
    zonas = models.IntegerField(db_column='Zonas')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Parque'


class Periodicidade(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    periodicidade = models.CharField(db_column='Periodicidade', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hora_de_in�cio = models.DateField(db_column='Hora de in�cio', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hora_de_t�rmino = models.DateField(db_column='Hora de t�rmino', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Periodicidade'


class RegistoMovimento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    data_de_entrada = models.DateField(db_column='Data de entrada', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    data_de_sa�da = models.DateField(db_column='Data de sa�da', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hora_de_inicio = models.DateField(db_column='Hora de inicio', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hora_de_t�rmino = models.DateField(db_column='Hora de t�rmino', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    provas = models.CharField(db_column='Provas', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Registo-movimento'


class Reserva(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    data_de_in�cio = models.DateField(db_column='Data de in�cio', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    data_de_t�rmino = models.DateField(db_column='Data de t�rmino', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hora_de_inicio = models.DateField(db_column='Hora de inicio', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hora_de_t�rmino = models.DateField(db_column='Hora de t�rmino', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Reserva'


class TabelaPreos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    parqueid = models.ForeignKey(Parque, models.DO_NOTHING, db_column='ParqueID')  # Field name made lowercase.
    pre�o_por_hora = models.FloatField(db_column='Pre�o por hora')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    taxa_por_hora = models.FloatField(db_column='Taxa por hora')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    taxa_noturna = models.FloatField(db_column='Taxa noturna')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    taxa_da_multa = models.FloatField(db_column='Taxa da multa')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Tabela-Pre�os'


class Viatura(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    contratoid = models.ForeignKey(Contrato, models.DO_NOTHING, db_column='ContratoID')  # Field name made lowercase.
    registo_movimentoid = models.ForeignKey(RegistoMovimento, models.DO_NOTHING, db_column='Registo-movimentoID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    marca = models.CharField(db_column='Marca', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modelo = models.CharField(db_column='Modelo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    matr�cula = models.CharField(db_column='Matr�cula', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Viatura'


class Zona(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    parqueid = models.ForeignKey(Parque, models.DO_NOTHING, db_column='ParqueID')  # Field name made lowercase.
    n�mero_da_zona = models.IntegerField(db_column='N�mero da zona')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lugares = models.IntegerField(db_column='Lugares')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Zona'
