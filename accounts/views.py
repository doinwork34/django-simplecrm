from django.shortcuts import render, redirect
from django.db import connections, connection, models
from accounts.models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from accounts.forms import *
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.forms import modelform_factory
from django.http import HttpResponse, JsonResponse
from django.db.models import F


def home(request):
	return redirect ('/account/profile')

def register(request):
	if request.method=='POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/account') 
	else:
		form = UserCreationForm()

		args= {'form': form}
		return render(request, 'accounts/reg_form.html', args)

def view_profile(request):
	if request.method == 'POST':
		if 'recent_tickets' in request.POST and request.POST['recent_tickets']:
			techname = request.POST['recent_tickets']
			tickets = Servicetickets.objects.filter(technician=techname).order_by('-ticketstartdate')
			lib={'user':request.user,'tickets':tickets}
			return render (request, 'accounts/view_profile.html', lib)
	else:		
		args = {'user': request.user}
		return render(request, 'accounts/view_profile.html', args)

def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance = request.user)

		if form.is_valid():
			form.save()
			return redirect('/account/profile')
	else:
		form = EditProfileForm(instance=request.user)
		args= {'form':form}
		return render(request, 'accounts/edit_profile.html', args)



def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user = request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('/account/profile')
		else:
			return redirect('account/change-password')
	else:
		form = PasswordChangeForm(user=request.user)
		args= {'form':form}
		return render(request, 'accounts/change_password.html', args)



def client(request):
	if request.method == "POST":
		if 'q' in request.POST and request.POST['q']:
			q = request.POST['q']
			profile = Clientlist.objects.get(oid=q)
			contact = Contacts.objects.filter(clientid = q)
			 
			 
			lib= {'clientinfo':profile, 'contact':contact}
			return render(request, 'accounts/client_profile.html',lib)
		else:
			q = request.POST['tickets']
			tickets = Servicetickets.objects.filter(clientid=q).order_by("-timestamp")
			test = Clientlist.objects.get(oid=q)
			lib= {'tickets':tickets,
				  'name':test,
				  }

			return render(request, 'accounts/tickets.html',lib)
	elif request.method == "GET":
			if 'tech' in request.GET and request.GET['tech']:
				q = request.GET['tech']
				qset = Servicetickets.objects.filter(technician=q)
				lib = {'tickets': qset}
				return render(request, 'accounts/ticket-details.html', lib)
			else:
				query = Clientlist.objects.all().values()
				prnt = print(request)
				value = {'client': query}
				return render(request, 'accounts/client.html', value)

def tickets(request):
	if request.method == "GET":

		if 'cid' in request.GET and request.GET['cid']:
			q = request.GET['cid']
			tickets = Servicetickets.objects.filter(clientid=q)
			lib = {'tickets':tickets}
			return render(request, 'accounts/tickets.html', lib)
		elif 'tech' in request.GET and request.GET['tech']:
			q=request.GET['tech']
			tickets = Servicetickets.objects.filter(technician=q)
			lib = {'tickets':tickets}
			return render(request, 'accounts/tickets.html', lib)
		elif 'filter' in request.GET and request.GET['filter']:
			q = request.GET['filter']
			tickets = Servicetickets.objects.filter(ticket_status=1)
			lib={'tickets':tickets}
			return render(request, 'accounts/tickets.html')

		else:	
			tickets = Servicetickets.objects.all().order_by('-ticketstartdate')[:30]
			lib = {'tickets': tickets}
			return render(request, 'accounts/tickets.html', lib)


def ticket_detail(request):
	if request.method == "GET":
		if 'tdetails' in request.GET and request.GET['tdetails']:
			q= request.GET['tdetails']
			qset = Servicetickets.objects.get(oid=q)
			tset = Timeentries.objects.filter(ticketid = q)
			lib = {'tickets':qset, 'entries':tset}
			return render(request, 'accounts/ticket-details.html', lib)


def create_ticket(request):
	if request.method == "GET":
		ticket = NewTicketForm(request.GET)
		entries = NewTicketTimeEntries(request.GET)
		lib = {'ticket':ticket, 'entries':entries}
		return render(request, 'accounts/new-ticket.html', lib)
		
	if request.method == "POST":
		ticket = NewTicketForm(request.POST)
		entries = NewTicketTimeEntries(request.POST)
		subject = request.POST.get("ticket_title","")
		message = request.POST.get("notes","")
		from_email = request.POST.get("emailcomplete","")
		if ticket.is_valid() and entries.is_valid():
			m = ticket.save()
			entryintance = entries.instance
			k = m.timestamp
			ticket.save()
			v = Servicetickets.objects.get(timestamp = k)
			f = v.oid
			p = entryintance.ticketid
			entryintance.ticketid = f
			entries.save()
			
			send_mail(subject, message, from_email, ['admin@example.com'])

			return HttpResponse(entryintance.ticketid)


def edit_ticket(request):
	if request.method == "GET": 
		if 'editticket' in request.GET and request.GET['editticket']:
			req = request.GET['editticket']
			ticketreq = Servicetickets.objects.get(oid = req)
			timeentries = Timeentries.objects.filter(ticketid = req)
			lib = {"ticket":ticketreq, "timeentries":timeentries}
			return render(request, 'accounts/edit-ticket.html', lib)
			
def new_entry(request):
	if request.method == "GET":
		if 'editticket' in request.GET and request.GET['editticket']:
			req = request.GET['editticket']
			entry = NewTicketTimeEntries(request.GET)
			initialvalue = NewTicketTimeEntries(initial = {'ticketid':req})
			ticketreq = Servicetickets.objects.get(oid = req)
			timeentries = Timeentries.objects.filter(ticketid = req)
			lib = {'entries':entry, "tid":initialvalue, "ticket":ticketreq, "timeentries":timeentries}
			return render(request, 'accounts/new-entry.html', lib)
	if request.method == "POST":
		entry = NewTicketTimeEntries(request.POST)
		if entry.is_valid():
			s = entry.save()
			return HttpResponse('saved')
			
		

			
def test(request):
	if request.method == "GET":
		ticket = testticket(request.GET)
		lib = {'ticket':ticket}
		return render(request, 'accounts/create-ticket.html', lib)
	else:	
		ticket = testticket(request.POST)
		if ticket.is_valid():
			ticket.save()
			return HttpResponse('Save Successful')

from django.core import serializers
def ajax_req(request):
	if request.method == "GET":
		return HttpResponse('')
	if request.is_ajax():
		result = request.POST['clientid']
		q = Contacts.objects.filter(clientid = result)
		jsrz = serializers.serialize('json',q)
		return HttpResponse(jsrz, content_type = 'application/json')


from django.core.mail import send_mail, EmailMessage


def testEmail(request):
	if request.method == "GET":
		form = emailTest(request.GET)
		lib = {'form':form}
		return render(request, 'accounts/email.html', lib)
	else:	
		form = emailTest(request.POST)
		
		if form.is_valid():
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			from_email = form.cleaned_data['from_email']
			send_mail(subject, message, from_email, ['admin@example.com'])

