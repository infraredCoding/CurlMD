from django.shortcuts import render
from workout.models import WorkoutPlan


def index(request):
    active_plan = WorkoutPlan.objects.get(status='Active')
    context = {'plan': active_plan}
    return render(request, 'landing/index.html', context)
