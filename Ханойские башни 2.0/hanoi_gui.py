
from tkinter import *
import tkinter.messagebox as messagebox
from hanoi import *

class HanoiSolver:

    def __init__(self, master):



        self.title = 'Ханойские башни'
        self.delay = 500
        self.max_disks = 10
        self.canv_width = 500
        self.canv_height = 300
        self.disk_height = 20
        self.disk_width_increment = 14
        self.base_height = 50
        self.base_colour = 'gray'
        self.stack_width = 10
        self.stack_height = 200
        self.space_between = 100
        self.colours = ["blue",'violet', 'orange', 'yellow', 'green', 'pink', 'purple','red',"green"]


        master.resizable(False, False)
        master.title(self.title)
        self.root = master


        self.toolbar = Frame(master, relief = RAISED)
        self.toolbar.pack(side = TOP, fill = X)


        self.canv = Canvas(width = self.canv_width, height = self.canv_height, bg = "white")
        self.canv.pack()


        Label(self.toolbar, text = "Задать количество дисков: ").pack(side = LEFT)


        self.enternum = Entry(self.toolbar, width = 7)
        self.enternum.pack(side = LEFT)
        self.enternum.insert(0, str(self.max_disks))


        Button(self.toolbar, text = "Правила", command = self.about).pack(side = RIGHT)
        Button(self.toolbar, text = "Следующая башня", command = self.next_step).pack(side = RIGHT)
        Button(self.toolbar, text = "Предыдущая башня", command = self.prev_step).pack(side = RIGHT)
        Button(self.toolbar, text = 'Стоп', command = self.stop).pack(side = RIGHT)
        Button(self.toolbar, text = 'Начать', command = self.auto).pack(side = RIGHT)
        Button(self.toolbar, text = 'Сначала', command = self.generate).pack(side = RIGHT)


        self.state = 0
        self.num_disks = self.max_disks
        self.states = []
        self.auto_running = True


        self.generate()

    def check_num_disks(self):
        try:
            num = int(self.enternum.get())
            if num < 1 or num > 10:
                messagebox.showwarning("Предупреждение", "Количество дисков должно быть от 1 до 10")
                return False
            else:
                return True
        except ValueError:
            messagebox.showerror("Ошибка", "Некорректный ввод")
            return False

    def generate(self):
        if self.check_num_disks():
            self.num_disks = int(self.enternum.get())
            self.state = 0
            self.states = hanoi(self.num_disks)
            self.draw_current_state()

    def prev_step(self):


        self.state -= 1

        if self.state < 0:
            self.state = len(self.states) - 1

        self.draw_current_state()

    def next_step(self):


        self.state = (self.state + 1) % len(self.states)
        self.draw_current_state()

    def get_stack_coordinate(self, stack_num):

        return (self.canv_width // 3) * stack_num + (self.canv_width // 6)

    def draw_base(self):



        self.canv.create_rectangle(
                0, self.canv_height - self.base_height, self.canv_width, self.canv_height,
                outline = self.base_colour,
                fill = self.base_colour
            )


        for i in range(3):

            start_x = self.get_stack_coordinate(i)


            self.canv.create_rectangle(
                    start_x, self.canv_height - self.base_height - self.stack_height, start_x + self.stack_width, self.canv_height - self.base_height,
                    outline = self.base_colour,
                    fill = self.base_colour
                )

    def draw_stack(self, stack_num, current_stacks):



        center = self.get_stack_coordinate(stack_num) + (self.stack_width // 2)


        y = self.stack_height + self.base_height - (self.disk_height * len(current_stacks[stack_num]))


        for index in range(len(current_stacks[stack_num])):

            value = current_stacks[stack_num][::-1][index]


            width = self.disk_width_increment * value + self.disk_width_increment;


            self.canv.create_rectangle(
                    center - (width // 2), y, center + (width // 2), y + self.disk_height,
                    fill = self.colours[(value - 1) % len(self.colours)]
                )


            y += self.disk_height


    def draw_current_state(self):


        self.canv.delete(ALL)


        self.draw_base()


        to_draw = self.states[self.state]


        for i in range(3):
            self.draw_stack(i, to_draw)


        self.canv.create_text(self.canv_width // 2, self.canv_height - (self.base_height // 2), text = f'Ходы: {self.state}')

    def auto_step(self):


        if self.state == len(self.states) - 1 or not self.auto_running:
            self.auto_running = False
            return


        self.next_step()


        self.root.after(self.delay, self.auto_step)

    def auto(self):

        self.auto_running = True
        self.root.after(self.delay, self.next_step)
        self.root.after(2 * self.delay, self.auto_step)

    def stop(self):

        self.auto_running = False

    def about(self):
        messagebox.showinfo("Правила", "Максимум 10 дисков. "
                                       "Есть три башни, на одной из которых находятся диски."
                                       "Нужно переложить их на свободную башню сохранив начальное чередование. "
                                       "За один ход может переложить одно кольцо. Диски перекладывается только с меньшего на большее и никак иначе."
                                       "Диски откладывать нельзя, только на другой свободный стержень. Принцип решения задачи будет заключаться в том, чтобы полностью переложить диски на свободную пирамидку, таким образом, чтобы они сохранили свое начальное чередование. "
                                       "Задача решена тогда и только тогда, когда диски будут полностью переложены на свободную пирамидку, с учетом правил. ")


root = Tk()
window = HanoiSolver(root)
root.mainloop()
