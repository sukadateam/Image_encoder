#Classes
#Created by Brandon Robinson

class char_encoder:
    #SHOULD NEVER RETURN 0, will casue problems if so
    def lowercase(par_):
        set='abcdefghijklmnopqrstuvwxyz'
        for i in range(len(set)):
            if set[i] == par_:
                return i+1
    def uppercase(par_):
        set='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(len(set)):
            if set[i] == par_:
                return i+1
    def number(par_):
        set='0123456789'
        for i in range(len(set)):
            if set[i] == par_:
                return i+1














#print(char_encoder.uppercase('z'))