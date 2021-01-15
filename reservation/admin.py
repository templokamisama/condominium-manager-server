from django.contrib import admin
from reservation.models import Proprietor, ReservationShift, ReservationStates


@admin.register(Proprietor)
class ProprietorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(ReservationShift)
class ReservationShiftAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(ReservationStates)
class ReservationStatesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')
    search_fields = ('id', 'name')