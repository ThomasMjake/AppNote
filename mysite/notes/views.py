from django.shortcuts import render,redirect
from .models import Note
from django.utils.timezone import now
from .forms import NoteForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def notes_list(request):
    notes = Note.objects.all().order_by('-created_at')

    if request.method == 'POST':
        form =NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes_list')
    else:
        form = NoteForm()

    return render(request, 'notes/note_list.html', {
        'notes': notes,
        'timestamp': int(now().timestamp()),
        'form': form
    })

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return redirect('notes_list')

@login_required
def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes_list')
    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/edit_note.html', {
        'notes': note,
        'timestamp': int(now().timestamp()),
        'form': form
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})