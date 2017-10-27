from django.contrib import admin

# Register your models here.
from AuthorizeRestApiProject.AuthorizationApp.models import User
admin.site.register(User)

