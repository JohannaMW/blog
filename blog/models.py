from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=120)

    def __unicode__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()
    author = models.ForeignKey(Author, related_name="posts")

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    body = models.CharField(max_length=200)
    author = models.ForeignKey(Author, related_name="comments")

    def __unicode__(self):
        return self.body

class Tag(models.Model):
    name = models.CharField(max_length=120)
    post = models.ManyToManyField(BlogPost, blank=True, null=True, related_name="tag")

class Reader(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()

    def __unicode__(self):
        return self.name