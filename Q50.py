all = set(['John','Mary','Tina','Fiona','Claire','Eva','Ben','Bill','Bert'])
en = set(['John','Mary','Fiona','Claire','Ben','Bill'])
math = set(['Mary','Fiona','Claire','Eva','Ben'])
a = all - math
print("英文數學都及格",en & math)
print("數學不及格",a)
print("英文及格且數學不及格",en & a)