def sortsize(filename,sortlist,order):
    numberlist = []
    if((filename == "SHIRTDETAILS.txt") or (filename == "TROUSERSDETAILS.txt") or (filename == "WALLETDETAILS.txt")):
        for each in sortlist:
            if(each == "XS"):
                numberlist.append(1)
            elif(each == "S"):
                numberlist.append(2)
            elif(each == "M"):
                numberlist.append(3)
            elif(each == "L"):
                numberlist.append(4)
            else:
                numberlist.append(5)               
        zippedlist = zip(numberlist, sortlist)
        if(order):
            sortedzippedlist = sorted(zippedlist)
        else:
            sortedzippedlist = sorted(zippedlist,reverse = True)
        sortlist = [element for _, element in sortedzippedlist]
    else:
        sortlist = processsortorder(sortlist,order)
    return sortlist

def processsortorder(sortlist,order):
    if(order):
        sortlist.sort()
    else:
        sortlist.sort(reverse = True)
    return sortlist

def sorting(filename,index,extra):
    order = sortorder()
    startsort(filename,index,order,extra)
    
def sortorder():
    while True:
        print("\nDo you wish to sort by ascending order or descending order?")
        order = input("Enter 0 for ascending | 1 for descending: ")
        if(order == "0"):
            return True
        elif(order == "1"):
            return False
        else:
            print("Invalid input! Please choose either 0 or 1")

def startsort(filename,index,order,extra):           
    myfile = open(filename,"r")
    originallist = []
    sortlist = []
    for line in myfile:
        line = line.rstrip()
        lines = line.split(" | ")        
        originallist.append(line)
        if(index == 5):
            sortlist.append(int(lines[index].replace("RM","")))
        else:
            if(filename == "SHOESDETAILS.txt"):
                if(index == 4):
                    sortlist.append(int(lines[index]))
                else:
                    sortlist.append(lines[index])
            else:
                sortlist.append(lines[index])
            
    if(index == 4):
        sortlist = sortsize(filename,sortlist,order)
    else:
        sortlist = processsortorder(sortlist,order)    
    print()
    print ("{:<8} {:<41} {:<10} {:<7} {:<5} {:<8} {:<6}".format('ITEMCODE','ITEMNAME','CATEGORY','GENDER','SIZE','PRICE','AMOUNT'))
    for sorteditem in sortlist:
        for original in originallist:
            original = original.rstrip()
            originals = original.split(" | ")
            if(originals[index] == (extra+str(sorteditem))):            
                print ("{:<8} {:<41} {:<10} {:<7} {:<5} {:<8} {:<6}".format(originals[0],originals[1],originals[2],originals[3],originals[4],originals[5],originals[6]))
                originallist.remove(original)

def sortaspect(filename):
    while True:
        print("\n   Which aspect do you wish to Sort by?")
        print("1. Gender\n2. Size\n3. Price\n4. Exit")
        aspect = input("Your option is (1-4): ")
        if(aspect == "1"):
            sorting(filename,3,"")
        elif(aspect == "2"):
            sorting(filename,4,"")
        elif(aspect == "3"):
            sorting(filename,5,"RM")
        elif(aspect == "4"):
            break
        else:
            print("Invalid input! Please choose from 1-4")

def sort_products():
    while True:
        print("\n*****WELCOME TO SORT PRODUCTS PAGE*****")
        print("1. Sort Shirt\n2. Sort Trousers\n3. Sort Shoes\n4. Sort Wallet\n5. Exit")
        sort = input("Your option is (1-5): ")
        if(sort == "1"):
            sortaspect("SHIRTDETAILS.txt")
        elif(sort == "2"):
            sortaspect("TROUSERSDETAILS.txt")
        elif(sort == "3"):
            sortaspect("SHOESDETAILS.txt")
        elif(sort == "4"):
            sortaspect("WALLETDETAILS.txt")
        elif(sort == "5"):
            break
        else:
            print("Invalid input! Please choose from 1-5")

def view_notification():
    print("{:<8} {:<41} {:<10} {:<7} {:<5} {:<8} {:<6} {:<20}".format('ITEMCODE','ITEMNAME','CATEGORY','GENDER','SIZE','PRICE','AMOUNT','DATE&TIME'))
    myfile = open("NOTIFICATIONDETAILS.txt","r")
    for line in myfile:
        line = line.rstrip()
        lines = line.split(" | ")
        print ("{:<8} {:<41} {:<10} {:<7} {:<5} {:<8} {:<6} {:<20}".format(lines[0],lines[1],lines[2],lines[3],lines[4],lines[5],lines[6],lines[7]))

def show_notification():
    cnt = 0
    Allfiles = ["SHIRTDETAILS.txt","TROUSERSDETAILS.txt","SHOESDETAILS.txt","WALLETDETAILS.txt"]
    for filing in Allfiles:
        myfile = open(filing,"r")
        for line in myfile:
            line = line.rstrip()
            lines = line.split(" | ")
            if(int(lines[6]) == 0):
                cnt += 1
                if(cnt == 1):
                    print("\nNotification")
                    print ("{:<8} {:<41} {:<10} {:<7} {:<5} {:<8} {:<6}".format('ITEMCODE','ITEMNAME','CATEGORY','GENDER','SIZE','PRICE','AMOUNT'))
                print ("{:<8} {:<41} {:<10} {:<7} {:<5} {:<8} {:<6}".format(lines[0],lines[1],lines[2],lines[3],lines[4],lines[5],lines[6]))
    if(cnt > 0):
        print("The above items are out of stock. Do take note of the ITEM CODE")

