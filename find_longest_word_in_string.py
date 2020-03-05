def longest_st(S, slist, longest=''):
	if S in slist and len(S)>len(longest):
            print(S, slist, longest)
		#return S
	else:
		for i in range(len(S)):
			longest = longest_st(S[:i]+S[i+1:], slist, longest)
	return longest
print(longest_st('abppplee', ['ale', 'apple', 'aple', 'plea'])) 
