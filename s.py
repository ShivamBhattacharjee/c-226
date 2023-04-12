print("Welcome to the cr cryptography")

def main():
    print()
    print("choose the one option below")
    choice=int(input("1.Encryption\n2.Decryption:"))

    if choice==1:
        encryption()

    elif choice==2:
        decryption()

    else:
        print("Wrong choice")

def encryption():
    print("encryption")
    msg=input("Enter your encrpyted message: ")
    key=int(input("enter the key(1-94): "))
    encryption_text=" "

    for i in range(len(msg)):
        #  print(i)
         temp=(ord(msg[i])+key)
    
         if temp>126:
             temp=temp-127+32

         encryption_text+=chr(temp)
    print(encryption_text)
        #  print(temp)

def decryption():
    print("decryption")
    msg=input("enter your message to decrypt:")
    key=int(input("enter the key(1-94):"))
    decryption_text=" "

    for i in range(len(msg)):
        # print(i)
        temp=(ord(msg[i])-key)

        if temp<32:
            temp=temp+127-32

        decryption_text+=chr(temp)
    print(decryption_text)

        # print(temp)


main()
