import random
from textblob import TextBlob

# 1] NAME CHATING
print("Hi,what is ur name ?:")
name=input('--')
print("Do u have nick name ?:")
ans=input('--')
if 'y' in ans.lower():
    print('what is ur nickname?:')
    nickname = input('--')
    print('Nice name',nickname)
else:
    nickname=name[0]+'o'+name[-1]+'a'
    print('i will call u',nickname)

# 2] GREETING
greetings=[
            'How r u today '+nickname +'?',
           'how r u feeling '+nickname,
           'whats up '+nickname+'?'
]
print(random.choice(greetings))
a=input('--')
b=TextBlob(a)

if b.polarity > 0:  # means positive feelings
    print('well,all going good')
else:
    print('sorry to hear that')


# 3] new topics
topic=['motogp',
       'grilling',
       'chicken-fish',
       'cristiano',
       'python',
       'utubr'
       ]

question=['how much u like ',
          'what is your opinion about ',
          'what is ur intrest in '
              ]
for i in range(0,random.randint(2,3)):
    q1=random.choice(question)
    question.remove(q1)
    t1=random.choice(topic)
    topic.remove(t1)
    print(q1+t1+'?:')

    a1=input('--')
    b1=TextBlob(a1)

    if b1.polarity > 0.5:  # means positive feelings
        print('ohhh u really like ',t1)
    elif b1.polarity > 0.1:  # means less positive feelings
        print('u less intrested in ',t1)
    elif b1.polarity < -0.5:  # means more +ve feelings
        print('u not intrested in ',t1)
    else:
        print('yeahh , its really common about ',t1)



    if b1.subjectivity > 0.6:
        print('u r so biased')
    if b1.subjectivity > 0.3:
        print('u r little bit biased')
    else:
        print('u r quite objective')
