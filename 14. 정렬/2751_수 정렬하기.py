print(*sorted(map(int,[*open(0)][1:])))  #*(asterisk)는 리스트에 들어가면 리스트 각 원소를 하나씩 언팩킹하는 역할
#open() 은 파일 형태 객체를 생성 (0) 은 stdin 을 의미하는데 stdin으로 input을 입력 받고, 프로그램 종료시 sorted()로 정렬해서 하나씩 프린트