def view_customerpurchasehistory():
    print("{:<31} {:<8} {:<41} {:<10} {:<7} {:<5} {:<8} {:<6} {:<20}".format('NAME','ITEMCODE','ITEMNAME','CATEGORY','GENDER','SIZE','PRICE','AMOUNT','DATE&TIME'))
    myfile = open("PURCHASEHISTORYDETAILS.txt","r")    
    for line in myfile:
        line = line.rstrip()
        lines = line.split(" | ")
        print ("{:<31} {:<8} {:<41} {:<10} {:<7} {:<5} {:<8} {:<6} {:<20}".format(lines[0],lines[1],lines[2],lines[3],lines[4],lines[5],lines[6],lines[7],lines[8]))

def view_allcustomer():
    print()
    print("{:<31} {:<13} {:<33} {:<13}".format('NAME','PASSWORD','EMAIL','PHONENUMBER'))
    myfile = open("CUSTOMERDETAILS.txt","r")
    for line in myfile:
        line = line.rstrip()
        lines = line.split(" | ")
        print ("{:<31} {:<13} {:<33} {:<13}".format(lines[0],lines[1],lines[2],lines[3]))

def view_purchasehistory(username):
    myfile = open("PURCHASEHISTORYDETAILS.txt","r")
    count = 0
    for line in myfile:
        line = line.rstrip()
        lines = line.split(" | ")
        if(lines[0] == username):
            count += 1
            if(count == 1):
                print()
                print("{:<6} {:<8} {:<41} {:<10} {:<7} {:<5} {:<8} {:<6} {:<20}".format('ITEM','ITEMCODE','ITEMNAME','CATEGORY','GENDER','SIZE','PRICE','AMOUNT','DATE&TIME'))
            print ("{:<6} {:<8} {:<41} {:<10} {:<7} {:<5} {:<8} {:<6} {:<20}".format(str(count),lines[1],lines[2],lines[3],lines[4],lines[5],lines[6],lines[7],lines[8]))
    if(count == 0):
        print("No purchase history")

def notifyemptyitem(itemcode,itemname,category,gender,size,price,remainder):
    timing = time.localtime() 
    time_string = time.strftime("%d/%m/%Y, %H:%M:%S", timing)
    folder = open("NOTIFICATIONDETAILS.txt","a")
    folder.write(itemcode + " | " + itemname + " | " + category + " | " + gender + " | " + size + " | " + price + " | " + str(remainder) + " | " + time_string + "\n")
    folder.close()

def autochoosefile(category):
    if(category == "Shirt"):
        filename = "SHIRTDETAILS.txt"
    elif(category == "Trousers"):
        filename = "TROUSERSDETAILS.txt"
    elif(category == "Shoes"):
        filename = "SHOESDETAILS.txt"
    else:
        filename = "WALLETDETAILS.txt"
    return filename

def saveintopurchasehistory(line):
    timing = time.localtime() 
    time_string = time.strftime("%d/%m/%Y, %H:%M:%S", timing)
    myfiles = open("PURCHASEHISTORYDETAILS.txt","a")
    myfiles.write(line+ " | " + time_string + "\n")
    myfiles.close()

def view_cart(username):
    myfile = open("CARTDETAILS.txt","r")
    cartlist = []
    count = 0
    lack = 0
    for line in myfile:
        line = line.rstrip()
        cartlist.append(line)
        lines = line.split(" | ")
        if(lines[0] == username):
            total = int(lines[6].replace("RM","")) * int(lines[7])
            count += 1
            print()
            print("{:<6} {:<8} {:<41} {:<10} {:<7} {:<5} {:<8} {:<6}".format('ITEM','ITEMCODE','ITEMNAME','CATEGORY','GENDER','SIZE','PRICE','AMOUNT'))
            print("{:<6} {:<8} {:<41} {:<10} {:<7} {:<5} {:<8} {:<6}".format(str(count),lines[1],lines[2],lines[3],lines[4],lines[5],lines[6],lines[7]))
            print("--------------------------------------------------------------------------------------------------")
            print("{:<91} {:<6}".format('Total Payment','RM'+str(total)))
            print("\n   Cart Options as below:")
            while True:
                proceed = input("1. Payment\n2. Remove from cart\n3. Move to the next item or exit\nYour option is (1-3): ")
                if(proceed == "1"):
                    filename = autochoosefile(lines[3])                   
                    files = open(filename,"r")
                    itemlist = []
                    itemexist = 0
                    itemexists = 0
                    for data in files:
                        itemexist += 1
                        data = data.rstrip()
                        datas = data.split(" | ")
                        if((lines[1] == datas[0]) and (int(lines[7]) > int(datas[6]))):
                            lack = 1
                            print("Insufficient stock! Kindly remove item from cart or wait until further updates")                          
                            break
                        elif((lines[1] == datas[0]) and (int(lines[7]) <= int(datas[6]))):
                            remainder = int(datas[6]) - int(lines[7])
                            document = open("CUSTOMERDETAILS.txt","r")
                            valid = False
                            balancelist = []
                            for detail in document:
                                detail = detail.rstrip()
                                balancelist.append(detail)
                                details = detail.split(" | ")
                                if(details[0] == username):
                                    balance = int(details[4].replace("RM",""))
                                    if(balance >= total):
                                        valid = True
                                        balance = balance - total
                                        itemlist.append(datas[0] + " | " + datas[1] + " | " + datas[2] + " | " + datas[3] + " | " + datas[4] + " | " + datas[5] + " | " + str(remainder))
                                        balancelist.remove(detail)
                                        balancelist.append(username + " | " + details[1] + " | " + details[2] + " | " + details[3] + " | " + "RM"+str(balance))                                        
                                        if(remainder == 0):                                           
                                            notifyemptyitem(datas[0],datas[1],datas[2],datas[3],datas[4],datas[5],remainder)
                                    else:
                                        lack = 1
                                        print("Your Balance is insufficient! Please top up")
                                        break
                            if(valid):
                                filing = open("CUSTOMERDETAILS.txt","w")
                                for balancing in balancelist:
                                    filing.write(balancing + "\n")
                                print("Payment made successfully!")
                                print("Your current balance is RM"+str(balance))
                                filing.close()                               
                        else:
                            itemexists += 1
                            itemlist.append(data)

                    if(itemexist == itemexists):
                        lack = 1
                        print("This "+datas[2]+ " has been removed from store. Payment not made")
                        cartlist.remove(line)
                        break
                        
                    if(lack == 0):
                        saveintopurchasehistory(line)
                        cartlist.remove(line)
                    
                        doc = open(filename,"w")
                        for rows in itemlist:
                            doc.write(rows + "\n")
                        doc.close()
                        break
                    
                elif(proceed == "2"):
                    print("This item is removed from the cart!")
                    cartlist.remove(line)
                    break
                elif(proceed == "3"):
                    break
                else:
                    print("Invalid input! Please choose from 1-3")
                             
    if(count == 0):
        print("Your cart is empty")
    else:
        file = open("CARTDETAILS.txt","w")
        for row in cartlist:
            file.write(row + "\n")
        file.close()

