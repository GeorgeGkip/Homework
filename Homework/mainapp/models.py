from django.db import models


class Tutor(models.Model):
  
  subject_dict = {
    "Algebra": "Algebra",
    "Geometry": "Geometry",
    "Physics": "Physics",
    "Chemistry": "Chemistry",
  }

  fname = models.CharField(max_length=100, blank=False, null=False)
  sname = models.CharField(max_length=100, blank=False, null=False)
  email = models.EmailField(max_length=254, blank=False, null=False)
  subjects = models.Charfield(max_length=1, choices=subject_dict)
  
  def __str__(self):
      return f"{self.fname} {self.sname}" 
  
  
class Student(models.Model):
  
  fname = models.CharField(max_length=100, blank=False, null=False)
  sname = models.CharField(max_length=100, blank=False, null=False)
  email = models.EmailField(max_length=254, blank=False, null=False)
  
  def __str__(self):
      return f"{self.fname} {self.sname}" 
  
  