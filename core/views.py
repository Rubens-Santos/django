from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Servico, Funcionario, Recurso
from .forms import ContatoForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all() #Order_by é para toda vez que carregar a paginas trazer os produtos em outra ordem
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['recursosRight'] = Recurso.objects.filter(id__lte=Recurso.objects.count()/2).order_by('?')
        context['recursosLeft'] = Recurso.objects.filter(id__gt=Recurso.objects.count() / 2).order_by('?')
        context['recursos'] = Recurso.objects.order_by('?').all()

        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar o formulario')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)

