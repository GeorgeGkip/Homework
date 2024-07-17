from django.db import models


class User(models.Model):
  user_dict = {
    "Tutor": "Tutor",
    "Student": "Student",
  }

  fname = models.CharField(max_length=100, blank=False, null=False)
  sname = models.CharField(max_length=100, blank=False, null=False)
  email = models.EmailField(max_length=254, blank=False, null=False)
  user_type = models.CharField(max_length=100, choice=user_dict)
  
  def __str__(self):
      return f"{self.fname} {self.sname}"
  
  class Meta:
        abstract = True

class Tutor(models.Model):
  
  subject_dict = {
    "Algebra": "Algebra",
    "Geometry": "Geometry",
    "Physics": "Physics",
    "Chemistry": "Chemistry",
  }
  
  user = models.ForeignKey(User, on_delete=CASCADE)
  subjects = models.CharField(max_length=100, choices=subject_dict)
  
  def __str__(self):
      return f"{self.fname} {self.sname}" 
  
  
class Student(User):
  
  user = models.ForeignKey(User, on_delete=CASCADE)
  
  def __str__(self):
      return f"{self.fname} {self.sname}" 
  
  