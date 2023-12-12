from django.contrib import admin

from .models import guides, reviews

# Register your models here.
admin.site.register(guides)
admin.site.register(reviews)