def confirmaddtocart(username,itemcode,itemname,category,gender,size,price,amount):
    while True:
        confirm = input("Enter 0 for no | 1 for yes: ")
        if(confirm == "0"):
            break
        elif(confirm == "1"):                 
            myfiles = open("CARTDETAILS.txt","a")
            myfiles.write(username + " | " + itemcode + " | " + itemname + " | " + category + " | " + gender + " | " + size + " | " + price + " | " + str(amount) + "\n")
            myfiles.close()
            print("Item is added to your cart :)")
            break
        else:
            print("Invalid input! Please enter either 0 or 1")

def checkmaximumquantity():
    quantity = 0
    while True:
        try:
            while(quantity < 1 or quantity > 5):
                quantity = int(input("Enter item quantity (1 - 5): "))
            return quantity
        except ValueError:
            print("Invalid item quantity! Quantity eligible at one go is (1-5)")

def purchasedirect(username,filename):
    print()
    enter = input("Enter the item code of the item that you wish to add to cart: ")
    got = True
    myfile = open(filename,"r")
    for line in myfile:
        line = line.rstrip()
        lines = line.split(" | ")
        if(lines[0] == enter):
            if(int(lines[6]) == 0):
                got = False
                print("Out of Stock!!!")
                break
            else:
                got = False
                quantity = checkmaximumquantity()                
                print("\nIs this the item that you wish to add to cart? Check item details below:")
                print ("{:<8} {:<41} {:<10} {:<7} {:<5} {:<8} {:<6}".format('ITEMCODE','ITEMNAME','CATEGORY','GENDER','SIZE','PRICE','AMOUNT'))
                print ("{:<8} {:<41} {:<10} {:<7} {:<5} {:<8} {:<6}".format(lines[0],lines[1],lines[2],lines[3],lines[4],lines[5],str(quantity)))         
                confirmaddtocart(username,lines[0],lines[1],lines[2],lines[3],lines[4],lines[5],quantity)
                break
    if(got):
        print("Sorry, no such item code!")

def purchaseitem(username,filename):
    while True:
        viewallitems(filename)
        print("\n   Purchase options:")
        choose = input("1. Proceed to purchase\n2. Search\n3. Filter by price\n4. Sort\n5. Exit\nYour option is (1-5): ")
        if(choose == "1"):
            purchasedirect(username,filename)
        elif(choose == "2"):
            searchaspect(filename)
        elif(choose == "3"):
            filterprice(filename)
        elif(choose == "4"):
            sortaspect(filename)
        elif(choose == "5"):
            break
        else:
            print("Invalid input! Please choose from 1-5")

def checkminprice():
    minimum = -1
    while True:
        try:
            while(minimum < 0 or minimum > 1000):
                minimum = int(input("Minimum price of your choice (0-1000): RM"))
            return minimum
        except ValueError:
            print("Invalid minimum price! Minimum price range is from (0-1000)")

def checkmaxprice():
    maximum = -1
    while True:
        try:
            while(maximum < 0 or maximum > 1000):
                maximum = int(input("Maximum price of your choice (0-1000): RM"))
            return maximum
        except ValueError:
            print("Invalid maximum price! Maximum price range is from (0-1000)")

def filterprice(filename):
    minimum = checkminprice()
    maximum = checkmaxprice()
    found = 0
    myfile = open(filename,"r")
    for line in myfile:
        line = line.rstrip()
        lines = line.split(" | ")
        price = int(lines[5].replace("RM",""))
        if((price >= minimum) and (price <= maximum)):
            found += 1
            if(found == 1):
                print("{:<8} {:<41} {:<10} {:<7} {:<5} {:<8} {:<6}".format('ITEMCODE','ITEMNAME','CATEGORY','GENDER','SIZE','PRICE','AMOUNT'))
            print("{:<8} {:<41} {:<10} {:<7} {:<5} {:<8} {:<6}".format(lines[0],lines[1],lines[2],lines[3],lines[4],lines[5],lines[6]))
    if(found == 0):
        print("No result found")
            
