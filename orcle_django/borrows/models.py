from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class TipoItem(models.Model):
    nome = models.CharField(max_length=200, help_text='Digite o nome tipo de objeto')
    descricao = models.TextField(max_length=1000, help_text='Insirta uma breve descrição do objeto')
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.nome}'    

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, primary_key=True)
    dt_nasc = models.DateField()
    cep = models.CharField(max_length=8, help_text='Digite o CEP do seu endereço')
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=2)
    pais = models.CharField(max_length=50)
    foto = models.ImageField(upload_to = 'media/profile_pics/', default = 'media/profile_pics/no-image-icon.png')
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.user.first_name} {self.user.last_name}'   

#Integração do Profile com User
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


class Item(models.Model):
    nome = models.CharField(max_length=200, help_text='Digite o nome do objeto')
    autor = models.CharField(max_length=200, help_text='Digite o nome do autor, cantor, banda, criador, marca etc...')
    descricao = models.TextField(max_length=1000, help_text='Insirta uma breve descrição do objeto')
    dono = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.ForeignKey('TipoItem', on_delete=models.SET_NULL, null=True)
    foto = models.ImageField(upload_to = 'item_pics', default = 'item_pics/no-image-item.png')
    LOAN_STATUS = (
        ('e', 'Emprestado'),
        ('i', 'Indisponível'),
        ('d', 'Disponível'),
    )
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        default='d',
        help_text='Status do item',
    )
    dtCadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.tipo.nome}: {self.autor} - {self.nome} '


class Emprestimo(models.Model):
    dtEmprestimo = models.DateField()
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    pessoa = models.ForeignKey('Profile', on_delete=models.CASCADE)
    dtDevolucao = models.DateField()
    aberto = models.BooleanField()
    dtCadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['dtCadastro']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.item.dono.user.first_name} {self.item.dono.user.last_name} emprestou o {self.item} para {self.pessoa.user.first_name} {self.pessoa.user.last_name}'


