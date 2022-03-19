import csv
import time
from datetime import date
import math
import webbrowser
import random
##
#change path to the downloaded path or copy those files to the original path
def movieslist():
    f=open("Project1.txt")
    m=f.read()
    print(m)



##
def seereview():
    f=open("addreview.txt",'r')
    print(f.read())
    n=int(input("Enter 999 to go back"))
    while n!=999:
        n=int(input("Plz enter a specific value(999 for back)"))

    mrt()
    
        
        
##
def addreview():
    f=open("addreview.txt",'a')
    print("Please type your review about the movie:")
    s=""
    name=input("Enter your name:")
    s+=(name+":\n")
    m=input("Line 1: (999 for previous page)\n")
    
    i=2
    while m!='999':
        print("Line ",i,": (999 for previous page)")
        m=input()
        s+=(m+"\n")
        i+=1
    s=s[0:len(s)-4]
    s+="\n"
    f.write(s)
    print("Review Added !!\n")
    print("Redirecting to HomePage ......")
    time.sleep(2)
    home()

        
    
    
    
    
##    
s=["www.youtube.com/watch?v=vOCM9wztBYQ","www.youtube.com/watch?v=zAGVQLHvwOY","www.youtube.com/watch?v=KyhrrdpA2YA","www.youtube.com/watch?v=GWxF84mWfxs","www.youtube.com/watch?v=tsxemFX0a7k"]    
def trailer():
        a=int(input("1.Asuran (90%)\n2.Joker (88%)\n3.Sye Raa (85%)\n4.Pailwaan (83%)\n5.Chichchore (88%)\n6.Back to Previous Page\n"))
        if a==1 or a==2 or a==3 or a==4 or a==5:
            webbrowser.open(s[a-1],new=0)#Trailer
            mrt()
        elif a==6:
            mrt()
        
            
                                                                                            
##            
def mrt():
    print("MOVIES TRAILERS AND REVIEWS\n\n1.Movie Trailer\n2.Movie Review\n3.Back to HomePage")
    n=int(input())
    if n==1:
        trailer()
    elif n==2:
        n2=int(input("1.User Reviews\n2.Add Review\n3.Back"))
        if n2==1:
            seereview()
        elif n2==2:
            addreview()
        elif n2==3:
            mrt()
    elif n==3:
        home()
    
        
    
            
##       
def confirm():
            
            n=int(input("Enter Movie to book : "))
            
            if n==1:
                print("Asuran (U/A)\nAction, Drama\nCast : Dhanush,Manju Warrier,Ken Karunas,Teejay,Prakash Raj,Pasupathy,Naren,Pawan\nDirector : Vetri Maaran\nMusic Composer : G V Prakash Kumar\nLanguage : Tamil, Malayalam\nDuration : 2 hrs 21 mins")
                print("\nTrailer  - ")
                s=int(input("Enter 0 to confirm and 999 to previous page:\n"))
                if s==0:
                    book(n)
                elif s==999:
                    movieslist()
                    confirm()
            elif n==2:
                print("Joker (A)\nCrime,Fantasy,Thriller\nCast : Joaquin, Robert, Zazie, Brian Tyree\nDirector : Todd Philips\nMusic Composer : Hildur\nLanguage : English\nDuration : 2 hrs 16 mins")
                s=int(input("Enter 0 to confirm and 999 to previous page:\n"))
                if s==0:
                    book(n)
                elif s==999:
                    movieslist()
                    confirm()
            elif n==3:
                print("SyeRaa Narasimha Reddy (U)\nAction,Drama,Historical\nCast : Chiranjeevi,Kicha Sudeep, Vijay Sethupathi,Jagapati Babu,Nayantara\nDirector : Surender Reddy\nMusic Composer : Amit Trivedi\nLanguage : Telugu,Kannada,Tamil,Hindi\nDuration : 3 hrs 5 mins")
                s=int(input("Enter 0 to confirm and 999 to previous page:\n"))
                if s==0:
                    book(n)
                elif s==999:
                    movieslist()
                    confirm()
            elif n==4:
                print("Pailwaan (U/A)\nAction, Drama\nCast : Kicha Sudeep,Sunil Shetty,Sushant Singh,Akansha Singh\nDirector : S Krishna \nMusic Composer : Arjun Janya\nLanguage : Kannada, Telugu, Tamil, Malayalam\nDuration : 2 hrs 46 mins")
                s=int(input("Enter 0 to confirm and 999 to previous page:\n"))
                if s==0:
                    book(n)
                elif s==999:
                    movieslist()
                    confirm()
            elif n==5:
                print("Chichhorre (U)\nComedy,Romantic,Drama\nCast : Sushant Singh, Shradda Kapoor, Varun Sharma, Tushar Pandey\nDirector : Nithesh Tiwari\nMusic Composer : Pritam\nLanguage : Hindi\nDuration : 2 hrs 29 mins")
                s=int(input("Enter 0 to confirm and 999 to previous page:"))
                if s==0:
                    book(n)
                elif s==999:
                    movieslist()
                    confirm()
            elif n==999:
                home()
            
                
