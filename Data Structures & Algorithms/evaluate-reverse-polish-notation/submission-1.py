class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        op = ["+", "-", "/", "*"]

        for t in tokens:
            if t in op:
                num2 = int(s.pop())
                num1 = int(s.pop())

                if t == "+":
                    res = (num1 + num2)
                if t == "-":
                    res = (num1 - num2)
                if t == "*":
                    res = (num1 * num2)
                if t == "/":
                    res = int(num1 / num2)

                s.append(res)

            else:
                s.append(t)

        return int(s[-1])