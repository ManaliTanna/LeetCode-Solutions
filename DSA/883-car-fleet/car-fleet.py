class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # Store position and speed together
        ps_pairs = [[p,s] for p,s in zip(position,speed)]

        # Sort according to positions of car in Ascending order
        ps_pairs = sorted(ps_pairs,reverse=True)

        # Keep stack to keep track of number of fleets
        stack = []

        for p, s in ps_pairs:
            # Calculate time take to reach target
            distance = target - p
            time = distance/s
            stack.append(time)
            # If the old car will reach before (less time) the newly added car in stack
            # It will collide and now travel at the same speed as the slower car
            # So we can remove higher speed car and only keep the lower one 
            # It has now become a fleet
            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)



