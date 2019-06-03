def count_substring(string, sub_string):
    count = 0
    counter = 0

    while counter < len(string):
        new_content = string[counter:]
        foundat = new_content.find(sub_string)

        if(foundat != -1):
            count += 1
            counter += (foundat + 1)
        else:
            counter += 1

    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
