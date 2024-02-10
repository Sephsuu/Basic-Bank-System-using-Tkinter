import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from Bank import accounts, savings_accounts
from PIL import Image, ImageTk

blue1 = "#6b8fb5"
blue2 = "#11295D"
lightBlue = "#71929F"
white = "#fdfdfd"
navyBlue = "#03254c"
lightgray = "#f5f5ed"
def exit(bank):
    bank.destroy()
    main_window()

def back(window, account):
    window.destroy()
    if window == check or window == save:
        bank_window(account)

def main_window():
    root = tk.Tk()
    root.title("Main Window")
    window_size = (500, 500)
    root.geometry(f"{window_size[0]}x{window_size[1]}")
    image_path = "images/01.png"
    original_image = Image.open(image_path)
    resized_image = original_image.resize(window_size, 3)
    photo = ImageTk.PhotoImage(resized_image)
    image_label = tk.Label(root, image=photo)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)

    b = tkFont.Font(family='Verdana', size=14)
    p = tkFont.Font(family='Verdana', size=18)

    def enter(e):
        pin_in.delete(0, "end")

    def leave(e):
        if pin_in.get() == "":
            pin_in.insert(0, "Enter your PIN number")

    def isValid():
        global entered_pin
        entered_pin = pin_in.get()
        if entered_pin in accounts:
            selected_account = accounts[entered_pin]
            root.destroy()
            bank_window(selected_account)
        else:
            messagebox.showerror("Invalid PIN", "Entered PIN is not in the accounts. Please try again.")

    pin_in = tk.Entry(root, width=25, fg="#383838", border=0, bg="white", font=p, justify="center", relief=tk.FLAT,highlightbackground="black", highlightcolor="black", highlightthickness=2, bd=0)
    pin_in.pack(pady=(210, 0), anchor="n")
    pin_in.configure(bg="white")
    tk.Frame(root, width=280, height=2, bg="black").place(x=545, y=200)
    pin_in.insert(0, "Enter your PIN number")
    pin_in.bind("<FocusIn>", enter)
    pin_in.bind("<FocusOut>", leave)

    button = tk.Button(root, text="Enter", bg="white", fg="#71929F", font=b, width=15, command=isValid)
    button.pack(pady=(30, 0), anchor="n")

    root.resizable(False, False)
    root.mainloop()

def bank_window(account):
    bank = tk.Tk()
    bank.title("Bank Window")
    bank.geometry("500x500")
    window_size = (500, 500)
    bank.geometry(f"{window_size[0]}x{window_size[1]}")
    image_path = "images/02.png"
    original_image = Image.open(image_path)
    resized_image = original_image.resize(window_size, 3)
    photo = ImageTk.PhotoImage(resized_image)
    image_label = tk.Label(bank, image=photo)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)

    h1 = tkFont.Font(family="Verdana", weight="bold", size=32)
    b = tkFont.Font(family='Verdana', size=14)
    p = tkFont.Font(family='Verdana', size=20)

    header2 = tk.Label(bank, text=f"{account.account_name}", fg=lightBlue, bg=white, font=h1, anchor="e", padx=20)
    header2.pack(pady=(85, 0), anchor="n")

    checking_button = tk.Button(bank, text="Checking", width=20, bg=white, fg=lightBlue, font=p, command=lambda: checking(bank, account))
    checking_button.pack(pady=(40, 0), anchor="n")

    savings_button = tk.Button(bank, text="Savings", width=20, bg=white, fg=lightBlue, font=p, command=lambda: saving(bank, account))
    savings_button.pack(pady=(20, 0), anchor="n")

    exit_button = tk.Button(bank, text="Exit", width=20, bg=white, fg=lightBlue, font=p, command=lambda: exit(bank))
    exit_button.pack(pady=(20, 0), anchor="n")

    header3 = tk.Label(bank, text=f"Account No. {account.account_number}", font=b, bg="#d1e3ee")
    header3.pack(pady=(20, 0), anchor="n")

    bank.resizable(False, False)
    bank.mainloop()

