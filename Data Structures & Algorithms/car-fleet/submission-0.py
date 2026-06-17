class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pair_dict = {p:s for p,s in zip(position,speed)}
        pairs = dict(sorted(pair_dict.items(),reverse = True))
        print(pairs)

        stack=[]

        for p,s in pairs.items():
            stack.append((target-p)/s)

            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

