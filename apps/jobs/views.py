from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Job, Application
from .forms import JobForm, ApplicationForm
def job_list(request):
    jobs = Job.objects.all().order_by('-posted_date')
    query = request.GET.get('q')
    if query:
        jobs = jobs.filter(title__icontains=query)
    return render(request, 'jobs/job_list.html', {'jobs': jobs, 'query': query or ''})
def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    already_applied = False
    if request.user.is_authenticated:
        already_applied = Application.objects.filter(job=job, applicant=request.user).exists()
    return render(request, 'jobs/job_detail.html', {'job': job, 'already_applied': already_applied})
@login_required
def job_create(request):
    if request.user.role != 'employer':
        messages.error(request, "Only employers can post jobs.")
        return redirect('job_list')
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user
            job.save()
            messages.success(request, 'Job posted successfully!')
            return redirect('job_list')
    else:
        form = JobForm()
    return render(request, 'jobs/job_form.html', {'form': form, 'title': 'Post a New Job'})
@login_required
def job_update(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if job.posted_by != request.user:
        messages.error(request, "You can only edit jobs you posted.")
        return redirect('job_detail', pk=job.pk)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job updated successfully!')
            return redirect('job_detail', pk=job.pk)
    else:
        form = JobForm(instance=job)
    return render(request, 'jobs/job_form.html', {'form': form, 'title': 'Edit Job'})
@login_required
def job_delete(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if job.posted_by != request.user:
        messages.error(request, "You can only delete jobs you posted.")
        return redirect('job_detail', pk=job.pk)
    if request.method == 'POST':
        job.delete()
        messages.success(request, 'Job deleted successfully!')
        return redirect('job_list')
    return render(request, 'jobs/job_delete.html', {'job': job})
@login_required
def apply_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.user.role != 'seeker':
        messages.error(request, "Only job seekers can apply for jobs.")
        return redirect('job_detail', pk=job.pk)
    already_applied = Application.objects.filter(job=job, applicant=request.user).exists()
    if already_applied:
        messages.error(request, "You have already applied for this job.")
        return redirect('job_detail', pk=job.pk)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user
            application.save()
            messages.success(request, "Application submitted successfully!")
            return redirect('job_detail', pk=job.pk)
    else:
        form = ApplicationForm()
    return render(request, 'jobs/apply_job.html', {'form': form, 'job': job})
@login_required
def my_jobs(request):
    if request.user.role != 'employer':
        messages.error(request, "Only employers can view this page.")
        return redirect('job_list')
    jobs = Job.objects.filter(posted_by=request.user).order_by('-posted_date')
    return render(request, 'jobs/my_jobs.html', {'jobs': jobs})
@login_required
def my_applications(request):
    if request.user.role != 'seeker':
        messages.error(request, "Only job seekers can view this page.")
        return redirect('job_list')
    applications = Application.objects.filter(applicant=request.user).order_by('-applied_date')
    return render(request, 'jobs/my_applications.html', {'applications': applications})
@login_required
def job_applications(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.user != job.posted_by:
        messages.error(request, "You can only view applications for your own jobs.")
        return redirect('my_jobs')
    applications = Application.objects.filter(job=job).order_by('-applied_date')
    return render(request, 'jobs/job_applications.html', {
        'job': job,
        'applications': applications
    })