def checking(bank, account):
    global check
    bank.destroy()
    check = tk.Tk()
    check.title("Checking Window")
    window_size = (500, 500)
    check.geometry(f"{window_size[0]}x{window_size[1]}")
    image_path = "images/03.png"
    original_image = Image.open(image_path)
    resized_image = original_image.resize(window_size, 3)
    photo = ImageTk.PhotoImage(resized_image)
    image_label = tk.Label(check, image=photo)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)

    b = tkFont.Font(family='Verdana', size=18)

    deposit_button = tk.Button(check, text="Deposit", width=20, fg=lightBlue, bg=white, font=b, command=lambda: deposit_checking(check, account))
    deposit_button.pack(pady=(170, 0), anchor="n")

    withdraw_button = tk.Button(check, text="Withdraw", width=20, font=b, fg=lightBlue, bg=white, command=lambda: withdraw_checking(check, account))
    withdraw_button.pack(pady=(20, 0), anchor="n")

    back_button = tk.Button(check, text="Back", width=20, font=b, fg=lightBlue, bg=white, command=lambda: back(check, account))
    back_button.pack(pady=(20, 0), anchor="n")

    check.resizable(False, False)
    check.mainloop()

def saving(bank, account):
    global save
    bank.destroy()
    save = tk.Tk()
    save.title("Savings Window")
    window_size = (500, 500)
    save.geometry(f"{window_size[0]}x{window_size[1]}")
    image_path = "images/04.png"
    original_image = Image.open(image_path)
    resized_image = original_image.resize(window_size, 3)
    photo = ImageTk.PhotoImage(resized_image)
    image_label = tk.Label(save, image=photo)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)

    b = tkFont.Font(family='Verdana', size=18)

    deposit_button = tk.Button(save, text="Deposit", width=20, fg=lightBlue, font=b, bg=white, command=lambda: deposit_savings(save, account))
    deposit_button.pack(pady=(170, 0), anchor="n")

    withdraw_button = tk.Button(save, text="Withdraw", width=20, fg=lightBlue, font=b, bg=white, command=lambda: withdraw_savings(save, account))
    withdraw_button.pack(pady=(20, 0), anchor="n")

    back_button = tk.Button(save, text="Back", width=20, fg=lightBlue, font=b, bg=white, command=lambda: back(save, account))
    back_button.pack(pady=(20, 0), anchor="n")

    save.resizable(False, False)
    save.mainloop()

def deposit_checking(check, account):
    deposit = tk.Toplevel(check)
    deposit.title("Deposit Checking")
    window_size = (500, 500)
    deposit.geometry(f"{window_size[0]}x{window_size[1]}")
    image_path = "images/05.png"
    original_image = Image.open(image_path)
    resized_image = original_image.resize(window_size, 3)
    photo = ImageTk.PhotoImage(resized_image)
    image_label = tk.Label(deposit, image=photo)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)

    h1 = tkFont.Font(family="Verdana", weight="bold", size=24)
    p = tkFont.Font(family='Verdana', size=18)
    b = tkFont.Font(family='Verdana', size=14)

    def on_button_click(value):
        if value == "C":
            entry.delete(0, "end")  # Clear the content of the entry field
        else:
            current_text = entry.get()
            entry.delete(0, "end")
            entry.insert("end", current_text + value)

    def deposit_action():
        try:
            deposited_amount = float(entry.get())
            if deposited_amount > 0:
                account.balance += deposited_amount
                messagebox.showinfo("Deposit Successful",f"You have deposited an amount of ₱{deposited_amount}. Your balance is now: ₱{account.get_balance()}")
                deposit.destroy()
            else:
                header2.config(text="Please Enter a Valid Amount")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please Enter a Valid Amount")

    header2 = tk.Label(deposit, text=f"Balance: ₱{account.get_balance()}", bg=white, fg=navyBlue, font=p)
    header2.pack(pady=(50, 0), anchor="n")

    entry = tk.Entry(deposit, width=25, fg="#383838", border=0, bg="white", font=p, justify="center", relief=tk.FLAT, highlightbackground="black", highlightcolor="black", highlightthickness=2, bd=0)
    entry.pack(pady=(20, 0), anchor="n")
    entry.configure(bg=white)

    num1 = tk.Button(deposit, text="1", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("1"), width=5)
    num1.place(x=130, y=150)
    num2 = tk.Button(deposit, text="2", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("2"), width=5)
    num2.pack(pady=(10, 0), anchor="n")
    num3 = tk.Button(deposit, text="3", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("3"), width=5)
    num3.place(x=300, y=150)

    num4 = tk.Button(deposit, text="4", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("4"), width=5)
    num4.place(x=130, y=200)
    num5 = tk.Button(deposit, text="5", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("5"), width=5)
    num5.pack(pady=(10, 0), anchor="n")
    num6 = tk.Button(deposit, text="6", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("6"), width=5)
    num6.place(x=300, y=200)

    num7 = tk.Button(deposit, text="7", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("7"), width=5)
    num7.place(x=130, y=250)
    num8 = tk.Button(deposit, text="8", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("8"), width=5)
    num8.pack(pady=(10, 0), anchor="n")
    num9 = tk.Button(deposit, text="9", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("9"), width=5)
    num9.place(x=300, y=250)

    point = tk.Button(deposit, text=".", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("."), width=5)
    point.place(x=130, y=300)
    num0 = tk.Button(deposit, text="0", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("0"), width=5)
    num0.pack(pady=(10, 0), anchor="n")
    clear = tk.Button(deposit, text="C", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("C"), width=5)
    clear.place(x=300, y=300)

    deposit_button = tk.Button(deposit, text="Deposit", width=15, font=b, fg=lightBlue, bg=lightgray, command=deposit_action)
    deposit_button.pack(pady=(15, 0), anchor="n")

    back_button = tk.Button(deposit, text="Back", width=15, font=b, fg=lightBlue, bg=lightgray, command=lambda: back(deposit, account))
    back_button.pack(pady=(10, 0), anchor="n")

    def on_close():
        deposit.destroy()
        check.destroy()

    deposit.protocol("WM_DELETE_WINDOW", on_close)

    deposit.resizable(False, False)
    deposit.mainloop()

