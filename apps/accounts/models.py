from django.db import models
from django.contrib.auth.models import AbstractUser 


class User(AbstractUser):
    
    favorite_character = models.CharField(
        max_length = 80,
        blank = True,
        choices = [
        # Utilizei IA para gerar o nomes dos personagens de rick and morty
        ('Rick Sanchez', 'Rick Sanchez'),
        ('Morty Smith', 'Morty Smith'),
        ('Summer Smith', 'Summer Smith'),
        ('Beth Smith', 'Beth Smith'),
        ('Jerry Smith', 'Jerry Smith'),
        ('Mr. Poopybutthole', 'Mr. Poopybutthole'),
        ('Birdperson', 'Birdperson'),
        ('Squanchy', 'Squanchy'),
        ('Evil Morty', 'Evil Morty'),
        ('Unity', 'Unity'),
        ('Mr. Meeseeks', 'Mr. Meeseeks'),
        ('Krombopulos Michael', 'Krombopulos Michael'),
        ('Abradolf Lincler', 'Abradolf Lincler'),
        ('Scary Terry', 'Scary Terry'),
        ('Zeep Xanflorp', 'Zeep Xanflorp'),
        
        ],
        help_text = "Seu personagem de anime favorito de rick and morty" 
    )
    collection_theme = models.CharField(
        max_length=20,
        blank=True,
        choices=[
            ('portal', 'Portal Gun'),
            ('pickle', 'Pickle Rick'),
            ('citadel', 'Citadel of Ricks'),
            ('c137', 'Dimension C-137'),
            ('purge', 'Purge Planet'),
            ('meeseeks', 'Mr. Meeseeks Box'),
            ('unity', 'Unity Hive Mind'),
            ('morty', 'Morty Adventure'),
        ],
        help_text="tema visual da sua coleção")
    
    bio = models.TextField(max_length=350, blank=True)
    profile_picture = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now=True) #auto_now=True é usado para atualizar automaticamente a data e hora sempre que o objeto for salvo.
    updated_at = models.DateTimeField(auto_now=True)
    # coloquei uma piadinha pro usuario
    @property
    def is_rick_fan(self):
        return self.favorite_character == 'Rick Sanchez'

    def get_nickname(self):
        if self.favorite_character == 'Rick Sanchez':
            return "Wubba Lubba Dub Dub!"
        return f"Fã de {self.get_favorite_character_display()}"

    def __str__(self):
        return f"{self.username} - {self.get_nickname()}"
    