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

#========================================== Button ===================================================================
gen_password_button= Button(width=18, text= "Generate Password")
gen_password_button.place(x=329, y= 258)
add_button= Button(width= 43, text= "Add")
add_button.place(x= 156, y=289)
search_button= Button(width=15, text="Search")
search_button.place(x= 350, y= 197)

window.mainloop()