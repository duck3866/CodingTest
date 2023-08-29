
a = int(input())
word = []

for i in range(a):
    word.append(input())

new_word = list(word[0])  # 문자열을 리스트로 변환

for j in word:
    for k in range(len(new_word)):
        if j[k] != new_word[k]:
            new_word[k] = '?'  # 리스트 내용 수정

new_word = ''.join(new_word)  # 리스트를 문자열로 변환
print(new_word)
