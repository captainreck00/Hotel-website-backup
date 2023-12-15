import sqlite3
import datetime


def verify(email,password):
    conn=sqlite3.connect("HOTEL MANAGEMENT.db")
    cursor=conn.cursor()

    cursor.execute("Select * FROM users")
    r=cursor.fetchall()
    for i in r:
        if email==i[0] and password==i[1]:
            return True
    return False    


def date_reverse(input_date):
    from datetime import datetime
    date_object = datetime.strptime(input_date, "%Y-%m-%d")
    formatted_date = date_object.strftime("%d-%m-%Y")

    return formatted_date


def advance_booking(name , email , adults , number , room_type , preference , gym , mini_bar , extra_bed ,breakfast , checkin_date , checkout_date ):

    conn = sqlite3.connect("HOTEL MANAGEMENT.db")
    cursor = conn.cursor()

    start_date = datetime.datetime.strptime(checkin_date, '%d-%m-%Y')
    end_date = datetime.datetime.strptime(checkout_date, '%d-%m-%Y')
    dates_reserved = []
    current_date = start_date
    room=0
    dates_reserved_str =""

    while current_date <= end_date:
        dates_reserved.append(current_date.strftime('%d-%m-%Y'))
        current_date += datetime.timedelta(days=1)


    for f in dates_reserved:
        dates_reserved_str = dates_reserved_str + f + " , "
       
    cursor.execute("SELECT * FROM Room_table")
    r= cursor.fetchall()

    i=0
    while i<=(len(r) - 1):
        if r[i][1] == room_type and r[i][2] == preference :

            cursor.execute(''' SELECT reserved_dates FROM Room_table WHERE Room_no = ?''' , (r[i][0] ,))
            c= cursor.fetchall()
            g=0
            for k in dates_reserved:
                if k in  c[0][0] :
                    i=i+1
                    break
                else:
                    g=1
            if g == 1 :
                    x = c[0][0]
                    y=x
                    room =r[i][0]

                    for h in dates_reserved:
                        y = y + h +  " , " 
                    
                    cursor.execute('''INSERT INTO  Mother_table(name , phone_no , email_id ,adults, Room_no , Room_type  , preference , gym , mini_bar , extra_bed , breakfast, check_in , check_out ,reserved_dates, Amount_payable ) 
                           VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)  ''' , ( name, number , email , adults , r[i][0] , r[i][1] , preference , gym , mini_bar , extra_bed ,breakfast ,checkin_date , checkout_date, dates_reserved_str ,  0 ))
                    
                    conn.commit()

                    booking_id=int(cursor.lastrowid)
                    pay_data=pay_entry(booking_id)

                    cursor.execute('''
                        INSERT INTO payement_table (
                            booking_id, roomCharges, roomServices, service, vat  ,preference, gym, bed, breakfast, bar, discount,total, status
                        ) VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (
                        booking_id,
                        pay_data["roomCharges"],
                        pay_data["roomService"],
                        pay_data["service"],
                        pay_data["vat"],
                        pay_data["preference"],
                        pay_data["gym"],
                        pay_data["bed"],
                        pay_data["breakfast"],
                        pay_data["bar"],
                        pay_data["discount"],
                        pay_data["total"],
                        "pending"
                    ))

                    conn.commit()
                    
                    cursor.execute('''UPDATE Room_table SET reserved_dates = ? WHERE Room_no = ?''',  ( y, r[i][0] ))

                    conn.commit()
                    conn.close()
                    break      
        else:
            i=i+1
    return room
            
        

def discount(check_in, amount_payable):
    
    date = datetime.datetime.strptime(check_in, "%d-%m-%Y")   
    month = date.month
    
    if month == 5 or month == 6 or month == 7 :
        dis = 0.1 * amount_payable
        amount_payable= amount_payable - dis
    elif month == 1 or month == 12 or month == 11 :
        dis = 0.1 * amount_payable
        amount_payable = amount_payable - dis 

    return amount_payable


def pay_entry(booking_id):
    conn = sqlite3.connect("HOTEL MANAGEMENT.db")
    cursor = conn.cursor()
   
    cursor.execute(''' SELECT * FROM Mother_table WHERE booking_id = ? ''' , ( booking_id ,)) 
    r=cursor.fetchall()
    

    try:
        check_in = r[0][12]
        room_type = r[0][6]
        preference=r[0][7]
        gym =  r[0][8]
        mini_bar =  r[0][9]
        extra_bed =  r[0][10]
        breakfast=r[0][11]
        reserved_dates = r[0][14]
        
    except:
        return "Invalid ID"    
    
    
    count = reserved_dates.count(",")
    roomCharge=0
    room_service_tax=0
    vat=0
    service_tax=0
    gym_pay=0
    bed_pay=0
    bar_pay=0
    breakfast_pay=0
    prefCharge=0
    


    if room_type == "Deluxe room":
        amount_to_be_paid = 8000*count
        roomCharge=amount_to_be_paid

        if int(gym):
            amount_to_be_paid = amount_to_be_paid + (500*count)
            gym_pay=500
        if int(mini_bar):
            amount_to_be_paid = amount_to_be_paid + (500*count)
            bar_pay=500
        if int(extra_bed):
            amount_to_be_paid = amount_to_be_paid + (500*count)
            bed_pay=500
        if int(breakfast):
            amount_to_be_paid = amount_to_be_paid + (500*count)
            breakfast_pay=500
        
    if room_type == "Premier suite":
        amount_to_be_paid = 10000*count
        roomCharge=amount_to_be_paid

        if int(gym):
            amount_to_be_paid = amount_to_be_paid + (500*count)
            gym_pay=500
        if int(mini_bar):
            amount_to_be_paid = amount_to_be_paid + (500*count)
            bar_pay=500
        if int(extra_bed):
            amount_to_be_paid = amount_to_be_paid + (500*count)
            bed_pay=500
        if int(breakfast):
            amount_to_be_paid = amount_to_be_paid + (500*count)
            breakfast_pay=500

    if room_type == "Executive suite":
        amount_to_be_paid = 12000*count
        roomCharge=amount_to_be_paid

        if int(gym):
            amount_to_be_paid = amount_to_be_paid + (500*count)
            gym_pay=500
        if int(mini_bar):
            amount_to_be_paid = amount_to_be_paid + (500*count)
            bar_pay=500
        if int(extra_bed):
            amount_to_be_paid = amount_to_be_paid + (500*count)
            bed_pay=500
        if int(breakfast):
            amount_to_be_paid = amount_to_be_paid + (500*count)
            breakfast_pay=500

    if room_type == "standard room":
        amount_to_be_paid = 6000*count
        roomCharge=amount_to_be_paid

        if int(gym):
            amount_to_be_paid = amount_to_be_paid + (500*count)
            gym_pay=500
        if int(mini_bar):
            amount_to_be_paid = amount_to_be_paid + (500*count)
            bar_pay=500
        if int(extra_bed):
            amount_to_be_paid = amount_to_be_paid + (500*count)
            bed_pay=500
        if int(breakfast):
            amount_to_be_paid = amount_to_be_paid + (500*count)
            breakfast_pay=500

    if preference =="Smoking":
        prefCharge=(roomCharge*0.1)*3
    elif preference == "Honeymoon":
        prefCharge=(roomCharge*0.1)*4  
    elif preference == "Pet":
        prefCharge=(roomCharge*0.1)*3 

    amount_to_be_paid+=prefCharge

    service_tax = 0.12 * amount_to_be_paid
    vat = 0.14 * amount_to_be_paid
    room_service_tax = 0.05 * amount_to_be_paid

    amount_to_be_paid = amount_to_be_paid + service_tax + vat + room_service_tax 

    dis_amount = discount(check_in, amount_to_be_paid)
    disc=amount_to_be_paid-dis_amount
    amount_to_be_paid = dis_amount

    return {"roomCharges":roomCharge,"roomService":int(room_service_tax),"service":int(service_tax),"preference":prefCharge,"vat":int(vat),"gym":gym_pay,"bed":bed_pay,"breakfast":breakfast_pay,"bar":bar_pay,"discount":disc,"total":amount_to_be_paid}



def sorting_time2():
    conn = sqlite3.connect("HOTEL MANAGEMENT.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Mother_table")
    data = cursor.fetchall()

    today = datetime.datetime.now().date()  

    present = []
    past = []
    future = []

    for item in data:
        check_in_date = datetime.datetime.strptime(item[12], '%d-%m-%Y').date()
        reserved_dates = item[14].count(',') + 1

        if check_in_date == today:
            if item[15] != 0:  # Check if the "amount" is non-zero
                past.append((check_in_date, reserved_dates, item))
            else:
                present.append((reserved_dates, item))
        elif check_in_date < today:
            past.append((check_in_date, reserved_dates, item))
        else:
            future.append((check_in_date, reserved_dates, item))

    present.sort(reverse=True)
    past.sort(key=lambda x: (x[0], x[1]))
    future.sort(key=lambda x: (x[0], x[1])) 

    present = [item[1] for item in present]
    past = [item[2] for item in past]
    future = [item[2] for item in future]

    sorted_date = [present, future, past]

    for i in range(3):
        l = []
        for j in sorted_date[i]:
            k = {
                "id": j[0],
                "name": j[1],
                "phone_no": j[2],
                "email_id": j[3],
                "guests": j[4],
                "room_no": j[5],
                "room_type": j[6],
                "preference":j[7],
                "addons": [j[8], j[9], j[10], j[11]],
                "check_in": j[12],
                "check_out": j[13],
                "amount": j[15]
            }
            l.append(k)
        sorted_date[i] = l

    return sorted_date



def bill_paid(booking_id):
    conn = sqlite3.connect("HOTEL MANAGEMENT.db")
    cursor = conn.cursor()

    cursor.execute(''' SELECT * FROM payement_table WHERE booking_id = ? ''' , ( booking_id ,)) 
    amount=cursor.fetchone()[11]

    cursor.execute(''' UPDATE MOther_table SET Amount_payable = ? WHERE booking_id = ? ''' ,
                (amount, booking_id))
    cursor.execute(''' UPDATE payement_table SET status = 'done' ''' )
    conn.commit()
    conn.close()

def pay_data():
    conn = sqlite3.connect("HOTEL MANAGEMENT.db")
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM payement_table WHERE status='pending' ''')
    data=cursor.fetchall()

    conn.commit()
    conn.close()

    l={}
    for i in data:
        k={"id":i[0],"roomCharges":i[1],"roomService":i[2],"service":i[3],"vat":i[4],"preference":i[5],"gym":i[6],"bed":i[7],"breakfast":i[8],"bar":i[9],
           "discount":i[10],"total":i[11]}
        l[i[0]]=k

    return l






