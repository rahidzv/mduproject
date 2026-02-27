from django.db import models


class Abuneci(models.Model):
    # xeberler bulleteni abunecileri
    email = models.EmailField(unique=True, verbose_name='E-poct')
    tarix = models.DateTimeField(auto_now_add=True, verbose_name='Abune tarixi')

    class Meta:
        verbose_name = 'Abuneci'
        verbose_name_plural = 'Abuneciler'
        ordering = ['-tarix']

    def __str__(self):
        return self.email


class ElaqeMesaji(models.Model):
    # elaqe sehifesinden gelen mesajlar
    ad = models.CharField(max_length=100, verbose_name='Ad')
    email = models.EmailField(verbose_name='E-poct')
    mesaj = models.TextField(verbose_name='Mesaj')
    tarix = models.DateTimeField(auto_now_add=True, verbose_name='Gonderilme tarixi')
    oxunub = models.BooleanField(default=False, verbose_name='Oxunub')

    class Meta:
        verbose_name = 'Elaqe mesaji'
        verbose_name_plural = 'Elaqe mesajlari'
        ordering = ['-tarix']

    def __str__(self):
        return f'{self.ad} — {self.email}'
