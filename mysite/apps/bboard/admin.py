
from unicodedata import name
from django.contrib import admin
from . models import Bb, Rubric, Piople


class BbAdmin (admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'publisched', 'rubric')
    list_display_links=('title', 'content')
    search_fields=('title', 'content')
admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)

# register Date Base name: Piople

class PiopleAdmin (admin.ModelAdmin):
    # list_display = [field.name for field in Piople._meta.fields]
    list_display = ('name', 'adress')
    list_display_links = ('name', 'adress')
    search_fields = ('name', 'adress')
admin.site.register(Piople, PiopleAdmin)
