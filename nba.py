from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats


stats_idx = { 
    'G' : 3,
    'PTS' : 23, 
    'AST' : 18,
    'REB' : 17,
    'BLK' : 20,
    'STL' : 19,
    'TOV' : 21
}

def find_player_by_name(name):
    player_dict = players.get_players()
    try:
        pl = [p for p in player_dict if p['full_name'].lower() == name.lower()][0]
        return pl['id']
    except Exception:
        return 0


def get_player_stats(id):
    player_info = playercareerstats.PlayerCareerStats(player_id=id)
    rs = player_info.career_totals_regular_season.get_dict()['data']
    ps = player_info.career_totals_post_season.get_dict()['data']
    
    stats_total = {
        'post_season': { 
            'G'   : ps[0][stats_idx['G']],
            'PTS' : ps[0][stats_idx['PTS']],
            'AST' : ps[0][stats_idx['AST']],
            'REB' : ps[0][stats_idx['REB']],
            'BLK' : ps[0][stats_idx['BLK']],
            'STL' : ps[0][stats_idx['STL']],
            'TOV' : ps[0][stats_idx['TOV']]
        }, 

        'reg_season': {
            'G'   : rs[0][stats_idx['G']],
            'PTS' : rs[0][stats_idx['PTS']],
            'AST' : rs[0][stats_idx['AST']],
            'REB' : rs[0][stats_idx['REB']],
            'BLK' : rs[0][stats_idx['BLK']],
            'STL' : rs[0][stats_idx['STL']],
            'TOV' : rs[0][stats_idx['TOV']]
        }

    }

    stats_avg = {
        'post_season': { 
            'PTS' : round(stats_total['post_season']['PTS'] / stats_total['post_season']['G'], 2),
            'AST' : round(stats_total['post_season']['AST'] / stats_total['post_season']['G'], 2),
            'REB' : round(stats_total['post_season']['REB'] / stats_total['post_season']['G'], 2),
            'BLK' : round(stats_total['post_season']['BLK'] / stats_total['post_season']['G'], 2),
            'STL' : round(stats_total['post_season']['STL'] / stats_total['post_season']['G'], 2),
            'TOV' : round(stats_total['post_season']['TOV'] / stats_total['post_season']['G'], 2)
        }, 

        'reg_season': {
            'PTS' : round(stats_total['reg_season']['PTS'] / stats_total['reg_season']['G'], 2),
            'AST' : round(stats_total['reg_season']['AST'] / stats_total['reg_season']['G'], 2),
            'REB' : round(stats_total['reg_season']['REB'] / stats_total['reg_season']['G'], 2),
            'BLK' : round(stats_total['reg_season']['BLK'] / stats_total['reg_season']['G'], 2),
            'STL' : round(stats_total['reg_season']['STL'] / stats_total['reg_season']['G'], 2),
            'TOV' : round(stats_total['reg_season']['TOV'] / stats_total['reg_season']['G'], 2)
        }

    }

    return stats_total, stats_avg

