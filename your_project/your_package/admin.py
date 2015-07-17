from django.contrib import admin
from your_package.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from modeltranslation.admin import TranslationStackedInline


class ProfileInline(TranslationStackedInline):
	model = Profile
	can_delete = False

class UserAdmin(UserAdmin):
	inlines = (ProfileInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
