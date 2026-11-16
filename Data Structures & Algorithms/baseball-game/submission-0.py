class Solution:
    def calPoints(self, operations: List[str]) -> int:
        temp = []
        for i in range(len(operations)):
            match operations[i]:
                case "+":
                    temp.append(temp[-1]+temp[-2])
                case "D":
                    temp.append(temp[-1]*2)
                case "C":
                    temp.pop()
                case _:
                    temp.append(int(operations[i]))
        return sum(temp)

