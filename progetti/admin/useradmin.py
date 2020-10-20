from django.contrib import admin
from progetti.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
