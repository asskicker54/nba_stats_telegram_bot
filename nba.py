from operator import pos
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
    pl = [p for p in player_dict if p['full_name'].lower() == name.lower()][0]

    return pl['id'] #Returns int


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

def compare_players(id1, id2):
    p1_stats = get_player_stats(id1)[1]
    p2_stats = get_player_stats(id2)[1]

    stats = {
        'post_season': {
            'PTS' : round(p1_stats['post_season']['PTS'] - p2_stats['post_season']['PTS'], 2),
            'AST' : round(p1_stats['post_season']['REB'] - p2_stats['post_season']['REB'], 2),
            'REB' : round(p1_stats['post_season']['AST'] - p2_stats['post_season']['AST'], 2),
            'BLK' : round(p1_stats['post_season']['BLK'] - p2_stats['post_season']['BLK'], 2),
            'STL' : round(p1_stats['post_season']['STL'] - p2_stats['post_season']['STL'], 2),
            'TOV' : round(p1_stats['post_season']['TOV'] - p2_stats['post_season']['TOV'], 2) * -1
        }, 

        'reg_season' : {
            'PTS' : round(p1_stats['reg_season']['PTS'] - p2_stats['reg_season']['PTS'], 2),
            'AST' : round(p1_stats['reg_season']['AST'] - p2_stats['reg_season']['AST'], 2),
            'REB' : round(p1_stats['reg_season']['REB'] - p2_stats['reg_season']['REB'], 2),
            'BLK' : round(p1_stats['reg_season']['BLK'] - p2_stats['reg_season']['BLK'], 2),
            'STL' : round(p1_stats['reg_season']['STL'] - p2_stats['reg_season']['STL'], 2),
            'TOV' : round(p1_stats['reg_season']['TOV'] - p2_stats['reg_season']['TOV'], 2) * -1
        }

    }

    return stats

print(compare_players(find_player_by_name('LeBron James'), find_player_by_name('Michael Jordan')))
