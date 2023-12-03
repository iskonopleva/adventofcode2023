import re

# open 1.txt
with open('1.txt', 'r') as f:
    # create dictionary to with digits speleld out as keys and their numerical value as values
    dict = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5,
            'six':6, 'seven':7, 'eight':8, 'nine':9}
    sum = 0
    for line in f:
        # find substring that starts and ends with number
        p = re.compile('^[a-zA-Z]*(one|two|three|four|five|six|seven|eight|nine|[0-9])+([a-zA-z0-9])*(one|two|three|four|five|six|seven|eight|nine|[0-9])*([a-zA-Z])*$')
        m = p.match(line)
        if m:
            # get the matched string from match object
            s = m.group()
            print(s)
            # get the first number from the matched string
            # myltiply by 10 to get the correct sum
            num1 = re.search('(one|two|three|four|five|six|seven|eight|nine|[0-9])', s).group()
            if num1 in dict:
                num1 = dict[num1] * 10
            else:
                num1 = int(num1) * 10
            # can't reverse string because of literal numbers
            # start iterating from end of string and then try and match every substring from index to end
            # if substring is found, then add it to the sum
            # if substring is not found, then add the last number to the sum
            for i in range(len(s)-1, -1, -1):
                num2 = re.match('(one|two|three|four|five|six|seven|eight|nine|[0-9])', s[i:])
                if num2:
                    num2 = num2.group()
                    if num2 in dict:
                        num2 = dict[num2]
                        break
                    else:
                        num2 = int(num2)
                        break
            # add the sum of the first and last number to the total sum
            sum += num1 + num2
            print(num1+num2)
    print(sum)