def searchitem(filename,aspect,index,extra):
    viewallitems(filename)
    searches = input("Enter "+aspect+" that you want to search for: "+extra)
    myfile = open(filename,"r")
    valid = 0
    for line in myfile:
        line = line.rstrip()
        lines = line.split(" | ")
        if(lines[index] == (extra+searches)):
            valid += 1
            if(valid == 1):
                print("{:<8} {:<41} {:<10} {:<7} {:<5} {:<8} {:<6}".format('ITEMCODE','ITEMNAME','CATEGORY','GENDER','SIZE','PRICE','AMOUNT'))
            print("{:<8} {:<41} {:<10} {:<7} {:<5} {:<8} {:<6}".format(lines[0],lines[1],lines[2],lines[3],lines[4],lines[5],lines[6]))
    if(valid == 0):
        print("Search failed")
    
def searchaspect(filename):
    while True:
        print("\n   Which aspect do you wish to search for?")
        print("1. Item Code\n2. Size\n3. Price\n4. Exit")
        searching = input("Your choice is (1-4): ")
        if(searching == "1"):
            searchitem(filename,"Item Code",0,"")
        elif(searching == "2"):
            searchitem(filename,"Size",4,"")
        elif(searching == "3"):
            searchitem(filename,"Price",5,"RM")
        elif(searching == "4"):
            break
        else:
            print("Invalid input! Please choose from 1-4")
        
def search_products():
    while True:
        print("\n*****WELCOME TO PRODUCT SEARCHING PAGE*****")
        print("1. Search Shirt\n2. Search Trousers\n3. Search Shoes\n4. Search Wallet\n5. Exit")
        search = input("Your choice is (1-5): ")
        if(search == "1"):
            searchaspect("SHIRTDETAILS.txt")
        elif(search == "2"):
            searchaspect("TROUSERSDETAILS.txt")
        elif(search == "3"):
            searchaspect("SHOESDETAILS.txt")
        elif(search == "4"):
            searchaspect("WALLETDETAILS.txt")
        elif(search == "5"):
            break
        else:
            print("Invalid input! Please choose from 1-5")
    

def purchase_products(username):
    while True:
        print("\n*****WELCOME TO PURCHASING PAGE*****")
        print("1. Purchase Shirt\n2. Purchase Trousers\n3. Purchase Shoes\n4. Purchase Wallet\n5. Exit")
        purchase = input("Your choice is (1-5): ")
        if(purchase == "1"):
            purchaseitem(username,"SHIRTDETAILS.txt")
        elif(purchase == "2"):
            purchaseitem(username,"TROUSERSDETAILS.txt")
        elif(purchase == "3"):
            purchaseitem(username,"SHOESDETAILS.txt")
        elif(purchase == "4"):
            purchaseitem(username,"WALLETDETAILS.txt")
        elif(purchase == "5"):
            break
        else:
            print("Invalid input! Please choose from 1-5")


def viewallitems(filename):
    print()
    print ("{:<8} {:<41} {:<10} {:<7} {:<5} {:<8} {:<6}".format('ITEMCODE','ITEMNAME','CATEGORY','GENDER','SIZE','PRICE','AMOUNT'))
    myfile = open(filename,"r")
    for line in myfile:
        line = line.rstrip()
        lines = line.split(" | ")
        print ("{:<8} {:<41} {:<10} {:<7} {:<5} {:<8} {:<6}".format(lines[0],lines[1],lines[2],lines[3],lines[4],lines[5],lines[6]))

def view_products():
    while True:
        print("\n*****WELCOME TO PRODUCT VIEWING PAGE*****")
        print("1. View Shirt\n2. View Trousers\n3. View Shoes\n4. View Wallet\n5. Exit")
        view = input("Your choice is (1-5): ")
        if(view == "1"):
            viewallitems("SHIRTDETAILS.txt")
        elif(view == "2"):
            viewallitems("TROUSERSDETAILS.txt")
        elif(view == "3"):
            viewallitems("SHOESDETAILS.txt")
        elif(view == "4"):
            viewallitems("WALLETDETAILS.txt")
        elif(view == "5"):
            break
        else:
            print("Invalid input! Please choose from 1-5")

def add_item(passcode,category,sizes,filename):
    itemcode = checkitemcode(passcode,filename)
    itemname = checkitemname(itemcode)
    itemgender = checkitemgender()
    itemsize = checkitemsize(sizes)
    itemprice = checkitemprice()
    itemquantity = checkitemquantity()
    saveadditem(itemcode,itemname,category,itemgender,itemsize,itemprice,itemquantity,filename)

def saveadditem(itemcode,itemname,category,itemgender,itemsize,itemprice,itemquantity,filename):
    while True:
        print("\nDo you wish to add the new "+category+"? Check new "+category+" details as below:")
        print ("{:<8} {:<41} {:<10} {:<7} {:<5} {:<8} {:<6}".format('ITEMCODE','ITEMNAME','CATEGORY','GENDER','SIZE','PRICE','AMOUNT'))
        print ("{:<8} {:<41} {:<10} {:<7} {:<5} {:<8} {:<6}".format(itemcode,itemname,category,itemgender,str(itemsize),itemprice,str(itemquantity)))
        saveadd = input("\nEnter 0 for no | 1 for yes: ")
        if(saveadd == "0"):
            break
        elif(saveadd == "1"):
            myfile = open(filename,"a")
            myfile.write(itemcode + " | " + itemname + " | " + category + " | " + itemgender + " | " + str(itemsize) + " | " + itemprice + " | " + str(itemquantity) + "\n")
            myfile.close()
            print("New "+category+" added successfully")
            break
        else:
            print("Invalid input! Please enter either 0 or 1")

