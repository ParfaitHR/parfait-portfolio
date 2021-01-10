from django.db import models

# Create your models here.
class Job(models.Model):

    STATUS = (
        ('Accepting CVs', 'Accepting CVs'),
        ('Interviewing', 'Interviewing'),
        ('Vacancy Filled', 'Vacancy Filled'),
    )

    ROLE = (
        ('Permanent','Permanent'),        
        ('Temporary','Temporary'),
    )

    job_title = models.CharField(max_length=30, null=True)
    company_name = models.CharField(max_length=30, null=True)
    role = models.CharField(max_length=30, null=True, choices=ROLE)
    salary = models.CharField(max_length=30, null=True)
    location = models.CharField(max_length=30, null=True)
    experience = models.IntegerField(null=True)
    jd = models.CharField(max_length=30, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return (self.job_title + ' | ' + self.company_name)
