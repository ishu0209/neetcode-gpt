class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        prev_output = init

        if iterations >0:
            for i in range(iterations):
                prev_output = (prev_output - learning_rate*(2*prev_output))
        
        return round(prev_output,5)
        pass
