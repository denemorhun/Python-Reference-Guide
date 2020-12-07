# strings and bytes are not directly interchangeable
# strings contain unicode, bytes are raw 8-bit values

def main():
    # define some starting values
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)
    
    s = "This is a string"
    print(s)
    
    # TODO: Try combining them. 
   # print(b + s)
    
    # TODO: Bytes and strings need to be properly encoded and decoded
    # before you can work on them together
    
    # TODO: encode the string as UTF-32
    enc = bytes(s, 'utf-32')
    print(enc + b)

    my_str = str(b, 'utf-8')

    #using encode method

    my_str_enc = s.encode('utf-32')
    my_byte_env = b.decode('utf-8')

    print(my_str + s)
    print(my_str_enc)
    print(my_byte_env)


    
if __name__ == "__main__":
    main()
