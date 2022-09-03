print('Enter a greeting:')
greeting = input()

print('Enter a recipient:')
recipient = input()

print('How many times to repeat:')
numberOfIterations = int(input())

for x in range(numberOfIterations):
  print(greeting + ' ' + recipient + '!')