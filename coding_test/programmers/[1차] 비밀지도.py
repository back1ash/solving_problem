def solution(n, arr1, arr2):
    """비밀 지도를 해독하는 함수.
    
    arr1과 arr2를 입력으로 받아 해독한 지도를 return하는 함수.
    Args:
        n (int) : 지도 한 변의 길이
        arr1 (list[int]) : 암호화 된 1번 지도
        arr2 (list[int]) : 암호화 된 2번 지도
        
    Returns:
        list[str] : 해독된 지도의 형태. "#" = 벽, " " = 공백
    """
    answer = []
    decoding_map = [bin(a|b)[2:].zfill(n) for a, b in zip(arr1, arr2)]
    
    answer = [row.replace("1", "#").replace("0", " ") for row in decoding_map]
    
    return answer
