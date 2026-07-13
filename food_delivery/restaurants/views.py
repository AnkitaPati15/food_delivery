from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)


from menu.models import (
    Category,
    MenuItem,
)

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters, generics
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)

from .models import Restaurant
from .serializers import RestaurantSerializer
from django.shortcuts import get_object_or_404
from reviews.models import RestaurantReview
from menu.models import Category
from menu.models import Category, MenuItem
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from menu.models import MenuItem
from orders.models import Order
from django.contrib.auth.decorators import login_required
from .forms import RestaurantForm
from django.contrib import messages
from django.db.models import (
    Sum,
    Count,
    Avg,
)
from django.shortcuts import render

from .models import Restaurant
from menu.models import MenuItem

@login_required
def owner_analytics(request):

    if request.user.role != "restaurant_owner":

        return redirect("/")

    restaurants = Restaurant.objects.filter(
        owner=request.user
    )

    orders = Order.objects.filter(
        items__menu_item__restaurant__owner=request.user
    ).distinct()

    menu_items = MenuItem.objects.filter(
        restaurant__owner=request.user
    )

    restaurant_reviews = RestaurantReview.objects.filter(
        restaurant__owner=request.user
    )

    revenue = orders.aggregate(
        total=Sum("total_amount")
    )["total"] or 0

    average_rating = restaurant_reviews.aggregate(
        avg=Avg("rating")
    )["avg"] or 0

    orders_by_status = orders.values(
        "status"
    ).annotate(
        total=Count("id")
    )

    top_items = (
        OrderItem.objects.filter(
            menu_item__restaurant__owner=request.user
        )
        .values(
            "menu_item__name"
        )
        .annotate(
            total=Sum("quantity")
        )
        .order_by("-total")[:5]
    )

    context = {

        "restaurant_count": restaurants.count(),

        "order_count": orders.count(),

        "menu_count": menu_items.count(),

        "revenue": revenue,

        "average_rating": round(
            average_rating,
            2,
        ),

        "orders_by_status": orders_by_status,

        "top_items": top_items,

    }

    return render(
        request,
        "owner/analytics.html",
        context,
    )



@login_required
def owner_dashboard(request):

    restaurants = Restaurant.objects.filter(
        owner=request.user
    )

    menu_items = MenuItem.objects.filter(
        restaurant__owner=request.user
    )

    orders = Order.objects.filter(
        items__menu_item__restaurant__owner=request.user
    ).distinct()

    revenue = sum(
        order.total_amount
        for order in orders
    )

    context = {

        "restaurant_count": restaurants.count(),

        "menu_count": menu_items.count(),

        "order_count": orders.count(),

        "revenue": revenue,

    }

    return render(
        request,
        "owner/dashboard.html",
        context,
    )

@login_required
def owner_restaurant_list(request):

    if request.user.role != "restaurant_owner":
        return redirect("/")

    restaurants = Restaurant.objects.filter(
        owner=request.user,
        is_deleted=False,
    )

    context = {
        "restaurants": restaurants,
    }

    return render(
        request,
        "owner/restaurant_list.html",
        context,
    )
@login_required
def owner_restaurant_create(request):

    if request.user.role != "restaurant_owner":
        return redirect("/")

    if request.method == "POST":

        form = RestaurantForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():

            restaurant = form.save(commit=False)

            restaurant.owner = request.user

            restaurant.save()

            messages.success(
                request,
                "Restaurant created successfully."
            )

            return redirect(
                "owner-restaurant-list"
            )

    else:

        form = RestaurantForm()

    return render(
        request,
        "owner/restaurant_form.html",
        {
            "form": form,
            "title": "Add Restaurant",
        },
    )
