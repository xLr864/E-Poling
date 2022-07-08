from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Registeration,User

# Register your models here.
@admin.register(Registeration)
class SudoRegistration(admin.ModelAdmin):
    list_display = ['Name','Email','Mobile','Address','Aadhar','VoterID',"DOB"]

@admin.register(User)
class SudoUser(admin.ModelAdmin):
    list_display = ["user_name","VoterID","DOB"]