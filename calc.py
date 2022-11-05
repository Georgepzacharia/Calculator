def add(n1,n2):
    return (n1+n2)
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
import art
operations={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}
def calculator():
    print(art.logo)
    num1=float(input("What is the first number?: "))
    answer=num1
    for i in operations:
            print(i)
    while True:
        opsym=input("Pick an operation ")
        num2=float(input("What's the next number?: "))
        old_ans=answer
        answer=operations[opsym](answer,num2)
        print(f"{old_ans} {opsym} {num2} = {answer}")
        choice=input(f"Type 'y' to continue calculating with {answer},type 'n' to exit or type 'a' to start new calculation: ")
        if choice == 'n':
            break
        elif choice == 'a':
            calculator()

calculator()