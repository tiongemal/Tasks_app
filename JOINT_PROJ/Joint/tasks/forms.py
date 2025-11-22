from django import forms
import string
class NewTaskForm(forms.Form):
    task = forms.CharField(max_length=30,)
    priority = forms.IntegerField(min_value=1, max_value=10, required=False, label='Priority')
    completed = forms.BooleanField(initial=False, required=False, label='completed', widget=forms.CheckboxInput(attrs={'class':'task-check-input'}) )

    def clean_task(self):
        task = self.cleaned_data['task']
        if any(char in string.punctuation for char in task):
            raise forms.ValidationError("Task cannot contain punctuation.")

        return task

