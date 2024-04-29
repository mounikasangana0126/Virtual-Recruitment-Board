from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from hr.models import JobPost , CandidateApplications , Hr
from candidate.models import MyApplyJobList
# Create your views here.

@login_required
def candidateHome(request):
    if Hr.objects.filter(user=request.user).exists():
        return redirect('hrdash')
    jobpost = JobPost.objects.all()
    return render(request,'candidate/dashboard.html',{'jobpost':jobpost})

@login_required
def applyJob(request,pk):
    if Hr.objects.filter(user=request.user).exists():
        return redirect('hrdash')
    if JobPost.objects.filter(id=pk).exists():
        job = JobPost.objects.get(id=pk)
        if CandidateApplications.objects.filter(user=request.user,job=job).exists():
            return redirect('dash')
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            college = request.POST.get('college')
            passing_year = request.POST.get('passing_year')
            yearOfExperience = request.POST.get('yearOfExperience')
            resume = request.FILES.get('resume')
            # if CandidateApplications.objects.filter(user=request.user,job=job).exists():
            #     return redirect('dash')
            candidate_application=CandidateApplications(user=request.user,job=job,passingYear=passing_year,yearOfExperience=yearOfExperience,resume=resume)
            candidate_application.save()
            MyApplyJobList(user=request.user,job=candidate_application).save()
            job.applyCount+=1
            job.save()
            return redirect('dash')
    return render(request,'candidate/apply.html')

@login_required
def myjoblist(request):
    if Hr.objects.filter(user=request.user).exists():
        return rediresc('hrdash')
    joblist = MyApplyJobList.objects.filter(user=request.user)
    return render(request,'candidate/myjoblist.html',{'joblist':joblist})

