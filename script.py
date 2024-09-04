#  _   _   ___   _____  _   _  _____  _   _  _____                
# | | | | / _ \ /  ___|| | | ||_   _|| \ | ||  __ \               
# | |_| |/ /_\ \\ --. | |_| |  | |  |  \| || |  \/               
# |  _  ||  _  | --. \|  _  |  | |  | .  || | __                
# | | | || | | |/\__/ /| | | | _| |_ | |\  || |_\ \               
# \_| |_/\_| |_/\____/ \_| |_/ \___/ \_| \_/ \____/                                                                         
#   ___   _      _____  _____ ______  _____  _____  _   _ ___  ___
#  / _ \ | |    |  __ \|  _  || ___ \|_   _||_   _|| | | ||  \/  |
# / /_\ \| |    | |  \/| | | || |_/ /  | |    | |  | |_| || .  . |
# |  _  || |    | | __ | | | ||    /   | |    | |  |  _  || |\/| |
# | | | || |____| |_\ \\ \_/ /| |\ \  _| |_   | |  | | | || |  | |
# \_| |_/\_____/ \____/ \___/ \_| \_| \___/   \_/  \_| |_/\_|  |_/
#
# Python 3.10.2                                                        
# By ahmed tarek (0xxnum) 2023

sbox = [198, 101, 83, 27, 238, 53, 44, 182, 56,
    39, 219, 28, 76, 12, 22, 237, 128,
    156, 23, 70, 153, 223, 158, 165, 71,
    210, 135, 202, 196, 82, 38, 68, 178,
    20, 89, 21, 220, 85, 11, 134, 249,
    111, 84, 67, 9, 65, 95, 51, 207,
    124, 96, 119, 87, 5, 236, 25, 205,
    78, 234, 137, 253, 145, 150, 6, 163,
    125, 29, 143, 194, 49, 73, 199, 240,
    250, 247, 208, 7, 172, 209, 157,
    103, 104, 231, 225, 155, 151, 254,
    69, 245, 55, 18, 30, 8, 222, 200, 2,
    189, 192, 193, 226, 167, 115, 191,
    252, 248, 221, 133, 91, 1, 146, 154,
    109, 211, 108, 181, 34, 92, 37, 16,
    94, 173, 174, 170, 251, 113, 31, 36,
    93, 184, 138, 40, 33, 214, 106, 14,
    203, 97, 116, 243, 188, 81, 212, 19,
    161, 233, 75, 48, 122, 166, 190,
    176, 54, 43, 235, 46, 42, 144, 136,
    206, 130, 61, 140, 148, 102, 63, 62,
    224, 177, 80, 218, 162, 180, 10, 35,
    141, 90, 41, 117, 107, 129, 204,
    230, 79, 228, 110, 4, 139, 88, 195,
    232, 86, 227, 99, 52, 149, 255, 131,
    57, 169, 171, 186, 152, 217, 17,
    114, 215, 0, 3, 175, 32, 242, 98,
    126, 168, 47, 24, 59, 197, 159, 72,
    185, 74, 187, 66, 123, 15, 239, 244,
    121, 50, 179, 77, 241, 26, 105, 118,
    127, 164, 100, 147, 201, 112, 58,
    216, 45, 60, 246, 160, 64, 13, 132,
    183, 120, 229, 142, 213
]

def block(data, BLOCKSIZE=16):
    blockers = []
    padding = BLOCKSIZE - len(data) % BLOCKSIZE
    data += "=" * padding
    counts = len(data) // BLOCKSIZE
    for chunk in range(counts):
        blockers.append(data[chunk * BLOCKSIZE:(chunk + 1) * BLOCKSIZE])
    return blockers

def permute(lst):
    length = len(lst)
    determinant = 4 # optimal to be a multiple of 2  (most optimized tested = 4)
    for i in range(length):
       # for a 16 byte digest, there are 14 rounds of permutations 
        computed = (determinant * (length + i)) % length
        lst[i], lst[computed] = lst[computed], lst[i]
    return lst

