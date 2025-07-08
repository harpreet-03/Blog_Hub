from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import os

class Post(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(null=True, blank=True, upload_to='Files')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # New fields for file sharing
    shared_with = models.ManyToManyField(User, related_name='shared_files', blank=True)
    is_public = models.BooleanField(default=True)
    download_count = models.IntegerField(default=0)
    file_size = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

    def extension(self):
        if self.file:
            _, extension = os.path.splitext(self.file.name)
            return extension.lower()
        return ''

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def get_file_type(self):
        """Return the file type category based on extension"""
        ext = self.extension()
        if ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg']:
            return 'image'
        elif ext in ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.webm']:
            return 'video'
        elif ext in ['.pdf', '.doc', '.docx', '.txt', '.rtf']:
            return 'document'
        elif ext in ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c']:
            return 'code'
        elif ext in ['.zip', '.rar', '.7z', '.tar', '.gz']:
            return 'archive'
        else:
            return 'other'

    def get_file_size_display(self):
        """Return human readable file size"""
        if not self.file_size:
            return 'Unknown size'
        
        size = self.file_size
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024.0:
                return f"{size:.1f} {unit}"
            size /= 1024.0
        return f"{size:.1f} TB"

    def save(self, *args, **kwargs):
        # Auto-calculate file size
        if self.file and hasattr(self.file, 'size'):
            self.file_size = self.file.size
        super().save(*args, **kwargs)


