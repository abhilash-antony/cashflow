# expenses/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("add/", views.add_expense, name="add_expense"),
    path("edit/<str:expense_id>/", views.edit_expense, name="edit_expense"),
    path("delete/<str:expense_id>/", views.delete_expense, name="delete_expense"),
    path("list/", views.expense_list, name="expense_list"),
    path('deleted/', views.deleted_expenses, name='recently_deleted'),
    path('deleted/delete_all/', views.delete_all_deleted_expenses, name='delete_all_deleted'),
    path('reports/', views.reports, name='reports'), 
    path('restore/<int:expense_id>/', views.restore_expense, name='restore_expense'),
]
