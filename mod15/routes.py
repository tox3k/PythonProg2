from flask import Flask, request, Response
import json
import services


app = Flask(__name__)

@app.route('/room', methods=['GET'])
def get_room():
    if request.args.to_dict() == {}:
        rooms = services.get_all_rooms()
        response = {
        "rooms": []
        }
        for room in rooms:
            add = {
            "roomId": room[0],
            "floor": room[1],
            "guestNum": room[2],
            "beds": room[3],
            "price": room[4]
            }
            response['rooms'].append(add)
        
        return json.dumps(response)
    
    args = request.args.to_dict()
    checkIn = args['checkIn']
    checkOut = args['checkOut']
    guestNum = args['guestsNum']
    print(args)
    room = services.get_room(checkIn, checkOut, guestNum)
    
    response = {
        "rooms": [
            {
            "roomId": room[0],
            "floor": room[1],
            "guestNum": room[2],
            "beds": room[3],
            "price": room[4]
            }
        ]
        
        
    }

    return json.dumps(response)

@app.route('/add-room', methods=['POST'])
def add_room():
    args = request.get_json()
    room = services.add_room(**args)

    return Response('', status=201)

@app.route('/booking', methods=['POST'])
def booking():
    body = request.get_json()
    data = services.booking(body['bookingDates']['checkIn'], body['bookingDates']['checkOut'], body['firstName'], body['lastName'], body['roomId'])
    room = data[0]
    print(room)
    response = {
        "rooms":[
            {
                "roomId": room[0],
                "floor": room[1],
                "guestNum": room[2],
                "beds": room[3],
                "price": room[4]
            }
        ]
        
    }
        
    response = json.dumps(response)
    return Response(response, status=data[1])

if __name__ == '__main__':
    app.run(debug=True)