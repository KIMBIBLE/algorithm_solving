def solution(bridge_length, weight, truck_weights):
    answer = 0  # time
    bridge = [0 for i in range(bridge_length)]
    bridge_weight = 0

    # bridge가 비어있다면 종료
    #while sum(bridge) != 0 or len(truck_weights) != 0:
    while True:
        if(bridge_weight == 0 and len(truck_weights) == 0):
            break

        answer += 1
        item = bridge.pop(0)
        bridge_weight -= item

        if len(truck_weights) == 0:
            continue

        if weight >= truck_weights[0] + bridge_weight:
            bridge.append(truck_weights[0])
            bridge_weight += truck_weights[0]
            del truck_weights[0]

        else:
            bridge.append(0)

    return answer

res = solution(2, 10, [7, 4, 5, 6])
print(res)