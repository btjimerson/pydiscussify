from django.db import models

class Post(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=256, null=True)
    post_date = models.DateTimeField("post_date")

    class Meta:
        ordering = ["-post_date"]
        
    def __str__(self):
        return f"title: '{self.title}', author: '{self.author}', post_date: '{self.post_date}', content: '{self.content}'"
    
class Comment(models.Model):
    author = models.CharField(max_length=100)
    comment = models.CharField(max_length=256)
    comment_date = models.DateTimeField("comment_date")
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="comments")

    class Meta:
        ordering = ["-comment_date"]

    def __str__ (self):
        return f"author: '{self.author}', comment: '{self.comment}', comment_date: '{self.comment_date}', post: '{self.post}"