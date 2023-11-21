from django.contrib import admin

from .models import Me, Project, Pricing, Skill, Contact


@admin.register(Me)
class MeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    search_fields = ['first_name', 'last_name', 'email', 'phone']
    list_filter = ['education', 'work_history']
    fieldsets = (
        ('Основная информация', {
            'fields': ('first_name', 'last_name', 'email', 'phone')
        }),
        ('Социальные сети', {
            'fields': ('instagram', 'github', 'linkedin', 'telegram'),
            'classes': ('collapse',),
        }),
        ('Образование и работа', {
            'fields': ('education', 'work_history'),
            'classes': ('collapse',),
        }),
    )



@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_data', 'end_data', 'url', 'repository')
    search_fields = ['title', 'description', 'technologies_used']
    list_filter = ['start_data', 'end_data']
    date_hierarchy = 'start_data'
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'description', 'technologies_used')
        }),
        ('Даты', {
            'fields': ('start_data', 'end_data'),
        }),
        ('Ссылки', {
            'fields': ('url', 'repository'),
            'classes': ('collapse',),
        }),
        ('Медиафайлы', {
            'fields': ('file', 'image'),
            'classes': ('collapse',),
        }),
    )
    

@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    list_display = ('service', 'rate_per_hour', 'estimated_hours', 'total_cost')
    search_fields = ['service', 'description']
    list_filter = ['rate_per_hour']
    readonly_fields = ['total_cost']
    fieldsets = (
        ('Основная информация', {
            'fields': ('service', 'description')
        }),
        ('Расценки', {
            'fields': ('rate_per_hour', 'estimated_hours', 'total_cost'),
        }),
    )
    

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'percentage']
    search_fields = ['name', 'category']
    list_filter = ['category']
    ordering = ['category', 'name']
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'category', 'percentage')
        }),
    )
    

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    search_fields = ['name', 'email', 'subject', 'message']
    list_filter = ['is_read']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at']
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'email', 'subject', 'message', 'is_read')
        }),
    )