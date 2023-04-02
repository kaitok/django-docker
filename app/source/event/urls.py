from django.urls import path
from . import views
app_name = "event"
urlpatterns = [
    path("", views.indexView, name="event-index"),
    path("create/", views.createView, name="event-create"),
]
