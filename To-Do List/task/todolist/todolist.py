# Write your code here
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

Base = declarative_base()


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today())


class ToDoList:

    def __init__(self):
        engine = create_engine('sqlite:///todo.db?check_same_thread=False')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def menu(self):
        while True:
            option = int(input("1) Today's tasks\n"
                               "2) Week's tasks\n"
                               "3) All tasks\n"
                               "4) Missed tasks\n"
                               "5) Add task\n"
                               "6) Delete task\n"
                               "0) Exit"))

            if option == 1:
                self.show_tasks_today()
            elif option == 2:
                self.show_tasks_week()
            elif option == 3:
                self.show_tasks()
            elif option == 4:
                self.show_tasks_missed()
            elif option == 5:
                self.add_task()
            elif option == 6:
                self.delete_task()
            elif option == 0:
                print('Bye!')
                exit()

    def show_tasks_today(self):
        today = datetime.today()
        tasks = self.session.query(Task).filter(Task.deadline == today.date()).all()
        print(f'Today {today.strftime("%d %b")}:')
        print('\n'.join(f'{task.id}. {task.task}' for task in tasks) if tasks else 'Nothing to do!', end='\n\n')

    def show_tasks_week(self):
        today = datetime.today()
        for i in range(7):
            date = today.date() + timedelta(days=i)
            tasks = self.session.query(Task).filter(Task.deadline == date).all()
            print(f'{date.strftime("%A %d %b").lstrip("0")}:')
            print('\n'.join(f'{task.id}. {task.task}' for task in tasks) if tasks else 'Nothing to do!', end='\n\n')

    def show_tasks(self):
        tasks = self.session.query(Task).order_by(Task.deadline).all()
        print('All tasks:')
        print('\n'.join(f'{task.id}. {task.task}. {task.deadline.strftime("%d %b").lstrip("0")}' for task in tasks)
              if tasks else 'Nothing to do!', end='\n\n')

    def show_tasks_missed(self):
        today = datetime.today()
        tasks = self.session.query(Task).filter(Task.deadline < today.date()).all()
        print('Missed tasks:')
        print('\n'.join(f'{task.id}. {task.task}. {task.deadline.strftime("%d %b").lstrip("0")}' for task in tasks)
              if tasks else 'Nothing is missed!', end='\n\n')

    def add_task(self):
        new_task = input('Enter task')
        new_deadline = datetime.strptime(input('Enter deadline'), '%Y-%m-%d')
        new_task = Task(task=new_task, deadline=new_deadline)
        self.session.add(new_task)
        self.session.commit()
        print('The task has been added!', end='\n\n')

    def delete_task(self):
        tasks = self.session.query(Task).order_by(Task.deadline).all()
        print('Choose the number of the task you want to delete:')
        print('\n'.join(f'{task.id}. {task.task}. {task.deadline.strftime("%d %b").lstrip("0")}' for task in tasks)
              if tasks else 'Nothing to do!', end='\n\n')
        self.session.query(Task).filter(Task.id == int(input())).delete()
        self.session.commit()
        print('The task has been deleted!', end='\n\n')


if __name__ == '__main__':
    ToDoList().menu()
