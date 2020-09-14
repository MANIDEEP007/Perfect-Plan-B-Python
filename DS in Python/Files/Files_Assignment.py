'''
Make a file names "file.txt" and copy paste the following lines in the file:
"From xyz.vhy@perfectplanb.net Sat Jan 5 09:14:16 2008. Return-Path:
Received: from murder (perfectplanb.net [141.211.14.90]) by mail.perfectplanb.net with
LMTPA;Sat, 05 Jan 2008 09:14:16 -0500"
Then, Write a program to read through this file and print the contents of the file
(line by line) all in uppercase.
Output should be as follows: "FROM XYZ.VHY@PERFECTPLANB>NET SAT JAN 5 09:14:16 2008.
RETURN-PATH: RECEIVED: FROM MURDER (PERFECTPLANB>NET [141.211.14.90])
BY MAIL.PERFECTPLANB.NET WITH LMTPA; SAT, 05 JAN 2008 09:14:16 -0500"
'''
file_obj = open("file.txt")
for line in file_obj:
    print(line.rstrip().upper())
