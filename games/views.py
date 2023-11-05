from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models, forms
from django.views import generic


class GameListViews(generic.ListView):
    template_name = 'games_template/games_list.html'
    queryset = models.Games.objects.all()

    def get_queryset(self):
        return models.Games.objects.all()


# def gameViews(request):
#     gameVal = models.Games.objects.all()
#     html_name = 'games_template/games_list.html'
#     context = {
#         'game_key': gameVal,
#     }
#     return render(request, html_name, context)


class GameDetailInfo(generic.DetailView):
    template_name = 'games_template/games_detail.html'

    def get_object(self, **kwargs):
        game_id = self.kwargs.get('id')
        return get_object_or_404(models.Games, id=game_id)

# def gameDetailInfo(request, id):
#     game_id = get_object_or_404(models.Games, id=id)
#     html_name = 'games_template/games_detail.html'
#     context = {
#         'game_id': game_id,
#     }
#     return render(request, html_name, context)

class GameCreateView(generic.CreateView):
    template_name = 'games_template/create_game.html'
    form_class = forms.GamesForm
    queryset = models.Games.objects.all()
    success_url = '/game_list'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(GameCreateView, self).form_valid(form=form)


# def gameCreateView(request):
#     method = request.method
#     if method == "POST":
#         form = forms.GamesForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Игра успешно добавлена')
#
#     else:
#         form = forms.GamesForm()
#
#     return render(request, 'games_template/create_game.html', {'form': form})

class DeleteGameView(generic.DeleteView):
    template_name = 'games_template/confirm_delete.html'
    success_url = '/game_list'

    def get_object(self, **kwargs):
        game_id = self.kwargs.get('id')
        return get_object_or_404(models.Games, id=game_id)

#def deleteGameView(request, id):
#    game_id = get_object_or_404(models.Games, id=id)
#    game_id.delete()
#    return HttpResponse('Игра успешно удалена')

class UpdateGameView(generic.UpdateView):
    template_name = 'games_template/update_game.html'
    form_class = forms.GamesForm
    success_url = '/game_list'

    def get_object(self, **kwargs):
        game_id = self.kwargs.get('id')
        return get_object_or_404(models.Games, id=game_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateGameView, self).form_valid(form=form)



#def updateGameView(request, id=id):
#    game_id = get_object_or_404(models.Games, id=id)
#    if request.method == 'POST':
#        form = forms.GamesForm(instance=game_id, data=request.POST)
#        if form.is_valid():
#            form.save()
#            return HttpResponse('Игра изменена')
#
#    else:
#        form = forms.GamesForm(instance=game_id)
#    return render(request, 'games_template/update_game.html',
#                         {
#                      'form': form,
#                      'game_id': game_id
#                         }
#                )

class Search(generic.ListView):
    template_name = 'games_template/games_list.html'
    context_object_name = 'game'
    paginate_by = 5

    def get_queryset(self):
        return models.Games.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


class FormCommentView(generic.CreateView):
    template_name = 'games_template/create_review.html'
    form_class = forms.ReviewForm
    queryset = models.ReviewGame.objects.all()
    success_url = '/game_list'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(FormCommentView, self).form_valid(form=form)