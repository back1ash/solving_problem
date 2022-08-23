import datetime
def solution(a, b):
    answer = ""
    week = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    date = datetime.datetime(2016, a, b)
    answer = week[int(date.strftime("%w"))]
    return answer
