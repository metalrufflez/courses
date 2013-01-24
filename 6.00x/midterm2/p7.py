import random, pylab

def sampleQuizzes():
    # Your code here
    targetCount = 0
    trials = 10000
    for i in range(trials):
        midterm1 = random.randint(50,80)
        midterm2 = random.randint(60,90)
        finalExam = random.randint(55,95)

        finalScore = midterm1*.25 + midterm2*.25 + finalExam*.5

        if finalScore >= 70 and finalScore <= 75:
            targetCount += 1

    return float(targetCount) / trials

def generateScores(numTrials):
    """
    Runs numTrials trials of score-generation for each of
    three exams (Midterm 1, Midterm 2, and Final Exam).
    Generates uniformly distributed scores for each of 
    the three exams, then calculates the mean score and
    appends it to a list of scores.
    
    Returns: A list of numTrials scores.
    """
    scores = []
    for i in range(numTrials):
        midterm1 = random.randint(50,80)
        midterm2 = random.randint(60,90)
        finalExam = random.randint(55,95)

        finalScore = midterm1*.25 + midterm2*.25 + finalExam*.5

        scores.append(finalScore)

    return scores

def plotQuizzes():
    # Your code here
    pylab.title("Distribution of Scores")
    pylab.xlabel("Final Score")
    pylab.ylabel("Number of Trials")
    pylab.hist(generateScores(10000),bins = 7)
    pylab.show()

print sampleQuizzes()
