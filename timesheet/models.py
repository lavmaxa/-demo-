from django.db import models

class IMIT(models.Model):
    title = models.CharField(max_length=150)
    book = models.FileField(upload_to='media')

    def __str__(self):
        return self.title

class Physicists(models.Model):
    title = models.CharField(max_length=150)
    book = models.FileField(upload_to='media')

    def __str__(self):
        return self.title

class LAU(models.Model):
    title = models.CharField(max_length=150)
    book = models.FileField(upload_to='media')

    def __str__(self):
        return self.title

class PI(models.Model):
    title = models.CharField(max_length=150)
    book = models.FileField(upload_to='media')

    def __str__(self):
        return self.title


class MIEL(models.Model):
    title = models.CharField(max_length=150)
    book = models.FileField(upload_to='media')

    def __str__(self):
        return self.title


class INYAZ(models.Model):
    title = models.CharField(max_length=150)
    book = models.FileField(upload_to='media')

    def __str__(self):
        return self.title


class ISN(models.Model):
    title = models.CharField(max_length=150)
    book = models.FileField(upload_to='media')

    def __str__(self):
        return self.title


class BMB(models.Model):
    title = models.CharField(max_length=150)
    book = models.FileField(upload_to='media')

    def __str__(self):
        return self.title


class BIO(models.Model):
    title = models.CharField(max_length=150)
    book = models.FileField(upload_to='media')

    def __str__(self):
        return self.title


class GEOG(models.Model):
    title = models.CharField(max_length=150)
    book = models.FileField(upload_to='media')

    def __str__(self):
        return self.title


class HIST(models.Model):
    title = models.CharField(max_length=150)
    book = models.FileField(upload_to='media')

    def __str__(self):
        return self.title


class SAF(models.Model):
    title = models.CharField(max_length=150)
    book = models.FileField(upload_to='media')

    def __str__(self):
        return self.title


class SR(models.Model):
    title = models.CharField(max_length=150)
    book = models.FileField(upload_to='media')

    def __str__(self):
        return self.title


class PSY(models.Model):
    title = models.CharField(max_length=150)
    book = models.FileField(upload_to='media')

    def __str__(self):
        return self.title


class CHEM(models.Model):
    title = models.CharField(max_length=150)
    book = models.FileField(upload_to='media')

    def __str__(self):
        return self.title
