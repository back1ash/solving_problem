def solution(survey, choices):
    answer = ''
    
    score = {'R': 0, 'T': 0,
            'C': 0, 'F': 0,
            'J': 0, 'M': 0,
            'A': 0, 'N': 0}
    for character, choice in zip(survey, choices):
        disagree = character[0]
        agree = character[1]
        if choice < 4:
            score[disagree] += 4-choice
        if choice > 4:
            score[agree] += choice-4
    
    first = 'R' if score['R'] >= score['T'] else 'T'
    second = 'C' if score['C'] >= score['F'] else 'F'
    third = 'J' if score['J'] >= score['M'] else 'M'
    fourth = 'A' if score['A'] >= score['N'] else 'N'
    
    return ''.join([first,second,third,fourth])
