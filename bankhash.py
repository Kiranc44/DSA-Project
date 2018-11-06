from banklinkedlist import LinkedList
from bankqueue import Queue
import datetime
stint=0
def h(v):
	return int(v)%10

class hashtable:
    def __init__(self):
        self.T=[None for i in range(0,10)]

    def chained_insert(self,a,ln):
        k=h(a)
        if(self.T[k]==None):
            self.T[k]=LinkedList()
            self.T[k].head=ln
        else:
            p=self.T[k].head
            while (p.next is not None):
                p=p.next
            p.next=ln

    def chained_search(self,a):
        k=h(a)
        if(self.T[k]==None):
            return False
        else:
            p=self.T[k].head
            while(p is not None):
                if(a==p.key):
                    return p
                p=p.next
            return False

    def chained_delete(self,a):
    	k=h(a)
    	p=self.T[k].head
    	while p!=None:
        	if(a!=p.key):
        		z=p
        		p=p.key
        	else:
        		z.next=p.next

    def createAC(self):
    	global stint
    	stint=stint+1
    	#print("To create a new zero balance savings account do : ")
        newNode=ListNodell(stint)
        newNode.name=input("Enter the account holders name : ")
        newNode.Address=input("Enter the Address of the account holder : ")
        newNode.phno=input("Enter the phone number account holder : ")
        self.chained_insert(stint,newNode)
        self.acc_pass(stint)

    def show(self):
    	for i in range(0,len(self.T)):
    		if self.T[i]!=None:
    			self.T[i].print()

    def transactions(self,k):
    	x=int(input("Enter 1 to withdraw and 2 to deposite"))
    	date = datetime.datetime.now()
    	date=date.strftime("%Y-%m-%d %H:%M")
    	if(x==1 and self.balance!=0):
            print("Please deposite amount..!")
            a=int(input("Enter the amount to withdraw"))
            account=self.chained_search(k)
            account.balance=account.balance-a
            account.qu.enqueue(date,"W",a,account.balance)

        #elif(x==1 and self.balance==0):
         #   print("Please deposite your money...!")

    	elif(x==2):
    		a=int(input("Enter the amount to deposite"))
    		account=self.chained_search(k)
    		account.balance=account.balance+a
    		account.qu.enqueue(date,"D",a,account.balance)

    def passbookdisplay(self,k):
    	account1=self.chained_search(k)
    	print('DATE   |   TRANSACTION   | AMOUNT   | BALANCE')
    	account1.qu.dequeue()

    #def loanIssue(self,K):
    #	person=
    def acc_pass(self,k):
    	k=h(k)
    	account=self.chained_search(k)
    	if(account.password==None):
    		q=input("Enter a new password")
    		l=input("Confirm password")
    		if(q==l):
    			account.password=q

    	else:
            while True:
                q=input("Enter your password")
                if account.password==q:
                    a=input("Enter a new password")
                    b=input("Confirm password")
                    if a==b:
                        account.password=a
                        print("Password changhed sucessfully!")
                        return
                else:
                    print("Enter correct password or account no")



    def loanIssue():
        pass

    			







class ListNodell:
    def __init__(self,k=None):
        self.key=k
        self.next=None
        self.qu=Queue()
        self.phno=None
        self.balance=0
        self.Address=None
        self.name=None
        self.Loan=None
        self.password=None


def main():
	"""h=hashtable()
	h.createAC()
	h.createAC()
	h.show()
	print(h.chained_search(1))
	h.transactions(1)
	h.transactions(1)
	h.passbookdisplay(1)"""
    h=hashtable()
    date = datetime.datetime.now()
    date=date.strftime("%Y-%m-%d %H:%M")
    print("Enter 1:Coustomer")
    print("Enter 2:Staff")
    q=int(input("Enter ur choice:"))
    if(q==1):
        print("Enter 1:Login")
        print("Enter 2:createAC")
        print("Enter 3:Loan")
        z=int(input("Enter your option"))

        if(z==1):
            accno=int(input("Enter your Acc.No"))
            passwrd=input("Enter your password")
            if(self.T[k].password!=passwrd):
                print("Wrong account no. or password")#shd go back to first statement

            else:
                print("Enter 1 for transactions")
                print("Enter 2 for checking balance")
                print("Enter 3 for printing passbook")
                print("Enter 4 for changing password")

                m=int(input("Enter your option"))
                if(m==1):
                    h.transactions(accno)

                elif(m==2):
                    print("Your current balance is: ",h[accno].balance,"   as of:",date)

                elif(m==3):
                    h.passbookdisplay(accno)

                elif(m==4):
                    h.acc_pass(accno)

        elif(z==2):
            h.createAC()




if __name__ == '__main__':
	main()
