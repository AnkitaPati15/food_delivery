from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from cart.models import Cart, CartItem
from menu.models import Category, MenuItem
from restaurants.models import Restaurant


User = get_user_model()


class CartFlowTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="tester",
            password="pass1234",
        )
        self.client.force_login(self.user)

        self.restaurant = Restaurant.objects.create(
            owner=self.user,
            name="Test Restaurant",
            description="A test restaurant",
            address="123 Test Street",
            phone_number="1234567890",
            opening_time="10:00:00",
            closing_time="22:00:00",
        )
        self.category = Category.objects.create(
            restaurant=self.restaurant,
            name="Pizza",
        )
        self.menu_item = MenuItem.objects.create(
            restaurant=self.restaurant,
            category=self.category,
            name="Margherita Pizza",
            description="Cheesy pizza",
            price=Decimal("199.00"),
        )

    def test_add_to_cart_creates_cart_item(self):
        response = self.client.get(
            reverse("add-to-cart", args=[self.menu_item.id])
        )

        self.assertEqual(response.status_code, 302)
        cart = Cart.objects.get(user=self.user)
        self.assertEqual(cart.items.count(), 1)

        cart_item = cart.items.get()
        self.assertEqual(cart_item.menu_item, self.menu_item)
        self.assertEqual(cart_item.quantity, 1)

    def test_remove_cart_item_deletes_it(self):
        cart, _ = Cart.objects.get_or_create(user=self.user)
        cart_item = CartItem.objects.create(
            cart=cart,
            menu_item=self.menu_item,
            quantity=1,
        )

        response = self.client.post(
            reverse("remove-cart-item", args=[cart_item.id])
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(CartItem.objects.filter(id=cart_item.id).exists())
