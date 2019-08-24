from tkinter import *
from tkinter.ttk import Combobox
root = Tk()
root.title('Marketing Calculator')
root.geometry('600x300+0+0')

def cpc1():
    a=int(entry1.get())/int(entry4.get())
    return a
def ctr():
    b=int(entry4.get())/int(entry5.get())*100
    return b

def expensive():
    beauty=['body shop','Timeless skin care', 'forest essential','goat milk soap']
    cryp = ['ecentralized cryptocurrency', 'cryptocurrency creation service' ,'bitcoin', 'blockchain game']
    health = ['crossfit challenge' ,'crossfit boston' ,'crossfit open' ,'crossfit games']
    internet= ['database security tools' ,'secure data transfer' ,'data leakage prevention','big data']
    marketing = ['marketing agencies chicago' ,'b2b marketing agency', 'search engine marketing services']
    if entry3.get()=='Beauty & Skincare':
        for i in beauty:
            return i
    elif entry3.get() == 'Cryptocurrency':
        for i in cryp:
            return i
    elif entry3.get() == 'Fitness & Health':
        for i in health:
            return i
    elif entry3.get() == 'Internet & Telecom':
        for i in internet:
            return i
    elif entry3.get() == 'Marketing & Advertisinge':
        for i in marketing:
            return i






def keyword():
    f3 = Frame(root,bg='pink', relief=SUNKEN)
    f3.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.9)
    Label(f3, text='keyword suggestions', font="-weight bold", bg='pink', fg='black').grid(row=1, column=1)
    Label(f3, text=' Keywords', font="-weight bold", bg='pink', fg='black').grid(row=2, column=1)
    Label(f3, text='{}'.format(expensive()), font="-weight bold", bg='pink', fg='black').grid(row=2, column=1)
    Button(f3, text='back', command=main1, bg='WHITE', fg='black').grid(row=8, column=0)




def cpc():
    if entry3.get()=='Beauty & Skincare':
        return '$0.08'
    elif entry3.get() == 'Cryptocurrency':
        return '$0.12'
    elif entry3.get() == 'Fitness & Health':
        return '$0.11'
    elif entry3.get() == 'Internet & Telecom':
        return '$0.61'
    elif entry3.get() == 'Marketing & Advertisinge':
        return '$0.49'


def final():

    f2 = Frame(root, bg='pink', relief=SUNKEN)
    f2.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.9)
    Label(f2, text='Currently we dont have a sufficient marketing data in {}'.format(entry4.get()), font="-weight bold", bg='pink', fg='BLACK').grid(row=2,column=1)


def others():
    Label(f1, text= 'Mention other', font="-weight bold", bg='pink', fg='black').grid(row=10, column=1)
    global entry4
    entry4 = Entry(f1, bg='white')
    entry4.grid(row=10, column=2, sticky=N + S + E + W)
    button1 = Button(f1, text='Submit', command=final, bg='WHITE', fg='black').grid(row=12, column=1)


def credit():
    if entry3.get() == 'other':
        others()
    else:
        main1()

def main1():
    f2 = Frame(root, bg='pink', relief=SUNKEN)
    f2.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.9)
    Label(f2, text=' Online Marketing budget Calculator', font="-weight bold", bg='pink', fg='BLACK').grid(row=1,
                                                                                                           column=0)
    Label(f2, text='{} PPC according to your budget i.e {} in {}'.format(entry2.get(),entry1.get(),entry3.get()), font="-weight bold", bg='pink', fg='BLACK').grid(row=2, column=0)
    Label(f2, text='Avg CPC (Area of work):{}'.format(cpc()), font="-weight bold", bg='white', fg='BLACK').grid(row=5,column=0)
    Label(f2, text='Avg CPC (clicks) : ${}'.format(cpc1()), font="-weight bold", bg='white', fg='BLACK').grid(row=6,column=0)
    Label(f2, text='Avg CTR (click through rate):{}'.format(ctr()), font="-weight bold", bg='white', fg='BLACK').grid(row=7,column=0)


    Button(f2, text='back', command=main, bg='WHITE', fg='black').grid(row=8, column=0)
    Button(f2, text='Keyword suggestions', command=keyword, bg='WHITE', fg='black').grid(row=9, column=0)

def main():
    v1=['Google','Facebook']
    v2=['Beauty & Skincare', 'Cryptocurrency','Fitness & Health','Internet & Telecom','Marketing & Advertising','other']
    global f1
    f1 = Frame(root, bg='pink', relief=SUNKEN)
    f1.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.9)
    Label(f1, text=' Online Marketing budget Calculator', font="-weight bold", bg='pink', fg='BLACK').grid(row=2, column=1)
    Label(f1, text='Enter your PPC budget?', font="-weight bold", bg='pink', fg='BLACK').grid(row=5, column=1)
    Label(f1, text='Enter the PPC Platform ', font="-weight bold", bg='pink', fg='BLACK').grid(row=6, column=1)
    Label(f1, text='No of clicks? ', font="-weight bold", bg='pink', fg='BLACK').grid(row=7, column=1)
    Label(f1, text='No of impressions?', font="-weight bold", bg='pink', fg='BLACK').grid(row=8, column=1)
    Label(f1, text='Area of work? ', font="-weight bold", bg='pink', fg='BLACK').grid(row=9, column=1)
    global entry1
    entry1 = Entry(f1, bg='white')
    entry1.grid(row=5, column=2, sticky=N + S + E + W)
    global entry2
    entry2 = Combobox(f1, value= v1)
    entry2.grid(row=6, column=2, sticky=N + S + E + W)
    global entry3
    entry3 = Combobox(f1, value=v2)
    entry3.grid(row=9, column=2, sticky=N + S + E + W)
    global entry4                                          #clicks
    entry4 = Entry(f1, bg='white')
    entry4.grid(row=7, column=2, sticky=N + S + E + W)
    global entry5                                           #impressions
    entry5 = Entry(f1, bg='white')
    entry5.grid(row=8, column=2, sticky=N + S + E + W)

    button1 = Button(f1, text='Submit', command=credit, bg='WHITE', fg='black').grid(row=12, column=1)


if __name__ == '__main__':
    main()
    root.mainloop()