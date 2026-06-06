print("\n🔐 Welcome to secrete messege code encoder/decoder")

def encoder (Message,key):
    encrypted = " "
    for Char in Message:
        encrypted +=chr((ord(Char)+ key) % 256)
    return encrypted

def decoder (Message,key):
    decrypted = " "
    for Char in Message:
        decrypted +=chr((ord(Char)- key) % 256)
    return decrypted

while True:
    print(" what do you want to do ?")
    print("1. encode the message ")
    print("2. decode the message")
    print("3. exit")

    ch=input("enter your choice (1/2/3):")

    if ch=="1":
        Message=input("enter the message:")
        key=int(input("enetr the secret key (1-100):"))
        encoded= encoder(Message,key)
        print(f"\n your encoded message is:{encoded}")
    
    elif ch=="2":
        Message=input("enter the encoded message: ")
        key=int(input("enete the secret key (1-100):"))
        decoded= decoder(Message,key)
        print(f"\n🧩 your encoded message is:{decoded}")

    elif ch=="3":
        print("\n👋 goodbye,serect message agent")
        break
    else:
        print("\n❌ invalid choice")



