def solution(nums):
    can_choice = len(nums) / 2
    num_kind = len(set(nums))
    
    answer = num_kind if can_choice >= num_kind else can_choice
    return answer
