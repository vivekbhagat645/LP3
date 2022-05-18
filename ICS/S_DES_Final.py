P10 = (3,5,2,7,4,10,1,9,8,6)
P8 = (6,3,7,4,8,5,10,9)
P4 = (2,4,3,1)

IP = (2,6,3,1,4,8,5,7)
IPi = (4,1,3,5,7,2,8,6)

E = (4,1,2,3,2,3,4,1)

s0=[
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 3, 2]
]
s1=[
    [0, 1, 2, 3],
    [2, 0, 1, 3],
    [3, 0, 1, 0],
    [2, 1, 0, 3]
]

def permutation(pattern,key):
    permuted = ""

    for i in pattern:
        permuted += key[i-1]
    return permuted


def generate_first(left,right):
    left = left[1:] + left[:1]
    right = right[1:] + right[:1]
    key = left + right

    return permutation(P8,key)


def generate_second(left,right):
    left = left[3:] + left[:3]
    right = right[3:] + right[:3]
    key = left + right

    return permutation(P8,key)


def transform(right, key):
    extended = permutation(E, right)
    xor_cipher = bin(int(extended,2) ^ int(key,2))[2:].zfill(8)
    xor_left = xor_cipher[:4]
    xor_right = xor_cipher[4:]

    new_left = Sbox(xor_left,s0)
    new_right = Sbox(xor_right,s1)

    return permutation(P4, new_left+new_right)


def Sbox(data,box):
    row = int(data[0] + data[3],2)
    column = int(data[1] + data[2],2)

    return bin(box[row][column])[2:].zfill(2)


def encrypt1(left, right, key):
    cipher = bin(int(left,2) ^ int(transform(right, key),2))[2:].zfill(4)

    return right, cipher


def encrypt2(left, right, key):
    cipher = bin(int(left,2) ^ int(transform(right, key),2))[2:].zfill(4)

    return cipher,right

key = input("Enter a 10-bit key: ")
if len(key)!=10:
    raise Exception("Check the input")


plaintext = input("Enter 8-bit Plaintext:")
if len(plaintext)!=8:
    raise Exception("Check the input")

p10key = permutation(P10,key)
print("First Permutation (P10)")
print(p10key)

left_key = p10key[:len(p10key)//2]
print("Left Key part: ",left_key)

right_key = p10key[len(p10key)//2:]
print("Right Key part: ",right_key)

first_key = generate_first(left_key,right_key)
print("First SubKey: ",first_key)

second_key = generate_second(left_key,right_key)
print("Second SubKey: ",second_key)

initial_permutation = permutation(IP,plaintext)
print("Initial Permutation: ",initial_permutation)

left_data = initial_permutation[:len(initial_permutation)//2]
right_data = initial_permutation[len(initial_permutation)//2:]

left,right = encrypt1(left_data, right_data, first_key)
print("After Round1 & Swap: ",left+right)
left,right = encrypt2(left , right, second_key)
print("After Round2: ",left+right)

key=left+right
cipher=permutation(IPi, key)
print("Cipher Text After Encryption: ", cipher)

ipD= permutation(IP, cipher)

left_partD=ipD[:4]
right_partD=ipD[4:]

leftD, rightD = encrypt1(left_partD, right_partD, second_key)
print("After Round2 & swap", leftD+rightD)

left_D,right_D=encrypt2(leftD,rightD,first_key)
print("After Round1", left_D+right_D)

pltext=permutation(IPi,left_D+right_D)
print("Plain Text", pltext)