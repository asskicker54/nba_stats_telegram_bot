from operator import pos
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats

player_dict = players.get_players()
stats_idx = {
    'TEAM': 2, 
    'PTS' : 23, 
    'AST' : 18,
    'REB' : 17,
    'BLK' : 20,
    'STL' : 19,
    'TOV' : 21
}

def find_player_by_name(name):
    pl = [p for p in player_dict if p['full_name'] == name][0]
    return pl['id'] #Returns int

def print_player_stats(id):
    player_info = playercareerstats.PlayerCareerStats(player_id=id)
    rs = player_info.career_totals_regular_season.get_dict()['data']
    ps = player_info.career_totals_post_season.get_dict()['data']
    
    stats = {
        'post_season': {
            'TEAM': ps[0][stats_idx['TEAM']], 
            'PTS' : ps[0][stats_idx['PTS']],
            'AST' : ps[0][stats_idx['AST']],
            'REB' : ps[0][stats_idx['REB']],
            'BLK' : ps[0][stats_idx['BLK']],
            'STL' : ps[0][stats_idx['STL']],
            'TOV' : ps[0][stats_idx['TOV']]
        }, 

        'reg_season': {
            'TEAM': rs[0][stats_idx['TEAM']], 
            'PTS' : rs[0][stats_idx['PTS']],
            'AST' : rs[0][stats_idx['AST']],
            'REB' : rs[0][stats_idx['REB']],
            'BLK' : rs[0][stats_idx['BLK']],
            'STL' : rs[0][stats_idx['STL']],
            'TOV' : rs[0][stats_idx['TOV']]
        }

    }
    return stats
    
print(print_player_stats(find_player_by_name('LeBron James')))

