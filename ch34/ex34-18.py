# assert문

assert test, data               # data 부분은 옵션이다


if __debug__:
    if not test:
        raise AssertionError(data)
