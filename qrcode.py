import qrcode

# Function to generate QR code
def generate_qr_code(url):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,  # version defines the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
        box_size=10,  # size of each box in the QR code
        border=4,  # width of the border
    )
    qr.add_data(url)  # add URL data to the QR code
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill='black', back_color='white')
    return img

# Main function to take URL input and generate QR code
if __name__ == '__main__':
    url = input("Enter the URL you want to generate the QR code for: ")
    img = generate_qr_code(url)
    img.show()  # Display the QR code
    img.save('qr_code.png')  # Optionally, save the QR code as an image
