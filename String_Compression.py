class Solution:
    def compress(self, chars: List[str]) -> int:
        left= i = 0
        while i < len(chars):
            char, length = chars[i], 1
            while (i+1)<len(chars) and char == chars[i+1]:
                length, i = length+1, i+1
            chars[left] = char
            if length > 1:
                len_str = str(length)
                chars[left + 1: left + 1 + len(len_str) ] = len_str
                # print((len_str))
                left += len(len_str)
            left, i = left + 1, i+1
        return left
#         current = ''
#         loc = 0
#         for i in range(len(chars)):
#             if chars[i] != current:
#                 current = chars[i]
#                 loc = i
#                 count = 1
#             else:
#                 count += 1
#                 chars[i] = str(count)
                
#         # count = 0
# #         while count < len(chars) - 1:
# #             # if chars[count].ischar():
# #                 # continue
# #             print(chars)
# #             print(count)
# #             if chars[count].isdigit():
# #                 while chars[count+1].isdigit()
                
# #                 # while chars[count+1].isdigit() and count < len(chars)-1:
# #                 #     print(chars)
# #                 #     print(count)
# #                 #     del chars[count]
# #                 #     count += 1
            
# #             # if chars[count].isdigit() and chars[count+1].isdigit():
# #             #     del chars[count]
                
# #             # else:
# #             # continue
# #             count += 1
#         count = 0
#         for i in chars:
#             if i.isalpha():
#                 count += 2
#         return count
        