import unittest
from players import Player, Quarterback, DefensivePlayer
from possible_values import *
from game import Game
# TODO - some things you can add...
import season

# import the `season` file and make sure generate_random_games only
# makes games with appropriate team names (and never has a team playing itself)

# Complete the FootballGameTest

class FootballGameTest(unittest.TestCase):
    '''test the class'''
    def test_field_goal_made(self):
        g = Game(teams=['Redskins','Browns'])
        p = Game(teams=['Redskins','Browns'])
        g.field_goal('Redskins')
        self.assertEqual(g.score['Redskins'] - 3, p.score['Redskins'])

    def test_get_winner(self):
        g = Game(teams=['Redskins','Browns'])
        p = Game(teams=['Redskins','Browns'])
        g.touchdown('Browns')
        self.assertGreater(g.score['Browns'], g.score['Redskins'])

class FootballPlayerTest(unittest.TestCase):
    '''Check the default values for Player and Quarterback
    yards=120, touchdowns=5, safety=1,
                 interceptions=0
    '''
    def test_default_player_yards(self):
        player = Player(name='Dude')
        self.assertEqual(player.yards, 120)

    def test_player_yards_set_to(self):
        player = Player(name='OtherDude', yards=150)
        self.assertEqual(player.yards, 150)

    def test_default_qb_interceptions(self):
        qb = Quarterback(name='FancyDude')
        self.assertEqual(qb.interceptions, 4)

    def test_default_qb_completed_passes(self):
        qb = Quarterback()
        self.assertEqual(qb.completed_passes, 20)

    def test_passing_score(self):
        qb = Quarterback()
        self.assertEqual((20 - (2 * 4)), qb.passing_score())

    def test_dplayer_tackles(self):
        d = DefensivePlayer('Bob')
        self.assertEqual(d.tackles, 12)

    def test_dplayer_sacks(self):
        d = DefensivePlayer()
        self.assertEqual(d.sacks, 2)

    def test_dplayer_yards(self):
        d = DefensivePlayer()
        self.assertEqual(d.yards, 20)

    def test_dplayer_interceptions(self):
        d = DefensivePlayer()
        self.assertEqual(d.interceptions, 1)

if __name__ == '__main__':
    unittest.main()
