# 1 read the n line in the file
def read_line(n, file):
    if not isinstance(n, int) or n <= 0:
        return "invalid input detected"
    try:
        f = open(file, 'r')
        text_list = f.readlines()
        if len(text_list) < n:
            return "line " + str(n) + " doesn't exist"
        return text_list[n - 1].rstrip('\n')
    except:
        return "file not found"


# print(read_line(1400,'C:/python_hw/ex3_text.txt'))
# print(read_line(4, 'C:/python_hw/ex3_text.txt')) #should return: " There is much more to black holes than meets the eye. In fact,".
# print(read_line(29, 'C:/python_hw/ex3_text.txt'))#should return: "line 29 doesn't exist".
# print(read_line(9, 'C:/python_hw/ex3_text.txt'))#should return: " ".
# print(read_line("c", 'C:/python_hw/ex3_text.txt'))# should return: "invalid input detected".
# print(read_line(9, 'C:/python_hw/ex4_text.txt'))# should return: "file not found".

# 2- 5 longest word
#
import re


def longest_words(file):
    try:
        f = open(file, 'r')
        data = re.sub("[^a-zA-Z ']+", " ", f.read())  # remove all characters except words
        words_list = data.split() # create list of words
        list_5_max_word = []
        for i in range(5):
            max_word = max(words_list, key=len)
            words_list.remove(max_word)
            list_5_max_word.append(max_word)

        return list_5_max_word


    except:
        return "file not found"
#if the len of file too short also return "file not found"

print(longest_words('C:/python_hw/ex3_text.txt'))
print(longest_words('C:/python_hw/try2.txt'))
