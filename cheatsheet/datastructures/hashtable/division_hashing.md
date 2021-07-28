# Hashing with `Division Method`

Division Method는 modular 연산을 활용해, 가장 간단하면서도 빠른 연산이 가능한 Hash Function이다. Division Method의 Hashing은 <img src="https://chart.apis.google.com/chart?cht=tx&chl=h(k)%5C%20%3D%5C%20k%5C%20%5Cbmod%5C%20m" />을 통해 수행되며, 생성되는 Key는 `0 ~ m-1`의 범위 내에서 생성된다. 한편, Division Method를 사용하는 경우 `m`값을 어떻게 설정하는지가 매우 중요하다.

먼저, `m`을 어떻게 설정하는지에 따라 해시 테이블의 성능이 크게 좌우되는데, m의 크기는 보통 Key의 수의 3배수가 적당하다고 한다.(적재율이 30% 정도쯤까지는 Collision 발생이 거의 일어나지 않음.)

다음으로, `m` 값은 소수(Prime Number) 형태를 권장한다. `m`값이 <img src="https://chart.apis.google.com/chart?cht=tx&chl=m%5C%20%3D%5C%202%5E3%5C%20%3D%5C%2000001000%5C%20(2)" />과 같이 2의 거듭 제곱 형태라면, 2진수의 4자리 이하의 숫자만 Hash Value에 영향을 주게되기 때문이다.

    m   = 0x00001000
    k1  = 0x10111001
    k2  = 0x00001001
    h(k1) = h(k2) = 1

정리하자면, Division Method을 활용하여 Hashing할 때의 최적의 `m`의 크기는 `key의 갯수의 3배 정도`이며, `2의 exponential에 근접한 Prime Number`를 선택해야 한다.
