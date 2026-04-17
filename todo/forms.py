from django import forms 
from todo.models import Task

class TaskForm(forms.ModelForm):
    class Meta :
        model = Task 
        fields = ['title','complete','description']
        widgets = {
            "title":forms.TextInput(attrs={"placeholder":"Enter task title"}),
            "complete":forms.CheckboxInput(),
            "description":forms.Textarea(attrs={"placeholder":"Enter title description"}),
            
        }
