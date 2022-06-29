from pickle import NONE
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from .models import *
from .forms import *

def homepage(request):
    return render(request, "main/homepage.html", {"reservas": Reserva.objects.all})

def create(request):
    if request.POST:
        form = CreateReserve(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = CreateReserve()


    return render(request, "main/create.html", {"form": form})

def read(request):
    reservas = Reserva.objects.all()
    viatura = Viatura.objects.all()
    lugar = Lugar.objects.all()
    return render(request, 'main/read.html', {'reservas': reservas, 'lugar' : lugar, 'viatura': viatura})
    

def delete(request, reserva_id):
    reserva = Reserva.objects.get(pk=reserva_id)
    if request.method == "POST":
        reserva.delete()
        return redirect("../read")
    return render(request, "main/delete.html", {'reserva': reserva})

def update(request, reserva_id):
    reserva = Reserva.objects.get(pk=reserva_id)
    form = CreateReserve(request.POST or None, instance=reserva)
    if form.is_valid():
        form.save()
        return redirect("../read")
    return render(request, 'main/update.html', {'reserva': reserva, 'form':form})

def createTable(request):
    if request.POST:
        form = CreateTable(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = CreateTable()

    return render(request, "main/create_table.html", {"form": form})

def readTable(request):
    tabelas = TabelaPrecos.objects.all()
    return render(request, 'main/read_table.html', {'tabelas': tabelas})

def deleteTable(request, tabela_id):
    tabela = TabelaPrecos.objects.get(pk=tabela_id)
    if request.method == "POST":
        tabela.delete()
        return redirect("../read_table")
    return render(request, "main/delete_table.html", {'tabela': tabela})

def updateTable(request, tabela_id):
    tabela = TabelaPrecos.objects.get(pk=tabela_id)
    form = UpdateTable(request.POST or None, instance=tabela)
    if form.is_valid():
        form.save()
        return redirect("../read_table")
    return render(request, 'main/update_table.html', {'tabela': tabela, 'form':form})




