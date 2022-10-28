def simple_interest(p, t, r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of intrest is',r)

 


    si=(p * t * r)/100

    print('The simple Interest is ',si)

    return si

simple_interest(
    p=int(input("Enter principal\n")),
    t=int(input("Enter Time period\n")),
    r=int(input("Enter Intrest"))
)