def withdraw_checking(check, account):
    withdraw = tk.Toplevel(check)
    withdraw.title("Withdrawal Checking")
    window_size = (500, 500)
    withdraw.geometry(f"{window_size[0]}x{window_size[1]}")
    image_path = "images/06.png"
    original_image = Image.open(image_path)
    resized_image = original_image.resize(window_size, 3)
    photo = ImageTk.PhotoImage(resized_image)
    image_label = tk.Label(withdraw, image=photo)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)

    p = tkFont.Font(family='Verdana', size=18)
    b = tkFont.Font(family='Verdana', size=14)

    def on_button_click(value):
        if value == "C":
            entry.delete(0, "end")  # Clear the content of the entry field
        else:
            current_text = entry.get()
            entry.delete(0, "end")
            entry.insert("end", current_text + value)

    def withdraw_action():
        try:
            withdrawal_amount = float(entry.get())
            if withdrawal_amount <= 0:
                header2.config(text="Please Enter Positive Amount")
            elif withdrawal_amount <= account.balance:
                account.balance -= withdrawal_amount
                messagebox.showinfo("Withdrawal Successful", f"You have withdrawn an amount of ₱{withdrawal_amount}. Your balance is now: ₱{account.get_balance()}")
                withdraw.destroy()
            else:
                header2.config(text="Insufficient Funds")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please Enter a Valid Amount")

    header2 = tk.Label(withdraw, text=f"Balance: ₱{account.get_balance()}", bg=white, fg=navyBlue, font=p)
    header2.pack(pady=(50, 0), anchor="n")

    entry = tk.Entry(withdraw, width=25, fg="#383838", border=0, bg="white", font=p, justify="center", relief=tk.FLAT,
                     highlightbackground="black", highlightcolor="black", highlightthickness=2, bd=0)
    entry.pack(pady=(20, 0), anchor="n")
    entry.configure(bg=white)

    num1 = tk.Button(withdraw, text="1", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("1"), width=5)
    num1.place(x=130, y=150)
    num2 = tk.Button(withdraw, text="2", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("2"), width=5)
    num2.pack(pady=(10, 0), anchor="n")
    num3 = tk.Button(withdraw, text="3", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("3"), width=5)
    num3.place(x=300, y=150)

    num4 = tk.Button(withdraw, text="4", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("4"), width=5)
    num4.place(x=130, y=200)
    num5 = tk.Button(withdraw, text="5", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("5"), width=5)
    num5.pack(pady=(10, 0), anchor="n")
    num6 = tk.Button(withdraw, text="6", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("6"), width=5)
    num6.place(x=300, y=200)

    num7 = tk.Button(withdraw, text="7", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("7"), width=5)
    num7.place(x=130, y=250)
    num8 = tk.Button(withdraw, text="8", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("8"), width=5)
    num8.pack(pady=(10, 0), anchor="n")
    num9 = tk.Button(withdraw, text="9", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("9"), width=5)
    num9.place(x=300, y=250)

    point = tk.Button(withdraw, text=".", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("."), width=5)
    point.place(x=130, y=300)
    num0 = tk.Button(withdraw, text="0", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("0"), width=5)
    num0.pack(pady=(10, 0), anchor="n")
    clear = tk.Button(withdraw, text="C", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("C"), width=5)
    clear.place(x=300, y=300)

    withdraw_button = tk.Button(withdraw, text="Withdraw", width=15, font=b, fg=navyBlue, bg=lightgray,
                                command=withdraw_action)
    withdraw_button.pack(pady=(15, 0), anchor="n")

    back_button = tk.Button(withdraw, text="Back", width=15, font=b, fg=navyBlue, bg=lightgray,
                            command=lambda: back(withdraw, account))
    back_button.pack(pady=(10, 0), anchor="n")

    def on_close():
        withdraw.destroy()
        check.destroy()

    withdraw.protocol("WM_DELETE_WINDOW", on_close)

    withdraw.resizable(False, False)
    withdraw.mainloop()

