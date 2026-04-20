def vowel(val):
    count = 0
    for i in range(len(val)):
        if (
            val[i] == "a"
            or val[i] == "e"
            or val[i] == "i"
            or val[i] == "o"
            or val[i] == "u"
        ):
            count += 1

    return count


res = vowel("aeiousssssss")
print(res)
