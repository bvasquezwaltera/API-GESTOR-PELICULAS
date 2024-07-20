from django.db import models
from .consonants import EstadosEntidades, TiposAfectacionIgv

# Definir la función upload_to si no está definida previamente.
def upload_to(instance, filename):
    return 'avatars/{filename}'.format(filename=filename)


# Create your models here.

class Distrito(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'distritos'
        ordering = ['nombre']

class Empresa(models.Model):
    empresa_id = models.CharField(max_length=5,primary_key=True)
    empresa_nro_ruc = models.CharField(max_length=11,null=False,unique=True)
    empresa_razon_social = models.CharField(max_length=150,null=False)
    empresa_acronimo = models.CharField(max_length=5,null=False)
    empresa_direccion = models.CharField(max_length=150,null=False)
    empresa_avatar = models.ImageField(upload_to=upload_to, blank=True, null=True)
    empresa_estado = models.IntegerField(choices=EstadosEntidades.choices,default=EstadosEntidades.ACTIVO)

    def __str__(self):
        return '%s - %s - %s' % (self.empresa_id, self.empresa_razon_social, self.empresa_acronimo)
    
    class Meta:
        db_table = 'empresas'
        ordering = ['empresa_id']

class Sucursal(models.Model):
    sucursal_id = models.CharField(max_length=5,primary_key=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.RESTRICT,null=False)
    sucursal_nombre = models.CharField(max_length=150,null=False)
    sucursal_direccion = models.CharField(max_length=150,null=False)
    sucursal_acronimo = models.CharField(max_length=15,null=True)
    sucursal_ubigeo = models.ForeignKey(Distrito, on_delete=models.RESTRICT,null=EstadosEntidades.ACTIVO)

    def __str__(self):
        return '%s - %s - %s' % (self.sucursal_id, self.sucursal_acronimo, self.sucursal_nombre)
    
    class Meta:
        db_table = 'sucursales'
        ordering = ['sucursal_id']