def deposit_savings(check, account):
    deposit = tk.Toplevel(check)
    deposit.title("Deposit Savings")
    window_size = (500, 500)
    deposit.geometry(f"{window_size[0]}x{window_size[1]}")
    image_path = "images/07.png"
    original_image = Image.open(image_path)
    resized_image = original_image.resize(window_size, 3)
    photo = ImageTk.PhotoImage(resized_image)
    image_label = tk.Label(deposit, image=photo)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)

    sAccount = savings_accounts[entered_pin]

    p = tkFont.Font(family='Verdana', size=18)
    b = tkFont.Font(family='Verdana', size=14)

    def on_button_click(value):
        if value == "C":
            entry.delete(0, "end")  # Clear the content of the entry field
        else:
            current_text = entry.get()
            entry.delete(0, "end")
            entry.insert("end", current_text + value)

    def deposit_action():
        try:
            deposited_amount = float(entry.get())
            if deposited_amount > 0 and deposited_amount <= 1000:
                sAccount.balance += deposited_amount
                messagebox.showinfo("Deposit Successful",f"You have deposited an amount of ₱{deposited_amount}. Your balance is now: ₱{sAccount.get_balance()}")
                deposit.destroy()
            elif deposited_amount > 1000:
                header2.config(text="Deposit is limited to ₱1000.00")
            else:
                header2.config(text="Please Enter a Valid Amount")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please Enter a Valid Amount")

    header2 = tk.Label(deposit, text=f"Balance: ₱{sAccount.get_balance()}", bg=white, fg=navyBlue, font=p)
    header2.pack(pady=(50, 0), anchor="n")

    entry = tk.Entry(deposit, width=25, fg="#383838", border=0, bg="white", font=p, justify="center", relief=tk.FLAT,
                     highlightbackground="black", highlightcolor="black", highlightthickness=2, bd=0)
    entry.pack(pady=(20, 0), anchor="n")
    entry.configure(bg=white)

    num1 = tk.Button(deposit, text="1", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("1"), width=5)
    num1.place(x=130, y=150)
    num2 = tk.Button(deposit, text="2", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("2"), width=5)
    num2.pack(pady=(10, 0), anchor="n")
    num3 = tk.Button(deposit, text="3", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("3"), width=5)
    num3.place(x=300, y=150)

    num4 = tk.Button(deposit, text="4", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("4"), width=5)
    num4.place(x=130, y=200)
    num5 = tk.Button(deposit, text="5", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("5"), width=5)
    num5.pack(pady=(10, 0), anchor="n")
    num6 = tk.Button(deposit, text="6", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("6"), width=5)
    num6.place(x=300, y=200)

    num7 = tk.Button(deposit, text="7", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("7"), width=5)
    num7.place(x=130, y=250)
    num8 = tk.Button(deposit, text="8", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("8"), width=5)
    num8.pack(pady=(10, 0), anchor="n")
    num9 = tk.Button(deposit, text="9", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("9"), width=5)
    num9.place(x=300, y=250)

    point = tk.Button(deposit, text=".", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("."), width=5)
    point.place(x=130, y=300)
    num0 = tk.Button(deposit, text="0", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("0"), width=5)
    num0.pack(pady=(10, 0), anchor="n")
    clear = tk.Button(deposit, text="C", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("C"), width=5)
    clear.place(x=300, y=300)

    deposit_button = tk.Button(deposit, text="Deposit", width=15, font=b, fg=lightBlue, bg=lightgray,
                               command=deposit_action)
    deposit_button.pack(pady=(15, 0), anchor="n")

    back_button = tk.Button(deposit, text="Back", width=15, font=b, fg=lightBlue, bg=lightgray,
                            command=lambda: back(deposit, account))
    back_button.pack(pady=(10, 0), anchor="n")

    def on_close():
        deposit.destroy()
        check.destroy()

    deposit.protocol("WM_DELETE_WINDOW", on_close)

    deposit.resizable(False, False)
    deposit.mainloop()

