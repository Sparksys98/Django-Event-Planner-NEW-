from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import ListAPIView, CreateAPIView
from events.models import Event
from .serializer import ListSerializer, ListEventsSerializer, RegisterSerializer
from rest_framework.permissions import AllowAny
class BookingView(APIView):
	def get(self, request, booking_id=None):
		if booking_id:
			booking = Booking.objects.get(id=booking_id)
			serializer = BookingSerializer(booking)
			return Response(serializer.data)
		bookings = Booking.objects.all()
		serializer = BookingSerializer(bookings, many=True)
		return Response(serializer.data)
	def post(self, request, hotel_id):
		self.permission_classes = [IsAuthenticated]
		self.check_permissions(request)
		serializer = BookingCreateSerializer(data=request.data)
		if serializer.is_valid():
			hotel = Hotel.objects.get(id=hotel_id)
			serializer.save(hotel=hotel, user=request.user)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	def put(self, request, booking_id):
		self.permission_classes = [IsAuthenticated, IsBookingOwnerOrStaff]
		booking = Booking.objects.get(id=booking_id)
		self.check_object_permissions(request, booking)
		serializer = BookingCreateSerializer(booking, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	def delete(self, request, booking_id):
		self.permission_classes = [IsAuthenticated, IsAdminUser]
		self.check_permissions(request)
		booking = Booking.objects.get(id=booking_id)
		booking.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class ListView(ListAPIView):
    queryset=Event.objects.all()
    serializer_class=ListSerializer
    permission_classes=[AllowAny]

class ListEventsView(ListAPIView):
    serializer_class=ListEventsSerializer
    permission_classes=[IsAuthenticated]

class Register(CreateAPIView):
    queryset=User.objects.all()
    serializer_class = RegisterSerializer
