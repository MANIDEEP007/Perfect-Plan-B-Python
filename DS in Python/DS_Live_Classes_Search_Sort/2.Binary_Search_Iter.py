def binary_search(str_arr,ser_str):
  len_arr = len(str_arr)
  low = 0
  high = len_arr-1
  while(low<=high):
    mid = (low+high)//2
    if(str_arr[mid] == ser_str):
      print("Element found at index "+str(mid))
      return
    if(str_arr[mid]<ser_str):
      low = mid +1
    else:
      high = mid -1
  print("Element Not Found")
str_arr = [2,3,4,10,40]
num_in = int(input("Enter Size of Array\n"))
for i in range(num_in):
  str_arr.append(int(input("Enter"+str(i+1)+" Input\n")))
ser_str = int(input("Enter Search String\n"))
binary_search(str_arr,ser_str)
