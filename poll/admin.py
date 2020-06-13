from django.contrib import admin

from .models import Candidate
from .models import User
from .models import List_of_candidates

admin.site.register(Candidate)
admin.site.register(User)
admin.site.register(List_of_candidates)

