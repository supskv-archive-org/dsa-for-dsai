open_parenthesis = ['(', '{', '[']
close_parenthesis = [')', '}', ']']

# <-- use stack
def check_parenthesis_stack(arr, stack = [], show_step=False):
    if (show_step):
        print(f"Stack: {stack}.")

    if (len(arr) == 0):
        if (len(stack) != 0):
            return 'NOT OK'
        return 'OK'
    
    value = arr[0]
    if (value in open_parenthesis):
        stack.append(value)
    elif (value in close_parenthesis and close_parenthesis.index(value) == open_parenthesis.index(stack[-1])):
        stack.pop()
    return check_parenthesis_stack(arr[1:], stack, show_step)

def check_parenthesis_queue(queue, attempt, show_step=False):
    if (show_step):
        print(f"Queue: {queue}, attempt: {attempt}.")

    if (len(queue) == 0):
        return 'OK'
    if (attempt == 0 or len(queue) == 1): # <-- prevent out of range
        return 'NOT OK'

    #1 pull queue
    first, new_queue = queue[0], queue[1:]

    #2 mapping bracket n and n+1, and pull it again, otherwise re-queue
    if (first in open_parenthesis):
        open_i = open_parenthesis.index(first)
        opposite = close_parenthesis[open_i]
        second = queue[1]
        if (second == opposite):
            new_queue = new_queue[1:]
            attempt = len(new_queue)
        else:
            new_queue.append(first)
            attempt -= 1
    else:
        new_queue.append(first)
        attempt -= 1
    
    # use attempt to prevent inf. loop
    return check_parenthesis_queue(new_queue, attempt, show_step)

def check_parenthesis(str, method = 'stack', show_step=False):
    arr = list(str)
    if (method == 'stack'):
        return check_parenthesis_stack(arr, [], show_step)
    elif (method == 'queue'):
        return check_parenthesis_queue(arr, len(arr), show_step)
    raise ValueError('Method is invalid, please choose stack or queue.')

str = "{[[]]{()}}"
# str = "[{}"
# str = "([[]])({[{()}]}{}[[]])"
# str = "[[{}}"

print(f"Bracket String [Stack]: {str}")
result = check_parenthesis(str)
print(f"Result [Stack]: {result}")
result = check_parenthesis(str, method="queue", show_step=True)
print(f"Result [Queue]: {result}")
