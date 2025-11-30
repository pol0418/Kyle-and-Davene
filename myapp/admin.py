from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ('title', 'created_at')
	search_fields = ('title', 'description')
	list_filter = ('created_at',)
	readonly_fields = ('preview',)

	def preview(self, obj):
		if obj.image:
			return f'<img src="{obj.image.url}" style="max-height:120px;" />'
		return '(no image)'
	preview.allow_tags = True
	preview.short_description = 'Image Preview'
