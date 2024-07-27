def roman_into_num(numerical):
    final_ans = 0

    if "CM" in numerical:
        final_ans += 900
        numerical = numerical.replace("CM", "")
    if "CD" in numerical:
        final_ans += 400
        numerical = numerical.replace("CD", "")
    if "XC" in numerical:
        final_ans += 90
        numerical = numerical.replace("XC", "")
    if "XL" in numerical:
        final_ans += 40
        numerical = numerical.replace("XL", "")
    if "IX" in numerical:
        final_ans += 9
        numerical = numerical.replace("IX", "")
    if "IV" in numerical:
        final_ans += 4
        numerical = numerical.replace("IV", "")

    for i in numerical:
        if i == "M":
            final_ans += 1000
        elif i == "D":
            final_ans += 500
        elif i == "C":
            final_ans += 100
        elif i == "L":
            final_ans += 50
        elif i == "X":
            final_ans += 10
        elif i == 'V':
            final_ans += 5
        elif i == 'I':
            final_ans += 1

    print("The roman numerals you entered translates to: " + str(final_ans) + "!")

roman_input = input("Enter roman numerals for conversion: ")
roman_into_num(roman_input)
