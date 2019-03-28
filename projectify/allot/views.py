from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse

from django.utils import timezone

from .models import Student,Mentor,Notifications

def index(request):
	student_list=Student.objects.all()
	notification_list=Notifications.objects.all()
	print(notification_list)
	context={"student_list":student_list,"notification_list":notification_list}
	return render(request,"allot/student.html",context)

def maintain(request):
	return render(request,"allot/maintain.html")


def addmentor(request):
	name=request.POST['name']
	count=request.POST['count']
	mentor = Mentor(mentor_name=name,mentor_project_count=count)
	mentor.save()
	return redirect("maintain")

def notifyleaders(request):
	count=int(request.POST['count'])
	leaders = Student.objects.order_by('-student_cpi')
	for l in range(count):
		ld=leaders[l]
		ld.project_id=leaders[l].id
		ld.save()
		print(leaders[l])
		n = Notifications(student_id=leaders[l].id,notify=1,time=timezone.now())
		n.save()
	return redirect("maintain")