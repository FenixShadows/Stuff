inputs = [1,2,3,2.5]
weights1 = [0.2,0.8,-0.5,1]
weights2 = [0.5,-0.91,0.26,-0.5]
weights3 = [-0.26,-0.27,0.17,87]

biais1 = 2
biais2 = 3
biais3 = 0.5

output = [(inputs[0]*weights1 + inputs[1]*weights1 + inputs[2]*weights1 + inputs[3]*weights1 + biais1),(inputs[0]*weights2 + inputs[1]*weights2 + inputs[2]*weights2 + inputs[3]*weights2 + biais2),(inputs[0]*weights3 + inputs[1]*weights3 + inputs[2]*weights3 + inputs[3]*weights3 + biais3) ]

print(output)