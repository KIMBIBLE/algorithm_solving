
#### :bulb:&ensp; `Open Addressing` vs `Seperate Chaining`

|                   |Time Complexity    |Bucket Resize|
|-                  |-                  |-|
|Open Addressing    |<img src="https://chart.apis.google.com/chart?cht=tx&chl=O(M)" />|버킷을 계속 사용하기 때문에 |
|Separate Chaining  |<img src="https://chart.apis.google.com/chart?cht=tx&chl=O(M)" />||

* `해시 버킷의 밀도가 높을 때`: 일반적으로 Open Addressing 방식은 Separate Chaining 방식 보다 느림.

  * Separate Chaining 방식에서는 해시 버킷을 채운 밀도가 높을수록 Worst Case 발생 빈도가 높아지기 때문.

  * 이는 Separate Chaining 방식이 보조 해시 함수를 사용하여 해시 충돌이 발생하는 빈도를 조절할 수 있지만, Open Addressing 방식은 해시 충돌이 발생하는 빈도를 임의로 조절할 수 없기 때문.

* `해시 버킷의 밀도가 낮을 때`: Open Addressing 방식이 Separate Chaining 방식보다 성능이 더 좋음.

  * 먼저, Open Addressing 방식은 연속된 메모리 공간 내에 데이터를 저장하기 때문에 캐시 효율이 높음.
  
  * 다음으로, 