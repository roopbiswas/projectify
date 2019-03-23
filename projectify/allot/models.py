from django.db import models

class Mentor(models.Model):
	mentor_name = models.CharField(max_length=50)
	mentor_description = models.CharField(max_length=250)
	project_count = models.IntegerField(default=0)

	def __str__(self):
		return self.mentor_name


class Student(models.Model):
	mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
	student_name = models.CharField(max_length=50)
	student_description = models.CharField(max_length=250)
	project_id = models.IntegerField(default=0)
	group_id = models.IntegerField()

	def __str__(self):
		return self.student_name
						