def delete_products():
    while True:
        print("\n*****WELCOME TO DELETE PRODUCT PAGE*****")
        print("1. Delete Shirt\n2. Delete Trousers\n3. Delete Shoes\n4. Delete Wallet\n5. Exit")
        delete = input("Your choice is (1-5): ")
        if(delete == "1"):
            change_item("SHIRTDETAILS.txt","delete","Shirt",False)
        elif(delete == "2"):
            change_item("TROUSERSDETAILS.txt","delete","Trousers",False)
        elif(delete == "3"):
            change_item("SHOESDETAILS.txt","delete","Shoes",False)
        elif(delete == "4"):
            change_item("WALLETDETAILS.txt","delete","Wallet",False)
        elif(delete == "5"):
            break
        else:
            print("Invalid input! Please choose from 1-5")

def saveupdateitem(itemcode,itemname,category,gender,size,itemprice,itemquantity,filename):
    fil = open("CARTDETAILS.txt","r")
    cartlist = []
    for line in fil:
       line = line.rstrip()
       cartlist.append(line)
       lines = line.split(" | ")
       if((lines[1] == itemcode) and (lines[6] != itemprice)):
          cartlist.remove(line)
          cartlist.append(lines[0] + " | " + itemcode + " | " + itemname + " | " + category + " | " + gender + " | " + size + " | " + itemprice + " | " + lines[7])

    files = open("CARTDETAILS.txt","w")
    for data in cartlist:
       files.write(data+ "\n")

def change_item(filename,function,category,check):
    viewallitems(filename)
    changelist = []
    change = input("\nEnter the item code to "+function+": ")
    myfile = open(filename,"r")
    found = 0
    for line in myfile:
        line = line.rstrip()
        changelist.append(line)
        lines = line.split(" | ")
        if(lines[0] == change):
            found = 1
            print("\nOriginal Details")
            print ("{:<8} {:<41} {:<10} {:<7} {:<5} {:<8} {:<6}".format('ITEMCODE','ITEMNAME','CATEGORY','GENDER','SIZE','PRICE','QUANTITY'))
            print ("{:<8} {:<41} {:<10} {:<7} {:<5} {:<8} {:<6}".format(lines[0],lines[1],lines[2],lines[3],lines[4],lines[5],lines[6]))
            if(check):
                itemprice = checkitemprice()
                itemquantity = checkitemquantity()               
            while True:
                decide = False
                if(check):
                    print("\nDo you wish to update the "+category+"? Check updated "+category+" details as below:")
                    print ("{:<8} {:<41} {:<10} {:<7} {:<5} {:<8} {:<6}".format('ITEMCODE','ITEMNAME','CATEGORY','GENDER','SIZE','PRICE','AMOUNT'))
                    print ("{:<8} {:<41} {:<10} {:<7} {:<5} {:<8} {:<6}".format(lines[0],lines[1],lines[2],lines[3],lines[4],itemprice,str(itemquantity)))
                confirmation = input("\nEnter 0 for no | 1 for yes: ")
                if(confirmation == "0"):
                    decide = True
                    print("Item not "+function+"d")
                    break
                elif(confirmation == "1"):
                    if(check):
                        changelist.remove(line)
                        changelist.append(lines[0] + " | " + lines[1] + " | " + lines[2] + " | " + lines[3] + " | " + str(lines[4]) + " | " + itemprice + " | " + str(itemquantity))
                        saveupdateitem(lines[0],lines[1],lines[2],lines[3],lines[4],itemprice,str(itemquantity),filename)
                        break
                    else:
                        changelist.remove(line)
                        break
                else:
                    print("Invalid input! Please choose either 0 or 1")
            if(decide):
                break
    if(found == 0):
       print("No such item code")
    else:
       file = open(filename,"w")
       for Str in changelist:
           file.write(Str + "\n")
       print(category+" "+function+"d successfully!")

def update_products():
    while True:
        print("\n*****WELCOME TO UPDATE PRODUCTS PAGE*****")
        print("1. Update Shirt\n2. Update Trousers\n3. Update Shoes\n4. Update Wallet\n5. Exit")
        update = input("Your option is (1-5): ")
        if(update == "1"):
            change_item("SHIRTDETAILS.txt","update","Shirt",True)
        elif(update == "2"):
            change_item("TROUSERSDETAILS.txt","update","Trousers",True)
        elif(update == "3"):
            change_item("SHOESDETAILS.txt","update","Shoes",True)
        elif(update == "4"):
            change_item("WALLETDETAILS.txt","update","Wallet",True)
        elif(update == "5"):
            break
        else:
            print("Invalid input! Please choose from 1-5")

def add_products():
    while True:
        print("\n*****WELCOME TO ADD PRODUCTS PAGE*****")
        print("1. Add Shirt\n2. Add Trousers\n3. Add Shoes\n4. Add Wallet\n5. Exit")
        add = input("Your option is (1-5): ")
        if(add == "1"):
            add_item("S","Shirt","standard","SHIRTDETAILS.txt")
        elif(add == "2"):
            add_item("T","Trousers","standard","TROUSERSDETAILS.txt")
        elif(add == "3"):
            add_item("SH","Shoes","UK","SHOESDETAILS.txt")
        elif(add == "4"):
            add_item("W","Wallet","three","WALLETDETAILS.txt")
        elif(add == "5"):
            break
        else:
            print("Invalid input! Please choose from 1-5")


