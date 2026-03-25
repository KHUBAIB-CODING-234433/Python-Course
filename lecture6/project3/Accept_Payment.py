import qrcode
id_my = input("Enter the id =")
phone_url =f'upi://pay?pa={id_my}&pn=Recipient%20Name&mc=1234'
paytm_url =f'upi://pay?pa={id_my}&pn=Recipient%20Name&mc=1234'
google_url =f'upi://pay?pa={id_my}&pn=Recipient%20Name&mc=1234'
easypasa_url =f'upi://pay?pa={id_my}&pn=Recipient%20Name&mc=1234'
jazzcash_url =f'upi://pay?pa={id_my}&pn=Recipient%20Name&mc=1234'

phone_qr=qrcode.make(phone_url)
paytm_qr=qrcode.make(paytm_url)
google_qr=qrcode.make(google_url)
easypasa_qr=qrcode.make(easypasa_url)
jazzcash_qr=qrcode.make(jazzcash_url)

phone_qr.save('phone_qr.png')
paytm_qr.save('paytm_qr.png')
google_qr.save('google_qr.png')
easypasa_qr.save('easypasa_qr.png')
jazzcash_qr.save('jazzcash_qr.png')

phone_qr.show()
paytm_qr.show()
google_qr.show()
easypasa_qr.show()
jazzcash_qr.show()



