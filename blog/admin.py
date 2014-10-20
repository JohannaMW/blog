from django.contrib import admin
from blog.models import BlogPost, Author, Comment, Tag, Reader

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Reader)