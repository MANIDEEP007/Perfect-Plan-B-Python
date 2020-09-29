file_obj = open("Sample_File.txt")
file_obj1 = open("Sample_File_Odd.txt","w")
lines = file_obj.readlines()
for index in range(0,len(lines)):
    if (index+1) % 2 != 0:
        file_obj1.write(lines[index])
file_obj.close()
file_obj1.close()
    
