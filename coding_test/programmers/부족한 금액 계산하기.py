def solution(price, money, count):
    """
    Args:
        price : 이 기구의 이용료,  1 ≤ price ≤ 2,500, price는 자연수
        money : 처음 가지고 있던 금액, 1 ≤ money ≤ 1,000,000,000, money는 자연수
        count : 놀이기구의 이용 횟수, 1 ≤ count ≤ 2,500, count는 자연수
        
    Returns:
        int: 모자란 금액
    """
    for i in range(1,count+1):
        money -= price * i
    return abs(money) if money < 0 else 0
