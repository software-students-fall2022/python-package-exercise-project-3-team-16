import pytest
from fortunetelleracs1029 import wisdom

class Tests:
    #
    # Fixtures - these are functions that can do any optional setup or teardown before or after a test function is run.
    #
    @pytest.fixture
    def example_fixture(self):
        '''
        An example of a pytest fixture - a function that can be used for setup and teardown before and after test functions are run.
        '''

        # place any setup you want to do before any test function that uses this fixture is run

        yield # at th=e yield point, the test function will run and do its business

        # place with any teardown you want to do after any test function that uses this fixture has completed

    def test_sanity_check(self, example_fixture):
        """
        Test debugging... making sure that we can run a simple test that always passes.
        Note the use of the example_fixture in the parameter list - any setup and teardown in that fixture will be run before and after this test function executes
        From the main project directory, run the `python3 -m pytest` command to run all tests.
        """
        expected = True # the value we expect to be present
        actual = True # the value we see in reality
        assert actual == expected, "Expected True to be equal to True!"


    def test_getCSFortune(self):
        """
        Verify getCSFortune() function and make sure it returns a non-empty string.
        """
        for i in range(100):
            actual = wisdom.getCSFortune("question", False)
            assert isinstance(actual, str), f"Expected get() to return a string. Instead, it returned {actual}"
            assert len(actual) > 0, f"Expected get() not to be empty. Instead, it returned a string with {len(actual)} characters"

        for i in range(100):
            actual = wisdom.getCSFortune("question", True)
            assert isinstance(actual, str), f"Expected get() to return a string. Instead, it returned {actual}"
            assert len(actual) > 0, f"Expected get() not to be empty. Instead, it returned a string with {len(actual)} characters"

    def test_getCSFortune_content(self):
        """
        Make sure that the text returned by the get() function is actually from the correct poem.
        """
        # the full text of the actual Jabberwocky poem by Lewis Carroll
        nondebug = []
        debug = [
            "You forgot a semicolon",
            "You forgot to close a bracket",
            "You misspelled a keyword",
            "Incorrect indentation",
            "Incorrect version",
            "There is no saving this one",
            "You are screwed. Switch major. Go next."
        ]

        # since get returns a random string, run it a bunch of times and verify the output
        for i in range(100):
            actual = wisdom.getCSFortune("question", False)
            allWords = actual.split()
            if allWords[-2].isnumeric():
                frontWords = allWords[:-2]
                frontWords = ' '.join(frontWords) + " " + allWords[-1]
                assert frontWords == "You are on the right track and will finish your assignment/project in days.", f"Expected the text returned by getCSFortune() to be a debug error fortune with expected completion.  Instead, it returned '{actual}'."
            else:
                assert actual == "You are screwed. Switch major. Go next.", f"Expected the text returned by getCSFortune() to be a debug error fortune.  Instead, it returned '{actual}'."

        for i in range(100):
            actual = wisdom.getCSFortune("question", True)
            assert actual in debug, f"Expected the text returned by getCSFortune() to be a fortune.  Instead, it returned '{actual}'."

    ########################
    def test_getLifeAdvice(self):
        """
        Verify getLifeAdvice() function and make sure it returns a non-empty string.
        """
        for i in range(100):
            actual = wisdom.getLifeAdvice("learning")
            assert isinstance(actual, str), f"Expected get() to return a string. Instead, it returned {actual}"
            assert len(actual) > 0, f"Expected get() not to be empty. Instead, it returned a string with {len(actual)} characters"

        for i in range(100):
            actual = wisdom.getLifeAdvice("detach")
            assert isinstance(actual, str), f"Expected get() to return a string. Instead, it returned {actual}"
            assert len(actual) > 0, f"Expected get() not to be empty. Instead, it returned a string with {len(actual)} characters"
            
    def test_getLifeAdvice_category(self):
        """
        Verify that getLifeAdvice is pulling from the right list given the category
        """
        learning = [
            "Whatever you do, give it 100%",
            "Never stop learning",
            "Your thinking changes your life",
            "Be kind to people; treat people as you'd like to be treated",
            "Starting is the hardest part"
        ]
        
        detach = [
            "Forgive and let go",
            "You can't contorl others",
            "Find your own happy",
            "Don't react, respond",
            "Meditate on it"
        ]
        
        actual = wisdom.getLifeAdvice("learning")
        assert actual in learning, f"Expected to return a result from learning. Instead, returned something not in learning"
        
        actual = wisdom.getLifeAdvice("detach")
        assert actual in detach, f"Expected to return a result from detach. Instead, returned something not in learning"

    ##########
    def test_getInspired(self):
        # trying to verify that the right quote is being returned given a particular name

        LS_quotes = [
            "Do the scary thing first, and get scared later.",
            "All cannot be lost when there is still so much being found.",
            "When things don\'t go right, go left.",
            "Sometimes the things you\'ve lost can be found again in unexpected places."
        ]

        AE_quotes = [
            "The most difficult thing is the decision to act, the rest is merely tenacity."
        ]

        AB_quotes = [
            ("Don't settle for average. Bring your best to the moment. Then, whether it fails or succeeds, "
            "at least you know you gave all you had.")
        ]

        BES_quotes = [
            "I have stood on a mountain of no\'s for one yes."
        ]

        MAR_quotes = [
            ("Courage doesn't always roar. Sometimes courage is a quiet voice at the end of the day saying, "
            "\"I will try again tomorrow.\"")
        ]

        MA_quotes = [
            ("Courage is the most important of all the virtues because without courage, "
            "you can't practice any other virtue consistently.")
        ]

        FD_quotes = [
            "If there is no struggle, there is no progress."
        ]

        actualLS = wisdom.getInspiration("Lemony Snicket")
        assert actualLS in LS_quotes, f"Expected to return a quote from LS_quotes, instead returned something else"

        actualAE = wisdom.getInspiration("Amelia Earhart")
        assert actualAE in AE_quotes, f"Expected to return a quote from AE_quotes, instead returned something else"
        
        actualAB = wisdom.getInspiration("Angela Bassett")
        assert actualAB in AB_quotes, f"Expected to return a quote from AB_quotes, instead returned something else"

        actualBES = wisdom.getInspiration("Barbara Elaine Smith")
        assert actualBES in BES_quotes, f"Expected to return a quote from BES_quotes, instead returned something else"

        actualMAR = wisdom.getInspiration("Mary Anne Radmacher")
        assert actualMAR in MAR_quotes, f"Expected to return a quote from MAR_quotes, instead returned something else"

        actualMA = wisdom.getInspiration("Maya Angelou")
        assert actualMA in MA_quotes, f"Expected to return a quote from MA_quotes, instead returned something else"

        actualFD = wisdom.getInspiration("Frederick Douglass")
        assert actualFD in FD_quotes, f"Expected to return a quote from FD_quotes, instead returned something else"
