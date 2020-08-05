from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Lead)
admin.site.register(Qualify)
admin.site.register(Call)
admin.site.register(Close)





