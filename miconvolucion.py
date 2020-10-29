import numpy as np
#calcula matriz resultante C después de aplicar convolución de A*B
def convolucion(A,B):
	C=np.zeros((len(A)-2, len(A[0])-2))
	for i in range (len(A)-2):
		for j in range (len(A[0])-2):
			C[i][j]=+(A[i][j]*B[i][j])
	return C

Matriz1=[[6,9,0,3],[8,4,9,1],[4,1,3,12],[3,2,1,100]]
Filtro=[[1,0,2],[5,0,9],[6,2,1]]
A=np.array(Matriz1)
B=np.array(Filtro)

r=convolucion(A,B)
print(r)
