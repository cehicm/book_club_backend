from django.contrib import admin
from apps.user.models import BCUser


class BCUserAdmin(admin.ModelAdmin):
    pass


admin.site.register(BCUser, BCUserAdmin)

# Register your models here.