def substitute(lst, operation=True):
    # creates a 16x16 table
    # finds the given value in the list
    # return its index as its substitution
    # if operation is TRUE  > normal  subst  (value to index)
    # if operation is FALSE > inverse subst  (index to value)
  
    substituted = []
    for integer in lst:
        if operation:
            out = sbox.index(integer)
        else:
            out = sbox[integer]
        substituted.append(out)
    return substituted

def hash(plaintext):
    # digests blocks of 16 bytes
    blocks = block(plaintext, 16)
    length = len(blocks)
    hashValue = []
    blocks = [[ord(i) for i in out] for out in blocks]
   # constant counter to kickstart xor
    ctr = 50
     # iterates hash multiple times to enhance avalanche effect
    for iteration in range(15):
        for i in range(len(blocks)):
            inTemp = []
           # substitutes and permutes each block
            blocks[i] = substitute(permute(blocks[i]))

            for j in blocks[i]:
                inTemp.append((ctr ^ j) % 256)
                ctr += j * 3 # 3 constant to enhance avalanche effect even 
            # substitutes and permutes each block again
            blocks[i] = substitute(permute(inTemp))
            # to enhance collision resistance
            ctr += length
            hashes = []
             # final sum xoring
            for j in blocks[i]:
                ctr = (ctr ^ j) % 256
                hashes.append(ctr)
            hashValue.append(hashes)
               # counter is brought over to second loop
    out = ""
      # compiles all calculated hash values into 16 bytes in hexadecimal
    for j in range(16):
        hexadecimal = sum([g[j] for g in hashValue]) % 256
        out += format(hexadecimal, "x").zfill(2)

    print(out)
    return out

# Hash-testing
if hash("alright can it verify passwords though?") == "82fc6794264cc0f9685e7dbb2900e54c":
    print("yep it can")
else:
    print("nah it cant")
# Test #1
#                                     v  capitalized character
hash("This is the first hashing test, i wonder what hash it will give me and how well the avalanche effect is on this hashing algorithm that i made by myself, 3:47AM in the morning!")
hash("This is the first hashing test, I wonder what hash it will give me and how well the avalanche effect is on this hashing algorithm that i made by myself, 3:47AM in the morning!")

# Results
# First hash  : 6738fa9368a580b1883814a5bbd7504f
# Second hash : d8f501e7293ad2a0714f9352fcfd7a20
# PASS

# Test #2
#                                                 v an extra character
hash("Wow this algorithm is pretty impressive, hmmm does it take into consideration the length of the message?")
hash("Wow this algorithm is pretty impressive, hmm does it take into consideration the length of the message?")

# Results
# First hash  : 6b9d7323df9a37bee65c5cd796616c93
# Second hash : a0868ac47fd2aa0bf2a6125e54d7c613
# PASS

# Test #3
#                                                                       v one bit alteration
hash("Ok now's the big challenge, a huge plaintext that has a ONE bit alseration, can the hashing algorithm detect a change in this massive plaintext? i think it might be able to. However I do have my doubts, after all i designed this hashing algorithm in less than a day, did absolutely no tests other than this one and did no form of optimization whatsoever. Enough typing i think its time for me to test what this thing can do")
hash("Ok now's the big challenge, a huge plaintext that has a ONE bit alteration, can the hashing algorithm detect a change in this massive plaintext? i think it might be able to. However I do have my doubts, after all i designed this hashing algorithm in less than a day, did absolutely no tests other than this one and did no form of optimization whatsoever. Enough typing i think its time for me to test what this thing can do")

# Results
# First hash  : 1acce02a9ad44b3e1533edaffa7934c0
# Second hash : 49a4ef3f09e9843b19001414f701c527
# PASS

# Test #4
# computed hash: 82fc6794264cc0f9685e7dbb2900e54c

if hash("alright can it verify passwords though?") == "82fc6794264cc0f9685e7dbb2900e54c":
    print("yep it can")

else:
    print("nah it cant")

## End
