from django.core.paginator import Paginator
from django.shortcuts import render
from iplapp.models import Matches
from django.views import View

class SeasonView(View):
    def get(self, request,*args,** kwargs):
        seasons = Matches.objects.values('season').distinct()
        if(kwargs):
            ma = Matches.objects.values('id','date', 'team_1', 'team_2', 'venue', 'toss_winner', 'toss_decision', 'result',
                                       'player_of_match').filter(season=kwargs['sid'])
            # paginator = Paginator(ma, 8)
            # page = request.GET.get('page')
            # m = paginator.get_page(page)
            return render(request, 'seasons.html',
                          context={
                              'd': ma,
                              's':seasons
                          }
                          )
        m = Matches.objects.values('id','date', 'team_1', 'team_2', 'venue', 'toss_winner', 'toss_decision', 'result',
                                   'player_of_match').filter(season=2019)
        return render(request, 'seasons.html',
                      context={
                          'd': m,
                          's': seasons
                      }
                      )

