from django.db import models

# Create your models here.
class Jadwal(models.Model):
    tanggal = models.CharField(max_length=50)
    imsak   = models.TimeField()
    subuh   = models.TimeField()
    terbit  = models.TimeField()
    duha    = models.TimeField()
    zuhur   = models.TimeField()
    ashar   = models.TimeField()
    magrib  = models.TimeField()
    isya    = models.TimeField()

    def __str__(self):
        return self.tanggal

    