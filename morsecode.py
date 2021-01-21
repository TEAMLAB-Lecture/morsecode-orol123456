# -*- coding: utf8 -*-


# Help Function - 수정하지 말 것
def get_morse_code_dict():
    morse_code = {
        "A": ".-", "N": "-.", "B": "-...", "O": "---", "C": "-.-.", "P": ".--.", "D": "-..", "Q": "--.-", "E": ".",
        "R": ".-.", "F": "..-.", "S": "...", "G": "--.", "T": "-", "H": "....", "U": "..-", "I": "..", "V": "...-",
        "K": "-.-", "X": "-..-", "J": ".---", "W": ".--", "L": ".-..", "Y": "-.--", "M": "--", "Z": "--.."
    }
    return morse_code


# Help Function - 수정하지 말 것
def get_help_message():
    message = "HELP - International Morse Code List\n"
    morse_code = get_morse_code_dict()

    counter = 0

    for key in sorted(morse_code):
        counter += 1
        message += "%s: %s\t" % (key, morse_code[key])
        if counter % 5 == 0:
            message += "\n"

    return message


def is_help_command(user_input):
    """
    Input:
        - user_input : 문자열값으로 사용자가 입력하는 문자
    Output:
        - 입력한 값이 대소문자 구분없이 "H" 또는 "HELP"일 경우 True,
          그렇지 않을 경우 False를 반환함
    Examples:
        >>> import morsecode as mc
        >>> mc.is_help_command("H")
        True
        >>> mc.is_help_command("Help")
        True
        >>> mc.is_help_command("Half")
        False
        >>> mc.is_help_command("HeLp")
        True
        >>> mc.is_help_command("HELLO")
        False
        >>> mc.is_help_command("E")
        False
    """
    tmp=user_input.lower()
    if tmp=='h' or tmp=='help':
        return True
    return False
    # ==================================


def is_validated_english_sentence(user_input):
    a="_@#$%^&*()-+=[]}{\"';:\|`~0123456789"
    if any(sym in user_input for sym in a):
        return False
    else:
        for i in range(len(user_input)):
            if user_input[i].isalpha():
                return True

        return False


def is_validated_morse_code(user_input):
    correct=[' ','.','-']
    for w in user_input:
        if w not in correct:
            return False
    user_input=user_input.split(' ')
    morse_code_dict=get_morse_code_dict()
    for w in user_input:
        if w:
            if w not in morse_code_dict.values():
                return False
    return True



def get_cleaned_english_sentence(raw_english_sentence):
    res=raw_english_sentence.strip().split()
    tmp=[]
    for w in res:
        ans=''
        for s in w:
            if s not in ',.!?':
                ans+=s
        tmp.append(ans)
    return ' '.join(tmp)
        





def decoding_character(morse_character):
    morse_code_dict = get_morse_code_dict()
    for k,v in morse_code_dict.items():
        if v==morse_character:
            return k

    # ==================================


def encoding_character(english_character):
    english_character=english_character.upper()
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    morse_code_dict = get_morse_code_dict()
    return morse_code_dict[english_character]
    # ==================================


def decoding_sentence(morse_sentence):
    """
    Input:
        - morse_sentence : 문자열 값으로 모스 부호를 표현하는 문자열
    Output:
        - 모스부호를 알파벳으로 변환한 문자열
    Examples:
        >>> import morsecode as mc
        >>> mc.decoding_sentence("... --- ...")
        'SOS'
        >>> mc.decoding_sentence("--. .- -.-. .... --- -.")
        'GACHON'
        >>> mc.decoding_sentence("..  .-.. --- ...- .  -.-- --- ..-")
        'I LOVE YOU'
        >>> mc.decoding_sentence("-.-- --- ..-  .- .-. .  ..-. ")
        'YOU ARE F'
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    ans=''
    s_split=morse_sentence.strip().split(' ')
    for m in s_split:
        if m == '':
            ans+=' '
        else:
            ans+=decoding_character(m)
    return ans
    # ==================================


def encoding_sentence(english_sentence):
    """
    Input:
        - english_sentence : 문자열 값으로 모스 부호로 변환이 가능한 영어문장
    Output:
        - 입력된 영어문장 문자열 값을 모스부호로 변환된 알파벳으로 변환한 문자열
          단 양쪽 끝에 빈칸은 삭제한다.
    Examples:
        >>> import morsecode as mc
        >>> mc.encoding_sentence("HI! Fine, Thank you.")
        '.... ..  ..-. .. -. .  - .... .- -. -.-  -.-- --- ..-'
        >>> mc.encoding_sentence("Hello! This is CS fifty Class.")
        '.... . .-.. .-.. ---  - .... .. ...  .. ...  -.-. ...  ..-. .. ..-. - -.--  -.-. .-.. .- ... ...'
        >>> mc.encoding_sentence("We Are Gachon")
        '.-- .  .- .-. .  --. .- -.-. .... --- -.'
        >>> mc.encoding_sentence("Hi! Hi!")
        '.... ..  .... ..'
    """
    tmp=get_cleaned_english_sentence(english_sentence)
    tmp=list(tmp)
    ans=''
    for w in tmp:
        if w.isalpha():
            ans+=encoding_character(w)+' '
        else:
            ans+=' '
    return ans
    # ==================================


def main():
    print("Morse Code Program!!")
    # ===Modify codes below=============
    while True:
        msg=input('Input your message(H - Help, 0 - Exit):')
        msg=msg.upper()
        print(msg)
        if msg=='0':
            break
        if is_help_command(msg):
            print(get_help_message())
        else:
            if is_validated_english_sentence(msg):
                print(encoding_sentence(msg))
            elif is_validated_morse_code(msg):
                print(decoding_sentence(msg))
            else:
                print('Wrong Input')
    # ==================================
    print("Good Bye")
    print("Morse Code Program Finished!!")

if __name__ == "__main__":
    main()