@login_required
def owner_restaurant_edit(request, pk):

    restaurant = get_object_or_404(
        Restaurant,
        pk=pk,
        owner=request.user,
    )

    if request.method == "POST":

        form = RestaurantForm(
            request.POST,
            request.FILES,
            instance=restaurant,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Restaurant updated successfully."
            )

            return redirect(
                "owner-restaurant-list"
            )

    else:

        form = RestaurantForm(
            instance=restaurant
        )

    return render(
        request,
        "owner/restaurant_form.html",
        {
            "form": form,
            "title": "Edit Restaurant",
        },
    )
@login_required
def owner_restaurant_delete(request, pk):

    restaurant = get_object_or_404(
        Restaurant,
        pk=pk,
        owner=request.user,
    )

    if request.method == "POST":

        restaurant.delete()

        messages.success(
            request,
            "Restaurant deleted successfully."
        )

        return redirect(
            "owner-restaurant-list"
        )

    return render(
        request,
        "owner/restaurant_delete.html",
        {
            "restaurant": restaurant,
        },
    )


from django.shortcuts import (
    render,
    get_object_or_404,
)

from menu.models import (
    Category,
    MenuItem,
)


def restaurant_detail(request, pk):

    restaurant = get_object_or_404(
        Restaurant,
        pk=pk,
        is_active=True,
    )

    average_rating = RestaurantReview.objects.filter(
        restaurant=restaurant
    ).aggregate(
        Avg("rating")
    )["rating__avg"] or 0

    review_count = RestaurantReview.objects.filter(
        restaurant=restaurant
    ).count()

    reviews = RestaurantReview.objects.filter(
        restaurant=restaurant
    ).select_related(
        "user"
    ).order_by("-created_at")

    categories = Category.objects.filter(
        restaurant=restaurant
    )

    menu_items = MenuItem.objects.filter(
        restaurant=restaurant,
        is_available=True,
    )

    search = request.GET.get("search")

    if search:
        menu_items = menu_items.filter(
            name__icontains=search
        )

    category = request.GET.get("category")

    if category:
        menu_items = menu_items.filter(
            category_id=category
        )

    context = {

        "restaurant": restaurant,

        "categories": categories,

        "menu_items": menu_items,
        "average_rating": round(average_rating, 1),
        "review_count": review_count,
        "reviews": reviews,

    }

    return render(

        request,

        "restaurant_detail.html",

        context,

    )




def home(request):

    restaurants = Restaurant.objects.filter(
        is_active=True
    )[:6]

    featured_menu_items = MenuItem.objects.filter(
        is_featured=True,
        is_available=True,
    )[:8]

    context = {
        "restaurants": restaurants,
        "featured_menu_items": featured_menu_items,
    }

    return render(
        request,
        "home.html",
        context,
    )


class RestaurantListCreateView(generics.ListCreateAPIView):

    serializer_class = RestaurantSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = [
        "is_active",
    ]

    search_fields = [
        "name",
        "description",
        "address",
    ]

    ordering_fields = [
        "name",
        "created_at",
        "delivery_time",
        "minimum_order",
        "delivery_fee",
        "average_rating",
    ]

    ordering = [
        "name",
    ]

    def get_permissions(self):

        if self.request.method == "POST":
            return [IsAuthenticated()]

        return [IsAuthenticatedOrReadOnly()]

    def get_queryset(self):

        return Restaurant.objects.active()

    def perform_create(self, serializer):

        if self.request.user.role != "restaurant_owner":
            raise PermissionError(
                "Only restaurant owners can create restaurants."
            )

        serializer.save(owner=self.request.user)


class RestaurantDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    serializer_class = RestaurantSerializer

    permission_classes = [
        IsAuthenticatedOrReadOnly
    ]

    def get_queryset(self):

        if self.request.method in [
            "PUT",
            "PATCH",
            "DELETE",
        ]:

            if not self.request.user.is_authenticated:
                return Restaurant.objects.none()

            if self.request.user.is_superuser:
                return Restaurant.objects.active()

            return Restaurant.objects.filter(
                owner=self.request.user
            )

        return Restaurant.objects.active()