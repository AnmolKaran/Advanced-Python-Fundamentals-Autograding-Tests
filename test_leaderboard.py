import unittest
from io import StringIO
from unittest.mock import patch
import re
# 
import leaderboard

class TestArcadeFunctions(unittest.TestCase):
    def setUp(self):
        # We use the original data, but also alternate data to ensure students didn't hardcode answers
        self.player_data = {
            "Zack": 1500, "Anmol": 5000, "Tyrone": 3000,
            "Alex": 2100, "Luigi": 1800, "Gigi": 2500, "Sam": 950
        }
        self.alt_data = {
            "PlayerA": 10, "PlayerB": 100, "PlayerC": 50
        }

    @patch('sys.stdout', new_callable=StringIO)
    def test_task1_print_alphabetical_roster(self, mock_stdout):
        arcade.print_alphabetical_roster(self.player_data)
        output = mock_stdout.getvalue().strip()
        
        expected_list_str = "['Alex', 'Anmol', 'Gigi', 'Luigi', 'Sam', 'Tyrone', 'Zack']"
        self.assertIn(
            expected_list_str, 
            output, 
            msg=f"Task 1 Failed: Expected output to contain {expected_list_str}."
        )

    def test_task2_find_champion(self):
        # Test with primary data
        champ = arcade.find_champion(self.player_data)
        self.assertEqual(champ, "Anmol", msg="Task 2 Failed: Did not find the correct champion in primary data.")
        
        # Test with alternate data to prevent hardcoding
        alt_champ = arcade.find_champion(self.alt_data)
        self.assertEqual(alt_champ, "PlayerB", msg="Task 2 Failed: Did not find the correct champion in hidden test data (did they hardcode 'Anmol'?).")

    def test_task3_lookup_score(self):
        # Test existing player
        alex_score = arcade.lookup_score("Alex", self.player_data)
        self.assertEqual(alex_score, 2100, msg="Task 3 Failed: Incorrect score returned for existing player.")
        
        # Test non-existing player
        mario_score = arcade.lookup_score("Mario", self.player_data)
        self.assertEqual(mario_score, "Player not found", msg="Task 3 Failed: Did not return 'Player not found' for missing player.")

    @patch('sys.stdout', new_callable=StringIO)
    def test_task4_print_leaderboard_by_score(self, mock_stdout):
        arcade.print_leaderboard_by_score(self.player_data)
        output = mock_stdout.getvalue()
        
        # Use regex to extract all numbers from the output to be robust against extra text/spaces
        numbers = re.findall(r'\d+', output)
        expected_scores = ["5000", "3000", "2500", "2100", "1800", "1500", "950"]
        
        self.assertEqual(
            numbers, 
            expected_scores, 
            msg="Task 4 Failed: Scores were not printed in the correct highest-to-lowest order."
        )

if __name__ == '__main__':
    unittest.main()
