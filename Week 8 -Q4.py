#Week8 Question 4

def pagetest(page):
    isEven = False
    if page % 2 == 0:
        isEven = True
    return isEven

def main():
    page = int(input("What is the page number ? :"))
    if pagetest(page):
        print(page)
    else:
        print("%60s%d" % (" ",page))
main()        


