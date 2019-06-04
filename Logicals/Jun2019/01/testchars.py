if __name__ == '__main__':
    s = input()

    print(s.isalnum())
    value = "".join(list(filter(str.isalpha, s)))
    print(value.isalpha())
    value = "".join(list(filter(str.isdigit, s)))
    print(value.isdigit())
    value = "".join(list(filter(str.islower, s)))
    print(value.islower())
    value = "".join(list(filter(str.isupper, s)))
    print(value.isupper())

    

    """
    
    
    print(s.isdigit())
    print(s.islower())
    print(s.isupper())
    """