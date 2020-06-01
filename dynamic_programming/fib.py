def fib(n):
    if n == 1 or n == 2:
        return(1)
    else:
        return(fib(n-1) + fib(n-2))

D = {}
D[1] = 1
D[2] = 1
def fib_dp_recursive(n):
    if n in D:
        return(D[n])
    curr_val = fib_dp_recursive(n-1) + fib_dp_recursive(n-2)
    D[n] = curr_val
    return(curr_val)
    
d = {}
d[1] = 1
d[2] = 1
def fib_dp_nonrecursive(n):
    for i in range(3, n+1):
        d[i] = d[i-2] + d[i-1]
    return(d[n])
    

if __name__ == '__main__':

    # print(f'- fib(1000): {fib(1000)}')

    print(f'- fib_dp_recursive(1000): {fib_dp_recursive(1000)}')

    print(f'- fib_dp_nonrecursive(1000): {fib_dp_nonrecursive(100000)}' )
    
