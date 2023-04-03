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
    success_url = reverse_lazy('event:event-index')

    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.save()
        return super().form_valid(form)


def updateView(request, pk):
    template_name = "event/create.html"
    obj = Event.objects.get(pk=pk)
    initial_values = {
        "title": obj.title,
        "text": obj.text,
        "start_datetime": obj.start_datetime,
        "end_datetime": obj.end_datetime,
        "mail": obj.mail,
        "tel_number": obj.tel_number,
    }
    form = EventForm(request.Post or initial_values)
    ctx = {"form": form}
    if form.is_valid():
        obj.title = form.cleaned_data["title"],
        obj.text = form.cleaned_data["text"],
        obj.start_datetime = form.cleaned_data["start_datetime"],
        obj.end_datetime = form.cleaned_data["end_datetime"],
        obj.mail = form.cleaned_data["mail"],
        obj.tel_number = form.cleaned_data["tel_numbe"]
        obj.save()

    return render(request, template_name, ctx)
