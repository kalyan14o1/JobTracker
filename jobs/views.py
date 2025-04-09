from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import Job, UserProfile
from .forms import JobForm
from job_utils.status_manager import JobStatusManager

def root_redirect(request):
    if request.user.is_authenticated:
        return redirect('jobs:index')  
    return redirect('login')  

def index(request):
    jobs = Job.objects.order_by('-created_at')
    return render(request, 'jobs/index.html', {'jobs': jobs})

def show(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)
        manager = JobStatusManager(job)
        history = manager.get_status_history()
    except Job.DoesNotExist:
        raise Http404("Job does not exist")
    return render(request, 'jobs/show.html', {'job': job, 'history': history})

def create(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jobs:index')
    else:
        form = JobForm()
    return render(request, 'jobs/form.html', {'form': form})

def update(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            manager = JobStatusManager(job)
            manager.update_status(form.cleaned_data['status'])
            return redirect('jobs:index')
    else:
        form = JobForm(instance=job)
    return render(request, 'jobs/form.html', {'form': form})

def delete(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if request.method == 'POST':
        job.delete()
        return redirect('jobs:index')
    return render(request, 'jobs/confirm_delete.html', {'job': job})

@login_required
def profile(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(
            user=request.user,
            name=request.user.username,
            email=request.user.email or 'x23419491@student.ncirl.ie',
            phone_number='08994433723'
        )
    return render(request, 'jobs/profile.html', {'profile': profile})