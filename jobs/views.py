from django.shortcuts import render, get_object_or_404
from .models import Job, JobApplication


def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})


def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        resume = request.FILES.get("resume")

        JobApplication.objects.create(
            job=job,
            applicant_name=name,
            email=email,
            resume=resume
        )

        return render(request, 'jobs/success.html')

    return render(request, 'jobs/apply_job.html', {'job': job})