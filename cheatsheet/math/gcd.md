# GCD(Greatest Common Divisor)

> 유클리드 알고리즘?
>
> 2개의 자연수(n, m)의 최대공약수를 구하는 알고리즘

1. 원리
> <img src="https://chart.apis.google.com/chart?cht=tx&chl= n%5C%20%5Cgeq%5C%20m" />인 2개의 자연수($n$, $m$)에 대해 $n\mod m = r$ 이라 하면,
> 
> $gcd(n, m) = gcd(m, r)$이다.

* example 1: $n = 32, m = 18$

    $gcd(32, 18) = gcd(18, 14) = gcd(14, 4) = gcd(4, 2) = gcd(2, 0) = 2$

* example 2: $n= 18, m = 6$

    $gcd(18, 6) = gcd(6, 0) = 6$

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
