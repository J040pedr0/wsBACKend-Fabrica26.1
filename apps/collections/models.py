from django.db import models
from django.conf import settings



class Collection(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='collections')
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'collections'
        ordering = ['-created_at']

class Characteristic(models.Model):
    external_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50 ,blank=True)
    species = models.CharField(max_length=50,blank=True)
    gender = models.CharField(max_length=20,blank=True)
    origin_name = models.CharField(max_length=100,blank=True)
    location_name = models.CharField(max_length=100,blank=True)
    image = models.URLField(blank=True)

    collections = models.ManyToManyField(Collection, related_name='characteristics', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='added_characteristics')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'characteristics'
        ordering = ['name']

class Userfavorite(models.Model):
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favorites')
        character = models.ForeignKey(Characteristic, on_delete=models.CASCADE, related_name='favorited_by')
        notes = models.TextField(blank=True)
        created_at = models.DateTimeField(auto_now_add=True)

        class Meta:
            db_table = 'user_favorites'
            unique_together = ['user', 'character']


