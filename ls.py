import sys
import webbrowser
from urllib.parse import urlparse

arguments = sys.argv
d = {}
# Url and code cant contain `
# mem.txt is always empty when program is installed and user cant edit mem.txt
# assume webbrowser.open() works everytime
try:
    with open('mem.txt', 'r') as file:
        link_list = file.readlines()
        number = len(link_list) + 1
        for i in range(len(link_list)):
            current_link = link_list[i].strip().split('`')
            d[current_link[0]] = current_link[1]
except FileNotFoundError:
    with open('mem.txt', 'w') as file:
        file.write("")
    link_list = []
    number = 1

def find_line(index, type = 'code'):
    i = 0
    l = []
    for x in d:
        if type == 'code':
            if x == arguments[index]:
                return i
            i += 1
        elif type == 'link':
            if arguments[index] in d[x]:
                l.append(i)
            i += 1
    return l

def write(content):
    with open('mem.txt', 'w') as file:
        file.writelines(content)

def url_validity(url):
    parsed = urlparse(url)
    return parsed.scheme in ('http', 'https') and bool(parsed.netloc)

def new_num(number):
    for x in link_list:
        if f'link{number}' == x.split("`")[0]:
            return new_num(number+1)
    return number

if len(arguments) > 1:

    if arguments[1] == 'shorten':
        if len(arguments) == 3:
            if url_validity(arguments[-1]):
                with open('mem.txt', 'a') as file:
                    file.write(f'link{new_num(number)}`{arguments[-1]}`0\n')
                    print(f'link{new_num(number)}')
            else:
                print('Invalid URL')
        elif len(arguments) == 5:
            if url_validity(arguments[-3]):
                if arguments[-2] == '--alias':
                    if "`" not in arguments[-1]:
                        if d.get(arguments[-1], 0) == 0:
                            with open('mem.txt', 'a') as file:
                                file.write(f'{arguments[-1]}`{arguments[-3]}`0\n')
                        else:
                            print('code already used')
                            choice = input('Do you want to overwrite it? y/N: ')
                            if choice.lower() == 'y':
                                line = find_line(-1)
                                temp = link_list[line].split('`')
                                temp[1] = arguments[-3]
                                link_list[line] = "`".join(temp)
                                write(link_list)
                    else:
                        print("Code name cant contain '`'")
                else:
                    print(f'{arguments[-2]} is not a recognised command')
                    print('Please read Readme.txt for list of commands')

            else:
                print('Invalid URL')
        elif len(arguments) == 2:
            print("No link entered to shorten")
        elif len(arguments) == 4 and arguments[-1] == '--alias':
            print('No alias was entered')
        elif len(arguments)  == 4:
            print(f'{arguments[-1]} is not a recognised command')
            print('Please read Readme.txt for list of commands')
        elif arguments[3] == '--alias':
            print("Only 1 argument expected after '--alias'")
        else:
            print('Invalid Input')


    elif arguments[1] == 'delete':
        if len(arguments) == 3:
            try:
                line = find_line(-1)
                link_list.pop(line)
                write(link_list)
            except TypeError:
                print("No such code found")
        elif len(arguments) == 2:
            print("Please enter a code to delete")
        else:
            print("Only 1 argument expected after 'delete'")

    elif arguments[1] == 'resolve':
        if len(arguments) == 3:
            try:
                print(f"Opening {d[arguments[-1]]}")
                webbrowser.open(d[arguments[-1]])
                with open('mem.txt', 'r') as file:
                    lines = file.readlines()
                line = find_line(-1)    
                temp_line = lines[line].split("`")
                temp_line[2] = str(int(temp_line[2]) + 1)
                lines[line] = "`".join(temp_line) + "\n"
                write(lines)
                
            except KeyError:
                print('no code found')
        elif len(arguments) == 2:
            print('Please enter a code to resolve')
        else:
            print("Only 1 argument expected after 'resolve'")

        
        
    elif arguments[1] == 'count':
        if len(arguments) == 3:
            try:
                line = find_line(-1)
                print(f"This code has been used {link_list[line].split('`')[2].strip()} times")
            except TypeError:
                print(f'{arguments[-1]} is not a saved code')

        elif len(arguments) == 2:
            print("No code entered to check use count")
        else:
            print("Only 1 argument expected after 'count'")

    elif arguments[1] == 'list':
        if len(arguments) == 2:
            for x in d:
                print(f'Code: {x}, Link: {d[x]}')
        else:
            print("No arguments expected after 'list'")
            
    elif arguments[1] == 'info':
        try:
            if len(arguments) == 3:
                line = link_list[find_line(-1)].split("`")
                print(f'Code: {line[0]}\nLink: {line[1]}\nCount: {line[2].strip()}')
            elif len(arguments) == 2:
                print('Please enter a code')
            elif len(arguments) > 3:
                print("Expected only 1 argument after 'info'")
        except TypeError:
            print("No such code found")

    elif arguments[1] == 'clear':
        if len(arguments) == 2:
            print("Are you sure you want to clear all saved links? y/N: ")
            choice = input()
            if choice.lower() == 'y':
                write("")
        else:
            print("No arguments expected after 'clear'")

    elif arguments[1] == 'reset':
        try:
            if len(arguments) == 3:
                line = link_list[find_line(-1)].split("`")
                line[2] = '0\n'
                link_list[find_line(-1)] = "`".join(line)
                write(link_list)
            elif len(arguments) == 2:
                print("No code entered")
            else:
                print("Only 1 argument expected after 'reset'")
        except TypeError:
            print("Please enter a valid code")

    elif arguments[1] == 'search':
        if len(arguments) == 3:
            lines = find_line(-1, 'link')
            if lines:
                for x in lines:
                    temp = link_list[x].split("`")
                    print(f'Code: {temp[0]}, Link: {temp[1]}, Count: {temp[2].strip()}')
            else:
                print("No results found")
        elif len(arguments) == 2:
            print("Please enter something to search")
        else:
            print("Only one argument expected after 'search'")

    elif arguments[1] == 'stats':
        total = 0
        most_used = 0
        ind = 0
        try:
            if len(arguments) == 2:
                for i in range(len(link_list)):
                    total += int(link_list[i].split("`")[2].strip())
                    if most_used < int(link_list[i].split("`")[2].strip()):
                        most_used = int(link_list[i].split("`")[2].strip())
                        ind = i
                print(f'Total Links: {len(link_list)}\nTotal Resolves: {total}\nMost used: {link_list[ind].split("`")[0]} resolved {link_list[ind].split("`")[2].strip()} times')
            else:
                print("No argument expected after 'stats'")
        except IndexError:
            print("No links shortened yet")

    elif arguments[1] == 'sort':
        if len(arguments) <= 3:
            new_list = []
            for i in range(len(link_list)):
                line = link_list[i].split('`')
                new_list.append(line[:2] + [int(line[2].strip())])
            if arguments[-1] == 'reversed':
                new_list.sort(key=(lambda x: x[2]))
                for x in new_list:
                    print(f'Count: {x[2]}, Code: {x[0]}, Link: {x[1]}')
            elif len(arguments) == 2:
                new_list.sort(key=(lambda x: x[2]), reverse=True)
                for x in new_list:
                    print(f'Count: {x[2]}, Code: {x[0]}, Link: {x[1]}')
            elif len(arguments) == 3:
                print(f'{arguments[-1]} is not a recognised command')
        else:
            print(f"Maximum 1 argument expected after 'sort'")
            


    else:
        print(f'{arguments[1]} is not a recognised command')
        print('Please read Readme.txt for list of commands')

else:
    print("no command entered to execute")
    print('Please read Readme.txt for list of commands')