import threading
def evenfactor(n):
    sum =0
    for i in range(2,n,2):
        if n % i == 0:
            sum = sum + i
    print ("Addition of EvenFactors is :",sum)

def oddfactor(n):
    sum =0
    for i in range(1,n,2):
        if n % i == 0:
            sum = sum + i
    print ("Addition of oddFactors is :",sum)
    


def main():
    print("Enter your Number :")
    value1 = int(input())
    
    T1= threading.Thread(target=evenfactor(value1))
    T2= threading.Thread(target=oddfactor(value1))
    T1.start()
    T1.join()
    T2.start()
    T2.join()
    
    print("exit from main.")
    
if __name__ == '__main__':
    main()
