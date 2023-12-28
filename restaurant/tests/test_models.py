from decimal import Decimal
from django.test import TestCase
from django.utils import timezone
from ..models import Menu, Booking

class MenuModelTest(TestCase):
    def setUp(self):
        Menu.objects.create(title='Test Menu Item', price=10.99, inventory=20)

    def test_menu_model(self):
        menu_item = Menu.objects.get(title='Test Menu Item')
        self.assertEqual(menu_item.title, 'Test Menu Item')
        self.assertEqual(float(menu_item.price), 10.99)
        self.assertEqual(menu_item.inventory, 20)
        self.assertEqual(str(menu_item), 'Test Menu Item : 10.99')

class BookingModelTest(TestCase):
    def setUp(self):
        Booking.objects.create(name='Test Guest 1', no_of_guests=5, bookingDate=timezone.now())
        Booking.objects.create(name='Test Guest 2', no_of_guests=3, bookingDate=timezone.now())

    def test_booking_model(self):
        booking_instance = Booking.objects.get(name='Test Guest 1')
        self.assertEqual(booking_instance.name, 'Test Guest 1')
        self.assertEqual(booking_instance.no_of_guests, 5)
        self.assertTrue(booking_instance.bookingDate)

    def test_booking_model_str_method(self):
        booking_instance = Booking.objects.get(name='Test Guest 1')
        self.assertEqual(str(booking_instance), 'Test Guest 1, {}'.format(booking_instance.bookingDate))
    
    def test_getall(self):
        # Retrieve all instances
        all_bookings = Booking.objects.all()

        # Assert that the number of retrieved items matches the number created in setUp
        self.assertEqual(len(all_bookings), 2)

        # Assert name of the retrieved items
        self.assertEqual(all_bookings[0].name, 'Test Guest 1')
        self.assertEqual(all_bookings[1].name, 'Test Guest 2')

        # Assert no_of_guests of the retrieved items
        self.assertEqual(all_bookings[0].no_of_guests, 5)
        self.assertEqual(all_bookings[1].no_of_guests, 3)

        # Assert bookingDate of the retrieved items
        self.assertTrue(all_bookings[0].bookingDate)
        self.assertTrue(all_bookings[1].bookingDate)
