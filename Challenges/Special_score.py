from collections import Counter

WORD_LIST = [
    "apple", "abuse", "zebra", "grape", "banana", "orange", "vision", "test", "examine",
    "study", "learning", "innovate", "creation", "energy", "priority", "future", "quality",
    "success", "developer", "scholar", "education", "university", "knowledge", "wisdom",
    "challenge", "research", "discovery", "solution", "project", "science", "mathematics",
    "physics", "biology", "chemistry", "technology", "engineering", "artificial", "intelligence",
    "programming", "computer", "network", "algorithm", "database", "security", "system",
    "automation", "robotics", "hardware", "software", "architecture", "data"
]


def ssw(word):
    freq_dict=dict()
    for char in word:
        if char in freq_dict:
            freq_dict[char]+=1
        else:
            freq_dict[char]=1
    
    result=[]
    for key,value in freq_dict.items():
        result.append(ord(key)* value)
    
    return sum(result)

def find_word(num_let, max_ssw):
    valid_words=[word for word in WORD_LIST if len(word)==num_let]
    best_word=None
    best_score=-1

    for word in valid_words:
        ssw_score=ssw(word)
        if ssw_score<=max_ssw:
            if ssw_score>best_score or (ssw_score==best_score and word>best_word):
                best_word,best_score=word,ssw_score
    
    return best_word

print(find_word(8,888))