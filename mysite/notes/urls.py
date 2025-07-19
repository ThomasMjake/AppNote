from django.urls import path
from . import views

urlpatterns = [
    path('',views.notes_list,name='notes_list'),
    path('delete/<int:note_id>', views.delete_note, name='delete_note'),
    path('edit/<int:note_id>', views.edit_note, name='edit_note'),
    path('register/', views.register, name='register'),
]
