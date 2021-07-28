# Hashing with `multiplication method`

숫자로 된 키가 `k`이고 `A`가 0과 1 사이의 실수일 때, Multiplication Method는 다음과 같이 정의됨. 이는 키를 0과 1 사이의 소수로 변환하고, 테이블의 크기 만큼 범위를 팽창시킨 것을 의미.

<div align="center">
    <img src="https://chart.apis.google.com/chart?cht=tx&chl=h(k)%5C%20%3D%5C%20(kA%5C%20%5Cbmod%5C%201)%5C%20%5Ctimes%5C%20m" />
</div>

보통 `m`값은 얼마가 되든 크게 중요하지 않으며, 2진수 연산에 최적화된 컴퓨터 구조를 고려하여, 보통 2의 제곱수로 정한다고 함. Multiplicion를 사용하여 Hashing하는 것은 Division Method를 사용하는 방식보다 다소 느리다고 함.

    m = 2 ** 12
    A = 0.12345
    k = 875654454
    hash_value = int((x * A) % 1 * m)