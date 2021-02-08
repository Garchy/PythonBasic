Questions = {
    'Question 1' : {
        'Question' : 'Whats is sky color?',
        'answer' : {
            'a' : 'Red',
            'b' : 'Green',
            'c' : 'Blue',
            'd' : 'Pink'
        },
        'rightAnswer' : 'c'
    },

    'Question 2' : {
        'Question' : 'Where is Brazil?',
        'answer' : {
            'a' : 'North America',
            'b' : 'South America',
            'c' : 'Asia',
            'd' : 'Africa'
        },
        'rightAnswer' : 'b'
    },

    'Question 3' : {
        'Question' : 'Giraffes exists?',
        'answer' : {
            'a' : 'Yes',
            'b' : 'Maybe',
            'c' : 'No',
            'd' : 'IDK'
        },
        'rightAnswer' : 'a'
    },
}

acertos = 0
print()

for qk, qv in Questions.items():
    print(f"{qk} : {qv['Question']}")

    for ak, av in qv['answer'].items():
        print(f"[{ak}] : {av}")
        
    print()
    respostaUsuario = input('Answers: ')

    if respostaUsuario == qv['rightAnswer']:
        print("You get!\n")
        acertos += 1
    else:
        print("You missed!\n")

print(f"You get {acertos} answer(s)")