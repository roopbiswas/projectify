from django.db import models

class Mentor(models.Model):
	mentor_name = models.CharField(max_length=50)
	mentor_gender = models.CharField(max_length=1,default='m')
	mentor_hostel = models.IntegerField(default=0)
	mentor_proficiency  = models.CharField(blank=True,null=False,max_length=255)
	mentor_description = models.CharField(max_length=250)
	mentor_project_count = models.IntegerField(default=0)
	mentor_major_projects = models.TextField(blank=True,null=True)
	mentor_cpi = models.DecimalField(decimal_places=2,max_digits=3,default=0.00)

	#def __str__(self):
	#	return self.mentor_name


class Student(models.Model):
	mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
	student_name = models.CharField(max_length=50)
	student_gender = models.CharField(max_length=1,default='m')
	student_hostel = models.IntegerField(default=0)
	student_proficiency  = models.CharField(blank=True,null=False,max_length=255)
	student_description = models.CharField(max_length=250)
	student_major_projects = models.TextField(blank=True,null=True)
	project_id = models.IntegerField(default=0)
	group_id = models.IntegerField()

	#def __str__(self):
	#	return self.student_name
						