from qrcode import QRCode, constants
from PIL import ImageTk
from tkinter import Tk, Label

def display_qr_code(my_qr_code):
    root = Tk()
    photo_img = ImageTk.PhotoImage(my_qr_code)
    panel = Label(root, image=photo_img)
    panel.pack()
    root.mainloop()

def generate_qr_code(url_link):
    qr = QRCode(
        version=1,
        error_correction=constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(url_link)
    qr.make(fit=True)
    return qr.make_image()

if __name__ == '__main__':
    url_link = input('Enter url for QR code: ')

    my_qr_code = generate_qr_code(url_link)
    display_qr_code(my_qr_code)
