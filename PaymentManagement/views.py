from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django_tables2 import MultiTableMixin, SingleTableMixin, SingleTableView
from django.views.generic import ListView
from .forms import ContratoForm
from .models import Cliente, Contrato, Dia, Lugar, Parque, Periodicidade
from .tables import ContratosTable
from django_filters.views import FilterView
from .filters import ContratosFilter
from django.db.models import F
from django.template import loader


# Create your views here.

# def cliente_create_view(request):
#     form = ClienteForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ClienteForm()
#     context ={
#         'form': form,
#     }
#     return render(request, "tables/create.html", context)

# def cliente_update_view(request, id):
#     obj=get_object_or_404(Cliente, id=id)
#     form = ClienteForm(request.POST or None, instance=obj)
#     if form.is_valid():
#         form.save()
#     context ={
#         'form': form,
#     }
#     return render(request, "tables/create.html", context)

# def cliente_list_view(request):
#     queryset = Cliente.objects.all()
#     context ={
#         'object_list': queryset,
#     }
#     return render(request, "tables/list.html", context)

# def cliente_detail_view(request, id):
#     obj=get_object_or_404(Cliente, id=id)
#     context ={
#         'object': obj,
#     }
#     return render(request, "tables/detail.html", context)

# def cliente_delete_view(request, id):
#     obj=get_object_or_404(Cliente, id=id)
#     if request.method == "POST":
#         obj.delete()
#         return redirect('../../')
#     context ={
#         "object": obj,
#     }
#     return render(request, "tables/delete.html", context)


# def contrato_create_view(request):
#     form = ContratoForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ContratoForm()
#     context ={
#         'form': form,
#     }
#     return render(request, "tables/create.html", context)

# def contrato_update_view(request, id):
#     obj=get_object_or_404(Contrato, id=id)
#     form = ContratoForm(request.POST or None, instance=obj)
#     if form.is_valid():
#         form.save()
#     context ={
#         'form': form,
#     }
#     return render(request, "tables/create.html", context)

# def contrato_detail_view(request, id):
#     obj=get_object_or_404(Contrato, id=id)
#     context ={
#         'object': obj,
#     }
#     return render(request, "tables/detail.html", context)

# def contrato_delete_view(request, id):
#     obj=get_object_or_404(Contrato, id=id)
#     if request.method == "POST":
#         obj.delete()
#         return redirect('../../')
#     context ={
#         "object": obj,
#     }
#     return render(request, "tables/delete.html", context)

# class consultar_contratos(SingleTableMixin, FilterView):
#     table_class = ContratosTable
#     template_name = 'list.html'
#     filterset_class = ContratosFilter
#     table_pagination = {
#         'per_page': 10
#     }
#     queryset = Contrato.objects.annotate(nome=F("clienteid__nome"), parque=F("parqueid__nome"))

# def contratos_list(request):
#     contratos = Contrato.objects.all()
#     for contrato in contratos:
#         contrato.nome_parque = contrato.parqueid.nome
#         contrato.nome_cliente = contrato.clienteid.nome
#         contrato.periodicidade = contrato.periodicidadeid.periodicidade
#     template = loader.get_template('contratos.html')
#     context={
#         'contratos': contratos
#     }

#     return HttpResponse(template.render(context, request))

class contratos_list(SingleTableMixin, FilterView):
    table_class = ContratosTable
    template_name = 'contratos.html'
    filterset_class = ContratosFilter
    table_pagination = {
        'per_page': 10
    }

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SingleTableMixin, self).get_context_data(**kwargs)
        table = self.get_table(**self.get_table_kwargs())
        context[self.get_context_table_name(table)] = table
        return context
    

def contrato_detail_view(request, id):
    contrato=Contrato.objects.get(id=id)
    lugares=Lugar.objects.filter(contratoid=contrato)
    dias=Dia.objects.filter(periodicidadeid=contrato.periodicidadeid)
    template = loader.get_template('detail.html')
    context ={
        'contrato': contrato,
        'lugares':lugares,
        'dias':dias,
    }
    return HttpResponse(template.render(context, request))


def contrato_delete_view(request, id):
    contrato=Contrato.objects.get(id=id)
    if request.POST:
        contrato.delete()
        return redirect('../../')
    template = loader.get_template('delete.html')
    context ={
        "contrato": contrato,
    }
    return HttpResponse(template.render(context, request))

def contrato_create_view(request):
    if request.method=='POST':
        form = ContratoForm(request.POST, current_user=Cliente.objects.get(id=1))
        if form.is_valid():
            form.save()
            return redirect('../')
    else:
        form = ContratoForm(current_user=Cliente.objects.get(id=1))
    context ={
        'form': form,
    }
    return render(request, "create.html", context)

def contrato_update_view(request, id):
    obj=get_object_or_404(Contrato, id=id)
    form = ContratoForm(request.POST or None, current_user=Cliente.objects.get(id=1), instance=obj)
    if form.is_valid():
        form.save(id)
    context ={
        'form': form,
    }
    return render(request, "create.html", context)
