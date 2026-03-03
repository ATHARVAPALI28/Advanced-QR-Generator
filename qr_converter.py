import customtkinter as ctk
import qrcode
from tkinter import filedialog, colorchooser
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

qr_color="black"
selected_logo=None

def qr_create():
    global selected_logo
    data=entry.get().strip()
    if(not data):
        return

    qr=qrcode.QRCode(version=None,box_size=10,border=2)
    qr.add_data(data)
    qr.make(fit=True)

    img=qr.make_image(fill_color=qr_color,back_color="white").convert("RGB")

    if(selected_logo):
        logo=Image.open(selected_logo)
        logo=logo.resize((60, 60))
        pos=((img.size[0]-60)//2,(img.size[1]-60)//2)
        img.paste(logo,pos)

    img=img.resize((260,260))

    qr_img=ctk.CTkImage(light_image=img,dark_image=img,size=(260,260))
    qr_label.configure(image=qr_img)
    qr_label.image=qr_img

    img.save("gen_qr.png")

def qr_save():
    file_path=filedialog.asksaveasfilename(defaultextension=".png")
    if(file_path):
        Image.open("gen_qr.png").save(file_path)

def pick_qr_color():
    global qr_color
    color=colorchooser.askcolor()[1]
    if(color):
        qr_color=color

def qr_logo():
    global selected_logo
    file_path=filedialog.askopenfilename(filetypes=[("Image Files","*.png;*.jpg;*.jpeg")])
    if(file_path):
        selected_logo=file_path

def copy_text():
    root.clipboard_clear()
    root.clipboard_append(entry.get())

root=ctk.CTk()
root.title("Advanced QR Generator")
root.geometry("600x720")
root.resizable(False,False)

main=ctk.CTkFrame(root,corner_radius=20)
main.pack(padx=30, pady=30, fill="both", expand=True)

title=ctk.CTkLabel(main,text="Advanced QR Generator",font=ctk.CTkFont(size=26,weight="bold"))
title.pack(pady=(25,10))

entry=ctk.CTkEntry(main,height=45,width=400,placeholder_text="Enter text or URL",corner_radius=10,justify="center")
entry.pack(pady=15)

frame=ctk.CTkFrame(main,fg_color="transparent")
frame.pack(pady=10)

generate_btn=ctk.CTkButton(frame,text="Generate",corner_radius=10,width=140,command=qr_create)
generate_btn.grid(row=0,column=0,padx=10,pady=10)
save_btn=ctk.CTkButton(frame,text="Save",corner_radius=10,width=140,command=qr_save)
save_btn.grid(row=0,column=1,padx=10,pady=10)
color=ctk.CTkButton(frame,text="Pick Color",corner_radius=10,width=140,command=pick_qr_color)
color.grid(row=1,column=0,padx=10,pady=10)
logo_btn=ctk.CTkButton(frame,text="Add Logo",corner_radius=10,width=140,command=qr_logo)
logo_btn.grid(row=1,column=1,padx=10,pady=10)

copy_btn = ctk.CTkButton(main,text="Copy Text",width=200,command=copy_text)
copy_btn.pack(pady=10)

qr_label=ctk.CTkLabel(main,text="")
qr_label.pack(pady=25)

footer=ctk.CTkLabel(main,text="© 2026 BluecraneEditZ™. Built with Python.",font=ctk.CTkFont(size=13))
footer.pack(side="bottom",pady=15)

root.mainloop()