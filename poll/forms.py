from django.forms import ModelForm
from django import forms 

from .models import Candidate
from .models import User
from .models import List_of_candidates


class CreateCandidateForm(ModelForm):
    class Meta:
         model = Candidate
         fields = ['image', 'first_name', 'last_name', 'age', 'activiti', 'biography']

class CreateUserForm(ModelForm):
    class Meta:
         model = User 
         fields = ['first_name', 'last_name', 'age', 'mail_address','select_candidate']
         
class CreateListCandidate(ModelForm):
    class Meta:
         model = List_of_candidates
         fields = ['candidate_in_list', 'number_of_votes']

class UserData(forms.Form):
    user_firstName = forms.CharField(max_length=30)
    user_lastName = forms.CharField(max_length=30)
    user_mail = forms.CharField(max_length=100)
    user_age = forms.IntegerField()