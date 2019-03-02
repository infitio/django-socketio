from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class ChatRoom(models.Model):

    name = models.CharField(max_length=20)
    slug = models.SlugField(blank=True)

    class Meta:
        ordering = ("name",)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("room", (self.slug,))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(ChatRoom, self).save(*args, **kwargs)


class ChatUser(models.Model):

    name = models.CharField(max_length=20)
    session = models.CharField(max_length=20)
    room = models.ForeignKey(ChatRoom, related_name="users", on_delete=models.CASCADE)

    class Meta:
        ordering = ("name",)

    def __unicode__(self):
        return self.name
