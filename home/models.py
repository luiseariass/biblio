from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
array_choices = (
(1,"Distrito Capital"),
(2,"Amazonas"),
(3,"Anzoátegui"),
(4,"Apure"),
(5,"Aragua"),
(6,"Barinas"),
(7,"Bolívar"),
(8,"Carabobo"),
(9,"Cojedes"),
(10,"Delta Amacuro"),
(11,"Falcón"),
(12,"Guárico"),
(13,"Lara"),
(14,"Mérida"),
(15,"Miranda"),
(16,"Monagas"),
(17,"Nueva Esparta"),
(18,"Portuguesa"),
(19,"Sucre"),
(20,"Táchira"),
(21,"Trujillo"),
(22,"Vargas"),
(23,"Yaracuy"),
(24,"Zulia"))

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    estado = models.CharField(max_length=80, choices=array_choices,default=1,blank=True,null=True)
    email_confirmed = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()