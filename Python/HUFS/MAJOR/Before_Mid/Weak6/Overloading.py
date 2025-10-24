# # class ConstructorOverload:
# #     def __init(self, val1,val2):
# #         self.first_val = val1
# #         self.second_val = val2

# #     @classmethod
# #     def withThreeInput(cls, val1, val2, val3):
# #         return cls(val1 + val2 + val3)
    
# #     @classmethod
# #     def fromListInput(cls, ListVal):
# #         return cls(ListVal[0], ListVal[1])
    
# #     def add(self):
# #         return self.first_val + self.second_val
# import math

# class Vector2D:
#     def __init__(self, x, y):
#         self.x, self.y= x, y

#     @classmethod
#     def from_seq(cls, seq):


#     def PrintVector(self):
#         return f"{self.__class__.__name__}(x={self.x:.2f}, y={self.y:.2f})"