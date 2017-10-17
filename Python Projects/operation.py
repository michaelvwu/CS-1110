# Michael Wu (mvw5mf)

import os

print(os.listdir(os.getcwd()))

total_size = 0
for filename in os.listdir(os.getcwd()):
      total_size = total_size + os.path.getsize(os.path.join(os.getcwd(),filename))

print(total_size)

output_file = open("output_file.txt", "w")

output_file.write(str(os.listdir(os.getcwd())))
output_file.write('\n')
output_file.write(str(total_size))
output_file.close()