def withdraw_savings(check, account):
    withdraw = tk.Toplevel(check)
    withdraw.title("Withdrawal Savings")
    window_size = (500, 500)
    withdraw.geometry(f"{window_size[0]}x{window_size[1]}")
    image_path = "images/08.png"
    original_image = Image.open(image_path)
    resized_image = original_image.resize(window_size, 3)
    photo = ImageTk.PhotoImage(resized_image)
    image_label = tk.Label(withdraw, image=photo)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)

    sAccount = savings_accounts[entered_pin]

    p = tkFont.Font(family='Verdana', size=18)
    b = tkFont.Font(family='Verdana', size=14)

    def on_button_click(value):
        if value == "C":
            entry.delete(0, "end")  # Clear the content of the entry field
        else:
            current_text = entry.get()
            entry.delete(0, "end")
            entry.insert("end", current_text + value)

    def withdraw_action():
        try:
            withdrawal_amount = float(entry.get())
            if withdrawal_amount <= 0 and withdrawal_amount <= 50000:
                header2.config(text="Please Enter Positive Amount")
            elif withdrawal_amount > 50000:
                header2.config(text="Withdrawal is limited to ₱50,000")
            elif withdrawal_amount <= sAccount.balance:
                sAccount.balance -= withdrawal_amount
                messagebox.showinfo("Withdrawal Successful", f"You have withdrawn an amount of ₱{withdrawal_amount}. Your balance is now: ₱{sAccount.get_balance()}")
                withdraw.destroy()
            else:
                header2.config(text="Insufficient Funds")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please Enter a Valid Amount")

    header2 = tk.Label(withdraw, text=f"Balance: ₱{sAccount.get_balance()}", bg=white, fg=navyBlue, font=p)
    header2.pack(pady=(50, 0), anchor="n")

    entry = tk.Entry(withdraw, width=25, fg="#383838", border=0, bg="white", font=p, justify="center", relief=tk.FLAT,
                     highlightbackground="black", highlightcolor="black", highlightthickness=2, bd=0)
    entry.pack(pady=(20, 0), anchor="n")
    entry.configure(bg=white)

    num1 = tk.Button(withdraw, text="1", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("1"), width=5)
    num1.place(x=130, y=150)
    num2 = tk.Button(withdraw, text="2", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("2"), width=5)
    num2.pack(pady=(10, 0), anchor="n")
    num3 = tk.Button(withdraw, text="3", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("3"), width=5)
    num3.place(x=300, y=150)

    num4 = tk.Button(withdraw, text="4", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("4"), width=5)
    num4.place(x=130, y=200)
    num5 = tk.Button(withdraw, text="5", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("5"), width=5)
    num5.pack(pady=(10, 0), anchor="n")
    num6 = tk.Button(withdraw, text="6", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("6"), width=5)
    num6.place(x=300, y=200)

    num7 = tk.Button(withdraw, text="7", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("7"), width=5)
    num7.place(x=130, y=250)
    num8 = tk.Button(withdraw, text="8", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("8"), width=5)
    num8.pack(pady=(10, 0), anchor="n")
    num9 = tk.Button(withdraw, text="9", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("9"), width=5)
    num9.place(x=300, y=250)

    point = tk.Button(withdraw, text=".", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("."), width=5)
    point.place(x=130, y=300)
    num0 = tk.Button(withdraw, text="0", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("0"), width=5)
    num0.pack(pady=(10, 0), anchor="n")
    clear = tk.Button(withdraw, text="C", font=b, bg=white, fg=lightBlue, command=lambda: on_button_click("C"), width=5)
    clear.place(x=300, y=300)

    withdraw_button = tk.Button(withdraw, text="Withdraw", width=15, font=b, fg=navyBlue, bg=lightgray,
                                command=withdraw_action)
    withdraw_button.pack(pady=(15, 0), anchor="n")

    back_button = tk.Button(withdraw, text="Back", width=15, font=b, fg=navyBlue, bg=lightgray,
                            command=lambda: back(withdraw, account))
    back_button.pack(pady=(10, 0), anchor="n")

    def on_close():
        withdraw.destroy()
        check.destroy()

    withdraw.protocol("WM_DELETE_WINDOW", on_close)

    withdraw.resizable(False, False)
    withdraw.mainloop()

main_window()