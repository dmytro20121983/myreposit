from django.shortcuts import render


from  django.urls import reverse_lazy
from .form import BbForm, PiopleForm

from .models import Bb, Rubric, Piople

from django.views.generic.edit import CreateView
#--------------------------------------------------------------------

def index(request):
    bbs = Bb.objects.all()
    rubrics=Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics' : rubrics}
    return render (request, 'bboard/index.html', context)

def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter (rubric=rubric_id)
    rubrics = Rubric.objects.all()
    context = {'bbs' : bbs, 'rubrics' : rubrics}
    curent_rubric = Rubric.objects.get(pk = rubric_id)
    context= {'bbs' : bbs, 'rubrics':rubrics, 'curent_rubric' : curent_rubric}
    return render(request, 'bboard/by_rubric.html', context)

class BbCreateView (CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy = '/bboard/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['rubrics'] = Rubric.objects.all()

        return context

def piples (request):
    piple = Piople.objects.all()
    pipless = {'piple' : piple}

    return render(request, 'bboard/password.html', pipless)

class PiopleCreateView (CreateView):
    template_name = 'bboard/password.html'
    form_class = PiopleForm
    success_url = reverse_lazy = '/bboard/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = Piople.objects.all()

        return context
