from django.contrib import admin
from dbshechka.models import AudioBK,AudioVk

# Register your models here.
class AuthorisationAdmin(admin.ModelAdmin):
    pass
admin.site.register(AudioBK,AuthorisationAdmin)
admin.site.register(AudioVk,AuthorisationAdmin)