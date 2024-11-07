grade = int(input('Enter your grade: '))

''' one line / sebaris '''
if grade >= 65: print('passed the exam')
if grade < 65: print('bellow the passing grade')

''' Ternary '''
print('lulus ujian') if grade >= 65 else print('tidak lulus ujian')

''' Ternary dengan nilai balik '''
message = "Lulus Terbaik" if grade >= 65 else "Langsung di Drop Out"
print(message)
