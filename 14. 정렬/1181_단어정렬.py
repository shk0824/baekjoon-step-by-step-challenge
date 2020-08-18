n,*j=[i.split()[0] for i in open(0)]; j=list(set(j)) #open으로 받아서 첫째번 숫자는 n에 넣고 나머지 모두 리스트로 j에 넣고 j 중복된 것 삭 
j.sort(key=lambda x: (len(x),x.lower())) # 정렬할 때 조건 두가지 (lambda 사용해서 길이 먼저 보고 같은값이면 알파벳 순)
print(*j, sep="\n") # *j로 각 객체당 sep으로 띄어쓰기
