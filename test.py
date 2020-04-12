from unittest import TestCase
from app import app
from flask import session, jsonify, json
from boggle import Boggle


class FlaskTests(TestCase):
    def setUp(self):
        """Before each test"""
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_home(self):
        with self.client:
            resp = self.client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>BOGGLE</h1>', html)
            self.assertIsNone(session.get('high_score'))
            self.assertIn('board', session)
            self.assertIn(b'Score:', resp.data)
            self.assertIn(b'Timer', resp.data)

    def test_valid_word(self):
        """Test if word is valid by modifying the board in the session"""
        with self.client:
            with self.client.session_transaction() as sess:
                sess['board'] = [["A", "B", "C", "C", "X"],
                                 ["A", "B", "C", "C", "X"], 
                                 ["A", "B", "C", "C", "X"],
                                 ["A", "B", "C", "C", "X"],
                                 ["C", "O", "R", "N", "X"]]

            resp = self.client.get('/check-word?word=corn')
            self.assertEqual(resp.json['result'], 'ok')

    def test_not_on_board(self):
        """Test if word is in the dictionary but not on the board"""
        self.client.get('/')
        resp = self.client.get('/check-word?word=literally')
        self.assertEqual(resp.json['result'], 'not-on-board')


    def test_non_english_word(self):
        """Test if word is on the board"""

        self.client.get('/')
        response = self.client.get(
            '/check-word?word=fsjdslkfjdlksf')
        self.assertEqual(response.json['result'], 'not-word')

    # def test_high_score(self):
    #     """Test if high score works"""
    #     with self.client:
    #         with self.client.session_transaction() as sess:
    #             sess['high_score'] = 99

    #         with app.app_context():
    #             data = jsonify({'score': 23})
    #         resp = self.client.post('/score', data)

    #         self.assertEqual(resp.status_code, 200)
    #         #self.assertTrue(resp.json['brokeRecord'])

