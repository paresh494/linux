#!/usr/bin/python
a = {'S':['D','E','M'],
      'D':['F','G','R'],
	'F':['E','K'],
	'G':['E','R'],
	'E':[20],
	'M':['R'],
	'R':['E'],
	'K':[]	}
path = [[] for _ in range(10)]
k=-1
def find_path(a,s,e):
	flag=False
	global path,k
	
	if s==e:
		k=k+1
		path[k] = path[k] + [s]
		return True
	for i in a[s]:
		r=k
		if find_path(a,i,e)==True:
			if r<=k:
				for j in range(1,k-r+1):
			          path[r+j]=path[r+j] + [s]	
			flag=True
	if flag==True:
		return True
	else:
		return False				

	
	
	
find_path(a,'D','E')
print path


