def encode(text,num):
    Output = []
    count = 0
    for i in range(0,len(text)):
        if count<len(num):
            ch = chr(ord(text[i])+int(num[count]))
            if text[i]>='a' and text[i]<='z':
                if ch>'z':
                    ch = chr(ord(ch)-26)
            elif text[i]>='A' and text[i]<='Z':
                if ch>'Z':
                    ch = chr(ord(ch)-26)
            Output.append(ch)
            count+=1
        else:
            count = 0
            ch = chr(ord(text[i])+int(num[count]))
            if text[i]>='a' and text[i]<='z':
                if ch>'z':
                    ch = chr(ord(ch)-26)
            elif text[i]>='A' and text[i]<='Z':
                if ch>'Z':
                    ch = chr(ord(ch)-26)
            Output.append(ch)
            count+=1
    return Output

def decode(text,num):
    Output = []
    count = 0
    for i in range(0,len(text)):
        if count<len(num):
            ch = chr(ord(text[i])-int(num[count]))
            if text[i]>='a' and text[i]<='z':
                if ch<'a':
                    ch = chr(ord(ch)+26)
            elif text[i]>='A' and text[i]<='Z':
                if ch<'A':
                    ch = chr(ord(ch)+26)
            Output.append(ch)
            count+=1
        else:
            count = 0
            ch = chr(ord(text[i])-int(num[count]))
            if text[i]>='a' and text[i]<='z':
                if ch<'a':
                    ch = chr(ord(ch)+26)
            elif text[i]>='A' and text[i]<='Z':
                if ch<'A':
                    ch = chr(ord(ch)+26)
            Output.append(ch)
            count+=1
    return Output

text,num = input("Enter String and Code : ").split(",")
txt=list(text.replace(' ',''))

print("Encode message is :  ",end="")
print(encode(txt,num))
print("Decode message is :  ",end="")
print(decode(encode(txt,num),num))