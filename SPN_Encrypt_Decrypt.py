#Parameters of S box
S_Box = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7]

#Parameters of P box
P_Box = [1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 16]


def gen_K_list(K):
    """
    Secret key arrangement algorithm, which generates five 16-bit sub-keys from a 32-bit secret key
    Param K: 32-bit secret key
    Return: [k1, k2, k3, k4, k5], five 16-bit subkeys
    """
    Ks = []
    for i in range(5, 0, -1):
        ki = K % (2 ** 16)
        Ks.insert(0, ki)
        K = K >> 4
    return Ks


def pi_s(s_box, ur):
    """
    Packet substitution operation
    Param s_box:S box parameter
    Paramur: Input Bit String, 16 Bits
    Return: Output Bit String, 16 Bits
    """
    vr = 0
    for i in range(4):
        uri = ur % (2 ** 4)
        vri = s_box[uri]
        vr = vr + (vri << (4 * i))
        ur = ur >> 4
    return vr


def pi_p(p_box, vr):
    """
    Single bit permutation operation
    Param p_box: P-box parameter
    Param vr: input bit string, 16 bits
    Return: Output Bit String, 16 Bits
    """
    wr = 0
    for i in range(15, -1, -1):
        vri = vr % 2
        vr = vr >> 1
        wr = wr + (vri << (16 - p_box[i]))
    return wr


def reverse_Sbox(s_box):
    """
    Finding the Inverse of S-Box
    Param s_box:S box parameter
    The inverse of return:S box
    """
    re_box = [-1] * 16
    for i in range(16):
        re_box[s_box[i]] = i
    return re_box


def reverse_Pbox(p_box):
    """
    Finding the Inverse of P-Box
    Param s_box:P-box parameter
    Return: The Inverse of P Box
    """
    re_box = [-1] * 16
    for i in range(16):
        re_box[p_box[i] - 1] = i + 1
    return re_box


def do_SPN(x, s_box, p_box, Ks):
    """
    Five rounds of SPN network can be used for encryption or decryption
    Param x: 16 bit input
    Param s_box: S box parameter
    Param p_box: P-box parameter
    Param Ks: [k1, k2, k3, k4, k5], five 16-bit subkeys
    Return: 16 bit output
    """
    wr = x
    for r in range(3):
        Ur = wr ^ Ks [r] #XOR operation
        VR = pi_s (s_box, ur) # packet substitution
        wr = pi_p (p_box, vr)  #single bit permutation

    ur = wr ^ Ks[3]
    vr = pi_s(s_box, ur)
    y = vr ^ Ks[4]
    return y


def encrypt(K, x):
    """
    Encryption of 16-bit plaintext x based on secret key K
    Param K:32-bit secret key
    Param x: 16 bits plaintext
    Return: 16 bits ciphertext
    """
    Ks = gen_K_list(K)
    return do_SPN(x, S_Box, P_Box, Ks)


def decrypt(K, y):
    """
    The 16-bit ciphertext y is decrypted according to the secret key K.
    Param K:32-bit secret key
    Param y: 16 bit ciphertext
    Return: 16 bits plaintext
    """
    Ks = gen_K_list(K)
    Ks. reverse ()# reverse key orchestration
    # Secret key replacement
    Ks[1] = pi_p(P_Box, Ks[1])
    Ks[2] = pi_p(P_Box, Ks[2])
    Ks[3] = pi_p(P_Box, Ks[3])

    S_rbox = reverse_Sbox (S_Box) # S-box inversion
    P_rbox = reverse_Pbox (P_Box) # P-box inversion
    return do_SPN(y, S_rbox, P_rbox, Ks)


if __name__ == '__main__':
    x = 0b0010011010110111
    K = 0b00111010100101001101011000111111
    print ('initial plaintext:', format (x,'016b'))
    print ('encrypted ciphertext:', format (encrypt (K, x),'016b'))
    print ('decryption result:', format (decrypt (K, encrypt (K, x),'016b')))
    assert decrypt(K, encrypt(K, x)) == x