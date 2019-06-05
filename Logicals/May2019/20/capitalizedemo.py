def capitalize(s): 
    for x in s[:].split(" "): 
        s = s.replace(x, x.capitalize()) 
        s = "".join(s) 
    
    return s

if __name__ == "__main__":
    output = capitalize(input())

    print(output)

