template = [
        "T[-2].lower", "T[-1].lower", "T[0].lower", "T[1].lower",
        "T[2].lower",
        "T[0].istitle", "T[-1].istitle", "T[1].istitle",
        # word unigram and bigram
        "T[-2]", "T[-1]", "T[0]", "T[1]", "T[2]",
        "T[-2,-1]", "T[-1,0]", "T[0,1]", "T[1,2]",
    ]