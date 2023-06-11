def main():
    n = int(input())
    for i in range(n):
        s=""
        for x in range(i+1):
            s += "*"
        print(s)
     


main()
