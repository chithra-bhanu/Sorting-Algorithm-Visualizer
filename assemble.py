from tkinter import *
from tkinter import ttk
import time
import random
class Graphics():
    def __init__(self, screen_size):
        self.screen_size = screen_size
        self.window = Tk()
        self.speed = 50
        self.clicked = False
        self.canvas = Canvas
        self.array = []
        self.sort_method = "Bubble Sort"
        self.open_window(self.window)

    def open_window(self, window):
        self.window = window
        window.title("Sorting Algorithms Visualizer")
        size = [str(i) for i in self.screen_size]
        size = "x".join(size)
        window.geometry(size)
        window.config(bg = '#f2f2f2')
        separator = ttk.Separator(window, orient='horizontal')
        separator.place(relx=0, rely=0.27, relwidth=1, relheight=1)
        self.canvas = Canvas(window, width=700, height= 365, bg='#f2f2f2')
        self.canvas.place(relx=0.0, rely=0.28)
        self.algorithm_selector()
        self.speed_selector()
        self.generate_button()
        self.sort_button()
        window.mainloop()

    def algorithm_selector(self):
        def change_method(*args):
            self.sort_method = drop.get()
        label = StringVar()
        label.set("Sorting Algoritm")
        algos = ["Bubble Sort", "Merge Sort", "Quick Sort"]
        drop = ttk.Combobox(self.window, values=algos, state="readonly")
        drop.current(0)
        drop.place(x = self.screen_size[0] * 0.6, y = self.screen_size[1] * 0.03)
        drop.bind("<<ComboboxSelected>>", change_method)

    def speed_selector(self):
        def change_speed(*args):
            self.speed = int(speeds[drop.get()])
        label = StringVar()
        label.set("Sorting Speed")
        speeds = {'Fast': '70', 'Medium' : '50', 'Slow': '30'}
        drop = ttk.Combobox(self.window, values=list(speeds.keys()), state="readonly")
        drop.place(x = self.screen_size[0] * 0.15, y = self.screen_size[1] * 0.03)
        drop.current(0)
        drop.bind("<<ComboboxSelected>>", change_speed)

    def generate_button(self):
        button = Button(self.window, text = "Generate Array", command = self.generate_bars)
        button.pack()
        button.place(x = self.screen_size[0] * 0.3, y = self.screen_size[1] * 0.17)


    def sort_button(self):
        button = Button(self.window, text = "Sort", command = self.sort)
        button.pack()
        button.place(x = self.screen_size[0] * 0.56, y = self.screen_size[1] * 0.17)

    def draw_bars(self, array: list[int], colour = '#000000'):
        self.canvas.delete("all")
        canvas_width = self.screen_size[0] * 0.98
        canvas_height = self.screen_size[1] * 0.7
        x_width = canvas_width / len(array)
        spacing = 2
        for i, height in enumerate(array):
            x1 = i * x_width + spacing
            y1 = canvas_height - height
            x2 = (i + 1) * x_width
            y2 = canvas_height
            self.canvas.create_rectangle(x1, y1, x2, y2, fill = colour)

    def generate_array(self):
        array = random.sample(range(1, 350), self.get_speed())
        self.array = array
        return array

    def generate_bars(self):
        array = self.generate_array()
        self.draw_bars(array, '#000000')

    def get_speed(self):
        return self.speed

    def sort(self):
        if self.sort_method == "Bubble Sort":
            self.bubble_sort()
        elif self.sort_method == "Merge Sort":
            self.merge_sort(self.array, 0, len(self.array) - 1)
        elif self.sort_method == "Quick Sort":
            self.quick_sort(0 ,len(self.array) - 1, self.array)

    def set_speed(self):
        if self.speed == 70:
            return 0.001
        elif self.speed == 50:
            return 0.1
        elif self.speed == 30:
            return 0.3

    def bubble_sort(self):
        size = len(self.array)
        for i in range(size-1):
            for j in range(size-i-1):
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
                    self.draw_bars(self.array, '#33334d')
                    self.canvas.update()
                    time.sleep(self.set_speed())
        self.draw_bars(self.array, '#00cc00')

    def merge(self, array, start, mid, end):
        p = start
        q = mid + 1
        temp_arr= []
        for i in range(start, end + 1):
            if p > mid:
                temp_arr.append(array[q])
                q += 1
            elif q > end:
                temp_arr.append(array[p])
                p += 1 
            elif array[p] < array[q]:
                temp_arr.append(array[p])
                p += 1
            else:
                temp_arr.append(array[q])
                q += 1

        for i in range(len(temp_arr)):
            array[start] = temp_arr[i]
            start += 1

    def merge_sort(self, array, start, end):
        if start < end:
            mid = ((start + end) // 2)
            self.merge_sort(array, start, mid)
            self.merge_sort(array, mid + 1, end)
            self.merge(array, start, mid, end)
            self.draw_bars(array, '#33334d')
            self.canvas.update()
            time.sleep(self.set_speed())
        self.draw_bars(array, '#00cc00')

    def quick_sort(self, start, end, array):
        if (start < end):
            p = self.partition(array, start, end)
            self.quick_sort(start, p - 1, array)
            self.quick_sort(p + 1, end, array)
            self.draw_bars(array, '#33334d')
            self.canvas.update()
            time.sleep(self.set_speed())
        self.draw_bars(array, '#00cc00')

    def partition(self, array, start, end):
        pivot_index = start
        pivot = array[pivot_index]
        while start < end:
            while start < len(array) and array[start] <= pivot:
                start += 1
            while array[end] > pivot:
                end -= 1
            if(start < end):
                array[start], array[end] = array[end], array[start]
        array[end], array[pivot_index] = array[pivot_index], array[end]
        return end
