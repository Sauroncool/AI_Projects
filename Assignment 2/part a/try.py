class Proplogic:

    def findbracs(s):
        # this function breaks code into smaller segments, and saves them in "var" list.
        var = []
        bracket = ''
        a = s
        c = 0
        brac = 0
        a.lower()
        while (a):
            if a[0] == '(':
                if brac == 0:
                    if c == 1:
                        bracket = '~('
                        a = a[1:]
                        c = 0
                    else:
                        bracket = '('
                        a = a[1:]
                else:
                    a = a[1:]
                    bracket = bracket + '('
                brac += 1
                continue
            if a[0] == ')':
                brac -= 1
                if brac == 0:
                    bracket = bracket + ')'
                    var.append(bracket)
                    a = a[1:]
                else:
                    a = a[1:]
                    bracket = bracket + ')'
                continue
            if brac > 0:
                bracket = bracket + a[0]
                a = a[1:]
                continue
            if a[0] == '~':
                # negation
                c += 1
                a = a[1:]
            elif a[0].isalpha():

                if a[0] != 'a' and a[0] != 'o':
                    if c == 1:
                        k=0
                        while( (not a[k].isspace()) and (a[k]!=')')):
                            if k==(len(a)-1):
                                break
                            k+=1
                        var.append('~' + a[:k])
                        a = a[k:]
                        c = 0
                    else:
                        k=0
                        while(not a[k].isspace() and a[k]!=')'):
                            if k==(len(a)-1):
                                k+=1
                                break
                            k+=1
                        var.append(a[:k])
                        a = a[k:]
                        c = 0
                    continue
                elif len(a) > 2 and a[0] == 'a':
                    if a[:3] == 'and':
                        var.append('and')
                        a = a[3:]
                    else:
                        if c == 1:
                            k=0
                            while((not a[k].isspace()) and a[k]!=')'):
                                k+=1
                                if k == (len(a)):
                                    break
                            var.append('~' + a[:k])
                            a = a[k:]
                            c = 0
                        else:
                            k=0
                            while((not a[k].isspace()) and a[k]!=')'):
                                k+=1
                                if k == (len(a)):
                                    break
                            var.append(a[:k])
                            a = a[k:]
                            c = 0
                elif len(a) > 1 and a[0] == 'o':
                    if a[:2] == 'or':
                        var.append('or')
                        a = a[2:]
                    else:
                        if c == 1:
                            k=0
                            while((not a[k].isspace()) and a[k]!=')'):
                                k+=1
                                if k == (len(a)):
                                    break
                            var.append('~' + a[:k])
                            a = a[k:]
                            c = 0
                        else:
                            k=0
                            while((not a[k].isspace()) and a[k]!=')'):
                                k+=1
                                if k == (len(a)):
                                    break
                            var.append(a[:k])
                            a = a[k:]
                            c = 0
               	else:
               	    if c == 1:
                        k=0
                        while((not a[k].isspace) and (a[k]!=')')):
                            k+=1
                            if k == (len(a)):
                                break
                        var.append('~' + a[k])
                        a = a[k:]
                        c = 0
                    else:
                        k=0
                        while((not a[k].isspace) and (a[k]!=')')):
                            k+=1
                            if k == (len(a)):
                                break
                        var.append(a[0])
                        a = a[1:]
                        c = 0
            elif a[0].isspace():
                a = a[1:]
            elif a[0] == '<':
                # double implication
                var.append('<=>')
                a = a[3:]
            elif a[0] == '=':
                # implies
                var.append('=>')
                a = a[2:]

            else:
                print("Invalid input")
                a=a[1:]

        print(var)
        return (var)

    def implies(block):
        # lets try to convert implication to "negation" and "or"
        for i in range(len(block)):
            if block[i] == '=>':
                if block[i - 1][0] == '~':
                    block[i - 1] = block[i - 1][1:]
                else:
                    block[i - 1] = '~' + block[i - 1]
                block[i] = 'or'

        print(block)
        return block

    def doubleimplies(block):
        a = []
        b = []
        for i in range(len(block)):
            if block[i] == '<=>':
                a = Proplogic.implies([block[i - 1], '=>', block[i + 1]])
                b = Proplogic.implies([block[i + 1], '=>', block[i - 1]])
                block[i - 1] = '('
                block[i] = 'and'
                block[i + 1] = '('
                for p in a:
                    block[i - 1] += p
                for q in b:
                    block[i + 1] += q
                block[i - 1] += ')'
                block[i + 1] += ')'
        print(block)
        return (block)

    # Now I am assuming that there is no implication/double implication in the code anywhere and solving de morgan's
    # rule However, if the implies and double implies functions are run before this one, it still works perfectly
    def demorgan(block):
        c = 0
        for i in range(len(block)):
            c = 0
            if block[i][0] == '~' and block[i][1] == '(':
                c = -1
                j = 0

                for k in range(len(block[i])):
                    # We dont want to access ands and ors inside say the second or third brackets
                    if block[i][k] == '(':
                        c += 1
                    elif block[i][k] == ')':
                        c -= 1
                    elif block[i][k] == 'a' and block[i][k + 1] == 'n' and c == 0:
                        # and
                        # find the next character that is not a whitespace:
                        l = k + 3
                        while block[i][l].isspace():
                            l += 1
                        m = k - 1
                        while block[i][m].isspace():
                            m -= 1
                        # Do the same for the previous character
                        if block[i][2] == '~':
                            block[i] = block[i][1] + block[i][3:m + 1] + ' or ' + '~' + block[i][l:]
                            break
                        if block[i][l] == '~':
                            block[i] = block[i][1] + '~' + block[i][2:m + 1] + ' or ' + block[i][l + 1:]
                            break
                        if block[i][l] == '~' and block[i][2] == '~':
                            block[i] = block[i][1] + block[i][3:m + 1] + ' or ' + block[i][l + 1:]
                            break
                        if block[i][l] != '~' and block[i][2] != '~':
                            block[i] = block[i][1] + '~' + block[i][2:m + 1] + ' or ' + '~' + block[i][l:]
                            break
                    elif block[i][k] == 'o' and block[i][k + 1] == 'r' and c == 0:
                        # or
                        # repeat what we did for and
                        l = k + 2
                        while block[i][l].isspace():
                            l += 1
                        m = k - 1
                        while block[i][m].isspace():
                            m -= 1
                        if block[i][2] == '~':
                            block[i] = block[i][1] + block[i][3:m + 1] + ' and ' + '~' + block[i][l:]
                            break
                        if block[i][l] == '~':
                            block[i] = block[i][1] + '~' + block[i][2:m + 1] + ' and ' + block[i][l + 1:]
                            break
                        if block[i][l] == '~' and block[i][2] == '~':
                            block[i] = block[i][1] + block[i][3:m + 1] + ' and ' + block[i][l + 1:]
                            break
                        if block[i][l] != '~' and block[i][2] != '~':
                            block[i] = block[i][1] + '~' + block[i][2:m + 1] + ' and ' + '~' + block[i][l:]
                            break
        print(block)
        return (block)

    def associateAND(block):
        # pls run demorgan block before this
        c = 0
        for i in range(len(block)):
            if block[i] == 'and':
                if block[i + 1][0] == '(':
                    c = -1
                    for k in range(len(block[i + 1])):
                        if block[i + 1][k] == '(':
                            c += 1
                            continue
                        elif block[i + 1][k] == ')':
                            c -= 1
                            continue
                        elif block[i + 1][k] == 'a' and block[i + 1][k + 1] == 'n' and c == 0:
                            # inner block is an AND block as well. Open the brackets
                            temp = Proplogic.findbracs(block[i + 1][1:len(block[i + 1])])
                            temp.reverse()
                            del block[i + 1]
                            for m in range(len(temp)):
                                block.insert(i + 1, temp[m])
                            block = Proplogic.associateAND(block)
                            break

        print(block)
        return (block)

    def associateOR(block):
        # We now do the same thing with OR
        for i in range(len(block)):
            if block[i] == 'or':
                if block[i + 1][0] == '(':
                    c = -1
                    for k in range(len(block[i + 1])):
                        if block[i + 1][k] == '(':
                            c += 1
                            continue
                        elif block[i + 1][k] == ')':
                            c -= 1
                            continue
                        elif block[i + 1][k] == 'o' and block[i + 1][k + 1] == 'r' and c == 0:
                            # inner block is an OR block as well. Open the brackets
                            temp = Proplogic.findbracs(block[i + 1][1:len(block[i + 1])])
                            temp.reverse()
                            del block[i + 1]
                            for m in range(len(temp)):
                                block.insert(i + 1, temp[m])
                            block = Proplogic.associateOR(block)
                            break

        print(block)
        return (block)


