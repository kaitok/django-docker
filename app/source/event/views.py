from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import EventForm
from .models import Event


class IndexView(ListView):
    model = Event
    template_name = "event/index.html"
    paginate_by = 5


class CreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = "event/create.html"
    success_url = reverse_lazy('event:index')

    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.save()
        return super().form_valid(form)


class UpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = "event/update.html"
    success_url = reverse_lazy('event:index')

    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.save()
        return super().form_valid(form)


class DeleteView(DeleteView):
    model = Event
    success_url = reverse_lazy('event:index')
