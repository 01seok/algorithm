while True:
    n = int(input())
    if n == -1:
        break
    
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
            
    if sum(divisors) == n:
        result = f"{n} = "
        result += " + ".join(map(str, divisors))
        print(result)
    else:
        print(f"{n} is NOT perfect.")