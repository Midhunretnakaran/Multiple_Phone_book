maindict={}
while True:
    choice=int(input('1.add contact\n2view contact\n3update contact\n4delete contact\n5exit\nselect your choice'))
    
    if choice==1:
        subdict={}
        na=input('enter the name')
        subdict['name']=na

        phonelist=[]
        x=int(input('how many phone numbers want to add'))
        for i in range(x):
            phone=input('enter the number')
            phonelist.append(x)
        subdict['phone']=phonelist

        emaillist=[]
        y=int(input('how many emails want to be add '))
        for i in range(y):
            em=input('enter the email')
            emaillist.append(em)
        subdict['email']=emaillist
        maindict[na]=subdict 

    elif choice==2:
        v=int(input('1.view all contact\n2view single contact\nselect your choice'))
        if v==1:
            print(maindict)
        elif v==2:
            w=input('enter the name to view')
            if w in maindict:
                print(maindict[w])
            else:
                print('invalid contact')
        else:
            print('invalid choice')

    elif choice==3:
        up=int(input('1.update name\n2update phone number\n3update email\nselect your choice'))
        if up==1:
            n=input('enter the name to update')
            if n in maindict:
                print(maindict[n])
                new=input('enter the new name')
                maindict[n]['name']=new
                o=maindict.pop(n)
                maindict[new]=o
                print(maindict[new])
            else:
                print('not in contact')
        elif up==2:
            m=input('enter the name of number to change') 
            if m in maindict:
                print(maindict[m]['phone number'])
                k=int(input('enter which position you want to update'))
                k-=1
                maindict[m]['phone number'].pop(k)
                print(maindict[m]['phone'])  
                newnum=int(input("enter the number:"))
                maindict[m]['phone'].insert(k,newnum) 
                print(maindict[m]['phone'])
            else:
                print('invalid')
            
        elif up==3:
            p=input('enter name of email to be changed:')
            if p in maindict:
                print(maindict[p]['email'])
                z=int(input("enter the portion you want to update:"))
                z-=1
                maindict[p]['email'].pop(z)
                print(maindict[p]['email'])
                newmail=input('enter the email:')
                maindict[p]['email'].insert(z,newmail)
                print(maindict[p]['email'])
            else:
                print('invalid choice')

    elif choice==4:
        del1=int(input('1.delete name\n2.delete number\n3.delete email\nselect your choice:'))
        if del1==1:
            e=input('enter the name:')
            if e in maindict:
                del maindict[e]
                print(maindict)
        elif del1==2:
            k=input('enter the name:')
            if k in maindict:
                print(maindict[k]['phone'])
                g=int(input("enter the portion to be deleted:"))
                g-=1
                del maindict[k]['phone'][g]
                print(maindict[k],['phone'])
            else:
                print('invalid')
        elif del1==3:
            q=input('enter the name:')
            if q in maindict:
                print(maindict[q]['email'])
                l=int(input("enter the portion to be removed:"))
                l-=1
                del maindict[q]['email'][l]
                print(maindict[q],['email'])
            else:
                print('invalid')
        else:
            print('invalid choice')
    else:
        print('exit')
        break