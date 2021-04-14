from django.shortcuts import render, redirect
from .models import WorkoutPlan, Workout, Sets
from .forms import WorkoutPlanForm, WorkoutForm, ExerciseForm
import csv
from datetime import datetime


def index(request):
    plans = WorkoutPlan.objects.all()
    context = {'all_plans': plans}
    return render(request, 'workout/index.html', context)


def add_plan(request):
    form = WorkoutPlanForm()
    if request.method == 'POST':
        form = WorkoutPlanForm(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.status = 'Inactive'
            p.save()
            return redirect('plans')
    context = {'form': form}
    return render(request, 'workout/add_plan.html', context)


def make_active(request, pk):
    current = WorkoutPlan.objects.get(status='Active')
    new = WorkoutPlan.objects.get(id=pk)
    current.status = 'Inactive'
    new.status = 'Active'
    current.save()
    new.save()
    return redirect('plans')


def add_workout(request, pk):
    form = WorkoutForm()
    plan = WorkoutPlan.objects.get(id=pk)
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            w = form.save(commit=False)
            w.plan = plan
            w.save()
            return redirect('view_plan', pk)
    context = {'form': form}
    return render(request, 'workout/add_workout.html', context)


def view_plan(request, pk):
    plan = WorkoutPlan.objects.get(id=pk)
    all_workouts = Workout.objects.filter(plan=plan)
    context = {'plan': plan, 'all_workouts': all_workouts}
    return render(request, 'workout/view_plan.html', context)


def add_sets(request, pk):
    workout = Workout.objects.get(id=pk)
    form = ExerciseForm()
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            w = form.save(commit=False)
            w.workout = workout
            w.save()
            if request.POST.get('addnewafterthis') == 'on':
                return redirect('add_sets', pk)
            
            return redirect('view_plan', str(workout.plan.id))
    context = {'form': form}
    return render(request, 'workout/add_sets.html', context)


def play_workout(request, pk):
    workout = Workout.objects.get(id=pk)
    if request.method == 'POST':
        time_now = datetime.now()
        with open('workout_log.csv', 'a') as log_file:
            writer = csv.writer(log_file)
            for sub in request.POST:
                if sub != 'csrfmiddlewaretoken':
                    set_id = sub.split('-')[1]
                    print(set_id)
                    set = Sets.objects.get(id=set_id)
                    writer.writerow([str(set.exercise), f'{set.sets}x{set.reps_or_time}', time_now])
                    print(sub)
        return redirect('view_plan', str(workout.plan.id))
    context = {'workout': workout}
    return render(request, 'workout/play_workout.html', context)