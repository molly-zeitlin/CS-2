#Author: Molly Zeitlin
#Date: 2/19/2026
#Description: analyzes a text file and returns 15 most frequent words
#Log: 1.0 MZ

import string

def count_words(file):
    with open("word_frequency.csv", "w") as output:
        counts = dict()
        for line in file:
            line = line.rstrip()
            line = line.translate(line.maketrans("", "", string.punctuation)) #First two parameters are empty strings and this deletes punctuation from "line"
            line = line.lower()
            words = line.split()
            filler_words = ["the", "go", "up", "art", "out", "tell", "night", "know", "take", "must", "and", "to", "of", "i", "a", "that", "ild", "selfsame", "madam", "mayst", "dost", "thyself", "whence", "shalt", "ist", "yourself", "forth", "thine", "hence", "put", "hath", "shall", "thee", "should", "in", "is", "it", "not", "his", "be", "have", "but", "you", "me", "my", "with", "your", "he", "our", "for", "what", "this", "all", "so", "as", "him", "we", "do", "which", "will", "are", "they", "no", "enter", "on", "upon", "mine", "other", "others", "yet", "us", "if", "o", "or", "nor", "very", "wouldst", "lets", "heres", "while", "em", "mere", "fort", "thouldst", "when", "like", "then", "where", "than", "most", "am", "how", "things", "ay", "has", "some", "none", "set", "come", "their", "at", "were", "there", "make", "such", "can", "an", "one", "had", "does", "give", "by", "now", "was", "them", "sir", "may", "too", "though", "way", "whose", "could", "each", "three", "hes", "goes", "use", "ones", "doing", "often", "alls", "t", "thing", "whats", "whom", "once", "much", "only", "these", "been", "third", "why", "see", "done", "thou", "from", "thy", "more", "would", "her", "he", "well", "who", "did", "here", "tis", "say", "own", "till", "second", "those", "she", "ere", "theres", "think", "thanks", "many", "thats", "hark", "doth", "after", "thrice", "didst", "thank", "twere", "alas", "ye", "whether", "youll", "canst", "hie", "gall", "showd", "yes", "thourt", "yours", "oh", "ont", "whos", "thus"]
            for word in words:
                if word not in filler_words:
                    if word not in counts:
                        counts[word] = 1
                    else:
                        counts[word] += 1    
                else:
                    del word
        des = {k: v for k, v in sorted(counts.items(), key=lambda item: item[1], reverse = True)} #sorts dictionary from highest to lowest frequency
        w_count = 0
        for key, value in des.items():
            if w_count < 15:
                output.write(f"{key, value}\n")
                w_count +=1
            else:
                break

def main():
    counter = 0
    while counter < 2:
        user_choice = input("Would you like to count the frequency of words in Shakespeare's Macbeth or Romeo and Juliet?\nPlease enter M or RJ: ")
        if user_choice == "m" or user_choice == "M":
            try:
                m_file = open("Macbeth.txt", "r")
                count_words(m_file)
                counter +=1
            except:
                print('File cannot be opened:', m_file)
                exit()
        elif user_choice == "rj" or user_choice == "RJ":
            try:
                rj_file = open("Romeo_and_Juliet.txt", "r")
                count_words(rj_file)
                counter +=1
            except:
                print('File cannot be opened:', rj_file)
                exit()
        else:
            print("INVALID RESPONSE")

main()