def checkitemcode(passcode,filename):
    import random
    while True:
        x = 0
        itemcode = passcode+str(random.randint(0,1000))
        myfile = open(filename,"r")
        for line in myfile:
            line = line.rstrip()
            lines = line.split(" | ")
            if(lines[0] == itemcode):
                x = 1
                break
        if(x == 0):
            break
    return itemcode

def checkitemname(itemcode):
    print("Item Code: "+itemcode)
    itemname = input("Enter item name: ")
    while not(re.match("^(?!.*[^a-zA-Z0-9\\s])(?=[A-Z].*)(?!.*\\s{2}.*).{4,39}[a-z]$",itemname)):
        print("Invalid item name!!! Item name format is as below:")
        print("-Only accept upper case, lower case and space (5-40 characters)")
        print("-Must start with upper case")
        print("-Must end with lower case")
        print("-No double spacing is allowed between two characters\n")
        itemname = input("Enter item name: ")
    return itemname

def checkitemgender():    
    genderlist = ["M","F"]
    gender = input("Enter gender type (M/F): ")
    while(gender not in genderlist):
        print("Invalid gender type!!! Gender available are M / F")
        gender = input("Enter gender type (M/F): ")
    return gender

def checkitemsize(sizes):
    if(sizes == "standard"):
        sizelist = ["XS","S","M","L","XL"]
        size = input("Enter item size (XS/S/M/L/XL): ")
        while (size not in sizelist):
            print("Invalid item size!!! Size available are XS / S / M / L / XL")
            size = input("Enter item size (XS/S/M/L/XL): ")           
    elif(sizes == "UK"):
        size = 0
        while True:
            try:
                while(size < 7 or size > 12):
                    size = int(input("Enter item UK size (7-12): "))
                break
            except ValueError:
                print("Invalid item size!!! Size available are 7-12")
    else:
        sizelist = ["S","M","L"]
        size = input("Enter item size (S/M/L): ")
        while (size not in sizelist):
            print("Invalid item size!!! Size available are S / M / L")
            size = input("Enter item size (S/M/L): ")        
    return size

def checkitemprice():
    price = 0
    while True:
        try:
            while(price < 80 or price > 1000):
                price = int(input("Enter item price (RM80-RM1000): RM"))
            break
        except ValueError:
            print("Invalid item price! Price range is from (RM80-RM1000)")
    return ("RM"+str(price))

def checkitemquantity():
    quantity = 0
    while True:
        try:
            while(quantity < 3 or quantity > 150):
                quantity = int(input("Enter item quantity (3 - 150): "))
            break
        except ValueError:
            print("Invalid item quantity! Quantity available are from (3-150)")
    return quantity

def confirmupdate(cnt,username,password,email,phonenumber,balance):
    linelist = []
    myfile = open("CUSTOMERDETAILS.txt","r")
    for line in myfile:
        linelist.append(line.rstrip())
    linelist[cnt] = username + " | " + password + " | " + email + " | " + phonenumber + " | " + balance
    myfiles = open("CUSTOMERDETAILS.txt","w")
    for row in linelist:
        myfiles.write(row+"\n")
    print("Changes are made successfully")
    myfiles.close()

def updateownprofile(username,cnt):
    balance = viewownprofile(username)
    password = checkpassword()
    email = checkemail()
    phonenumber = checkphonenumber()
    while True:
        print("\nDo you wish to update changes? Check updated details below:")
        print ("{:<31} {:<13} {:<33} {:<13} {:<7}".format('NAME','PASSWORD','EMAIL','PHONENUMBER','BALANCE'))
        print ("{:<31} {:<13} {:<33} {:<13} {:<7}".format(username,password,email,phonenumber,balance))
        update = input("\nEnter 0 for no | 1 for yes: ")
        if(update == "0"):
            print("Changes are not made")
            break
        elif(update == "1"):
            confirmupdate(cnt,username,password,email,phonenumber,balance)
            break
        else:
            print("Invalid input! Please choose either 0 or 1")
        
def viewownprofile(username):
    myfile = open("CUSTOMERDETAILS.txt","r")
    for line in myfile:
        line = line.rstrip()
        lines = line.split(" | ")
        if(lines[0] == username):
            print ()
            print ("{:<31} {:<13} {:<33} {:<13} {:<7}".format('NAME','PASSWORD','EMAIL','PHONENUMBER','BALANCE'))
            print ("{:<31} {:<13} {:<33} {:<13} {:<7}".format(lines[0],lines[1],lines[2],lines[3],lines[4]))
            return lines[4]

def confirmretrievepass(Password,Email,Phone):
    while True:
        print("\n   Do you wish to retrieve password through email or phone number?")
        print("1. Email\n2. Phone Number")
        retrieve = input("Your choice is: ")
        if(retrieve == "1"):
            email = input("Please Enter your Email: ")
            if(Email == email):
                return"Password retrieved: "+Password
            else:
                return"Email not found"
        elif(retrieve == "2"):
            phonenumber = input("Please Enter your Phone Number: ")
            if(Phone == phonenumber):
                return"Password retrieved: "+Password
            else:
                return"Phone Number not found"
        else:
            print("Invalid input! Please choose either 1 or 2")

