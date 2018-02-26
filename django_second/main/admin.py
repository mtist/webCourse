from django.contrib import admin
from .models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'surname', 'name', 'about')
    list_editable = ('name', 'surname')
    search_fields = ('surname', 'name')
    # list_display_links = None

admin.site.register(Person, PersonAdmin)
