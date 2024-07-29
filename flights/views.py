from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FlightStatus
from .serializers import FlightStatusSerializer

from django.shortcuts import render
from .models import FlightStatus
from .producer import send_message_to_queue
from django.http import JsonResponse

from django.http import JsonResponse
from .models import FlightStatus
from .mock_data import get_mock_flight_data

#get Data fetch Api Views
@api_view(['GET'])
def flight_status(request):
    status = FlightStatus.objects.all()
    serializer = FlightStatusSerializer(status, many=True)
    return Response(serializer.data)


def get_flight_status(request, flight_number):
    try:
        flight_status = FlightStatus.objects.get(flight_number=flight_number)
        response = {
            'flight_number': flight_status.flight_number,
            'status': flight_status.status,
            'gate': flight_status.gate,
            'scheduled_time': flight_status.scheduled_time,
            'estimated_time': flight_status.estimated_time,
        }
        return JsonResponse(response)
    except FlightStatus.DoesNotExist:
        return JsonResponse({'error': 'Flight not found'}, status=404)








#check the Update data how to its end point

def get_all_flights(request):
    flights = FlightStatus.objects.all()
    data = []
    for flight in flights:
        data.append({
            'flight_number': flight.flight_number,
            'status': flight.status,
            'gate': flight.gate,
            'scheduled_time': flight.scheduled_time,
            'estimated_time': flight.estimated_time,
        })
    return JsonResponse(data, safe=False)




def update_flight_status(request):
    data = get_mock_flight_data()
    flight_number = data['flight_number']
    status = data['status']
    gate = data['gate']
    scheduled_time = data['scheduled_time']
    estimated_time = data['estimated_time']

    flight_status, created = FlightStatus.objects.update_or_create(
        flight_number=flight_number,
        defaults={
            'status': status,
            'gate': gate,
            'scheduled_time': scheduled_time,
            'estimated_time': estimated_time,
        }
    )

    message = f"Flight {flight_number} status updated to {status}. Gate: {gate}, Scheduled Time: {scheduled_time}, Estimated Time: {estimated_time}"
    send_message_to_queue(message)

    return JsonResponse({'status': 'success', 'message': 'Flight status updated and notification sent'})




#notification Views
'''
def update_flight_check(request):
    flight_number = request.POST.get('flight_number')
    status = request.POST.get('status')
    gate = request.POST.get('gate')
    scheduled_time = request.POST.get('scheduled_time')
    estimated_time = request.POST.get('estimated_time')

    flight_status, created = FlightStatus.objects.update_or_create(
        flight_number=flight_number,
        defaults={
            'status': status,
            'gate': gate,
            'scheduled_time': scheduled_time,
            'estimated_time': estimated_time,
        }
    )

    message = f"Flight {flight_number} status updated to {status}. Gate: {gate}, Scheduled Time: {scheduled_time}, Estimated Time: {estimated_time}"
    send_message_to_queue(message)

    return JsonResponse({'status': 'success', 'message': 'Flight status updated and notification sent'})

'''
