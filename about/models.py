from django.db import models


class Courses(models.Model):
    course = models.TextField(max_length=100)
    by = models.TextField(max_length=100)
    date = models.TextField(max_length=100)

    def __str__(self):
        return self.course
    

class Experience(models.Model):
    role = models.TextField(max_length=100)
    company = models.TextField(max_length=100)
    type = models.TextField(max_length=100)
    period = models.TextField(max_length=100)
    location = models.TextField(max_length=100)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.company
    

class Projects(models.Model):
    name = models.TextField(max_length=100)
    at = models.TextField(max_length=100)
    period = models.TextField(max_length=100)
    role = models.TextField(max_length=100)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
    
    

class Testimonials(models.Model):
    by = models.TextField(max_length=100)
    role = models.TextField(max_length=100)
    description = models.TextField(max_length=5000)

    def __str__(self):
        return self.by
