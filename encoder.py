from tkinter import *
import base64

root = Tk()

root.geometry('500x300')
root.resizable (0, 0)
root.title("Encoder+Decoder - Code by DonGiovanni")

Label (root, text = 'Keep Your Secrets...Secret', font = 'arial 20 bold').pack()
Label (root, text = 'Remember to use the same key!!', font = 'arial 12 italic').pack()
Label (root, text = "DonGiovanni - Encoder", font = 'arial 20 bold').pack(side = BOTTOM)

Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()

def Encode(key, message):
    enc = []
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc) .encode()) .decode()

def Decode(key, message):
    dec = []
    message = base64.urlsafe_b64decode(message) .decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
    return "".join(dec)

def Mode():
    if(mode.get() == '1'):
        Result.set(Encode (private_key.get(), Text.get()))
    elif(mode.get() == '2'):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')

def Exit():
    root.destroy()

def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")

Label(root, font = 'arial 12 bold', text='Text to encrypt/decrypt : ') .place(x = 60, y = 80)
Entry(root, font = 'arial 10', textvariable = Text, bg = 'ghost white') .place(x = 290, y = 80)

Label(root, font = 'arial 12 bold', text='Private Key : ') .place(x = 60, y = 120)
Entry(root, font = 'arial 10', textvariable = private_key, bg = 'ghost white') .place(x = 290, y = 120)

Label(root, font = 'arial 12 bold', text='Mode (1-Encode, 2-Decode) : ') .place(x = 60, y = 160)
Entry(root, font = 'arial 10', textvariable = mode, bg = 'ghost white') .place(x = 290, y = 160)
Entry(root, font = 'arial 10', textvariable = Result, bg = 'ghost white') .place(x = 290, y = 200)

Button(root, font = 'arial 10 bold', text = 'RESULT', padx = 2, bg = 'LightGray', command = Mode) .place(x = 60, y = 200)

Button(root, font = 'arial 10 bold', text = 'RESET', width = 6, command = Reset, bg = 'LimeGreen', padx = 2, pady=2) .place(x = 290, y = 230)

Button(root, font = 'arial 10 bold', text = 'EXIT' , width = 6, command = Exit, bg = 'OrangeRed', padx=2, pady=2).place(x=370, y = 230)


root.mainloop()
