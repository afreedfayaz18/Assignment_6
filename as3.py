import math
import cmath
with open("quadeqn.txt","r") as f:
	eqn=f.read()
	print(eqn)
	eqn,coeff=eqn.split('+'),[]
	for i in eqn:
		if i=='x*x': coeff.append(1)
		for j in i:
			if j.isdigit():
				coeff.append(int(j))
	a,b,c=coeff[0],coeff[1],coeff[2]
	rootp1=cmath.sqrt(b*b-4*a*c)
	rootp2,rootp3=-b-rootp1,-b+rootp1
	root1,root2=rootp2/(2*a),rootp3/(2*a)
	print("roots = ",root1,",",root2)