from django.contrib import admin
from reservation.models import Proprietor, Structure, Reservation, Guest


@admin.register(Proprietor)
class ProprietorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(Structure)
class StructureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'shift', 'state')
    list_filter = ('id', 'date', 'shift', 'state')
    search_fields = ('id', 'date', 'shift', 'state')


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone')
    list_filter = ('id', 'name', 'phone')
    search_fields = ('id', 'name', 'phone')
