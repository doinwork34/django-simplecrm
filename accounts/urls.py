from django.conf.urls import url 
from . import views
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.urls import reverse
urlpatterns = [
	url(r'^$', views.home),
	url(r'^login/$', login, {'template_name':'accounts/login.html'}, name = 'login'),
	url(r'^logout/$', logout, {'template_name':"accounts/logout.html"}, name = 'logout'),
	url(r'^register/$', views.register, name='register'),
	url(r'^profile/$', views.view_profile, name='view_profile'),
	url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
	url(r'^change-password/$', views.change_password, name='change_password'),
	url(r'^reset-password/$', password_reset, {'template_name': 'accounts/reset_password.html',
	'post_reset_redirect': 'accounts:password_reset_done', 'email_template_name':'accounts/reset_password_email.html'},
	name='reset_password'),
	url(r'^reset-password/done/$', password_reset_done, name='password_reset_done'),
	url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 
	password_reset_confirm, name='password_reset_confirm'),
	url(r'^reset-password/complete/$', password_reset_complete, name='password_reset_complete'),
	url(r'^client/$', views.client, name='client'),
	url(r'^testemail/$', views.testEmail, name='testemail'),
	url(r'^tickets/$', views.tickets, name='tickets'),
	url(r'^tickets/details/$', views.ticket_detail, name='ticket_detail'),
	url(r'^tickets/new/$', views.create_ticket, name='create_ticket'),
	url(r'^tickets/new-entry/$', views.new_entry, name='new_entry'),
	url(r'^tickets/test/$', views.test, name='test'),
	url(r'^tickets/edit/$', views.edit_ticket, name="edit_ticket"),
	url(r'tickets/(?P<cid>[\w\s]+/$)', views.ticket_detail, name='ticket_detail'),
	url(r'tickets/(?P<tech>[\w\s]+/$)', views.ticket_detail, name='ticket_detail'),
	url(r'ajax_req/$', views.ajax_req, name='ajax_req'),

	


]