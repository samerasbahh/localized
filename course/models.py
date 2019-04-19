from django.db import models
from multiselectfield import MultiSelectField


class Time(models.Model):

    # Period Name
    period = models.CharField(max_length=32)
    start_time = models.time

    def __str__(self):
        return ' %s' % (self.period)


class Professor(models.Model):

    # Professor First name
    first_name = models.CharField(max_length=225)

    # Professor Last Name
    last_name = models.CharField(max_length=225)

    # Professor Email
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Course(models.Model):

    # Course Title
    title = models.CharField(max_length=255, null=False)

    # Course Description
    description = models.CharField(max_length=255)  # The tasks description is limited to 255 characters

    # Course Times many to many relation ship
    time = models.ManyToManyField(Time)

    # Name of the professor
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='professor')



