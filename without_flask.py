import pickle


with open('hotel_v.1.bin', 'rb') as f:
    dv, model = pickle.load(f)
   

def score_hotel(hotel):
    X = dv.transform([hotel])
    return model.predict_proba(X)[0, 1]

if __name__ == "__main__":
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

    print(score_hotel(hotel))
