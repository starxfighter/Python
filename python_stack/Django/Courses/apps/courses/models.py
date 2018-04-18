from __future__ import unicode_literals
from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['course_name']) < 5:
            errors['course_name'] = "Course name needs to be greater than 5 characters"
        return errors

class DescriptionManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['course_desc']) < 15:
            errors['course_desc'] = "Description needs to be greater than 15 characters"
        return errors

class Course(models.Model):
    name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()

class Description(models.Model):
    desc = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    course = models.OneToOneField(Course, on_delete = models.CASCADE)
    objects = DescriptionManager()


        