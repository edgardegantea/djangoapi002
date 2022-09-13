from django.db import models


# Create your models here.
class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=100, verbose_name='Nombre')
    eemail = models.EmailField(verbose_name='Correo electrónico')
    econtact = models.CharField(verbose_name='Contacto', max_length=15)

    class Meta:
        db_table = "employee"
