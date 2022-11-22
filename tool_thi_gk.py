from json.tool import main
from base64 import b64decode
import binascii


# tìm ước chung lớn nhất của a và b
def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


# eculid mở rộng
def ex_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d1, x1, y1 = ex_gcd(b, a % b)
        d, x, y = (d1, y1, x1 - (a//b)*y1)
        return d, x, y


# nghịch đảo của a theo modun n
def mod_inv(a, n):
    (d, x, y) = ex_gcd(a, n)
    b = x % n
    return b


# tính a^b mod n
def modular_exponentiation(a, b, n):
    if b == 0:
        return 1
    if b == 1:
        return a
    r = modular_exponentiation(a, b//2, n)
    r = (r*r) % n
    if b % 2 == 1:
        r = (r*a) % n
    return r


# tìm hàm diffie hellman
# DH(g^x) mode p
# g^x = m mode p
def diffie_hellman(p, m, g):
    for i in range(p-1):
        if(pow(g, i) % p == m):
            print("x = ", i)
            return i
            break


# tim các phần tử sinh và số các phần tử sinh Z*n
# n = int(input("Cac phan tu sinh cua :"))
def tim_cac_phan_sinh(n):
    z = []
    for i in range(1, n):
        if gcd(i, n) == 1:
            z.append(i)

    s = []
    for i in z:
        for j in z:
            if modular_exponentiation(i, j, n) == 1:
                if j == len(z):
                    s.append(i)
                break
    print("Cac phan tu sinh cua Z", n, " la :")
    for i in s:
        print(i)
    print("-----")
    print("So phan tu sinh :", len(s))


def find_plaintextRSA(p, q, e, y):
    N = q*p
    phi = (q-1)*(p-1)

    for d in range(phi - 1):
        if(((d*e) % phi) == 1):
            i = d
            break
    return modular_exponentiation(y, i, N)


def one_time_pad():
    mess = input('Plaintext..: ')
    # s = binascii.hexlify(bytes(mess, 'utf-8'))
    plaintext = mess.encode("utf-8").hex()
    ciphertext = input("Cipher is: ")
    key = hex(int(plaintext, 16) ^ int(ciphertext, 16))
    print("key OPT :", key)

    mess1 = input("Plaint text to encode : ")
    text = mess1.encode("utf-8").hex()
    print("Ciphertext is: ", hex(int(text, 16) ^ int(key, 16)))


def find_signaturalRSA(n, e):
    print("\nThử từng đáp án, nếu ra kết quả m giống với đáp án thì chọn.")
    for i in range(4):
        o = int(input("\nNhập o = "))
        print("m is : ", modular_exponentiation(o, e, n))


# tính DH_g(a,b)
def diffie_hellman_more(a, b, p, g):
    x = diffie_hellman(p, a, g)
    y = modular_exponentiation(b, x, p)
    print("D(", a, ",", b, ") =", y)


def input_pk():
    p = int(input("Nhập p = "))
    g = int(input("Nhập g = "))
    sk = int(input("Nhập sk = "))
    d = sk
    pk = modular_exponentiation(g, d, p)
    return (p, g, d)


# tìm chữ kí elgamal
def find_signatural_elgamal():
    kE = int(input("Nhập kE = "))
    m = int(input("Nhập m = "))
    (p, g, d) = input_pk()
    r = modular_exponentiation(g, kE, p)
    a = m - d*r
    b = mod_inv(kE, p - 1)
    s = (a * b) % (p - 1)
    return (r, s)


# tìm khóa trong đường cong elipttic
def find_key_share():
    print('Nhin bang cho can than den luc sai dung do tai code nha :D')
    p = int(input("Nhap p ( so tu P) :"))
    a = int(input("Nhap a ( so tu aP) :"))
    b = int(input("Nhap b ( so tu bP) :"))
    mod = int(input("!! Chu y cai nay = vi tri ma no hien la 0 nhe :"))

    for i in range(1, mod-1):
        if i*p % (mod) == a:
            dem1 = i
            break

    for i in range(1, mod-1):
        if i*p % (mod) == b:
            dem2 = i
            break

    print('Check bang vi tri nha : ', dem1*dem2*p % (mod))


# Tinh nP
def find_nP():
    print('Nhin bang cho can than den luc sai dung do tai code nha :D')
    p = int(input("Nhap p ( so tu P) :"))
    n = int(input("Nhap n :"))
    mod = int(input("!! Chu y cai nay = vi tri ma no hien la 0 nhe :"))
    print('Check bang vi tri nha : ', p*n % (mod))


def menu():
    print("")
    print("Menu")
    print("1.Tìm UCLN.")
    print("2.Tính eculid mở rộng.")
    print("3.Tìm a^-1 mode n.")
    print("4.Tính a^b mod n.")
    print("5.Hàm diffie hellman DH_g(m).")
    print("6.Tìm các phần tử sinh của dãy.")
    print("7.Mã hóa RSA, tìm bản rõ x.")
    print("8.Tìm key OTP")
    print("9.Tìm chữ ký RSA")
    print("10.Tìm chữ kí Elgamal")
    print("11.Hàm diffie hellman mở rộng DH_g(a,b).")
    print("12.Xét đường cong elliptic. Tìm key chia sẻ abP")
    print("13.Xét đường cong elliptic. Tìm key chia sẻ nP")
    print("0.Exit.")
    x = int(input("Chọn: "))
    print("")

    if x == 1:
        a1 = int(input("Nhap a = "))
        b1 = int(input("Nhap b = "))
        print("gcd(", a1, ",", b1, ") = ", gcd(a1, b1))
        slogan()
        menu()
    elif x == 2:
        a2 = int(input("Nhap a = "))
        b2 = int(input("Nhap b = "))
        print("ex_gcd(", a2, ",", b2, ") = ", gcd(a2, b2))
        slogan()
        menu()
    elif x == 3:
        a3 = int(input("Nhap a = "))
        n3 = int(input("Nhap n = "))
        a0 = mod_inv(a3, n3)
        print(a3, "^-1 mode ", n3, " = ", a0)
        slogan()
        menu()
    elif x == 4:
        a4 = int(input("Nhap a = "))
        b4 = int(input("Nhap b = "))
        n4 = int(input("Nhap n = "))
        print(a4, "^", b4, " mode ", n4, " = ",
              modular_exponentiation(a4, b4, n4))
        slogan()
        menu()
    elif x == 5:
        p5 = int(input("Nhap p = "))
        m5 = int(input("Nhap m = "))
        g5 = int(input("Nhap g = "))
        print("x = ", diffie_hellman(p5, m5, g5))
        slogan()
        menu()
    elif x == 6:
        n6 = int(input("Nhập n = "))
        tim_cac_phan_sinh(n6)
        slogan()
        menu()
    elif x == 7:
        p7 = int(input("Nhập p ="))
        q7 = int(input("Nhập q ="))
        e7 = int(input("Nhập e ="))
        y7 = int(input("Nhập y ="))
        print("Bản rõ là :", find_plaintextRSA(p7, q7, e7, y7))
        slogan()
        menu()
    elif x == 8:
        one_time_pad()
        slogan()
        menu()
    elif x == 9:
        n9 = int(input("Nhập n = "))
        e9 = int(input("Nhập e = "))
        find_signaturalRSA(n9, e9)
        slogan()
        menu()
    elif x == 10:
        print("(r,s) : ", find_signatural_elgamal())
        slogan()
        menu()

    elif x == 11:
        p11 = int(input("Nhap p = "))
        g11 = int(input("Nhap g = "))
        a11 = int(input("Nhap a = "))
        b11 = int(input("Nhap b = "))
        diffie_hellman_more(a11, b11, p11, g11)
        slogan()
        menu()
    elif x == 12:
        find_key_share()
        slogan()
        menu()
    elif x == 13:
        find_nP()
        slogan()
        menu()


def slogan():
    print('\n"Hãy làm việc hết mình, những điều tốt đẹp sẽ đến với bạn !')
    print('Do your best, the rest will come !"')
    print("--Nguyễn Tử Quảng\n")


if __name__ == "__main__":
    menu()
    print("\nChúc thi tốt! ^^\n")
