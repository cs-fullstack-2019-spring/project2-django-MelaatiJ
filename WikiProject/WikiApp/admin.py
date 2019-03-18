from django.contrib import admin

# Register your models here.
# from .models import UserModel
# admin.site.register(UserModel)

from .models import WikiEntryModel


# allows mde to view model better in admin
class WikiEntryModelAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "creator"]

    class Meta:
        model = WikiEntryModel


admin.site.register(WikiEntryModel, WikiEntryModelAdmin)

from .models import RIEntryModel

admin.site.register(RIEntryModel)