##
mlist=["Asuran","Joker","Sye Raa Narasimha Reddy","Pailwaan","Chichchore"]
tkprice=[250,450,300,300,400]
slotlist=["7:00 am to 10:15 am","11:00 am to 02:15 pm","3:00 pm to 06:15 pm","7:00 pm to 10:15 pm"]
def book(temp):
    tseats=""
    n=temp
    fprice=0
    pc=tkprice[n-1]+150
    gc=tkprice[n-1]
    sc=tkprice[n-1]-100
    slot=int(input("enter your slot :\n1.07:00 am to 10:15 am\n2.11:00 am to 02:15 pm\n3.03:00 pm to 06:15 pm\n4.07:00 pm to 10:15 pm\n"))
    nseats=int(input("Enter required number of seats :"))
    print("Platinum Class -> Rs.",pc,"\nGold Class     -> Rs.",gc,"\nSilver Class   -> Rs.",sc,"\nEnter P/G/S :")
    classtype=input()
    if classtype in 'pP':
        fprice=pc
    elif classtype in 'gG':
        fprice=gc
    elif classtype in 'sS':
        fprice=sc
    print("Please enter the seats you wish to book :")
    tseats=seatselection(nseats)
    fprice=fprice*nseats
    fpricetax=fprice*0.18
    total=fprice+fpricetax
    invoice(nseats,total,n,tseats,slot)

##
    

def seatselection(nseats):
    n=nseats
    
    l=[]
    bookingstatus=[]
    bookedseats=[]
    srow=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O']
    scol=list(range(20))
    for i in srow:
        for j in scol:
            l.append(i+str(j+1))
    with open("seats.csv",'r') as af:
        afread=csv.reader(af)
        status=list(afread)
        status=status[0::2]
        for i in status:
            bookingrow=[]
            for j in i:
                if j=='0':
                    bookingrow.append(' * ')
                else:
                    bookingrow.append(' $ ')
            bookingstatus.append(bookingrow)
                
    for i in range(len(srow)):
        k=[]
        for j in scol:
            if j<9:
                k.append(' '+srow[i]+str(j+1))
            else:
                k.append(srow[i]+str(j+1))
        print(k)
        print(bookingstatus[i])
    print(" * -> Unbooked\n $ -> Booked")
    c=0
    while n:
        n-=1
        nrow=input("Enter row")
        ncol=int(input("Enter col"))
        ndata=nrow+str(ncol)
        if ndata in l:
            with open("seats.csv",'r') as f:
                r=csv.reader(f)
                new=list(r)
                new=new[0::2]
                trow=srow.index(nrow)
                tcol=ncol-1
                temp=new[trow]
                if temp[tcol]=='0':
                    new.pop(trow)
                    temp.pop(tcol)
                    temp.insert(tcol,1)
                    new.insert(trow,temp)
                    bookedseats.append(nrow+str(ncol))
                    c+=1
                    print(c," seats selected")
                elif temp[tcol]=='1':
                    print("Seat already Booked")
                    n+=1
            with open("seats.csv",'w') as f1:
                w=csv.writer(f1)
                w.writerows(new)
        else:
            print("Invalid seat")
            n+=1
            continue
    print("Ticket booked")
    print("Seats : ",bookedseats)
    
    return bookedseats
    
    

    
