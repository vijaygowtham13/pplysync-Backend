# notes/urls.py
from django.urls import path
from .views import NoteListCreateView, NoteDetailView

urlpatterns = [
    path('', NoteListCreateView.as_view(), name='notes-list-create'),
    path('<uuid:note_id>/', NoteDetailView.as_view(), name='note-detail'),
]
