class Proplogic:

	def imply(a,b):
		return (not a) or b
	
	def iff(a,b):
		return imply(a,b) and imply(b,a)
	


	global var
	var=[]



	def findvar(s):
	#this function isnt essential for converting the given expression to conjuctive normal form, but it will help with evaluating the expresssion
		a=s
		a.lower()
		while(a):
	
			if a[0].isalpha():
				
				if a[0]!='a' and a[0]!='o':
					var.append(a[0])
					a=a[1:]
				elif len(a)>2 and a[0]=='a':
					if a[:3]=='and':
						a=a[3:]
					else:
						var.append(a[0])
						a=a[1:]
				elif len(a)>1 and a[0]=='o':
					if a[:2]=='or':
						a=a[2:]
					else:
						var.append(a[0])
						a=a[1:]
			elif a[0].isspace():
				a=a[1:]
			elif a[0]== '=':
				#implies
				a=a[2:]
			elif a[0]== '<':
				#double implication
				a=a[3:]
			elif a[0]=='(' or a[0] == ')':
				#brackets
				a=a[1:]
			elif a[0]=='~':
				#negation
				a=a[1:]
			else:
				print("Invalid input")

		print(var)
	def toCNF(s):
		#now we convert to cnf
		a=s
		for i in range(len(a)):
			if a[i]=='<':
				j=i
				while(not a[j].isalpha()):
					j-=1
				k=i
				while(not a[k].isalpha()):
					k+=1
				if a[j-1]=='~':
					a=a[:j]+'('+a[j+1]+' or '+a[k]+') and (~'+a[k]+' or '+a[j]+a[j+1]+')'+a[k+1:]
				else:
					a=a[:j]+'(~'+a[j]+' or '+a[k]+') and (~'+a[k]+' or '+a[j]+')'+a[k+1:]
		
		b=a
		i=0
		j=0
		k=0
		for i in range(len(b)):
			if b[i]=='=':
				j=i
				while(not b[j].isalpha()):
					j-=1
				k=i
				while(not b[k].isalpha()):
					k+=1
				if b[j-1]=='~':
					b=b[:j]+b[j]+' or '+b[k]+b[k+1:]
				else:
					b=b[:j]+'~'+b[j]+' or '+b[k]+b[k+1:]
		print(b)

print("Enter a logic statement of the following form:")
print("~ operator should precede the operand to represent the 'not' operation")
print("Use the words 'and' and 'or' to represent the logical And and Or operations respectively")
print("Use '=>' to represent implication")
print("Use '<=>' to represent double implication")
print("Make sure that every binary operator is written between the two operands it is operating on")
s=input()
Proplogic.findvar(s)
Proplogic.toCNF(s)