def retrievepassword():
    print("\n*****WELCOME TO PASSWORD RETRIEVAL PAGE*****")
    name = input("Please Enter your Username: ")
    myfiles = open("CUSTOMERDETAILS.txt","r")
    found = 0
    for data in myfiles:
        data = data.rstrip()
        datas = data.split(" | ")
        if(datas[0] == name):
            found = 1
            print(confirmretrievepass(datas[1],datas[2],datas[3]))
            break
    if(found == 0):
        print("Username not found")          

def topup(username):
    myfile = open("CUSTOMERDETAILS.txt","r")
    topuplist = []
    check = True
    for line in myfile:
        line = line.rstrip()
        topuplist.append(line)
        lines = line.split(" | ")
        if(lines[0] == username):
            if(lines[4] == "RM10000"):
                check = False
                print("You have exceeded balance limit of RM10000")
                break
            else:
                while True:
                    try:
                        add = int(input("Enter the amount to top up (RM50-RM10000): RM"))
                        amount = int(lines[4].replace("RM","")) + add
                        if((add < 50) or (add > 10000)):
                            print("Can only top up from RM50 to RM10000")
                        elif(amount > 10000):
                            print("Unable to top up, You have exceeded balance limit of RM10000")
                        else:
                            topuplist.remove(line)
                            topuplist.append(username + " | " + lines[1] + " | " + lines[2] + " | " + lines[3] + " | " + "RM"+str(amount))
                            break
                    except ValueError:
                        print("Invalid Input! Please enter from RM50 to RM10000")
    if(check):
        file = open("CUSTOMERDETAILS.txt","w")
        for item in topuplist:
            file.write(item + "\n")
        print("Top up successfully")
        file.close()

def userfunction_page(username,cnt):
    while True:
        print("\n*****Hi, "+username+" WELCOME!!!*****")
        print("************ENJOY SHOPPING*************")
        print("   Your Functionalities are:")
        print("1. View Products\n2. Search Products\n3. Sort Products\n4. Purchase Products\n5. View Cart\n6. View Profile\n7. Update Profile\n8. View Purchase History\n9. Top Up\n10.Log Out")
        function = input("Your choice is (1-9): ")
        if(function == "1"):
            view_products()
        elif(function == "2"):
            search_products()
        elif(function == "3"):
            sort_products()
        elif(function == "4"):
            purchase_products(username)
        elif(function == "5"):
            view_cart(username)
        elif(function == "6"):
            viewownprofile(username)
        elif(function == "7"):
            updateownprofile(username,cnt)
        elif(function == "8"):
            view_purchasehistory(username)
        elif(function == "9"):
            topup(username)
        elif(function == "10"):
            break
        else:
            print("Invalid input! Please enter from 1-10")

def admin_page():
    while True:
        print("\n*****WELCOME TO ADMIN PAGE*****")
        print("   Your Functionalities are:")
        print("1. View Customer Details\n2. View Products\n3. View Customer Purchase History\n4. View Notification\n5. Add Products\n6. Update Products\n7. Delete Products\n8. Log Out")
        choosing = input("Your choice is (1-8): ")
        if(choosing == "1"):
            view_allcustomer()
        elif(choosing == "2"):
            view_products()
        elif(choosing == "3"):
            view_customerpurchasehistory()
        elif(choosing == "4"):
            view_notification()
        elif(choosing == "5"):
            add_products()
        elif(choosing == "6"):
            update_products()
        elif(choosing == "7"):
            delete_products()
        elif(choosing == "8"):
            break
        else:
            print("Invalid input! Please choose from 1-8")

def login_page():
    while True:
        print("\n*****WELCOME TO LOGINPAGE*****")
        username = input("Username: ")
        password = input("Password: ")
        if((username == "Admin") and (password == "abc123")):
            print("Successfully logged in as Admin")
            show_notification()
            admin_page()
        else:
            myfile = open("CUSTOMERDETAILS.txt","r")
            x = 0
            cnt = -1
            for line in myfile:
                cnt += 1
                line = line.rstrip()
                lines = line.split(" | ")
                if(lines[0] == username):
                    if(lines[1] == password):
                        x = 1
                        break
                    else:               
                        print("Incorrect Password!!!")
                        x = 2
                        break                        
            if(x == 0):
                print("Incorrect Username")
            elif(x == 1):
                userfunction_page(username,cnt)

            if((x == 0) or (x == 2)):
                print("\n  Do you wish to login or return to HOME page?")
                print("  ANY KEY to Continue\n1.Forgotten Password\n2.Return to Homepage")
                choice = input("Your option is (1-2): ")
                if(choice == "1"):
                    retrievepassword()        
                elif(choice == "2"):
                    break
                                
def registration_page():
    print("\n*****WELCOME TO REGISTRATION PAGE*****")
    name = checkname()
    password = checkpassword()
    email = checkemail()
    phonenumber = checkphonenumber()
    createnewaccount(name,password,email,phonenumber)

def checknameexist(name):
    myfile = open("CUSTOMERDETAILS.txt","r")
    for line in myfile:
        line = line.rstrip()
        lines = line.split(" | ")
        if(lines[0] == name):
            return True
                  
