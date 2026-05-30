class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        # compare time it takes to get to target
        # go in reverse sorted order 
        # if next car has < t (time to target), it will become fleet with front car, so we can remove
        # same logic for next cars
        # use stack, if car becomes fleet, pop
        
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        # sorted based on position
        cars.sort(key=lambda x:x[0])

        stack = []
        for i in range(len(cars)-1, -1, -1):
            curr_time = (target - cars[i][0]) / cars[i][1]
            if len(stack) < 1 or curr_time > stack[-1]:
                stack.append(curr_time)
        
        return len(stack)