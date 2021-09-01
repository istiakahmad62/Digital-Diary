from django import forms

from .models import TaskModel


class DateTimeInputTemplate(forms.DateTimeInput):
    input_type = 'datetime-local'

class DateInputTemplate(forms.DateInput):
    input_type = 'date'

class TaskModelForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = "__all__"
        widgets = {
            "date" : DateTimeInputTemplate,
        }

        labels = {
            "title" : "Your Task",
            "date" : "Choose Date"
        }


class CalendarForm(forms.Form):
    date = forms.DateTimeField(
        label = 'Search Date',
        widget = DateInputTemplate,
    )
