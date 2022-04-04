from django.contrib import admin

# Register your models here.

'''from .models import Profile, User

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'slug']


admin.site.register(Profile, ProfileAdmin)
'''
from .models import Profile, Friend

class FriendAdmin(admin.ModelAdmin):
    list_display = ['profile', 'friend', 'is_accepted']

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'point', 'bio', 'first_name', 'last_name',  'id']

class ProfileAdmin(admin.ModelAdmin):
    list_display = [ 'user', 'point', 'bio', 'first_name', 'last_name', 'id']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Friend, FriendAdmin)
