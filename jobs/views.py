from django.shortcuts import render, get_object_or_404
from .models import JobPost


# Create your views here.
def index(request):
    active_jobs = JobPost.objects.filter(is_active=True)
    context = {
        "job_postings": active_jobs
    }
    return render(request, 'job_board/index.html', context)

def job_detail(request, id):
    job = get_object_or_404(JobPost, pk = id, is_active = True)
    context = {
        "job": job
    }
    return render(request, 'job_board/details.html', context)