def checkname():
    while True:
        name = input("Enter your name: ")
        if not (re.match("^(?!.*[^a-zA-Z\\s])(?=[A-Z].*)(?!.*\\s{2}.*)(?!.*[A-Z]{2}.*)(?!.*[a-z][A-Z].*)(?!.*[A-Z]\\s.*)(?!.*\\s[a-z].*).{5,29}[a-z]$",name)):
            print("Incorrect Name!!! Name format is as below:\n-Only Accept Upper case, lower case and space (6-30 characters)")
            print("-Must begin with upper case")
            print("-Upper case must be followed by lower case")
            print("-Upper case cannot be in between two lower cases")
            print("-Must begin with upper case after spacing")
            print("-Double spacing is not allowed")
            print("-Must end with lower case\n")
        elif(checknameexist(name)):
            print("Name exists! Please choose another one!")
        else:
            return name

def checkpassword():
    password = input("Enter your password: ")
    while not(re.match("^(?!.*[^a-zA-Z0-9])(?=(.*[0-9]){1})(?!(.*[0-9]){2,})(?=.*[a-z])(?=(.*[A-Z]){1})(?!(.*[A-Z]){2,}).{8,12}$",password)):
        print("Invalid password!!! Password format is as below:")
        print("-Accept 8-12 characters consisting of")
        print("-a must of only 1 upper case,")
        print("-a must of only 1 number")
        print("-and the rest lower cases (No symbols allowed)\n")
        password = input("Enter your password: ")
    return password

def checkemail():
    emaillist = ["(@gmail.com)$","(@yahoo.com)$","(@outlook.com)$","(@hotmail.com)$"]
    while True:
        check = 0
        email = input("Enter your email: ")
        for variable in emaillist:
            if (re.match("^[a-zA-Z](?!.*[^a-zA-Z0-9_@.])(?!(.*[@]){2,})(?!(.*[.]){2,})(?!(.*[_]){2,})(?=(.*[0-9]){0,})(?=(.*[A-Z]){0,}).{6,18}[a-zA-Z0-9]"+variable,email)):
                check = 1
                break

        if(check == 0):
            print("Invalid email!!! Email format is as below:")
            print("-Must begin with an alphabet(Upper case or Lower case)")
            print("-Must end with upper case, lower case or number (Cannot end with underscore)")
            print("-Accept Upper case, lower case, numbers, underscore (Only allow one underscore)")
            print("-No space is allowed")
            print("-@ and . reserved for (example: @gmail.com)")
            print("-Only accept 8-20 characters (Ex: X@gmail.com where X accepts 8-20 characters)")
            print("-Accept gmail/yahoo/outlook/hotmail\n")
        else:
            return email

def checkphonenumber():
    phonenumber = input("Enter your phone number: ")        
    while not ((re.match("^(01)[2-9]-[0-9]{7}$",phonenumber)) or (re.match("^(011)-[0-9]{8}$",phonenumber))):
        print("Invalid phone number!!! Phone Number format is as below:")
        print("-Malaysian Phone Number Example: 01X-3243423 where X can be 2-9\n\t\t\t\t 011-32323211\n")
        phonenumber = input("Enter your phone number: ")
    return phonenumber

def createnewaccount(name,password,email,phonenumber):
    while True:
        print("\nDo you wish to save your new account details? Check details as below:")
        print ("{:<31} {:<13} {:<33} {:<13} {:<7}".format('NAME','PASSWORD','EMAIL','PHONENUMBER','BALANCE'))
        print ("{:<31} {:<13} {:<33} {:<13} {:<7}".format(name,password,email,phonenumber,"RM0"))
        save = input("\nEnter 0 to cancel and 1 to save: ")
        if(save == "0"):
            print("Information not saved")
            break
        elif(save == "1"):
            myfile = open("CUSTOMERDETAILS.txt","a")
            myfile.write(name + " | " + password + " | " + email + " | " + phonenumber + " | " + "RM0\n")
            print("New account is created successfully")
            break
        else:
            print("Invalid input! Please choose from 1-2")

def Main_menu():
    while True:
        print ("\n"+time.asctime(time.localtime(time.time())))
        print("W    W    W  EEEEEE L        CCCCCC  OOOOOOO  M       M  EEEEEE                          TTTTTTT OOOOOOO")
        print("W    W    W  E      L       C        O     O  MM     MM  E                                  T    O     O")
        print(" W  W W  W   EEEEEE L       C        O     O  M M   M M  EEEEEE                             T    O     O")
        print(" W  W W  W   E      L       C        O     O  M  M M  M  E                                  T    O     O")
        print("  W    W     EEEEEE LLLLLLL  CCCCCC  OOOOOOO  M   M   M  EEEEEE                             T    OOOOOOO")
        print("\n")
        print("     TTTTTTT  OOOOO  MM     MM  MM     MM  Y   Y    H   H  II  L     FFFFF II   GGGG  EEEEEE  RRRR")
        print("        T     O   O  M M   M M  M M   M M   Y Y     H   H  II  L     F     II  G      E       R   R")
        print("        T     O   O  M  M M  M  M  M M  M    Y      HHHHH  II  L     FFFFF II  G  GGG EEEEEE  RRRR")
        print("        T     O   O  M   M   M  M   M   M    Y      H   H  II  L     F     II   GGGG  E       R   R")
        print("        T     OOOOO  M   M   M  M   M   M    Y      H   H  II  LLLLL F     II      G  EEEEEE  R    R\n")
        print("  Do you wish to\n1.Login\n2.Register\n3.Exit")     
        option = input("Select your option (1-3): ")
        if(option == "1"):
            login_page()
        elif(option == "2"):
            registration_page()
        elif(option == "3"):
            print("Thank You! Pls Come Again ^_^")
            break
        else:
            print("Invalid input! Please select from 1-3")

import re                  
import time
Main_menu()
