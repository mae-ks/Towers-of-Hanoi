from stacks import *
class Towers(Stacks):
    def rePeek(self):
        if self.peek() is None:
            return self.max_size + 1
        else:
            return self.peek()

print("Welcome to Mae's Towers of Hanoi:)")
disks = int(input("Number of disks: "))

stack_A = Towers(disks)
stack_B = Towers(disks)
stack_C = Towers(disks)
stacks = {"A": stack_A, "B": stack_B, "C": stack_C}

for x in range(disks, 0, -1):
    stack_A.push(x)

def visualize(stacks):
    for key, value in stacks.items():
        print("%s\n%s" %(key, value))

def move():
    moveFrom = input("Where do you want to move from? ")
    moveTo = input("Where do you want to move to? ")
    for key, value in stacks.items():
        if moveFrom == key:
            moveFrom = value
        if moveTo == key:
            moveTo = value
    if moveFrom.rePeek() < moveTo.rePeek():
        moveTo.push(moveFrom.pop())
    else:
        print("Invalid move.")

while stack_C.size != stack_C.max_size:
    move()
    visualize(stacks)

print("Congratulations!")