from django.urls import path
from . import views

urlpatterns = [
   path('', views.index),
   path('<int:id>', views.book),
   path('create', views.create),
   path('delete/<int:id>', views.delete),
   path('update/<int:id>', views.update),
   path("generic/<int:pk>", views.RUDBook.as_view()),
]