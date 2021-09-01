import datetime

from django.db.models import Q
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import CalendarForm, TaskModelForm
from .models import TaskModel


# Create Task
class CreateTaskManagerView(CreateView):
    model = TaskModel
    form_class = TaskModelForm
    template_name = "to_do_app/index.html"
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        curr_date = datetime.date.today()
        context['tasks'] = self.model.objects.order_by('-date').filter(Q(date__startswith=curr_date)|Q(date__gte=curr_date))
        context['button_name'] = 'Add'
        return context

#Edit Task
class TaskModelUpdateView(UpdateView):
    model = TaskModel
    form_class = TaskModelForm

    template_name = "to_do_app/edit-page.html"
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button_name'] = "Save"
        return context

#Delete Task
class TaskModelDeleteView(DeleteView):
    model = TaskModel
    template_name = "to_do_app/delete-page.html"
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button_name'] = 'Delete'
        return context

#Search
class SearchPageView(View):
    def get(self, request):
        return render(request, "to_do_app/search-page.html", {
            "form" : CalendarForm,
            "button_name" : "Search"
        })

    def post(self, request):
        date = CalendarForm(self.request.POST).data.get('date')
        task_obj = TaskModel.objects.filter(date__startswith=date)

        return render(request, "to_do_app/search-page.html", {
            "form" : CalendarForm,
            "tasks" : task_obj,
            "button_name" : "Search"
        })
