import random
from datetime import datetime, timedelta

def get_mock_flight_data():
    statuses = ['On Time', 'Delayed', 'Cancelled']
    flight_number = f"FL{random.randint(100, 999)}"
    status = random.choice(statuses)
    gate = f"G{random.randint(1, 20)}"
    scheduled_time = datetime.now() + timedelta(hours=random.randint(1, 6))
    estimated_time = scheduled_time + timedelta(minutes=random.randint(0, 60)) if status != 'On Time' else scheduled_time

    return {
        'flight_number': flight_number,
        'status': status,
        'gate': gate,
        'scheduled_time': scheduled_time,
        'estimated_time': estimated_time,
    }