##
def invoice(n,t,mvn,ts,sl):
    slot=sl
    tseats=ts
    nseats=n
    gtotal=t
    ntotal=gtotal/1.18
    gst=gtotal-ntotal
    moviename=mlist[mvn-1]
    print("\n"*10)
    
    print("             RND CINEMAS")
    print("Date/Time :",time.ctime())
    print("Ticket No:",random.randint(1,850),"        Screen No:",random.randint(1,5))
    print("-----------------------------------\n")
    print("Movie : ",moviename)
    print("Slot : ",slotlist[slot-1])
    print("Number of seats : ",nseats)
    print("Seats : ",tseats)
    print("Net Total           : Rs.",round(ntotal,2))
    print("GST 18 %            : Rs.",round(gst,2))
    print("Grand Total         : Rs.",round(gtotal,2))
    print("-----------------------------------")
    print("\n\n")

    q=int(input("1.Print Receipt\n2.Cancel (move to HomePage)"))
    if q==1:
        time.sleep(1)
        print("Sending details to Printer - EPSON ML 380 Series")
        time.sleep(1)
        print("Printing .....")
        time.sleep(3)
        print("Thank you for Booking ! Enjoying watching the movie and dont forget to rate us !")
        time.sleep(1)
        print("Redirecting to HomePage ......\n")
        time.sleep(2)
        home()
    elif q==2:
        print("Redirecting to HomePage ......\n")
        time.sleep(2)
        home()

##
def snacks():
    pricesnacks=0
    popcorn=[160,180,190]
    pizza=[130,180]
    burger=[80,120]
    kfc=[300,650]
    beverage=[40,95,40,90]
    l=[]
    lp=[]
    
    print("Welcome to RND Food Corner !! \n\n")
    print("What would you like to have ?")
    n=int(input("1.Popcorn\n2.Pizza\n3.Burger\n4.Chicken(KFC)\n5.Beverages\n6.Back to homepage"))
    while n!=6:
        if n==1:
            n1=int(input("  Types    Small     Big\n1.Salty - Rs.160     Rs.210\n2.Cheesy - Rs.180    Rs.240\n3.Caramel - Rs.190    Rs.270\n4.Back\n"))
            n1size=int(input("1.Big\n2.Small"))
            if n1==1:
                if n1size==1:
                    pricesnacks+=(popcorn[0]+50)
                    l.append("Big Salty Popcorn")
                    lp.append(popcorn[0]+50)
                else:
                    pricesnacks+=popcorn[0]
                    l.append("Small Salty Popcorn")
                    lp.append(popcorn[0])
            elif n1==2:
                if n1size==1:
                    pricesnacks+=(popcorn[1]+60)
                    l.append("Big Cheesy Popcorn")
                    lp.append(popcorn[1]+60)
                else:
                    pricesnacks+=popcorn[1]
                    l.append("Small Cheesy Popcorn")
                    lp.append(popcorn[1])
            elif n1==3:
                if n1size==1:
                    pricesnacks+=(popcorn[2]+80)
                    l.append("Big Caramel Popcorn")
                    lp.append(popcorn[2]+80)
                else:
                    pricesnacks+=popcorn[2]
                    l.append("Small Caramel Popcorn")
                    lp.append(popcorn[2])
            elif n1==4:
                n=int(input("1.Popcorn\n2.Pizza\n3.Burger\n4.Chicken(KFC)\n5.Beverages\n6.Back to homepage"))
                
            
        elif n==2:
            n2=int(input("  Types  Small  Large \n1.Veg Pizza - Rs.130  Rs.200\n2.Chicken Pizza - Rs.180  Rs.240\n3.Back"))
            n2size=int(input("1.Small\n2.Large"))
            if n2==1:
                   if n2size==1:
                       pricesnacks+=pizza[0]
                       l.append("Veg Pizza Small")
                       lp.append(pizza[0])
                           
                   else:
                       pricesnacks+=(pizza[0]+70)
                       l.append("Veg Pizza Big")
                       lp.append(pizza[0]+70)
            elif n2==2:
                   if n2size==1:
                       pricesnacks+=pizza[1]
                       l.append("Chicken Pizza Small")
                       lp.append(pizza[1])
                   else:
                       pricesnacks+=(pizza[1]+60)
                       l.append("Chicken Pizza Big")
                       lp.append(pizza[1]+60)
            elif n3==3:
                snacks()
            
        elif n==3:
            n3=int(input("  Types  Small  Large \n1.Veg Burger - Rs.80  Rs.100\n2.Chicken Burger - Rs.120  Rs.150\n3.Back"))
            n3size=int(input("1.Small\n2.Large"))
            if n3==1:
                   if n3size==1:
                       pricesnacks+=burger[0]
                       l.append("Veg Burger Small")
                       lp.append(burger[0])
                   else:
                       pricesnacks+=(burger[0]+20)
                       l.append("Veg Burger Big")
                       lp.append(burger[0]+20)
            elif n3==2:
                   if n3size==1:
                       pricesnacks+=burger[1]
                       l.append("Chicken Burger Small")
                       lp.append(burger[1])
                   else:
                       pricesnacks+=(burger[1]+30)
                       l.append("Chicken Burger Big")
                       lp.append(burger[1]+30)
            elif n3==3:
                snacks()

        elif n==4:
            n4=int(input("  Type     Rate \n1.4 legs  - Rs.300\n2.10 legs - Rs.650"))
            if n4==1:
                pricesnacks+=kfc[0]
                l.append("KFC Chicken 4 legs")
                lp.append(kfc[0])
            else:
                pricesnacks+=kfc[1]
                l.append("KFC Chicken 10 legs")
                lp.append(kfc[1])
                
        elif n==5:
            n5=int(input("   Type     Rate \n1.Pepsi (200ml) - Rs.40\n2.Pepsi (900ml) - Rs.95\n3.Coke (250ml) - Rs.40\n4.Coke (900ml) - Rs.90\n5.Back"))
            if n5==1:
                pricesnacks+=beverage[n5-1]
                l.append("Pepsi (200ml)")
                lp.append(beverage[0])
            elif n5==2:
                pricesnacks+=beverage[n5-1]
                l.append("Pepsi (900ml)")
                lp.append(beverage[1])
            elif n5==3:
                pricesnacks+=beverage[n5-1]
                l.append("Coke (250ml)")
                lp.append(beverage[2])
            elif n5==4:
                pricesnacks+=beverage[n5-1]
                l.append("Coke (900ml)")
                lp.append(beverage[3])
            elif n5==5:
                snacks()
        print("Items added :")
        for i in range(len(l)):
            print(i+1,".",l[i]," - Rs.",lp[i])
        choice=int(input("1.Continue to buy further\n2.Terminate"))
        if choice==1:
            n=int(input("1.Popcorn\n2.Pizza\n3.Burger\n4.Chicken(KFC)\n5.Beverages\n6.Back to homepage"))
            continue
        else:
            break
    if n in range(1,6):
        snacksbill(l,lp,pricesnacks)
    else:
        print("Redirecting to HomePage ......\n")
        time.sleep(3)
        home()

