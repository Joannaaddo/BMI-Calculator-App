import tkinter
from tkinter import ttk
from tkinter import messagebox
from matplotlib import pyplot as plt
import csv
def BMI_Cal():
    try:
        weight= float(weight_info_txt.get())
        height= float(height_info_txt.get())
        bmi= weight/(height**2)
    except ValueError:
          return(0,0)
    if bmi<18.5:
       return(bmi,'Underweight')
    elif bmi>=18.5 and bmi<25:
       return(bmi,'Normal')
    elif bmi>=25 and bmi<30:
       return(bmi,'Overweight')
    else:
       return (bmi,'Obesity')

def on_enter():
    result= BMI_Cal()
    print('Your BMI is',result)
    bmilbl.config(text=result)

    if True:
        with open('BMI_Data.csv','a') as filewriter:
            filewritercsv=csv.writer(filewriter)
            filewritercsv.writerow([first_name_txt,last_name_txt, result])


window=tkinter.Tk()
window.geometry("500x500")
window.title('BMI Calculator')

frame=tkinter.Frame(window)
frame.pack()

user_info_frame=tkinter.LabelFrame(frame,text='Personal Information')
user_info_frame.grid(row=0,column=0,sticky='news')

first_name_label= tkinter.Label(user_info_frame,text='First Name: ')
first_name_label.grid(row=0,column=0,padx=10,pady=10)
first_name_txt=tkinter.Entry(user_info_frame)
first_name_txt.grid(row=0,column=1,padx=10,pady=10)

last_name_label= tkinter.Label(user_info_frame,text='Last Name')
last_name_label.grid(row=0,column=2,padx=10,pady=10)
last_name_txt=tkinter.Entry(user_info_frame)
last_name_txt.grid(row=0,column=3,padx=10,pady=10)

user_age_label=tkinter.Label(user_info_frame,text="Age: ")
user_age_label.grid(row=1,column=0,padx=10,pady=10)
user_age_box=tkinter.Spinbox(user_info_frame,from_=0, to="infinity")
user_age_box.grid(row=1,column=1)

#Create another frame below for BMI INFO.
bmi_info_frame=tkinter.LabelFrame(frame,text='BMI Information')
bmi_info_frame.grid(row=1,column=0,sticky='news')

weight_info_label=tkinter.Label(bmi_info_frame,text='Weight: ')
weight_info_label.grid(row=0,column=0,padx=10,pady=10)
weight_info_txt=tkinter.Entry(bmi_info_frame)
weight_info_txt.grid(row=0,column=1,padx=10,pady=10)

height_info_label=tkinter.Label(bmi_info_frame,text='Height: ')
height_info_label.grid(row=0,column=2,padx=10,pady=10)
height_info_txt=tkinter.Entry(bmi_info_frame)
height_info_txt.grid(row=0,column=3,padx=10,pady=10)

enter_button=tkinter.Button(frame,text='ENTER', command=on_enter)
enter_button.grid(row=2,column=0,sticky= tkinter.W+tkinter.E)

bmilbl=tkinter.Label(frame,text='')
bmilbl.grid(row=3,column=0,padx=10,pady=10)




window.mainloop()




