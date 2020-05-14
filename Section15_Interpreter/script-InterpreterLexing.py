from Section15_Interpreter.InterpreterLexing.BinaryOperation import BinaryOperation
from Section15_Interpreter.InterpreterLexing.Integer import Integer
from Section15_Interpreter.InterpreterLexing.TokenEnum import TokenEnum


def lex(input):
    result = []

    i = 0
    while i < len(input):
        if input[i] == '+':
            result.append(TokenEnum(TokenEnum.Type.PLUS, '+'))
        elif input[i] == '-':
            result.append(TokenEnum(TokenEnum.Type.MINUS, '-'))
        elif input[i] == '(':
            result.append(TokenEnum(TokenEnum.Type.LPAREN, '('))
        elif input[i] == ')':
            result.append(TokenEnum(TokenEnum.Type.RPAREN, ')'))
        else:  # must be a number
            digits = [input[i]]
            for j in range(i + 1, len(input)):
                if input[j].isdigit():
                    digits.append(input[j])
                    i += 1
                else:
                    result.append(TokenEnum(TokenEnum.Type.INTEGER,
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

        if token.type == TokenEnum.Type.INTEGER:
            integer = Integer(int(token.text))
            if not have_lhs:
                result.left = integer
                have_lhs = True
            else:
                result.right = integer
        elif token.type == TokenEnum.Type.PLUS:
            result.type = BinaryOperation.TypeEnum.ADDITION
        elif token.type == TokenEnum.Type.MINUS:
            result.type = BinaryOperation.TypeEnum.SUBTRACTION
        elif token.type == TokenEnum.Type.LPAREN:  # note: no if for RPAREN
            j = i
            while j < len(tokens):
                if tokens[j].type == TokenEnum.Type.RPAREN:
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
