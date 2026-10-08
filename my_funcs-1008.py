def my_all(iterable):
	for x in iterable:
		if not x:
			return False
		return True

def my_any(iterable):
	for x in iterable:
		if x:
			return True
		return False

def my_enumerate(iterable,start=0):
	result=[]
	index=start
	for x in iterable:
		result.append((index,x))
		index +=1
	return result

def my_zip(*iterables):
	result=[]
	min_len=min(len(x) for x in iterables)
	for i in range(min_len):
		result.append(tuple(x[i] for x in iterables))
	return result

print(my_all([1,2,3]))
print(my_any([0,0,1]))
print(my_enumerate(['a','b'],start=1))
print(my_zip([1,2],['a','b']))
