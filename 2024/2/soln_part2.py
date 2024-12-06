'''
--- Day 2: Red-Nosed Reports ---

Fortunately, the first location The Historians want to search isn't a long walk from the Chief Historian's office.

While the Red-Nosed Reindeer nuclear fusion/fission plant appears to contain no sign of the Chief Historian, the engineers there run up to
you as soon as they see you. Apparently, they still talk about the time Rudolph was saved through molecular synthesis from a single
electron.

They're quick to add that - since you're already here - they'd really appreciate your help analyzing some unusual data from the Red-Nosed
reactor. You turn to check if The Historians are waiting for you, but they seem to have already divided into groups that are currently
searching every corner of the facility. You offer to help with the unusual data.

The unusual data (your puzzle input) consists of many reports, one report per line. Each report is a list of numbers called levels that
are separated by spaces. For example:

7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9

This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are
either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.

In the example above, the reports can be found safe or unsafe by checking those rules:

    7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
    1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
    9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
    1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
    8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
    1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.

So, in this example, 2 reports are safe.

Analyze the unusual data from the engineers. How many reports are safe?

To begin, get your puzzle input.

'''
import requests, re, bisect

def isSafe(report:str):
    diff = 0
    allPos = False
    listVals = list(map(int, report.split(' ')))
    for i in range(len(listVals) - 1):
        diff = listVals[i+1] - listVals[i]
        if 1 > abs(diff) or abs(diff) > 3:
            return False
            
        if i == 0 and diff > 0:
            allPos = True
        if i > 0:
            if allPos and diff < 0:
                return False
            elif not allPos and diff > 0:
                return False
    return True


def isSafe2(report:str):
    diff = 0
    all_pos = False
    list_vals = list(map(int, report.split(' ')))
    error_list = []
    for i in range(len(list_vals) - 1):
        diff = list_vals[i+1] - list_vals[i]
        if 1 > abs(diff) or abs(diff) > 3:
            # mark
            error_list.append(i)
        if i == 0 and diff > 0:
            all_pos = True
        if i > 0:
            if all_pos and diff < 0:
                error_list.append(i)
            elif not all_pos and diff > 0:
                error_list.append(i)
    if not error_list:
        return True
    a = 0
    
    for i in range(len(list_vals)):
        a += isSafe(" ".join(map(str, list_vals[:i] + list_vals[i+1:])))
        
    return a > 0
    
    # if len(error_list) > 1:
    #     return False
    
    # return isSafe(" ".join(map(str, list_vals[:error_list[0]] + list_vals[error_list[0]+1:]))) or isSafe(" ".join(map(str, list_vals[:error_list[0]+1] + list_vals[error_list[0]+2:])))

print(isSafe2('7 6 4 2 1'))
print(isSafe2('1 2 7 8 9'))
print(isSafe2('9 7 6 2 1'))
print(isSafe2('1 3 2 4 5'))
print(isSafe2('8 6 4 4 1'))
print(isSafe2('1 3 6 7 9'))

count = 0
with open('2\input.txt', 'r') as f:
    for line in f.readlines():
        line = line.rstrip()
        count += isSafe2(line)
        

print(count)

