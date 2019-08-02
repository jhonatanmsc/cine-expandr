import pdb
import datetime
from functools import reduce

from django.contrib.auth import logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView

from core.models import Movie, Session, Showtime, Seat, ItemSeat


class HomeView(TemplateView):
    name = 'home'
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        dias = []
        for i in range(5):
            diasemana = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']
            mes = [
                'jan', 'fev', 'mar', 'abr', 'mai', 'jun',
                'jul', 'ago', 'set', 'out', 'nov', 'dez'
            ]
            data = datetime.date.today() + datetime.timedelta(i)
            descr = ''
            if data == datetime.date.today():
                descr = 'Hoje'
            elif data == datetime.date.today() + datetime.timedelta(1):
                descr = 'Amanhã'
            else:
                descr = f'{diasemana[data.weekday()]}, {data.day} de {mes[data.month]}'
            dias.append({
                "data": data.strftime("%d-%m-%y"),
                "descr": descr
            })
        context['dias'] = dias
        context['movies'] = Movie.objects.filter(
            session__showtime__start_at__date=datetime.datetime.today()
        ).distinct()
        context['showtimes'] = []
        for movie in context['movies']:
            context['showtimes'] += Showtime.objects.filter(
                session__movie=movie,
                start_at__date=datetime.datetime.today()
            )

        return context


class CartazView(TemplateView):
    name = 'cartaz'
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(CartazView, self).get_context_data(**kwargs)
        dias = []
        for i in range(5):
            diasemana = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']
            mes = [
                'jan', 'fev', 'mar', 'abr', 'mai', 'jun',
                'jul', 'ago', 'set', 'out', 'nov', 'dez'
            ]
            data = datetime.date.today() + datetime.timedelta(i)
            descr = ''
            if data == datetime.date.today():
                descr = 'Hoje'
            elif data == datetime.date.today() + datetime.timedelta(1):
                descr = 'Amanhã'
            else:
                descr = f'{diasemana[data.weekday()]}, {data.day} de {mes[data.month]}'
            dias.append({
                "data": data.strftime("%d-%m-%y"),
                "descr": descr
            })
        context['dias'] = dias
        context['movies'] = Movie.objects.filter(
            session__showtime__start_at__date=datetime.datetime.strptime(context['data'], '%d-%m-%y')
        ).distinct()
        context['showtimes'] = []
        for movie in context['movies']:
            context['showtimes'] += Showtime.objects.filter(
                session__movie=movie,
                start_at__date=datetime.datetime.strptime(context['data'], '%d-%m-%y')
            )
        return context


class ReservarView(TemplateView):
    name = 'reservar'
    template_name = 'reservar.html'

    def get_context_data(self, **kwargs):
        context = super(ReservarView, self).get_context_data(**kwargs)
        context['showtime'] = Showtime.objects.get(id=context['pk'])
        p_1 = ["D", "C", "B", "A"]
        p_2 = ["H", "G", "F", "E"]
        context['p_1'] = Seat.objects.filter(reduce(lambda x, y: x | y, [Q(description__contains=char) for char in p_1]))
        context['p_2'] = Seat.objects.filter(reduce(lambda x, y: x | y, [Q(description__contains=char) for char in p_2]))
        return context


class SelectReservaView(View):
    name = 'select'

    def post(self, request, pk, pk_time, seat):
        seat_obj = Seat.objects.get(description=seat)
        if request.user.is_authenticated:
            ItemSeat.objects.create(showtime_id=pk_time, seat=seat_obj, user=request.user)
        return redirect('reservar', pk=pk)


@login_required
def logoutView(request):
    logout(request)
    return redirect('login')


class CreateUserView(View):
    name = 'create-user'

    def post(self, request):
        userDATA = request.POST
        userDATA
        if userDATA['password'][0] == userDATA['confirm'][0]:
            # pdb.set_trace()
            user, created = User.objects.get_or_create(username=userDATA['username'])
            user.set_password(userDATA['password'])
            authenticate(user)
            user.save()
        return redirect('home')
