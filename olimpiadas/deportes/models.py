from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=64, unique=True)


class Deporte(models.Model):
    nombre = models.CharField(max_length=64, unique=True)
    categoria = models.ForeignKey(Categoria,
                                  on_delete=models.CASCADE,
                                  default=1)


class Estado(models.Model):
    nombre = models.CharField(max_length=32, unique=True)
    abreviado = models.CharField(max_length=4)

    class Meta:
        ordering = ('nombre', )

    def __str__(self):
        return f'{self.nombre}, {self.abreviado}'


class Escuela(models.Model):
    nombre = models.CharField(max_length=128, unique=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    ciudad = models.CharField(max_length=64)
    direccion = models.CharField(max_length=128)
    cp = models.CharField(max_length=5)


class Sede(models.Model):
    nombre = models.CharField(max_length=128, unique=True)
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    ciudad = models.CharField(max_length=64)
    direccion = models.CharField(max_length=128)
    cp = models.CharField(max_length=5)


class Competencia(models.Model):
    nombre = models.CharField(max_length=128)
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)
    sede = models.ManyToManyField(Sede)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
