from django.contrib import admin
from .models import CustomUser, APIAccess


admin.site.register(CustomUser)
admin.site.register(APIAccess)