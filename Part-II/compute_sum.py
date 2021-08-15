def test(lst):
  pos_sum = 0
  neg_sum = 0
  for n in lst:
    if n > 0:
      pos_sum += n
    elif n < 0:
      neg_sum += n
  return max(pos_sum, neg_sum, key=abs)

nums = { 0, -10, -11, -12, -13, -14, 15, 16, 17, 18, 19, 20 };
print("Original array elements:");
print(nums)
print("Largest sum - Positive/Negative numbers of the said array: ", test(nums));
nums = { -11, -22, -44, 0, 3, 4 , 5, 9 };
print("\nOriginal array elements:");
print(nums)
print("Largest sum - Positive/Negative numbers of the said array: ", test(nums));
