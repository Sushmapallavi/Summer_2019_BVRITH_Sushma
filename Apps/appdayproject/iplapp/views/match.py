from django.shortcuts import render
from iplapp.models import Matches, Deliveries
from django.views import View

class MatchView(View):
    def get(self, request,*args,** kwargs):
        #m = Matches.objects.get(id=kwargs['id'])
        m = Matches.objects.values('team_1', 'team_2','toss_winner', 'toss_decision', 'result',
                                   'player_of_match','winner').filter(id=kwargs['id'])
        i1 = Deliveries.objects.values('inning','batting_team','bowling_team','over','total_runs','player_dismissed').filter(match=kwargs['id'],inning=1)
        i2 = Deliveries.objects.values('inning', 'batting_team', 'bowling_team', 'over', 'total_runs',
                                       'player_dismissed').filter(match=kwargs['id'],inning=2)
        return render(request, 'match.html',
                      context={
                          'match': m,
                          'innings1': i1,
                          'innings2': i2
                      }
                      )