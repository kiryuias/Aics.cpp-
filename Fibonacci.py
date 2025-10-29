def search(arr,x):
    n = len(arr)

    a = 0
    b = 1
    c = 1

    while c < n:
        a = b
        b = c
        c = a + b

    offset = -1

    while c > 1:
        i = min(offset + a, n - 1)

        if arr[i] < x:
            c = b
            b = a
            a = c - b
            offset = i

        elif arr[i] > x:
            c = a
            b = b - a
            a = c - b
        else:
            return i

    if b and arr[offset + 1] == x:
        return offset + 1
    return - 1

if __name__ == "__main__":
    arr = [2,3,4,10,40]
    x = 10
    print(search(arr,x))
    