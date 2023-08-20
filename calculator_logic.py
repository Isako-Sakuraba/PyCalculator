
class CalculatorLogic:
    @staticmethod
    def perform_action(action, num_l, num_r):
        if action == '+':
            result = num_l + num_r
        elif action == '-':
            result = num_l - num_r
        elif action == '*':
            result = num_l * num_r
        elif action == '/':
            result = num_l / num_r
        else:
            result = -1

        return result