#	def commutate
#	def toCNF(block):


# print("Enter a logic statement of the following form:")
# print("~ operator should precede the operand to represent the 'not' operation")
# print("Use the words 'and' and 'or' to represent the logical And and Or operations respectively")
# print("Use '=>' to represent implication")
# print("Use '<=>' to represent double implication")
# print("Make sure that every binary operator is written between the two operands it is operating on")
# s = input()



s = 'a and o12'
#s='a    '
#s = 'a => (b or c or ~(d and e))'
#s = '(a <=> b) and ~(c and d) and (~e => f)'
block0 = Proplogic.findbracs(s)

# block1 = Proplogic.doubleimplies(block0)
# block2 = Proplogic.implies(block1)
# block3 = Proplogic.demorgan(block2)
# block4 = Proplogic.associateAND(block3)
# block5 = Proplogic.associateOR(block4)
# block6 = Proplogic.demorgan(block5)
# block7 = Proplogic.associateOR(block6)


def do_all_in_loop(block0):
    copy_of_block0 = block0.copy()
    # Had to make a copy because for some reason the value of block0 is becoming same as block1, block2, block3 etc.
    block1 = Proplogic.doubleimplies(block0)
    block2 = Proplogic.implies(block1)
    block3 = Proplogic.demorgan(block2)
    block4 = Proplogic.associateAND(block3)
    block5 = Proplogic.associateOR(block4)
    if block5 == copy_of_block0:
        # print(f'block5={block5}')
        # print(f'block0={copy_of_block0}')
        return block5
    do_all_in_loop(block5)


do_all_in_loop(block0)

# Input ~a or (b or c or ~(d and e))
# Input a => (b or c or ~(d and e))
# Answer = ['~a', 'or', 'b', 'or', 'c', 'or', '~d', 'or', '~e']
