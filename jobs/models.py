from django.db import models
from django.conf import settings
class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.CharField(max_length=100, blank=True)
    posted_date = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='posted_jobs')
    def __str__(self):
        return self.title
class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applications')
    applied_date = models.DateTimeField(auto_now_add=True)
    cover_letter = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    class Meta:
        unique_together = ('job', 'applicant')
    def __str__(self):
        return f"{self.applicant.username} -> {self.job.title}"