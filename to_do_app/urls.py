from django.urls import path

from . import views

urlpatterns = [
    path('', views.CreateTaskManagerView.as_view(), name="index"),
    path('edit/<int:pk>', views.TaskModelUpdateView.as_view(), name="edit"),
    path('delete/<int:pk>', views.TaskModelDeleteView.as_view(), name="delete"),
    path('search-page', views.SearchPageView.as_view(), name="search-page"),
]
