from .models import WorkoutPlan,  Workout, Sets
from django import forms


class WorkoutPlanForm(forms.ModelForm):
    class Meta:
        model = WorkoutPlan
        fields = ['name', 'type', 'days']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of plan'}),
            'type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type'}),
            'days': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Days / Week'}),
        }


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'target']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Workout Name'}),
            'target': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Target Muscles'}),
        }


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Sets
        fields = ['exercise', 'reps_or_time', 'sets']
        widgets = {
            'exercise': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Exercise'}),
            'reps_or_time': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Reps/Time'}),
            'sets': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sets'}),
        }