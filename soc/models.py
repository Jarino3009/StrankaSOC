from django.db import models


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


class Tema(models.Model):
    nazov = models.CharField(max_length=155)
    popis =models.TextField()
    konzultant = models.ForeignKey(Ucitel, on_delete=models.SET_NULL, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)
    odbor = models.ForeignKey(Odbor, on_delete=models.SET_NULL, null=True, blank=True)
    dostupnost = models.CharField(max_length=10)
    pocet_konzultacii = models.IntegerField()

    def __str__(self):
        return f"{self.nazov} {self.popis} {self.konzultant} {self.student} {self.odbor} {self.dostupnost} {self.pocet_konzultacii}"