'''
序列中出现次数最多的元素
'''
from collections import Counter

if __name__ == "__main__":
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
        'my', 'eyes', "you're", 'under'
    ]
    word_counts = Counter(words)
    print(word_counts)

    top_three = word_counts.most_common(3)
    print(top_three)

    morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
    word_counts.update(morewords)
    top_three = word_counts.most_common(3)
    print(top_three)
