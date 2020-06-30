from django.contrib import admin
from .models import Story
from .models import Charity


admin.site.register(Story)
admin.site.register(Charity)