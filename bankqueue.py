class Queue:
	
	def __init__(self):
		self.front=None
		self.rear=None
		self.l=[]

	"""def toFile(self,date,parti,trans,amt,bal):
		file=open("Bank.txt","w")
		file.write("\n Date:")
		file.write("date")
		file.write("\n Particulars :")
		file.write("parti")
		if trans=="deposite":
			file.write("\n Deposite :")
			file.write("amt")
		else:
			file.write("\n withdrawal :")
			file.write("amt")

		file.write("\n Balance:")
		file.write("bal")"""

	def enqueue(self,date,trans,amt,bal):

		sam=[date,trans,amt,bal]
		#print(sam)
		if self.front==self.rear:
			self.front=0
			self.rear=0
		self.l.append(sam)
			#l[front+1]=[" "]
		self.front=self.front+1
		


	def dequeue(self):
		#if self.isEmpty==True:
			#empty transcation
		#else:
		#print("!!!!")
		while self.rear!=len(self.l):
			print(self.l[self.rear])
			self.rear=self.rear+1

		self.front=None
		self.rear=None

	def isEmpty(self):
		if self.front ==None and self.rare==None:
			return True

def main():
	print("hi")
	q=Queue()
	q.enqueue(1,2,3,4)
	q.enqueue(11,22,33,44)
	q.enqueue(111,222,333,444)
	#print(q.l)
	q.dequeue()
	#print("!!!!")

if __name__ == '__main__':
	main()
