def palindrome(word):
    if len(word)<=1:
        return True
    if word[0] == word[-1]:
        return palindrome(word[1:-1])
    return False

word="Ffffff"

word=word.lower()
if palindrome(word):
    print("회문입니다")
else:
    print("회문이 아닙니다.")
len("i")