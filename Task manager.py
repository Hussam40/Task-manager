finished_tasks = []
unfinished_tasks = []

tasks = input('Please enter your tasks separated by comma...\n').split(', ')
for t in tasks:
   while True:
      status = input(f"\n({t}) Did you finish this task(Yes/No)?\n").lower()
      if status not in ['yes', 'no']:
         print('Please enter Yes or No')
         continue
      
      elif status == 'no':
         unfinished_tasks.append(t)
         print('Try to finish it today')
      
      else:
         finished_tasks.append(t)
         print('Great job!')
      break
see_task = input('Do you want to see your progress(Yes/No)?').lower()
if see_task == 'yes':
   print(f'''
***Finished tasks***
   
{finished_tasks}

***Unfinished tasks***

{unfinished_tasks}''')

else:
   print('Exiting...') 