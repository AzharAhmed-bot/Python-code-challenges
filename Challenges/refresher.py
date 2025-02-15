
# Lesson 1
# def atbashEncoder():
#     alphabets='abcdefghijklmnopqrstuvwxyz'
#     backwards=alphabets[::-1]
#     result=dict()
#     result.update(zip(alphabets,backwards))
#     return result    
# print(atbashEncoder())

# def atBash(string):
#     alphabets='abcdefghijklmnopqrstuvwxyz'
#     result=''
#     for char in string:
#         if char.isalpha():
#             position=alphabets.index(char.lower())
#             result+=alphabets[len(alphabets)-position-1] if char.islower() else alphabets[len(alphabets)-position-1].upper()
#         else:
#             result+=char  
#     return result
# print(atBash('Ab cd'))


# Lesson 2

# chart=Bar(title='Olympics')
# with open('medals.csv') as f:
#     reader=csv.reader(f)
#     next(reader)
#     for row in reader:
#         chart.add(row[0],int(row[1]))
# chart.render_to_file('olympics.svg')


def frequency(text):
    result=dict()
    for char in text:
        if char.isalpha() or char.isspace():
            char=char.lower()
            if char in result:
                result[char]+=1
            else:
                result[char]=1
    return result

print(frequency('helLo world'))



