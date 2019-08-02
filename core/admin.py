from django.contrib import admin

from core.models import Movie, Session, Showtime, Seat, ItemSeat

admin.site.register(Movie)
admin.site.register(Session)
admin.site.register(Showtime)
admin.site.register(Seat)
admin.site.register(ItemSeat)
