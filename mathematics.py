
def vector_add(v,w):
	return[v_i + w_i for v_i, w_i in zip(v,w)]

def vector_substract(v,w):
	return[v_i - w_i for v_i, w_i in zip(v,w)]

def vector_sum(vectors):
	result = vectors[0]
	for vector in vectors[1:]:
		resukt = vector_add(result,vector)
	return result

def scalar_multiply(c,v):
	return [c * v_i for v_i in v]

def vector_mean(vectors):
	n=len(vectors)
	return scalar_multiply(1/n,vector_sum(vectors))

def dot(v,w):
	return sum(v_i * w_i for v_i, w_i in zip(v,w))

def get_row(A,i):
	return A[i]

def get_column(A,j):
	return [A_i[j] for A_i in A]

def make_matrix(num_rows,num_cols,entry_fn):
	return [[entry_fn(i,j) for j in range(num_cols)] for i in range(num_rows)]

def is_diagonal(i,j):
	return 1 if i == j else 0

def identity(n):
	return make_matrix(n,n,is_diagonal)

def mean(x):
	return sum(x)/len(x)

def median(v):
	n=len(v)
	sorted_v = sorted(v)
	midpoint = n // 2
	if n % 2 == 1 :
		return sorted_v[midpoint]
	else:
		lo = midpoint-1
		hi = midpoint
		return (sorted_v[lo]+sorted_v[hi])/2
