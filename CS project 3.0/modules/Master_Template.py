import sqlite3

def users():
    conn = sqlite3.connect("HOTEL MANAGEMENT.db")
    cursor = conn.cursor()

    cursor.execute('''
                    CREATE TABLE users (
                   email text,
                   password text
                    )
                    ''')
    
    insert_data=[
                 "deepansh@gmail.com","deepansh",
                 "rishit@gmail.com","rishit",
                 "adele_fisher@yahoo.com","PATHeID",
                 "brice_steuber55@gmail.com","fIcALco",
                 "mitchell90@yahoo.com","meLOgeR",
                 "lody.abernathy@hotmail.com","lechEdI",
                 "makayla.terry70@gmail.com","NeUspQ",
                 "nelle.brekke@yahoo.com","hlxCCU",
                 "syble_waelchi@hotmail.com","dElQzg",
                 "ona_douglas4@hotmail.com","oBUcRX",
                 "vidal_king@yahoo.com","LwzJyJ",
                 "antonietta_wisozk@gmail.com","fMCAbm",
                 "lourdes11@yahoo.com","vZsWsc",
                 "hilton.botsford52@yahoo.com","ZeamaY",
                 "wilburn45@hotmail.com","nt4Zsz",
                 "nels_swift@gmail.com","qa97NK",
                 "mafalda78@hotmail.com","17HKU2",
                 "betty_grady92@yahoo.com","zhQ4b0",
                 "erwin30@gmail.com","eq8Chv",
                 "antoinette_nienow@yahoo.com","sVMcYW",
                 "johathan.stroman@yahoo.com","fL7wh2",
                 "ashley.lynch30@yahoo.com","1YqK9T",
                ]
    
    for i in range (0,len(insert_data)-1,2 ):
                                
        cursor.execute('''INSERT INTO users (email,password) 
                        VALUES(?,?) ''',(insert_data[i],insert_data[i+1]) ) 

    conn.commit()
    conn.close()

def Mother_table():
    conn = sqlite3.connect("HOTEL MANAGEMENT.db")
    cursor = conn.cursor() 
    cursor.execute('''
                    CREATE TABLE Mother_table (
                        booking_id integer primary key,
                        name  text,
                        phone_no integer,
                        email_id text,
                        adults integer,
                        Room_no integer,
                        Room_type  text,
                        preference text,  
                        gym     text,
                        mini_bar    text,
                        extra_bed text,
                        breakfast text,
                        check_in text,
                        check_out text,
                        reserved_dates text,  
                        Amount_payable integer      )
                ''')




