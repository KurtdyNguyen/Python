def main():
    s0 = str(input())
    if s0.count('.')!=4:
        return 'Invalid'
    for c in s0:
        if c == '.':
            s0 = s0.replace(c, ' ')

    s = list(map(int, s0.split()))
    if len(s)!=4:
        return 'Invalid'
    if all(i in range(0, 256) for i in s)==False:
        return 'Invalid'
    return 'Valid'

if __name__ == "__main__":
    print(main())