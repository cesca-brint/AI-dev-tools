from django.forms import ModelForm
from .models import Assignment, Chore

class AssignmentForm(ModelForm):
       class Meta:
           model = Assignment
           fields = ['completed_date']

class ChoreForm(ModelForm):
    class Meta:
        model = Chore
        fields = ['name', 'description', 'points', 'type']