n=0
counter = 0
a = "nbobnbobbbobbb"
while n < len(a):
    if a[n]=='b':
        if n+1 <len(a):
            if a[n+1] == 'o':
                if n+2 < len(a):
                    if a[n+2]=='b':
                        counter = counter+1
    n=n+1    
print(counter)    
#if type(varA) == str
num = 5
if num > 2:
    print(num)
    num -= 1
print(num)
