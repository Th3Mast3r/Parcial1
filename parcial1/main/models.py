from django.db import models #importamos model de django
from django.template.defaultfilters import slugify # activamos el slugify
from ckeditor.fields import RichTextField #importamos el texto rico Xd

class Blogs(models.Model): #modelo del blog

    class Meta:
        verbose_name_plural = 'Blogs'
        verbose_name = 'Blog'
        ordering = ["name"]

    date = models.DateTimeField(blank=True, null=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="blog")
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Blogs, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/blog/{self.slug}"

class Reviews(models.Model): #modelo del review

    class Meta: 
        verbose_name_plural = 'Reviews'
        verbose_name = 'Review'
        ordering = ["title"]

    date = models.DateTimeField(blank=True, null=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="review")
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Reviews, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/review/{self.slug}"

class Contact(models.Model):
    
    class Meta:
        verbose_name_plural = 'Contacts'
        verbose_name = 'Contact'
        ordering = ["timestamp"]
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name",max_length=100)
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return f'{self.name}'
