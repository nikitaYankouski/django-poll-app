from django.shortcuts import render

from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse

from .forms import CreateCandidateForm
from .forms import CreateUserForm
from .forms import UserData
from .forms import List_of_candidates

from .models import Candidate
from .models import User
from .models import List_of_candidates

from django.contrib import messages


def home(request):
    listCand = List_of_candidates.objects.all()

    context = {
        'listCand' : listCand
    }
    return render(request, 'home.html', context)

def error(request, text):
    context = {
        'text': text
    }
    return render(request, 'error.html', context)

def create(request):
    candidates = Candidate.objects.all()

    if request.method == 'POST':
        form = CreateCandidateForm(request.POST, request.FILES)

        for cand in candidates:
            if cand.first_name == request.POST.get('first_name') and cand.last_name == request.POST.get('last_name'):
                return error(request, 'Already that candidate exists') 

        candBuf = Candidate(
                image = request.FILES['image'],
                first_name = request.POST.get('first_name'),
                last_name = request.POST.get('last_name'),
                age = request.POST.get('age'),
                activiti = request.POST.get('activiti'),
                biography = request.POST.get('biography'))

        if form.is_valid():
            candBuf.save()
            listCandidate = List_of_candidates(candidate_in_list = candBuf, number_of_votes = 0)
            listCandidate.save()
            messages.add_message(request, messages.INFO, 'Hello world.')
            return HttpResponseRedirect(reverse('home'))
    else:
        form = CreateCandidateForm()

    context = {
        'form' : form
    }
    return render(request, 'create.html', context)

def results(request):
    listCand = List_of_candidates.objects.all()

    context = {
        'listCand' : listCand
    }
    return render(request, 'results.html', context)

def vote(request):
    candidates = Candidate.objects.all()
    listCandidates = List_of_candidates.objects.all()
    form = CreateUserForm(request.POST)

    if request.method == 'POST':
        for can in candidates:
            if (can.auto_increment_id == int(request.POST['poll'])):
                user = User(first_name = request.session['first_name'], 
                            last_name = request.session['last_name'], 
                            age = request.session['age'], 
                            mail_address = request.session['mail'],
                            select_candidate = can)
                user.save()

                for listcan in listCandidates:
                    if (listcan.candidate_in_list == can):
                        listcan.number_of_votes += 1
                        listcan.save()

                to_user = request.session['mail']
                text = 'Dziekuje za glosowanie ' + request.session['first_name'] + ' ' + request.session['last_name']
                send_mail('Powiadomienie', text, 'systemForVote@mail.pl', [to_user])
                return HttpResponseRedirect(reverse('home'))
    else:
        form = CreateUserForm()
    
    context = {
        'form' : form,
        'candidates' : candidates
    }
    return render(request, 'vote.html', context)

def userdata(request):
    users = User.objects.all()

    if request.method == 'POST':
        form = UserData(request.POST)

        for us in users:
                if us.first_name == request.POST.get('user_firstName') and us.last_name == request.POST.get('user_lastName'):
                    return error(request, "Already that user exists") 

        if form.is_valid():
            request.session['first_name'] = form.cleaned_data['user_firstName']
            request.session['last_name'] = form.cleaned_data['user_lastName']
            request.session['age'] = form.cleaned_data['user_age']
            request.session['mail'] = form.cleaned_data['user_mail']
            return HttpResponseRedirect(reverse('vote'))
    else:
        form = UserData()

    context = {
        'form' : form
    }
    return render(request, 'userdata.html', context)