# List를 활용한 Stack 구현

## 1. 스택 생성

```py
stack = []          # empty stack
stack = [1, 2, 3]   # stack initialize
```

## 2. 스택 연산

```py
top = stack.pop()   # stack pop
top = stack[-1]     # stack top
stack.append(4)     # stack push
len(stack) == 0     # isempty
```

* `isfull`은 일반적인 경우 코테에서는 고려하지 않아도 됨!

  * 32비트 시스템에서 python의 list는 `536,870,912(5억)`까지 저장 가능!

  * 64비트 시스템의 경우 : `9,223,372,036,854,775,807` 까지 저장 가능.

    ```py
    import platform
    platform.architecture()     # ('64bit', '')
    sys.maxsize                 # 9223372036854775807
    ```

    <details>
    <summary>최대 할당 가능 사이즈 in <code>Objects/listobject.c</code></summary>

    ```cpp
    /* Ensure enough temp memory for 'need' array slots is available.
    * Returns 0 on success and -1 if the memory can't be gotten.
    */
    static int
    merge_getmem(MergeState *ms, Py_ssize_t need)
    {
        assert(ms != NULL);
        if (need <= ms->alloced)
            return 0;
        /* Don't realloc!  That can cost cycles to copy the old data, but
        * we don't care what's in the block.
        */
        merge_freemem(ms);

        /* 
            * 여기 코드에 최대 할당 가능한 사이즈가 나옴!
            * (size_t)need > PY_SSIZE_T_MAX / sizeof(PyObject*)
            * 
            * in <pyport.h>
            * Largest positive value of type Py_ssize_t.
            * #define PY_SSIZE_T_MAX ((Py_ssize_t)(((size_t)-1)>>1))
            * 
            */
            
        if ((size_t)need > PY_SSIZE_T_MAX / sizeof(PyObject*)) {
            PyErr_NoMemory();
            return -1;
        }
        ms->a = (PyObject **)PyMem_Malloc(need * sizeof(PyObject*));
        if (ms->a) {
            ms->alloced = need;
            return 0;
        }
        PyErr_NoMemory();
        merge_freemem(ms);          /* reset to sane state */
        return -1;
    }
    ```

    </details>
