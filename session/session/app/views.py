from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def create_session(request):
    request.session['sname'] = 'prachipanwar'
    request.session['semail'] = 'prachipanwar05@gmail.com'
    return HttpResponse("session is set")

def access_session(request):
    response = "<h1>Welcome to sessions</h1><br>"
    if request.session.get('sname'):
        response += "Name : {0} <br>".format(request.session.get('sname'))
    if request.session.get('semail'):
        response += "Email : {0} <br>".format(request.session.get('semail'))
        return HttpResponse(response)
    else:
        return HttpResponseRedirect('create/')
    # studentname = request.session['sname']
    # studentemail = request.session['semail']
    # return HttpResponse(studentname+" "+studentemail);

# # CREATING AND ACCESSING SESSIONS

# def create_session(request):
#     request.session['name'] = 'username'