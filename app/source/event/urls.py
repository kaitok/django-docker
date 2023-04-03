from django.urls import path
from . import views
app_name = "event"
urlpatterns = [
    path("", views.IndexView.as_view(), name="event-index"),
    path("create/", views.CreateView.as_view(), name="event-create"),
]
