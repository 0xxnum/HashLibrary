## Overview
A simple 16-byte hashing algorithm using a customized S-box and P-box for hashing.

### Digest Size
- 16 bytes

### Output Size
- 16 bytes (in hexadecimal)

### Known Issues
- Padding uses the character "=" which can cause issues if the plaintext contains "=" at the end, potentially compromising collision resistance.
- Computing power and RAM usage were not considered in the design, which might affect efficiency.
- Collision resistance is not guaranteed due to the lack of extensive research and testing.

## Implementation Details

### S-Box
A substitution box used in the hashing algorithm:
```python
sbox = [198, 101, 83, 27, 238, 53, 44, 182, 56, 39, 219, 28, 76, 12, 22, 237, 128, 156, 23, 70, 153, 223, 158, 165, 71, 210, 135, 202, 196, 82, 38, 68, 178, 20, 89, 21, 220, 85, 11, 134, 249, 111, 84, 67, 9, 65, 95, 51, 207, 124, 96, 119, 87, 5, 236, 25, 205, 78, 234, 137, 253, 145, 150, 6, 163, 125, 29, 143, 194, 49, 73, 199, 240, 250, 247, 208, 7, 172, 209, 157, 103, 104, 231, 225, 155, 151, 254, 69, 245, 55, 18, 30, 8, 222, 200, 2, 189, 192, 193, 226, 167, 115, 191, 252, 248, 221, 133, 91, 1, 146, 154, 109, 211, 108, 181, 34, 92, 37, 16, 94, 173, 174, 170, 251, 113, 31, 36, 93, 184, 138, 40, 33, 214, 106, 14, 203, 97, 116, 243, 188, 81, 212, 19, 161, 233, 75, 48, 122, 166, 190, 176, 54, 43, 235, 46, 42, 144, 136, 206, 130, 61, 140, 148, 102, 63, 62, 224, 177, 80, 218, 162, 180, 10, 35, 141, 90, 41, 117, 107, 129, 204, 230, 79, 228, 110, 4, 139, 88, 195, 232, 86, 227, 99, 52, 149, 255, 131, 57, 169, 171, 186, 152, 217, 17, 114, 215, 0, 3, 175, 32, 242, 98, 126, 168, 47, 24, 59, 197, 159, 72, 185, 74, 187, 66, 123, 15, 239, 244, 121, 50, 179, 77, 241, 26, 105, 118, 127, 164, 100, 147, 201, 112, 58, 216, 45, 60, 246, 160, 64, 13, 132, 183, 120, 229, 142, 213]
