import unittest
from spotyour2.quiz import testquizbuilder as tqb
from spotyour2.quiz import testplaygame as tpg

# Please make sure to run this file outside of the spotyour2 folder. 

def stats_suite():
    tests = unittest.TestLoader().discover(start_dir="spotyour2/stats", pattern="test*.py")
    # print("Tests: ", tests)
    if __name__ == "__main__":
        unittest.TextTestRunner(verbosity=2).run(tests)

def quiz_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(tqb.TestQuestion('test_getData'))
    suite.addTest(tqb.TestQuestion('test_checkerTrue'))
    suite.addTest(tqb.TestQuestion('test_checkerFalse'))
    suite.addTest(tqb.TestQuestion('test_invalidType'))

    suite.addTest(tqb.TestQuestionBuilder('test_makeQuestion'))
    suite.addTest(tqb.TestQuestionBuilder('test_artist_question'))
    suite.addTest(tqb.TestQuestionBuilder('test_label_question'))
    suite.addTest(tqb.TestQuestionBuilder('test_length_question'))
    suite.addTest(tqb.TestQuestionBuilder('test_age_question'))
    suite.addTest(tqb.TestQuestionBuilder('test_tempo_question'))
    
    suite.addTest(tpg.TestPlayGame('test_getOptions'))
    suite.addTest(tpg.TestPlayGame('test_setSeed'))
    suite.addTest(tpg.TestPlayGame('test_getScore'))
    suite.addTest(tpg.TestPlayGame('test_askQuestion'))
    suite.addTest(tpg.TestPlayGame('test_askQuestion'))
    suite.addTest(tpg.TestPlayGame('test_play'))
    
    runner = unittest.TextTestRunner(verbosity=2)
    print(runner.run(suite))

stats_suite()
quiz_suite()