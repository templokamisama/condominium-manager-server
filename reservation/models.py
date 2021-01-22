from django.db import models
from djchoices import ChoiceItem, DjangoChoices


class Proprietor(models.Model):
    name = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    block = models.IntegerField(null=True, blank=True, default=None)
    lot = models.IntegerField()
    principal_phone = models.CharField(max_length=14)
    secondary_phone = models.CharField(max_length=14, null=True, blank=True, default=None)

    def __str__(self):
        return f'Proprietor: {self.id} - {self.name} - {self.cpf}'


class Structure(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True, default=None)
    longitude = models.CharField(max_length=15, null=True, blank=True, default=None)
    latitude = models.CharField(max_length=15, null=True, blank=True, default=None)
    available = models.BooleanField()
    image = models.FileField(null=True, blank=True, default=None)


class Reservation(models.Model):
    class ReservationShiftChoices(DjangoChoices):
        morning = ChoiceItem('MANHA')
        evening = ChoiceItem('TARDE')
        night = ChoiceItem('NOITE')

    class ReservationStateChoices(DjangoChoices):
        initial = ChoiceItem('CONFIRMADO')
        free = ChoiceItem('LIVRE')
        pending = ChoiceItem('PENDENTE')
        unavailable = ChoiceItem('INDISPONIVEL')
        occupied = ChoiceItem('OCUPADO')

    date = models.DateField()
    proprietor = models.ForeignKey(Proprietor, on_delete=models.CASCADE, related_name="reservation")
    shift = models.CharField(max_length=5, choices=ReservationShiftChoices.choices)
    state = models.CharField(max_length=12, choices=ReservationStateChoices.choices)


class Guest(models.Model):
    name = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11, null=True, blank=True, default=None)
    phone = models.CharField(max_length=20)
    reservation = models.ForeignKey(Reservation, on_delete=models.SET_NULL, blank=True, null=True, default=None, related_name="guest")
