class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        stack = []
        tokens = []
        curr_tokens = [] ##
        while:
            curr = expression[i]
            if state == 'start':
                if curr == '{':
                    state = 'open'
                elif curr.isalpha():
                    state = 'id'
            elif state == 'open':
                tokens.append(curr_tokens)
                curr_tokens = []
                # id_start = None
                stack.push(None)
                if curr.isalpha():
                    state = 'id'
                elif curr == '{':
                    state = 'open'
            elif state == 'id':
                if curr.isalpha():
                    if id_start == None:
                        id_start = i
                else:
                    curr_tokens.append(expression[id_start:i])
                    id_start = None
                    if curr == '{' and stack.peek() == None:
                        stack[-1] = '&'
                        state = 'open'
                    elif curr == '{' and stack.peek() == '&':
                        state = 'open'
                    elif curr == ',' and stack.peek() == None:
                        stack[-1] = ','
                        state = 'comma'
                    elif curr == ',' and stack.peek() == ',':
                        state = 'comma'

                    elif curr == '}':
                        state = 'close'
            elif state == 'close':
                # Do our own
                operation = stack.pop()
                out = set()
                if operation == ',':
                    for t in curr_tokens:
                        out.add(t)
                # Do previous
                curr_tokens = tokens.pop()
                if stack.peek() == '&':
                    for t in curr_tokens:
                        for o in out:
                            
                if curr.isalpha():
                    state = 'id'
                elif curr == '}':
                    state = 'close'
                elif curr == '{':
                    state = 'open'
                elif curr == ',':
                    state = 'comma'
                
                    
                    

            elif state == 'comma':
                if curr == '{':


class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        def get_id(i):
        def do(tokens, op):
            if op==',':
            elif op=='&':
        def expand(start, pre_tokens):
            i = start
            while i<len(expression):
                if curr == ',':
                    op = ','
                elif curr.isalpha():
                    i, identifier = get_id(i)
                    tokens.append(identifier)####
                elif curr == '{':
                    if op==',':
                    else:
                    tokens = expand(i, tokens)####
                elif curr == '}':
                    if op==',':
                        ####
                    else:
                        do(tokens, op)

                    return tokens