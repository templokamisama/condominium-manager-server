from django.db import models

class Proprietor(models.Model):
    name = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    block = models.IntegerField()
    lot = models.IntegerField()
    principal_phone = models.CharField(max_length=14)
    secondary_phone = models.CharField(max_length=14)

    def __str__(self):
        return f'Proprietor: {self.id} - {self.name} - {self.cpf}'

class ReservationShift(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'Reservation shift: {self.id} - {self.name}'

class ReservationStates(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'Reservation states: {self.id} - {self.name}'
