from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import BbForm
from .models import Bb, Rubric


def index(requst):
    bbs = Bb.objects.order_by("-published")
    rubrics = Rubric.objects.all()
    context = {"bbs": bbs, "rubrics": rubrics}
    print({"bbs": bbs, "rubrics": rubrics})
    return render(requst, 'index.html', context)


def by_rubric(requst, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {"bbs": bbs, "rubrics": rubrics,
               "current_rubric": current_rubric}
    return render(requst, 'by_rubric.html', context)


class BbCreateView(CreateView):
    template_name = "create.html"
    form_class = BbForm
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rubrics"] = Rubric.objects.all()
        return context