
def count_vowels(bykvu):
    vowels = ['a', 'i', 'u', 'e', 'o']
    count = 0
    for char in bykvu.lower():
        if char in vowels:
            count += 1
    return count