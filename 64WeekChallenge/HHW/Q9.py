def PrimalityCheck(n:int)->bool:
    for i in range(2,int(n//(n**(1/2))+1),1):
        if n%i ==0:
            return False
    return True
print(PrimalityCheck(n=int(input())))
