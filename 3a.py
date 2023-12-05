import re

with open('3.txt', 'r') as f:
    sum = 0
    # skip first line
    prev = ""
    curr = f.readline()
    next = ""
    # create regex expression to match symbols that are not periods or digits
    p = re.compile('[^0-9\.]')
    # iterate through the rest
    for line in f:
        next = line.strip()
        # iterate through curr, check adjacents for each ecountered digit against prev and next
        # index to keep track of the last catched number
        index = 0
        i = 0
        while i < len(curr):
            valid = False
            # check if current character is a digit
            # and if it is, check adjacents
            if curr[i].isdigit():
                # check adjacents in prev
                if prev != "":
                    if p.match(prev[max(0, i-1)]) or p.match(prev[i]) or p.match(prev[min(i+1, len(prev)-1)]):
                        valid = True
                # check adjacents in curr
                if p.match(curr[max(0, i-1)]) or p.match(curr[min(i+1, len(curr)-1)]):
                    valid = True
                # check adjacents in next
                if p.match(next[max(0, i-1)]) or p.match(next[i]) or p.match(next[min(i+1, len(next)-1)]):
                    valid = True
            # if the character is valid (aka has an adjacent symbol)
            # retrieve adjacent number and add to sum
            # then adjust i to skip current number
            if valid:
                # get the number
                # go back from current i to the first instance of period and search from that index
                for j in range(len(curr[0:i]), -1, -1):
                    if not curr[j].isdigit():
                        index = j
                        break
                num = re.search('[0-9]+', curr[index:]).group()
                index = index + curr[index:].index(num) + len(num)
                # add to sum
                sum += int(num)
                # adjust i
                i = index
            else:
                i += 1        
        prev = curr.strip()
        curr = next.strip()
    # check last line against second to last (curr against prev)
    # iterate through curr, check adjacents for each ecountered digit against prev and next
    # index to keep track of the last catched number
    index = 0
    i = 0
    while i < len(curr):
        valid = False
        # check if current character is a digit
        # and if it is, check adjacents
        if curr[i].isdigit():
            # check adjacents in prev
            if prev != "":
                if p.match(prev[max(0, i-1)]) or p.match(prev[i]) or p.match(prev[min(i+1, len(prev)-1)]):
                    valid = True
            # check adjacents in curr
            if p.match(curr[max(0, i-1)]) or p.match(curr[min(i+1, len(curr)-1)]):
                valid = True
        # if the character is valid (aka has an adjacent symbol)
        # retrieve adjacent number and add to sum
        # then adjust i to skip current number
        if valid:
            # get the number
            # go back from current i to the first instance of period and search from that index
            for j in range(len(curr[0:i]), -1, -1):
                if not curr[j].isdigit():
                    index = j
                    break
            num = re.search('[0-9]+', curr[index:]).group()
            index = index + curr[index:].index(num) + len(num)
            # add to sum
            sum += int(num)
            # adjust i
            i = index
        else:
            i += 1

    print(sum)

