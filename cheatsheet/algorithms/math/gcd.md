# GCD(Greatest Common Divisor)

> 유클리드 알고리즘?
>
> 2개의 자연수(`n`, `m`)의 최대공약수를 구하는 알고리즘

1. 원리

    <img src="https://chart.apis.google.com/chart?cht=tx&chl=n%5C%20%5Cgeq%5C%20m" /> 인 2개의 자연수 `n`, `m`에 대해 <img src="https://chart.apis.google.com/chart?cht=tx&chl=n%5C%20%5Cbmod%5C%20m%5C%20%3D%5C%20r" /> 이라 하면, <img src="https://chart.apis.google.com/chart?cht=tx&chl=gcd(n%2C%5C%20m)%5C%20%3D%5C%20gcd(m%2C%5C%20r)" />이다.

* example 1: `n = 32, m = 18`

    <img src="https://chart.apis.google.com/chart?cht=tx&chl=gcd(32%2C%5C%2018)%5C%20%3D%5C%20gcd(18%2C%5C%2014)%5C%20%3D%5C%20gcd(14%2C%5C%204)%5C%20%3D%5C%20gcd(4%2C%5C%202)%5C%20%3D%5C%20gcd(2%2C%5C%200)%5C%20%3D%5C%202" />

* example 2: <img src="https://chart.apis.google.com/chart?cht=tx&chl=n%3D%5C%2018%2C%5C%20m%5C%20%3D%5C%206" />

    <img src="https://chart.apis.google.com/chart?cht=tx&chl=gcd(18%2C%5C%206)%5C%20%3D%5C%20gcd(6%2C%5C%200)%5C%20%3D%5C%206" />

1. 구현

    * Recursive
    ```py
    def gcd(n, m):
        if m == 0:
            return n
    
        return gcd(m, n % m)
    ```

    * Iterative
    ```py
    def gcd(n, m):
        while m != 0:
            r = n % m
            n = m
            m = r

        return n
    ```


2. 시간복잡도
  > `O(log(n+m))`
