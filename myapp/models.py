from django.db import models


class Project(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	url = models.URLField(blank=True, help_text='Optional link to project or repo')
	image = models.ImageField(upload_to='projects/', blank=True, null=True, help_text='Optional image for the project')
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return self.title
