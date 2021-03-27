from django.contrib import admin
from apps.review.models import Review


class ReviewAdmin(admin.ModelAdmin):
    pass


admin.site.register(Review, ReviewAdmin)
# Register your models here.
