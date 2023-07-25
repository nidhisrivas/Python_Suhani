

import matplotlib.pyplot as mpl

hoursSlept =  [ 6, 7, 8, 5, 5, 6, 5, 6, 7, 5, 6, 7, 6,8]
gpa =  [3.49, 3.65, 3.4, 3.8, 3.78, 3.6, 3.9, 3.8, 3.95,3.8, 3.7, 3.4, 4.0,3.5]


colors = ["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta","orange"]
print(len(colors))
print(len(hoursSlept))
print(len(gpa))
#exit()

mpl.xlabel("Number of hrs Slept")
mpl.ylabel("Underweighted GPA")
mpl.scatter(hoursSlept, gpa, c=colors,marker="o")

mpl.show()

