from django.shortcuts import render, HttpResponseRedirect
from .forms import Workout
from .models import Workoutmodel
# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = Workout(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['workout_type']
            em = fm.cleaned_data['duration']
            pw = fm.cleaned_data['notes']
            dt = fm.cleaned_data['date']
            reg = Workoutmodel(workout_type=nm, duration=em, notes=pw, date=dt)
            reg.save()
            fm = Workout()
            
    else:
        fm = Workout()
    wk = Workoutmodel.objects.all()

    return render(request, 'enroll/addandshow.html',{'form':fm, 'workout':wk})

def delete_data(request,id):
    if request.method == 'POST':
        pi = Workoutmodel.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    
def update_data(request, id):
    if request.method == 'POST':
        pi= Workoutmodel.objects.get(pk=id)
        fm= Workout(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi= Workoutmodel.objects.get(pk=id)
        fm= Workout(instance=pi)

    return render(request, 'enroll/update.html', {'form':fm} )