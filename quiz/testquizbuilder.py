import unittest
import random
from spotyour3.stats import readdata as rd
from spotyour3.quiz.quizbuilder import Question, QuestionBuilder

class TestQuestion(unittest.TestCase):
    """Test the Question class"""
    
    @classmethod
    def setUpClass(cls):
        cls.testpl = rd.Playlist("spotyour3/playlist")
        
    def setUp(self):
        self.question = Question(self.testpl)
        
    def tearDown(self):
        self.question = None
        
    @classmethod
    def tearDownClass(cls):
        cls.testpl = None
    
    def test_getData(self):
        data = self.question.getdata()
        self.assertEqual(len(data), 4, "Number of songs return is not 4")
        
    def test_checkerTrue(self):
        self.assertTrue(self.question.checker("True", "True"))
    
    def test_checkerFalse(self):
        self.assertFalse(self.question.checker("False", "True"))
        
    def test_invalidType(self):
        with self.assertRaises(ValueError):
            self.question.makequestion("invalid")
        

class TestQuestionBuilder(unittest.TestCase):
    """Test the QuestionBuilder class"""
    
    @classmethod
    def setUpClass(cls):
        cls.testpl = rd.Playlist("spotyour3/playlist")
        
    def setUp(self):
        self.qBuilder = QuestionBuilder(self.testpl)
    
    def tearDown(self):
        self.qBuilder = None
    
    @classmethod
    def tearDownClass(cls):
        cls.testpl = None

    def test_makeQuestion(self):
        question, options, solution = self.qBuilder.makequestion("artist")
        cur_question = self.qBuilder.cur_question
        cur_options = self.qBuilder.cur_options
        cur_solution = self.qBuilder.cur_solution
        self.assertEqual(cur_question, question, f"cur_question: {cur_question} does not match with question: {question}")
        self.assertEqual(cur_options, options, f"cur_options: {cur_options} does not match with options: {options}")
        self.assertEqual(cur_solution, solution, f"cur_solution: {cur_solution} does not match with solution: {solution}")
    
    def test_artist_question(self):
        question, options, solution = self.qBuilder.artist_question()
        self.assertIn(solution, options, "solution is not in the option list")
        self.assertIsInstance(question, str, "question is not string")
        self.assertIn(len(options), [3,4], "option length is not 3 or 4")
        
    def test_label_question(self):
        question, options, solution = self.qBuilder.label_question()
        self.assertIn(solution, options, "solution is not in the option list")
        self.assertIsInstance(question, str, "question is not string")
        self.assertIn(len(options), [3,4], "option length is not 3 or 4")
        
    def test_length_question(self):
        question, options, solution = self.qBuilder.length_question()
        self.assertIn(solution, options, "solution is not in the option list")
        self.assertIsInstance(question, str, "question is not string")
        self.assertIn(len(options), [3,4], "option length is not 3 or 4")
        
    def test_age_question(self):
        question, options, solution = self.qBuilder.age_question()
        self.assertIn(solution, options, "solution is not in the option list")
        self.assertIsInstance(question, str, "question is not string")
        self.assertIn(len(options), [3,4], "option length is not 3 or 4")
        
    def test_tempo_question(self):
        question, options, solution = self.qBuilder.tempo_question()
        self.assertIn(solution, options, "solution is not in the option list")
        self.assertIsInstance(question, str, "question is not string")
        self.assertIn(len(options), [3,4], "option length is not 3 or 4")
        
unittest.main(argv =[''], verbosity=2, exit=False)