##
def snacksbill(templ,templp,temppricesnacks):
    l=templ
    lp=templp
    pricesnacks=temppricesnacks
        
    print("                   RND Food Corner")
    print("                              taste never ends....")
    print("--------------------------------------------------")
    print("Date / Time:",time.ctime())
    print("Invoice:",random.randint(450,950))
    print("--------------------------------------------------")
    for i in range(len(l)):
        print(i+1,".",l[i]," - Rs.",lp[i])
    print("                         Net : Rs.",round(pricesnacks,2))
    print("                     GST(18%): Rs. ",round(pricesnacks*0.18,2))
    print("                        Total: Rs.",round(pricesnacks*1.18,2),"\n\n")
    print("--------------------------------------------------")
    
    choice=int(input("1.Print Receipt\n2.Cancel and Re-order\n3.Back to Homepage"))
    if choice==1:
        time.sleep(1)
        print("Sending details to Printer - EPSON ML 380 Series")
        time.sleep(1)
        print("Printing .....")
        time.sleep(3)
        print("Thank you for Ordering ! Enjoying watching the movie and dont forget to rate us !")
        time.sleep(1)
        print("Redirecting to HomePage ......\n")
        time.sleep(2)
        home()
    elif choice==2:
        print("Current order cancelled !\nRedirecting to Snacks Page ...\n")
        time.sleep(2)
        snacks()
    elif choice==3:
        print("Redirecting to HomePage ......\n")
        time.sleep(3)
        home()
        
            
####                
def home():
    print("                          Welcome to RND CINEMAS !!")
    print("                                         get into reality.....")
    print("\n"*2)
    n=int(input("1.Book a Movie Ticket\n2.Movie Reviews and Trailers\n3.Snacks and Refreshments\n4.Exit\n"))
    if n==1:
        movieslist()
        confirm()
    elif n==2:
        mrt()
    elif n==3:
        snacks()
    elif n==4:
        print("Thank you :) Hope you enjoy using our app !")
        


home()


