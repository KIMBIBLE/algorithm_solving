# 제약조건 : 참가자 중 동명이인이 있을 수 있다 -> hash 자료구조에 저장할 경우 collision 발생 가능함에 유의!

def solution(participant, completion):
    answer = ''
    participant_state = {}
    
    for p in participant:
        try:
            participant_state[p] += 1
        except:
            participant_state[p] = 1
    
    for c in completion:
        participant_state[c] -= 1

    for each in participant_state.keys():
        if participant_state[each] == 1:
            answer = each

    return answer

if __name__ == '__main__':
    partipant = ["leo", "kiki", "eden"]
    completion = ["eden", "kiki"]
    res = solution(partipant, completion)
    if "leo" == res:
        print("pass")
    else:
        print(res)

    
    partipant = ["marina", "josipa", "nikola", "vinko", "filipa"]
    completion = ["josipa", "filipa", "marina", "nikola"]
    res = solution(partipant, completion)
    if "vinko" == res:
        print("pass")
    else:
        print(res)

    partipant = ["mislav", "stanko", "mislav", "ana"]
    completion = ["stanko", "ana", "mislav"]
    res = solution(partipant, completion)
    if "mislav" == res:
        print("pass")
    else:
        print(res)