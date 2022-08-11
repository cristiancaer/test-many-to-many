from django.contrib import admin
from .models import Group, Membership, Person

admin.site.register(Person)
admin.site.register(Membership)
admin.site.register(Group)
