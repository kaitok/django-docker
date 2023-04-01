from django.shortcuts import render
from django.http import HttpResponse
from .forms import EventForm
from .models import Event


def createView(request):
    template_name = "event/index.html"
    form = EventForm(request.POST or None)
    ctx = {"form": form}
    if form.is_valid():
        title = form.cleaned_data["title"]
        text = form.cleaned_data["text"]
        start_datetime = form.cleaned_data["start_datetime"]
        end_datetime = form.cleaned_data["end_datetime"]
        mail = form.cleaned_data["mail"]
        tel_number = form.cleaned_data["tel_number"]
        obj = Event(
            title=title,
            text=text,
            start_datetime=start_datetime,
            end_datetime=end_datetime,
            mail=mail,
            tel_number=tel_number
        )
        obj.save()
    return render(request, template_name, ctx)
