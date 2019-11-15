# customer = { 
# "Name":"John Smith",
# "Email":"john@gmail.com",
# "Phone":1234567890,
# "is_verified":True
# }
# print(customer["Name"])

#dictionary keys should be unique

# phone = input("Phone: ")

# digits = {
#     "1":"One",
#     "2":"Two",
#     "3":"Three",
#     "4":"Four",
#     "5":"Five",
#     "6":"Six",
#     "7":"Seven",
#     "8":"Eight",
#     "9":"Nine "
# }
# output = " "
# for ch in phone:
#     output += digits.get(ch,"!") + " "
# print(output)

def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)":"😀",
        ":(":"😞"
    }
    output = " "
    for word in words:
        output += emojis.get(word,word) + " "
    return output

message =  input(">")
print(emoji_converter(message))