def Room_table():
    conn = sqlite3.connect("HOTEL MANAGEMENT.db")
    cursor = conn.cursor()
        
    cursor.execute('''
                    CREATE TABLE Room_table (
                        Room_no  integer ,
                        Room_type text,
                        preference text,
                        reserved_dates text
                         )
                ''')
    insert_data = [
        101, "Standard Room"  , "None" , "",
        102, "Standard Room"  , "None" , "",
        103, "Standard Room"  , "None" , "",
        104, "Standard Room"  , "None" , "",
        106, "Standard Room"  , "None" , "",
        107, "Standard Room"  , "None" , "",
        108, "Standard Room"  , "None","",
        109, "Standard Room"  , "None","",
        110, "Standard Room"  , "None","",
        111, "Standard Room"  , "None","",
        112, "Standard Room"  , "None","",
        114, "Standard Room"  , "None","",
        113, "Standard Room"  , "None","",
        115, "Standard Room"  , "None","",
        116, "Standard Room"  , "None","",
        117, "Standard Room"  , "None","",
        118, "Standard Room"  , "None","",
        119, "Standard Room"  , "None","",
        120, "Standard Room"  , "Honeymoon","",
        121, "Standard Room"  , "Honeymoon","",
        122, "Standard Room"  , "Honeymoon","",
        123, "Standard Room"  , "Honeymoon","",
        124, "Standard Room"  , "Honeymoon","",
        125, "Standard Room"  , "Smoking","",
        126, "Standard Room"  , "Smoking","",
        127, "Standard Room"  , "Smoking","",
        128, "Standard Room"  , "Smoking","",
        129, "Standard Room"  , "Smoking","",
        131, "Standard Room"  , "Smoking","",
        133, "Standard Room"  , "Pet","",
        132, "Standard Room"  , "Pet","",
        134, "Standard Room"  , "Pet","",
        135, "Standard Room"  , "Pet","",
        136, "Standard Room"  , "Pet","",
        137, "Standard Room"  , "Pet","",
        138, "Standard Room"  , "Pet","",
        139, "Standard Room"  , "Pet","",
                


        201, "Deluxe room"  ,"None","",
        202, "Deluxe room"  ,"None","",
        203, "Deluxe room"  ,"None","",
        204, "Deluxe room"  ,"None","",
        206, "Deluxe room"  ,"None","",
        207, "Deluxe room"  ,"None","",
        208, "Deluxe room"  ,"None","",
        209, "Deluxe room"  ,"None","",
        210, "Deluxe room"  ,"None","",
        211, "Deluxe room"  ,"None","",
        212, "Deluxe room"  ,"None","",
        213, "Deluxe room"  ,"None","",
        214, "Deluxe room"  ,"None","",
        215, "Deluxe room"  ,"None","",
        216, "Deluxe room"  ,"None","",
        217, "Deluxe room"  ,"None","",
        218, "Deluxe room"  ,"None","",
        219, "Deluxe room"  ,"Smoking","",
        220, "Deluxe room"  ,"Smoking","",
        221, "Deluxe room"  ,"Smoking","",
        222, "Deluxe room"  ,"Honeymoon","",
        223, "Deluxe room"  ,"Honeymoon","",
        224, "Deluxe room"  ,"Honeymoon","",
        225, "Deluxe room"  ,"Honeymoon","",
        226, "Deluxe room"  ,"Pet","",
        227, "Deluxe room"  ,"Pet","",
        228, "Deluxe room"  ,"Pet","",


        301, "Premier suite"  ,"None","",
        302, "Premier suite"  ,"None","",
        303, "Premier suite"  ,"None","",
        304, "Premier suite"  ,"None","",
        306, "Premier suite"  ,"None","",
        307, "Premier suite"  ,"None","",
        308, "Premier suite"  ,"None","",
        309, "Premier suite"  ,"None","",
        310, "Premier suite"  ,"None","",
        311, "Premier suite"  ,"None","",
        312, "Premier suite"  ,"Honeymoon","",
        313, "Premier suite"  ,"Honeymoon","",
        314, "Premier suite"  ,"Honeymoon","",
        315, "Premier suite"  ,"Smoking","",
        316, "Premier suite"  ,"Smoking","",
        317, "Premier suite"  ,"Smoking","",
        318, "Premier suite"  ,"Pet","",
        319, "Premier suite"  ,"Pet","",
        320, "Premier suite"  ,"Pet","",

        401, "Executive suite"  ,"None","",
        402, "Executive suite"  ,"None","",
        403, "Executive suite"  ,"None","",
        404, "Executive suite"  ,"None","",
        406, "Executive suite"  ,"None","",
        407, "Executive suite"  ,"None","",
        408, "Executive suite"  ,"None","",
        409, "Executive suite"  ,"Smoking","",
        410, "Executive suite"  ,"Smoking","",
        411, "Executive suite"  ,"Honeymoon","",
        412, "Executive suite"  ,"Honeymoon","",
        413, "Executive suite"  ,"Pet","",
        414, "Executive suite"  ,"Pet",""

        ]

    for i in range (0,len(insert_data),4 ):
                                
        cursor.execute('''INSERT INTO Room_table (Room_no,Room_type,preference,reserved_dates) 
                        VALUES(?,?,?,?) ''',(insert_data[i],insert_data[i+1],insert_data[i+2],insert_data[i+3] )  ) 
    conn.commit()
    conn.close()    

def payment_table():
    conn = sqlite3.connect("HOTEL MANAGEMENT.db")
    cursor = conn.cursor()
    cursor.execute('''
                    CREATE TABLE payement_table (
                        booking_id integer primary key,
                        roomCharges  integer ,
                        roomServices  integer ,
                        service  integer ,
                        vat  integer ,
                        preference integer,
                        gym  integer ,
                        bed  integer ,
                        breakfast  integer ,
                        bar  integer,
                        discount integer,
                        total integer,
                        status text
                         )
                ''')
    conn.commit()
    conn.close()


payment_table()
Room_table()
Mother_table()
users()


