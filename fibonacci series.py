from tkinter import*
root=Tk()

root.title("Fibonacci Series")
root.geometry("400x300")
root.config(bg="#E5E1EE")

label_series = Label(root, text="fibonacci series: ")
label_flower = Label(root)
label_spiral = Label(root)

def Fibonacci():
    num = 10
    first_n = 0
    second_n = 1
    sum = 0
    counter = 1
    while(counter <= num):
        label_series["text"]+= str(sum) + " "
        counter = counter+1
        first_n = second_n
        second_n = sum
        sum = first_n + second_n
        
    label_flower["text"]= "The flower has fully bloomed!"
    label_spiral["text"]= "Spirals in the right direction are "+ str(first_n)+ " and spirals in the left direction are "+ str(second_n)+ "|n. the total spirals are "+ str(sum)

btn = Button(root, text="Show Fibonacci series."command = Fibonacci)
btn.pack()
label_series.pack()
label_flower.pack()
label_spiral.pack()

root.mainloop()