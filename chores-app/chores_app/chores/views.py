from django.shortcuts import render, get_object_or_404, redirect
from .models import Assignment, FamilyMember
from .forms_chores import AssignmentForm, ChoreForm

def home(request):
    return render(request, 'chores/home.html')

def chores_list(request):
    return render(request, 'chores/chores_list.html')

def calendar(request):
    return render(request, 'chores/calendar.html')

def settings(request):
    return render(request, 'chores/settings.html')

def leaderboard(request):
    return render(request, 'chores/leaderboard.html')

def add_chore(request):
       if request.method == 'POST':
           form = ChoreForm(request.POST)
           if form.is_valid():
               form.save()
               return redirect('chores_list')
       else:
           form = ChoreForm()
       return render(request, 'chores/add_chore.html', {'form': form})

def update_reminders(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    if request.method == 'POST':
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            return redirect('chores_list')
    else:
        form = AssignmentForm(instance=assignment)
    return render(request, 'chores/update_reminders.html', {'form': form})

def chores_list(request):
       assignments = Assignment.objects.all()
       if request.method == 'POST':
           form = AssignmentForm(request.POST)
           if form.is_valid():
               form.save()
               return redirect('chores_list')
       else:
           form = AssignmentForm()
       return render(request, 'chores/chores_list.html', {'assignments': assignments, 'form': form})

def settings(request):
    assignment = Assignment.objects.first()
    family_members = FamilyMember.objects.all()
    
    return render(request, 'chores/settings.html', {
        'assignment': assignment,
        'family_members': family_members,
    })
