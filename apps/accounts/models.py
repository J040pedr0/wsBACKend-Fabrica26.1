from django.db import models
from django.contrib.auth.models import AbstractUser 

class User(AbstractUser):
    
    favorite_character = models.CharField(
        max_length = 80,
        blank = True,
        choices = [
        # Utilizei IA para gerar uma lista de personagens de anime populares, abrangendo várias séries e gêneros, para oferecer aos usuários uma ampla variedade de opções ao escolher seu personagem favorito.Fiz isso para não ter que perder tempo pesquisando e selecionando manualmente os personagens, garantindo uma lista diversificada e representativa dos animes mais conhecidos.(EXISTE UM DETALHE PARA FÃS DE GRIFFITH RSRS)
        ('Goku (Dragon Ball)', 'Goku'),
        ('Naruto (Naruto)', 'Naruto'),
        ('Sasuke (Naruto)', 'Sasuke'),  
        ('Sakura (Naruto)', 'Sakura'),  
        ('Luffy (One Piece)', 'Luffy'),
        ('Zoro (One Piece)', 'Zoro'),
        ('Sanji (One Piece)', 'Sanji'),
        ('Nami (One Piece)', 'Nami'),
        ('Usopp (One Piece)', 'Usopp'),
        ('Chopper (One Piece)', 'Chopper'),
        ('Robin (One Piece)', 'Robin'),
        ('Franky (One Piece)', 'Franky'),
        ('Brook (One Piece)', 'Brook'),
        ('Shanks (One Piece)', 'Shanks'),
        ('Kaido (One Piece)', 'Kaido'),
        ('Big Mom (One Piece)', 'Big Mom'),
        ('Blackbeard (One Piece)', 'Blackbeard'),
        ('Akainu (One Piece)', 'Akainu'),
        ('Aokiji (One Piece)', 'Aokiji'),
        ('Kizaru (One Piece)', 'Kizaru'),
        ('Ace (One Piece)', 'Ace'),
        ('Sabo (One Piece)', 'Sabo'),
        ('Boa Hancock (One Piece)', 'Boa Hancock'),
        ('Law (One Piece)', 'Law'), 
        ('Saitama (One Punch Man)', 'Saitama'),
        ('Deku (My Hero Academia)', 'Deku'),
        ('Tanjiro (Demon Slayer)', 'Tanjiro'),
        ('Eren (Attack on Titan)', 'Eren'),
        ('Mikasa (Attack on Titan)', 'Mikasa'),
        ('Levi (Attack on Titan)', 'Levi'),
        ('Jotaro (JoJo\'s Bizarre Adventure)', 'Jotaro'),
        ('Dio (JoJo\'s Bizarre Adventure)', 'Dio'),
        ('Edward (Fullmetal Alchemist)', 'Edward'),
        ('Alphonse (Fullmetal Alchemist)', 'Alphonse'),
        ('Gon (Hunter x Hunter)', 'Gon'),
        ('Killua (Hunter x Hunter)', 'Killua'),
        ('Hisoka (Hunter x Hunter)', 'Hisoka'),
        ('Gojo (Jujutsu Kaisen)', 'Gojo'),
        ('Itadori (Jujutsu Kaisen)', 'Itadori'),
        ('Megumi (Jujutsu Kaisen)', 'Megumi'),
        ('Nobara (Jujutsu Kaisen)', 'Nobara'),
        ('Sukuna (Jujutsu Kaisen)', 'Sukuna'),
        ('Ichigo (Bleach)', 'Ichigo'),
        ('Rukia (Bleach)', 'Rukia'),
        ('Aizen (Bleach)', 'Aizen'),
        ('Saiki (The Disastrous Life of Saiki K.)', 'Saiki'),
        ('Senku (Dr. Stone)', 'Senku'),
        ('Kohaku (Dr. Stone)', 'Kohaku'),
        ('Yusuke (Yu Yu Hakusho)', 'Yusuke'),
        ('Hiei (Yu Yu Hakusho)', 'Hiei'),
        ('Kurama (Yu Yu Hakusho)', 'Kurama'),
        ('Kenshin (Rurouni Kenshin)', 'Kenshin'),
        ('Inuyasha (Inuyasha)', 'Inuyasha'),
        ('Sesshomaru (Inuyasha)', 'Sesshomaru'),
        ('Vash (Trigun)', 'Vash'),
        ('Spike (Cowboy Bebop)', 'Spike'),
        ('L (Death Note)', 'L'),
        ('Light (Death Note)', 'Light'),
        ('Ryuk (Death Note)', 'Ryuk'),
        ('Guts (Berserk)', 'Guts'),
        ('Griffith (Berserk)', 'Griffith'),
        ('Alucard (Hellsing)', 'Alucard'),
        ('Ken (Tokyo Revengers)', 'Ken'),
        ('Mikey (Tokyo Revengers)', 'Mikey'),
        ('Draken (Tokyo Revengers)', 'Draken'),
        ('Toge (Jujutsu Kaisen)', 'Toge'),
        ('Maki (Jujutsu Kaisen)', 'Maki'),
        ('Panda (Jujutsu Kaisen)', 'Panda'),
        ('Hinata (Haikyuu!!)', 'Hinata'),
        ('Kageyama (Haikyuu!!)', 'Kageyama'),
        ('Nishinoya (Haikyuu!!)', 'Nishinoya'),
        ('Sawamura (Haikyuu!!)', 'Sawamura'),
    ],
        help_text = "Seu personagem de anime favorito" 
)
    collection_theme = models.CharField(
        max_length=20,
        blank=True,
        choices=[
            ('shonen', 'Shonen'),
            ('isekai', 'Isekai'),
            ('mecha', 'Mecha'),
            ('slice_of_life', 'Slice of Life'),
            ('fantasy', 'Fantasy'),
            ('horror', 'Horror'),
            ('comedy', 'Comedy'),
            ('romance', 'Romance'),
            ('action', 'Action'),
            ('adventure', 'Adventure'),
        ],
        help_text="Tema visual da sua coleção baseado no gênero de anime que você mais gosta")
    
    bio = models.TextField(max_length=350, blank=True)
    profile_picture = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now=True) #auto_now=True é usado para atualizar automaticamente a data e hora sempre que o objeto for salvo.
    updated_at = models.DateTimeField(auto_now=True)

    def is_berserk_fan(self):
        return self.favorite_character  == 'Griffith (Berserk)'
    
    def get_nickname(self):
        if self.favorite_character:
            return "Doente"
        return f"Fã de {self.favorite_character_display()}"

    def __str__(self):
        return f"{self.username} - fã de {self.favorite_character_display() or 'sem personagem favorito'}"

    