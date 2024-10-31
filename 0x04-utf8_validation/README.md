The task is to implement a function `valid_utf8(data)` in Python that checks if a given list of integers represents valid UTF-8 encoded data. UTF-8 encoding can represent characters in 1 to 4 bytes, with each byte following a specific bit pattern:

1. **1-byte character**: Starts with `0xxxxxxx`
2. **2-byte character**: Starts with `110xxxxx` followed by `10xxxxxx`
3. **3-byte character**: Starts with `1110xxxx` followed by two `10xxxxxx`
4. **4-byte character**: Starts with `11110xxx` followed by three `10xxxxxx`

### Steps to Validate UTF-8 Encoding

1. **Identify Leading Byte**: Check the number of leading `1`s in the first byte to determine the total bytes in the character.
2. **Check Continuation Bytes**: Each subsequent byte in the multi-byte character should start with `10`.
3. **Return Result**: If all characters meet the UTF-8 pattern, return `True`; otherwise, return `False`.

The solution uses bitwise operations to isolate specific bits in each byte, validating each part of the UTF-8 sequence in the data list.
