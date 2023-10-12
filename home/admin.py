from django.contrib import admin

# Register your models here.
from home.models import Contact
#Contact model contains the structure for the contact form backend db table

admin.site.register(Contact)