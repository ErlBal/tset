from django import forms
from . import models, parser

class ParserGameForm(forms.Form):
    MEDIA_CHOISCES = (
        ('metarankings.ru', 'metarankings.ru'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOISCES)

    class Meta:
        fields = [
            'media_type',
        ]
    def parser_data(self):
        if self.data['media_type'] == 'metarankings.ru':
            game_parser = parser.parser()
            for i in game_parser:
                models.GameRoguelike.objects.create(**i)