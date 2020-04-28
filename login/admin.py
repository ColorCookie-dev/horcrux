from django.contrib import admin
from .models import Organisation as Org, User
from django.forms import ModelForm


# Register your models here.
@admin.register(User)
class AccountManager(admin.ModelAdmin):
    filter_horizontal = ('user_permissions', 'groups')

    def get_list_filter(self, request):
        if request.user.is_superuser:
            return ('is_active', 'is_staff', 'org', 'date_joined', 'groups')
        return ('is_active', 'date_joined', 'is_staff', 'groups')

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ()
        return ('org',)

    def get_list_display(self, request):
        base_list = ('full_name', 'username', 'email', 'phone', 'addr', 'postcode', 'date_joined', 'is_active', 'last_login')
        if request.user.is_superuser:
            return base_list + ('org',)
        return base_list

    def get_fieldsets(self, request, obj=None):
        if request.user.is_superuser:
            return ((None, {
                    'fields': (
                        'username', 'password',
                        ('first_name', 'last_name'),
                        'email', 'phone', 'addr', 'postcode', 'org',
                        'groups', 'user_permissions', 'is_active',
                        'is_staff')
                }),)
        return ((None, {
                'fields': (
                    'username', 'password',
                    ('first_name', 'last_name'),
                    'email', 'phone', 'addr', 'postcode', 'is_active',)
            }),)

    search_fields = ('first_name', 'last_name', 'email',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(org=request.user.org)

    def save_model(self, request, obj, form, change):
        # if not request.user.is_superuser: obj.org = request.user.org
        # super().save_model(request, obj, form, change)

        if not request.user.is_superuser: obj.org = request.user.org
        if 'password' in form.changed_data:
            obj.set_password(form.cleaned_data.get('password'))
        obj.save()

    def full_name(self, obj):
        name = ("%s %s" % (obj.first_name, obj.last_name)).strip()
        return name if name else '--empty--'

@admin.register(Org)
class OrgAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'VAT', 'phone', 'website', 'CIN', 'postcode', 'addr')
    search_fields = ('name', 'email',)

