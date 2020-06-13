from django.db import models

class Candidate(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to = 'media/')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    activiti = models.TextField()
    biography = models.TextField()

class List_of_candidates(models.Model):
    candidate_in_list = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    number_of_votes = models.IntegerField(default=0)

class User(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    mail_address = models.CharField(max_length=100)
    select_candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
