# Django import:
from django.contrib import admin


# Base admin class:
class BaseAdmin(admin.ModelAdmin):

    @admin.action(description='Make device nonactive')
    def make_nonactive(self, request, queryset):
        change = queryset.update(is_active=False)
        self.message_user(request, '%d device was successfully marked as active.')

        # self.message_user(request,
        #     '%d device was successfully marked as nonactive.',
        #     '%d devices were successfully marked as nonactive.',
        #     change,
        # % change, messages.SUCCESS)

    @admin.action(description='Make device active')
    def make_active(self, request, queryset):
        change = queryset.update(is_active=True)
        self.message_user(request, '%d device was successfully marked as active.')
