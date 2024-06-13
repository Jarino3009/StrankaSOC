from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Ucitel(models.Model):
    meno = models.CharField(max_length=20)
    priezvisko = models.CharField(max_length=20)
    email = models.CharField(max_length=55)
    heslo = models.CharField(max_length=55)

    def __str__(self):
        return f"{self.meno} {self.priezvisko}"
        
    class Meta:
        verbose_name = "Učiteľ"
        verbose_name_plural = "Učitelia"
        ordering = ["priezvisko"]

class Student(models.Model):
    meno = models.CharField(max_length=20)
    priezvisko = models.CharField(max_length=20)
    email = models.CharField(max_length=55)
    heslo = models.CharField(max_length=55)

    def __str__(self):
        return f"{self.meno} {self.priezvisko}"
    
    class Meta:
        verbose_name = "Študent"
        verbose_name_plural = "Študenti"
        ordering = ["priezvisko"]

class Odbor(models.Model):
    nazov = models.CharField(max_length=55)

    def __str__(self):
        return f"{self.nazov}"
    
    class Meta:
        verbose_name = "Odbor"
        verbose_name_plural = "Odbory"

class Dostupnost(models.Model):
    nazov = models.CharField(max_length = 25)

    def __str__(self):
        return f"{self.nazov}"
    
    class Meta:
        verbose_name = "Dostupnosť"
        verbose_name_plural = "Dostupnosť" 

class Tema(models.Model):
    POCET_CHOICES = [
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
    ]
    nazov = models.CharField(max_length=155)
    popis = models.TextField()
    konzultant = models.ForeignKey(Ucitel, on_delete=models.SET_NULL, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)
    odbor = models.ForeignKey(Odbor, on_delete=models.SET_NULL, null=True, blank=True)
    dostupnost = models.ForeignKey(Dostupnost, on_delete=models.SET_NULL, null=True, blank=True)
    pocet_konzultacii = models.IntegerField(choices=POCET_CHOICES, default=0)

    def __str__(self):
        return f"{self.nazov}"
    
    class Meta:
        verbose_name = "Téma"
        verbose_name_plural = "Témy"
        ordering = ["dostupnost"]