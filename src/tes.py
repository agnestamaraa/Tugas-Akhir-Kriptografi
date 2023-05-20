# Menghitung nilai hash dari pesan M
from hashlib import sha3_256


# def Hash(message):
#     hash = sha3_256(message.encode("latin-1")).hexdigest()
#     hashed = int(hash, 16)
#     return hashed

# def enkrip(message, e, n):
#     if(message=="abel" or message=="Abel"):
#         m1 = '0001'
#         m1 = m1.lstrip('0')
#         m2 = '0411'
#         m2 = m2.lstrip('0')

#         encrypted_m1 = str((int(m1) ** e) % n).zfill(5)
#         encrypted_m2 = str((int(m2) ** e) % n).zfill(5)
#         combined_result = encrypted_m1 + encrypted_m2
#     elif(message=="daniel" or message=="Daniel"):
#         m1 = '0300'
#         m1 = m1.lstrip('0')
#         m2 = '1308'
#         m2 = m2.lstrip('0')
#         m3 = '0411'
#         m3 = m3.lstrip('0')

#         encrypted_m1 = str((int(m2) ** e) % n).zfill(5)
#         encrypted_m2 = str((int(m2) ** e) % n).zfill(5)
#         encrypted_m3 = str((int(m3) ** e) % n).zfill(5)
#         combined_result = encrypted_m1 + encrypted_m2 + encrypted_m3
#     return combined_result
#     # input.insert(Tk.END, f"Message: {message}\n")
#     # input.insert(Tk.END, f"Encrypted Result: {S}\n")
#     # messagebox.showinfo("Encryption Successful",f"Message encrypted successfully.")

# def enkrip(message, e, n):
#     # encryted = (int(message) ** e) % n
#     if(message=="abel" or message=="Abel"):
#         m1 = '0001'
#         m1 = m1.lstrip('0')
#         m2 = '0411'
#         m2 = m2.lstrip('0')

#         encrypted_m1 = (int(m1) ** e) % n
#         encrypted_m2 = (int(m2) ** e) % n
#         combined_result = str(encrypted_m1) + str(encrypted_m2)
#     elif(message=="daniel" or message=="Daniel"):
#         m1 = '0300'
#         m1 = m1.lstrip('0')
#         m2 = '1308'
#         m2 = m2.lstrip('0')
#         m3 = '0411'
#         m3 = m3.lstrip('0')

#         encrypted_m1 = (int(m1) ** e) % n
#         encrypted_m2 = (int(m2) ** e) % n
#         encrypted_m3 = (int(m3) ** e) % n 
#         combined_result = str(encrypted_m1) + str(encrypted_m2) + str(encrypted_m3)
#     return combined_result

def enkrip(message, e, n):
    cipher = [(ord(char) ** e) % n for char in message]
    return cipher


# dekripsi terhadap tanda-tangan S dengan kuncipublik si pengirim (PK) menggunakan persamaan dekripsi RSA:
# def dekrip(message, d, n2):
#     return (int(message) ** d % n2)

# def dekrip(encrypted_message, d, n):
#     decrypted_message = ""

#     # Mendekripsi pesan terenkripsi per lima digit
#     for i in range(0, len(encrypted_message), 5):
#         encrypted_block = encrypted_message[i:i+5]

#         # Mengembalikan angka terenkripsi menjadi angka asli menggunakan kunci dekripsi
#         decrypted_block = str((int(encrypted_block) ** d) % n)
#         decrypted_message += decrypted_block

#     # Mengonversi angka kembali menjadi pesan teks
#     decrypted_message = decrypted_message.zfill(8)  # Mengisi nol di depan jika perlu
#     decrypted_message = decrypted_message[:4]  # Mengambil empat digit pertama
#     decrypted_message = decrypted_message.lstrip('0')  # Menghapus nol di depan jika ada

#     return decrypted_message

def dekrip(encrypted_message, d, n2):
    plain = [chr((char ** d) % n2) for char in encrypted_message]
    # plain = [chr(pow(ord(char), d, n2)) for char in encrypted_message]
    return ''.join(plain)

# def dekrip(self, encrypted_message, d, n2):
#     encrypted_message = self.stringvar_message.get()
#     plain = [chr((char ** d) % n2) for char in encrypted_message]
#     # plain = [chr(pow(char, d, n2)) for char in encrypted_list]
#     decrypted_message = ''.join(plain)
#     self.output.delete('1.0', Tk.END)
#     self.output.insert(Tk.END, decrypted_message)
#     messagebox.showinfo("Decryption Successful", "Message decrypted successfully.")

e_hasil = enkrip("abel", 33857, 42233)
print(e_hasil)
hasil = dekrip(e_hasil, 28673, 42233)
print(hasil)