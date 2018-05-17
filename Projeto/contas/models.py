from django.db import models

# Create your models here.
class Usuario(models.Model):

    email = models.EmailField(db_column='Email', max_length=255, unique=True)
    senha = models.CharField(db_column='Senha', max_length=140)

    class Meta:
        db_table = 'Usuario'
