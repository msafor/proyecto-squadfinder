from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Game, SquadRequest

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'gamertag', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('Información de Gamer', {'fields': ('gamertag',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Información de Gamer', {'fields': ('gamertag',)}),
    )

class GameAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'slug')
    prepopulated_fields = {'slug': ('nombre',)}

class SquadRequestAdmin(admin.ModelAdmin):
    list_display = ('game', 'creator', 'rank_required', 'created_at')
    list_filter = ('game', 'rank_required')
    search_fields = ('description', 'rank_required')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(SquadRequest, SquadRequestAdmin)