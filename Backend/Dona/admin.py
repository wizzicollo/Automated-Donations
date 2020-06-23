from django.contrib import admin
from .models import Donation
from .models import Story
from .models import Donor
from .models import Charity


admin.site.register(Donation)
admin.site.register(Story)
admin.site.register(Donor)
admin.site.register(Charity)