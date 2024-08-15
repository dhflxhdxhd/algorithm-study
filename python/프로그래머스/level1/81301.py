# 코딩테스트 연습
# 2021 카카오 채용연계형 인턴십
# 숫자 문자열과 영단어



words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

words_dict = {"zero": 0, "one": 1, "two":2, "three": 3, "four":4, "five":5, 
             "six": 6, "seven":7, "eight":8, "nine":9}
def solution(s):
    num = ""
    answer = []
    for string in s:
        if string.isdigit() :
            answer.append(string)
        else:
            num += string
            if num in words_dict.keys():
                answer.append(words_dict.get(num))
                num = ""

    result = ''.join(map(str, answer))
        
    return int(result)

