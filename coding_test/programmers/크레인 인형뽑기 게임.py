def solution(board, moves):
    answer = 0
    basket = []
    top = -1
    
    for move in moves:
        select = 0
        i = 0
        while i<len(board):
            select = board[i][move-1]
            if select != 0:
                board[i][move-1] = 0
                break
            i += 1
            
        if select == top:
            basket.pop()
            answer += 2
        elif select:
            basket.append(select)
        top = basket[-1] if basket else -1
    return answer
