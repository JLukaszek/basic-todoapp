from django.views.generic import (
    ListView, UpdateView, DeleteView, CreateView,
)
from django.urls import reverse_lazy
from .models import Schedules


class HomePageView(ListView):
    model = Schedules
    template_name = 'todo/home.html'


class EditPageView(UpdateView):
    model = Schedules
    fields = [
        'title',
    ]
    template_name = 'todo/schedule_edit.html'


class DeletePageView(DeleteView):
    model = Schedules
    success_url = reverse_lazy('home')
    template_name = 'todo/schedule_delete.html'


class CreatePageView(CreateView):
    model = Schedules
    fields = [
        'title',
    ]
    template_name = 'todo/schedule_new.html'
