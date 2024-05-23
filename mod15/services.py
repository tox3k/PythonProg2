import sqlite3

DATABASE = 'mod15/hotel.db'


def add_room(floor: int, beds: int, guestNum: int, price: int) -> None:
    with sqlite3.Connection(DATABASE) as con:
        cur = con.cursor()
        cur.execute(f'INSERT INTO Rooms(floor, guestNum, beds, price) VALUES ({floor}, {guestNum}, {beds}, {price})')

def get_room(checkIn, checkOut, guestsNum):
    with sqlite3.Connection(DATABASE) as con:
        cur = con.cursor()
        query = f'SELECT Id FROM Rooms WHERE guestNum=\'{guestsNum}\''
        room_id = list(str(i[0]) for i in cur.execute(query).fetchall())
        room_id = ', '.join(room_id)

        room = cur.execute(f'SELECT roomId FROM Booking WHERE roomId in ({room_id}) AND checkIn<=\'{checkIn}\' AND checkOut<=\'{checkIn}\' OR checkIn>=\'{checkOut}\' AND checkOut>=\'{checkOut}\'').fetchone()
        if room == None:
            room = room_id.split(', ')[0]
        else:
            room = room[0]
        print('---------------------------------')
        print(room_id)
        print('----------------------------------')
        return cur.execute(f'SELECT * FROM Rooms WHERE Id={room}').fetchone()

def get_all_rooms():
    with sqlite3.Connection(DATABASE) as con:
        cur = con.cursor()
        data = cur.execute('SELECT * FROM Rooms').fetchall()
        return data

def booking(checkIn: str, checkOut: str, firstName: str, lastName: str, roomId: int):
    with sqlite3.Connection(DATABASE) as con:
        cur = con.cursor()
        room_status = int(cur.execute(f'SELECT COUNT(*) FROM Booking WHERE roomId=\'{roomId}\' AND checkOut>{checkIn}').fetchone()[0])
        if room_status == 1:
            return cur.execute(f'SELECT * FROM Rooms WHERE Id={roomId}').fetchone(), 409
        else:
            cur.execute(f'INSERT INTO Booking VALUES (NULL, \'{checkIn}\', \'{checkOut}\', \'{roomId}\', \'{firstName}\', \'{lastName}\') ')

    with sqlite3.Connection(DATABASE) as con:
        cur = con.cursor()
        return cur.execute(f'SELECT * FROM Rooms WHERE Id={roomId}').fetchone(), 201