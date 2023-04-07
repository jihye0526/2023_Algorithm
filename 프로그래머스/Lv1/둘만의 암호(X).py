def solution(s, skip, index):
    answer = ''
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for ch in skip:
        if ch in alphabet:
            alphabet = alphabet.replace(ch, "")

    for w in s:
        target = alphabet[(alphabet.index(w)+index) % len(alphabet)]
        answer += target

    return answer

print(solution("aukks","wbqd",5))