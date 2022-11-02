import requests

url = 'https://hotelbooking-api.herokuapp.com/'

hotel = {
        "lead_time": 342, 
        "stays_in_weekend_nights": 0,
        "stays_in_week_nights": 0,
        "adr": 0.0,
        "total_of_special_requests": 0,
        "agent_numeric": "", 
        "meal": "BB",
        "hotel": "Resort Hotel",
        "country": "PRT",
        "market_segment": "Direct",
        "reserved_room_type": "C",
        "assigned_room_type": "C",
        "season": "summer", 
    }

response = requests.post(url, json=hotel).json()
print(response)

if response['is_cancelled']:
    print(f'Cancelled')
else:
    print(f'Not Cancelled')