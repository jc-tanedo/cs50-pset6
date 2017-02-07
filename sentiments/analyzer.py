import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        # TODO
        myFile = open(positives, "r")
        self.posDict = myFile.readlines()
        self.posDict = [x.strip("\n") for x in self.posDict]
        myFile.close()
        
        myFile = open(negatives, "r")
        self.negDict = myFile.readlines()
        self.negDict = [x.strip("\n") for x in self.negDict]
        myFile.close()

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        # TODO
        score = 0
        if text in self.posDict:
            score += 1
        elif text in self.negDict:
            score -= 1
        return score