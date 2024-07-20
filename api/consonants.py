from django.db import models

class EstadosEntidades(models.IntegerChoices):
    SIN_ACTIVAR = 0, "Sin activar / Nuevo"
    ACTIVO = 1, "Activo"
    SUSPENDIDO = 2, "Suspendido"
    DE_BAJA = 9, "De baja"

class TiposAfectacionIgv(models.IntegerChoices):
    AFECTO_IGV = 1, "Afecto al IGV"
    EXONERADO = 2, "Exonerado al IGV"
    INAFECTO = 3, "Inafecto al IGV"
