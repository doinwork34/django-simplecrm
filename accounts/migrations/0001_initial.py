# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-22 01:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientlist',
            fields=[
                ('oid', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('clientname', models.CharField(blank=True, db_column='ClientName', max_length=255, null=True, unique=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=255, null=True)),
                ('techsupportplan', models.CharField(blank=True, db_column='TechSupportPlan', max_length=255, null=True)),
                ('address1', models.CharField(blank=True, db_column='Address1', max_length=255, null=True)),
                ('address2', models.CharField(blank=True, db_column='Address2', max_length=255, null=True)),
                ('address3', models.CharField(blank=True, db_column='Address3', max_length=255, null=True)),
                ('city', models.CharField(blank=True, db_column='City', max_length=255, null=True)),
                ('state', models.CharField(blank=True, db_column='State', max_length=255, null=True)),
                ('zipcode', models.CharField(blank=True, db_column='ZipCode', max_length=255, null=True)),
                ('phonenumber', models.CharField(blank=True, db_column='PhoneNumber', max_length=255, null=True)),
                ('extension', models.CharField(blank=True, db_column='Extension', max_length=50, null=True)),
                ('fax_number', models.CharField(blank=True, db_column='Fax Number', max_length=50, null=True)),
                ('primarycontact', models.CharField(blank=True, db_column='PrimaryContact', max_length=255, null=True)),
                ('donotassist', models.NullBooleanField(db_column='DoNotAssist')),
                ('clienttype', models.IntegerField(blank=True, db_column='ClientType', null=True)),
                ('notes', models.TextField(blank=True, db_column='Notes', null=True)),
            ],
            options={
                'db_table': 'ClientList',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Clientnotes',
            fields=[
                ('oid', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('clientid', models.IntegerField(blank=True, db_column='ClientID', null=True)),
                ('title', models.CharField(blank=True, db_column='Title', max_length=255, null=True)),
                ('notes', models.TextField(blank=True, db_column='Notes', null=True)),
                ('category', models.IntegerField(blank=True, db_column='Category', null=True)),
                ('new_ticket_popup', models.CharField(blank=True, db_column='New Ticket Popup', max_length=255, null=True)),
            ],
            options={
                'db_table': 'ClientNotes',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Clienttypes',
            fields=[
                ('oid', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('type', models.CharField(blank=True, db_column='Type', max_length=50, null=True)),
                ('createtickets', models.NullBooleanField(db_column='CreateTickets')),
                ('defaultchecked', models.NullBooleanField(db_column='DefaultChecked')),
            ],
            options={
                'db_table': 'ClientTypes',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Companyinventory',
            fields=[
                ('oid', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('itemid', models.IntegerField(db_column='ItemID')),
                ('typeid', models.IntegerField(blank=True, db_column='TypeID', null=True)),
                ('serialnumber', models.CharField(blank=True, db_column='SerialNumber', max_length=255, null=True)),
                ('datereceived', models.DateTimeField(blank=True, db_column='DateReceived', null=True)),
                ('dateinstalled', models.DateTimeField(blank=True, db_column='DateInstalled', null=True)),
                ('itemnotes', models.TextField(blank=True, db_column='ItemNotes', null=True)),
                ('currentclient', models.IntegerField(blank=True, db_column='CurrentClient', null=True)),
                ('billed', models.DateTimeField(blank=True, db_column='Billed', null=True)),
            ],
            options={
                'db_table': 'CompanyInventory',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Companyinventorydetail',
            fields=[
                ('oid', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('companyinventoryid', models.IntegerField(blank=True, db_column='CompanyInventoryID', null=True)),
                ('serviceticket', models.IntegerField(blank=True, db_column='ServiceTicket', null=True)),
                ('client', models.IntegerField(blank=True, db_column='Client', null=True)),
                ('workstart', models.DateTimeField(blank=True, db_column='WorkStart', null=True)),
                ('workstop', models.DateTimeField(blank=True, db_column='WorkStop', null=True)),
                ('detailnotes', models.TextField(blank=True, db_column='DetailNotes', null=True)),
                ('billable', models.NullBooleanField(db_column='Billable')),
                ('billed', models.NullBooleanField(db_column='Billed')),
                ('billableamount', models.DecimalField(blank=True, db_column='BillableAmount', decimal_places=4, max_digits=19, null=True)),
            ],
            options={
                'db_table': 'CompanyInventoryDetail',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('oid', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('clientid', models.IntegerField(blank=True, db_column='ClientID', null=True)),
                ('contactname', models.CharField(blank=True, db_column='ContactName', max_length=255, null=True)),
                ('title', models.CharField(blank=True, db_column='Title', max_length=255, null=True)),
                ('emailaddress', models.CharField(blank=True, db_column='EmailAddress', max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, db_column='Phone Number', max_length=255, null=True)),
                ('extension', models.CharField(blank=True, db_column='Extension', max_length=50, null=True)),
                ('cell_phone', models.CharField(blank=True, db_column='Cell Phone', max_length=255, null=True)),
                ('notes', models.CharField(blank=True, db_column='Notes', max_length=255, null=True)),
                ('primary', models.NullBooleanField(db_column='Primary')),
                ('sendticketassignemail', models.NullBooleanField(db_column='SendTicketAssignEmail')),
                ('sendticketcompleteemail', models.NullBooleanField(db_column='SendTicketCompleteEmail')),
            ],
            options={
                'db_table': 'Contacts',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Internalemailaddresses',
            fields=[
                ('oid', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('emailaddress', models.CharField(blank=True, db_column='EmailAddress', max_length=255, null=True)),
                ('smtphost', models.CharField(blank=True, db_column='SmtpHost', max_length=255, null=True)),
                ('smtpport', models.IntegerField(blank=True, db_column='SmtpPort', null=True)),
                ('password', models.CharField(blank=True, db_column='Password', max_length=255, null=True)),
            ],
            options={
                'db_table': 'InternalEmailAddresses',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Inventoryitems',
            fields=[
                ('oid', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('itemname', models.CharField(blank=True, db_column='ItemName', max_length=255, null=True)),
                ('model_number', models.CharField(blank=True, db_column='Model Number', max_length=255, null=True)),
                ('upc', models.CharField(blank=True, db_column='UPC', max_length=255, null=True)),
                ('description', models.TextField(blank=True, db_column='Description', null=True)),
                ('currentinventoryitem', models.NullBooleanField(db_column='CurrentInventoryItem')),
                ('cost', models.DecimalField(blank=True, db_column='Cost', decimal_places=4, max_digits=19, null=True)),
                ('client_price', models.DecimalField(blank=True, db_column='Client Price', decimal_places=4, max_digits=19, null=True)),
                ('reorderthreshold', models.IntegerField(blank=True, db_column='ReorderThreshold', null=True)),
                ('parcount', models.IntegerField(blank=True, db_column='ParCount', null=True)),
                ('vendorid', models.IntegerField(blank=True, db_column='VendorID', null=True)),
                ('manufacturerid', models.IntegerField(blank=True, db_column='ManufacturerID', null=True)),
                ('itemnotes', models.TextField(blank=True, db_column='ItemNotes', null=True)),
            ],
            options={
                'db_table': 'InventoryItems',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Inventorystatuses',
            fields=[
                ('oid', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('inventorystatus', models.CharField(blank=True, db_column='InventoryStatus', max_length=255, null=True)),
                ('defaultchecked', models.NullBooleanField(db_column='DefaultChecked')),
            ],
            options={
                'db_table': 'InventoryStatuses',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('oid', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('clientassignemailsubject', models.CharField(blank=True, db_column='ClientAssignEmailSubject', max_length=255, null=True)),
                ('clientassignemailbody', models.TextField(blank=True, db_column='ClientAssignEmailBody', null=True)),
                ('clientcompleteemailsubject', models.CharField(blank=True, db_column='ClientCompleteEmailSubject', max_length=255, null=True)),
                ('clientcompleteemailbody', models.TextField(blank=True, db_column='ClientCompleteEmailBody', null=True)),
                ('internalassignemailsubject', models.CharField(blank=True, db_column='InternalAssignEmailSubject', max_length=255, null=True)),
                ('internalassignemailbody', models.TextField(blank=True, db_column='InternalAssignEmailBody', null=True)),
                ('internalcompleteemailsubject', models.CharField(blank=True, db_column='InternalCompleteEmailSubject', max_length=255, null=True)),
                ('internalcompleteemailbody', models.TextField(blank=True, db_column='InternalCompleteEmailBody', null=True)),
                ('rootfolder', models.CharField(blank=True, db_column='RootFolder', max_length=255, null=True)),
                ('ticketnumber', models.IntegerField(blank=True, db_column='TicketNumber', null=True)),
                ('default_technician', models.IntegerField(blank=True, db_column='Default Technician', null=True)),
                ('refreshinterval', models.IntegerField(blank=True, db_column='RefreshInterval', null=True)),
                ('inventoryordersubject', models.CharField(blank=True, db_column='InventoryOrderSubject', max_length=255, null=True)),
                ('inventoryorderbody', models.TextField(blank=True, db_column='InventoryOrderBody', null=True)),
                ('inventoryordertoemail', models.CharField(blank=True, db_column='InventoryOrderToEmail', max_length=255, null=True)),
            ],
            options={
                'db_table': 'Options',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PasteErrors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oid', models.IntegerField(blank=True, db_column='ID', null=True)),
                ('ticketid', models.IntegerField(blank=True, db_column='TicketID', null=True)),
                ('timestamp', models.CharField(blank=True, db_column='TimeStamp', max_length=255, null=True)),
                ('technician', models.CharField(blank=True, db_column='Technician', max_length=255, null=True)),
                ('worktype', models.CharField(blank=True, db_column='WorkType', max_length=255, null=True)),
                ('startdate', models.DateTimeField(blank=True, db_column='StartDate', null=True)),
                ('enddate', models.DateTimeField(blank=True, db_column='EndDate', null=True)),
                ('notes', models.TextField(blank=True, db_column='Notes', null=True)),
            ],
            options={
                'db_table': 'Paste Errors',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Reservedwords',
            fields=[
                ('oid', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('word', models.CharField(blank=True, db_column='Word', max_length=255, null=True, unique=True)),
                ('notes', models.CharField(blank=True, db_column='Notes', max_length=255, null=True)),
            ],
            options={
                'db_table': 'ReservedWords',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SavedContacts',
            fields=[
                ('oid', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('clientid', models.IntegerField(blank=True, db_column='ClientID', null=True)),
                ('contactname', models.CharField(blank=True, db_column='ContactName', max_length=255, null=True)),
                ('title', models.CharField(blank=True, db_column='Title', max_length=255, null=True)),
                ('emailaddress', models.CharField(blank=True, db_column='EmailAddress', max_length=255, null=True)),
                ('phonenumber1', models.CharField(blank=True, db_column='PhoneNumber1', max_length=255, null=True)),
                ('phonenumber2', models.CharField(blank=True, db_column='PhoneNumber2', max_length=255, null=True)),
                ('notes', models.CharField(blank=True, db_column='Notes', max_length=255, null=True)),
                ('primary', models.NullBooleanField(db_column='Primary')),
                ('sendticketassignemail', models.NullBooleanField(db_column='SendTicketAssignEmail')),
                ('sendticketcompleteemail', models.NullBooleanField(db_column='SendTicketCompleteEmail')),
            ],
            options={
                'db_table': 'Saved Contacts',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Servicetickets',
            fields=[
                ('oid', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('timestamp', models.CharField(blank=True, db_column='TimeStamp', max_length=255, null=True, unique=True)),
                ('clientid', models.IntegerField(db_column='ClientID')),
                ('ticket_title', models.CharField(blank=True, db_column='Ticket Title', max_length=255, null=True)),
                ('technician', models.CharField(blank=True, db_column='Technician', max_length=255, null=True)),
                ('contact_name', models.CharField(blank=True, db_column='Contact Name', max_length=255, null=True)),
                ('ticketstartdate', models.DateTimeField(blank=True, db_column='TicketStartDate', null=True)),
                ('time_spent_minutes_field', models.IntegerField(blank=True, db_column='Time Spent (Minutes)', null=True)),
                ('ticket_status', models.IntegerField(blank=True, db_column='Ticket Status', null=True)),
                ('worktype', models.CharField(blank=True, db_column='WorkType', max_length=255, null=True)),
                ('internal_notes', models.TextField(blank=True, db_column='Internal Notes', null=True)),
                ('client_notes', models.TextField(blank=True, db_column='Client Notes', null=True)),
                ('complete', models.NullBooleanField(db_column='Complete')),
                ('ticketcategory1', models.IntegerField(blank=True, db_column='TicketCategory1', null=True)),
                ('ticketcategory2', models.IntegerField(blank=True, db_column='TicketCategory2', null=True)),
                ('ticketcategory3', models.IntegerField(blank=True, db_column='TicketCategory3', null=True)),
                ('billable', models.IntegerField(blank=True, db_column='Billable', null=True)),
                ('billed', models.NullBooleanField(db_column='Billed')),
                ('ticketnumber', models.IntegerField(blank=True, db_column='TicketNumber', null=True)),
            ],
            options={
                'db_table': 'ServiceTickets',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Technicians',
            fields=[
                ('oid', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nickname', models.CharField(blank=True, db_column='Nickname', max_length=255, null=True)),
                ('firstname', models.CharField(blank=True, db_column='FirstName', max_length=255, null=True)),
                ('lastname', models.CharField(blank=True, db_column='LastName', max_length=255, null=True)),
                ('fromemailaddress', models.IntegerField(blank=True, db_column='FromEmailAddress', null=True)),
                ('toemailaddress', models.IntegerField(blank=True, db_column='ToEmailAddress', null=True)),
                ('editclosedtickets', models.NullBooleanField(db_column='EditClosedTickets')),
                ('editclients', models.NullBooleanField(db_column='EditClients')),
                ('editsettings', models.NullBooleanField(db_column='EditSettings')),
                ('billing', models.NullBooleanField(db_column='Billing')),
                ('viewotherstickets', models.NullBooleanField(db_column='ViewOthersTickets')),
                ('assignticketstoothers', models.NullBooleanField(db_column='AssignTicketsToOthers')),
                ('alloweditsendemail', models.NullBooleanField(db_column='AllowEditSendEmail')),
                ('sendemaildefailt', models.NullBooleanField(db_column='SendEmailDefailt')),
            ],
            options={
                'db_table': 'Technicians',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Techsupportplans',
            fields=[
                ('oid', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('planname', models.CharField(blank=True, db_column='PlanName', max_length=255, null=True, unique=True)),
            ],
            options={
                'db_table': 'TechSupportPlans',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Ticketcategory1',
            fields=[
                ('oid', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('categoryname', models.CharField(blank=True, db_column='CategoryName', max_length=255, null=True)),
                ('sort', models.IntegerField(db_column='Sort')),
            ],
            options={
                'db_table': 'TicketCategory1',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Ticketcategory2',
            fields=[
                ('oid', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('category1id', models.IntegerField(db_column='Category1ID')),
                ('categoryname', models.CharField(blank=True, db_column='CategoryName', max_length=255, null=True)),
                ('sort', models.IntegerField(blank=True, db_column='Sort', null=True)),
            ],
            options={
                'db_table': 'TicketCategory2',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Ticketcategory3',
            fields=[
                ('oid', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('categoryname', models.CharField(blank=True, db_column='CategoryName', max_length=255, null=True)),
                ('category1id', models.IntegerField(db_column='Category1ID')),
                ('category2id', models.IntegerField(db_column='Category2ID')),
            ],
            options={
                'db_table': 'TicketCategory3',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Ticketstatuses',
            fields=[
                ('oid', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, db_column='Status', max_length=255, null=True)),
                ('defaultforticketview', models.NullBooleanField(db_column='DefaultForTicketView')),
                ('defaultforbillingview', models.NullBooleanField(db_column='DefaultForBillingView')),
            ],
            options={
                'db_table': 'TicketStatuses',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Timeentries',
            fields=[
                ('oid', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('ticketid', models.IntegerField(db_column='TicketID')),
                ('timestamp', models.CharField(blank=True, db_column='TimeStamp', max_length=255, null=True, unique=True)),
                ('technician', models.CharField(blank=True, db_column='Technician', max_length=255, null=True)),
                ('worktype', models.CharField(blank=True, db_column='WorkType', max_length=255, null=True)),
                ('startdate', models.DateTimeField(blank=True, db_column='StartDate', null=True)),
                ('enddate', models.DateTimeField(blank=True, db_column='EndDate', null=True)),
                ('notes', models.TextField(blank=True, db_column='Notes', null=True)),
            ],
            options={
                'db_table': 'TimeEntries',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=100)),
                ('website', models.URLField(default='')),
                ('phone', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Worktypes',
            fields=[
                ('oid', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('worktype', models.CharField(blank=True, db_column='WorkType', max_length=255, null=True)),
            ],
            options={
                'db_table': 'WorkTypes',
                'managed': True,
            },
        ),
        migrations.AlterUniqueTogether(
            name='timeentries',
            unique_together=set([('oid', 'ticketid')]),
        ),
        migrations.AlterUniqueTogether(
            name='ticketcategory3',
            unique_together=set([('oid', 'category1id', 'category2id')]),
        ),
        migrations.AlterUniqueTogether(
            name='ticketcategory2',
            unique_together=set([('oid', 'category1id')]),
        ),
        migrations.AlterUniqueTogether(
            name='servicetickets',
            unique_together=set([('oid', 'clientid')]),
        ),
        migrations.AlterUniqueTogether(
            name='companyinventory',
            unique_together=set([('oid', 'itemid')]),
        ),
    ]
