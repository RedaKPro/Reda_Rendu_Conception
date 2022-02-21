import datetime, time
import operator


class Task:

    def __init__(self, NAME, STATE, PERIOD, EXECUTION_TIME, PRIORITY=0):
        self.NAME = NAME
        self.STATE = STATE
        self.PERIOD = PERIOD
        self.EXECUTION_TIME = EXECUTION_TIME
        self.PRIORITY = PRIORITY  # 0 by default

        self.NEXT_DEADLINE = datetime.datetime.now()
        self.LAST_EXECUTED_TIME = datetime.datetime.now()

        self.EXECUTION_DONE = 100  # Big number by default

    def need_to_run(self):

        if datetime.datetime.now() > self.NEXT_DEADLINE + datetime.timedelta(seconds=self.PERIOD):
            print("\tTask " + self.NAME + "\Å§FAILED deadline.\t" + str(
                self.EXECUTION_DONE / self.EXECUTION_TIME) + "% done.")
            self.NEXT_DEADLINE += datetime.timedelta(seconds=self.PERIOD)
            self.EXECUTION_DONE = 0

        if datetime.datetime.now() > self.NEXT_DEADLINE:
            return True

        return False

    def run(self):

        global timer

        print(str(timer) + "\t=> " + self.NAME + " " + str(self.EXECUTION_DONE / self.EXECUTION_TIME) + "%")
        time.sleep(1)
        self.EXECUTION_DONE += 1

        if self.EXECUTION_DONE == self.EXECUTION_TIME:
            print(str(timer) + "\tTask " + self.NAME + " finished his job : 100%")
            self.EXECUTION_DONE = 0
            self.STATE = 'waiting'
            self.NEXT_DEADLINE = self.NEXT_DEADLINE + datetime.timedelta(seconds=self.PERIOD)
            return

        if self.EXECUTION_DONE < self.EXECUTION_TIME:
            print(str(timer) + "\tTask " + self.NAME + " en cours")

        if self.EXECUTION_DONE > self.EXECUTION_TIME:
            print(str(timer) + "\tTask " + self.NAME + " est bloqué")

        if self.NEXT_DEADLINE > datetime.datetime.now():
            print(str(timer) + "\tTask " + self.NAME + " finished his job : " + str(
                self.EXECUTION_DONE / self.EXECUTION_TIME) + "%")
            self.EXECUTION_DONE = 0
            self.NEXT_DEADLINE = self.NEXT_DEADLINE + datetime.timedelta(seconds=self.PERIOD)
            return


if __name__ == "__main__":

    # Definition of all tasks and instanciation
    task_list = [
        Task(NAME="Pump 1", STATE="waiting", PERIOD=5, EXECUTION_TIME=2, PRIORITY=1),
        Task(NAME="Pump 2", STATE="waiting", PERIOD=15, EXECUTION_TIME=3, PRIORITY=1),
        Task(NAME="Machine 1", STATE="waiting", PERIOD=5, EXECUTION_TIME=5, PRIORITY=1),
        Task(NAME="Machine 2", STATE="waiting", PERIOD=5, EXECUTION_TIME=3, PRIORITY=1)]

    global timer
    global tank
    timer = -1
    tank = -1

    # Global scheduling loop
    while (True):

        task_to_run = None
        task_priority = 0
        timer += 1
        tank += 1
        oil = 0

        # Choose the task to be run
        for current_task in task_list:

                if current_task.STATE == 'waiting':
                    if (task_list[1].NAME == 'Pump 2' and task_list[1].STATE == 'waiting') or (
                            task_list[2].NAME == 'Machine 1' and task_list[2].STATE == 'waiting') or (
                            task_list[3].NAME == 'Machine 2' and task_list[3].STATE == 'waiting'):
                        task_priority = current_task.PRIORITY
                        task_to_run = current_task
                        task_to_run.run()


        if task_to_run == None:
            time.sleep(1)
            print(str(timer) + "\tIdle")