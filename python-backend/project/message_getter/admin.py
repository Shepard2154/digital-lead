from django.contrib import admin

from .models import UserIdentifierModel, MessageModel, AddressModel


admin.site.register(UserIdentifierModel)
admin.site.register(AddressModel)
admin.site.register(MessageModel)
