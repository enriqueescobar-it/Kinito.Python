from Section15_Interpreter.InterpreterParsing.BinaryOperation import BinaryOperation
from Section15_Interpreter.InterpreterParsing.Integer import Integer
from Section15_Interpreter.InterpreterParsing.Token import Token


def lex(input):
    result = []

    i = 0
    while i < len(input):
        if input[i] == '+':
            result.append(Token(Token.TypeEnum.PLUS, '+'))
        elif input[i] == '-':
            result.append(Token(Token.TypeEnum.MINUS, '-'))
        elif input[i] == '(':
            result.append(Token(Token.TypeEnum.LPAREN, '('))
        elif input[i] == ')':
            result.append(Token(Token.TypeEnum.RPAREN, ')'))
        else:  # must be a number
            digits = [input[i]]
            for j in range(i + 1, len(input)):
                if input[j].isdigit():
                    digits.append(input[j])
                    i += 1
                else:
                    result.append(Token(Token.TypeEnum.INTEGER,
                                        ''.join(digits)))
                    break
        i += 1

    return result


# ↑↑↑ lexing ↑↑↑
# ↓↓↓ parsing ↓↓↓


def parse(tokens):
    result = BinaryOperation()
    have_lhs = False
    i = 0
    while i < len(tokens):
        token = tokens[i]

        if token.type == Token.TypeEnum.INTEGER:
            integer = Integer(int(token.text))
            if not have_lhs:
                result.left = integer
                have_lhs = True
            else:
                result.right = integer
        elif token.type == Token.TypeEnum.PLUS:
            result.type = BinaryOperation.TypeEnum.ADDITION
        elif token.type == Token.TypeEnum.MINUS:
            result.type = BinaryOperation.TypeEnum.SUBTRACTION
        elif token.type == Token.TypeEnum.LPAREN:  # note: no if for RPAREN
            j = i
            while j < len(tokens):
                if tokens[j].type == Token.TypeEnum.RPAREN:
                    break
                j += 1
            # preprocess subexpression
            subexpression = tokens[i + 1:j]
            element = parse(subexpression)
            if not have_lhs:
                result.left = element
                have_lhs = True
            else:
                result.right = element
            i = j  # advance
        i += 1
    return result


def eval(input):
    tokens = lex(input)
    print(' '.join(map(str, tokens)))

    parsed = parse(tokens)
    print(f'{input} = {parsed.value}')


if __name__ == '__main__':
    eval('(13+4)-(12+1)')
    eval('1+(3-4)')

    # this won't work
    eval('1+2+(3-4)')
