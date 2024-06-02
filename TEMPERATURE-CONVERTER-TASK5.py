import tkinter as tk
bg_color='light blue'
radio_fg_color='#068da9'
result_color='#0a4d68'
root=tk.Tk()
root.title('Temperature Converter')
root.geometry("500x500")
root.resizable(0,0)
root.config(bg=bg_color)
def convert():
    temperature=float(entry.get())
    if var.get()==1:
       converted_temp=(temperature *9/5)+32
       result_label.config(text=f"{converted_temp:.2f} °F ")
    elif var.get()==2:
        converted_temp=(temperature - 32)* 5/9
        result_label.config(text=f"{converted_temp:.2f} °C")
main_label=tk.Label(root,text='Temperature Converter',font=('Arial',20,'bold'),bg=bg_color,fg='#2a2f4f')
main_label.pack(pady=30)                                                            
entry_label=tk.Label(root,text='Enter temperature',font=('Arial',17,'bold'),bg=bg_color)                                                           
entry_label.pack()
entry=tk.Entry(root,font=('Arial',15))
entry.pack(pady=15)
var=tk.IntVar()
frame=tk.Frame(root,bg=bg_color)
frame.pack(pady=15)
c_to_f=tk.Radiobutton(frame,text=' Celsius to Farenheit',variable=var,value=1,font=('Arial',12),
             bg=bg_color,activebackground=bg_color,activeforeground=radio_fg_color)
c_to_f.grid(row=0,column=0)
f_to_c=tk.Radiobutton(frame,text=' Farenheit to  Celsius',variable=var,value=2,font=('Arial',12),
             bg=bg_color,activebackground=bg_color,activeforeground=radio_fg_color)
f_to_c.grid(row=0,column=1)
convert_button=tk.Button(root,text='Convert',font=('Arial',15),bg=bg_color,command=convert)
convert_button.pack()
result_label=tk.Label(root,text="",font=('Arial',17,'bold'),bg=bg_color,fg=result_color)
result_label.pack(pady=15)
root.mainloop()                      
