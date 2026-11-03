import qrcode

def generate_youtube_qr(youtube_url, filename="youtube_qr.png"):
    # Tworzenie obiektu QR kodu
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    
    # Dodanie linku do filmu z YouTube
    qr.add_data(youtube_url)
    qr.make(fit=True)

    # Generowanie obrazu
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Zapis do pliku
    img.save(filename)
    print(f"Kod QR został pomyślnie wygenerowany i zapisany jako: {filename}")

if __name__ == "__main__":
    # Podaj link do interesującego Cię filmu
    url = input("Wklej link do filmu na YouTube: ")
    generate_youtube_qr(url)