import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Task:
    def __init__(self, task_name, is_completed):
        self.task_name = task_name
        self.is_completed = is_completed

class TaskManager:
    def __init__(self):
        self.tasks_list = []

    def add_tasks(self):
        clear_screen()
        print("--- Add New Tasks ---")
        user_input = input("Enter your tasks (separated by commas):\n").strip()
        
        if not user_input:
            print("\nError: No tasks entered.")
            time.sleep(2)
            return

        raw_tasks = [t.strip().capitalize() for t in user_input.split(',') if t.strip()]

        for t_name in raw_tasks:
            while True:
                status = input(f"\n({t_name}) Did you finish this task (Yes/No)? ").strip().lower()
                if status in ['yes', 'y']:
                    new_task = Task(t_name, is_completed=True)
                    print("Great job! 🎉")
                    break
                elif status in ['no', 'n']:
                    new_task = Task(t_name, is_completed=False)
                    print("Try to finish it today! 💪")
                    break
                else:
                    print("Error: Please enter Yes or No.")

            self.tasks_list.append(new_task)
        
        print("\nAll tasks processed successfully!")
        time.sleep(2)

    def view_progress(self):
        clear_screen()
        if not self.tasks_list:
            print("No tasks available to show progress.")
            time.sleep(2)
            return

        finished = [t.task_name for t in self.tasks_list if t.is_completed]
        unfinished = [t.task_name for t in self.tasks_list if not t.is_completed]

        print("=======================================")
        print(f"🎯 TASK PROGRESS REPORT (Total: {len(self.tasks_list)})")
        print("=======================================")
        
        print("\n✅ Finished Tasks:")
        if finished:
            for i, task in enumerate(finished, 1):
                print(f"  {i}. {task}")
        else:
            print("  (None)")

        print("\n❌ Unfinished Tasks:")
        if unfinished:
            for i, task in enumerate(unfinished, 1):
                print(f"  {i}. {task}")
        else:
            print("  (None)")
        
        print("=======================================")
        input("\nPress Enter to return to menu...")

    def main_menu(self):
        while True:
            clear_screen()
            print("        HUSSAM TASK MANAGER    ")
            print("===============================")
            print("1) Input & Process Tasks")
            print("2) View Progress Report")
            print("3) Exit System")
            print("===============================")
            
            choice = input("Select Option: ").strip()

            if choice == '1':
                self.add_tasks()
            elif choice == '2':
                self.view_progress()
            elif choice == '3':
                print("\nExiting System... Goodbye!")
                break
            else:
                print("\nInvalid choice! Please try again.")
                time.sleep(1)

if __name__ == "__main__":
    manager = TaskManager()
    manager.main_menu()
