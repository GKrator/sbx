from django.contrib import admin
from foreground.models import Person
# Register your models here.
class PersonAdmin(admin.ModelAdmin):
	list_display = ('name','email','subject')
admin.site.register(Person,PersonAdmin)