from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from . import models, parser, forms

class ParserGameListView(generic.ListView):
    model = models.GameRoguelike
    template_name = 'parser/game_parser_list.html'

    def get_queryset(self):
        return models.GameRoguelike.objects.all()


class ParserFormView(generic.FormView):
    template_name = 'parser/start_pars.html'
    form_class = forms.ParserGameForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('Успешно')
        else:
            return super(ParserFormView, self).post(request, *args, **kwargs)
