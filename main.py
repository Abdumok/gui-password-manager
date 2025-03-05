from tkinter import *

# setup main screen
window= Tk()
window.title("Password Manager")
window.minsize(width=600, height=400)
window.config(padx=20, pady=20)

#=========================================== Labels ===================================================================
website_text = Label(text="Website: ", font=("Times New Roman", 10, "bold"))
website_text.place(x= 95, y= 200)
email_text= Label(text= "Email/Username: ", font=("Times New Roman", 10, "bold"))
email_text.place(x= 50, y= 230)
password_text= Label(text= "Password: ", font=("Times New Roman", 10, "bold"))
password_text.place(x= 87, y= 260)

#========================================== Entry ====================================================================
website_input= Entry(width=30)
website_input.place(x= 160, y= 200)
email_input= Entry(width=50)
email_input.place(x= 160, y= 230)
password_input= Entry(width=27)
password_input.place(x= 160, y=260)

window.mainloop()