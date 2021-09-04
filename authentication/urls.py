from rest_framework.routers import SimpleRouter
from .views import (
    ActiveSessionViewSet,
    LoginViewSet,
    LogoutViewSet,
    RegisterViewSet,
)
from .views import UserViewSet

app_name = "authentication"

router = SimpleRouter(trailing_slash=False)
router.register(r"checkSession", ActiveSessionViewSet, basename="check-session")
router.register(r"login", LoginViewSet, basename="login")
router.register(r"logout", LogoutViewSet, basename="logout")
router.register(r"register", RegisterViewSet, basename="register")
router.register(r"edit", UserViewSet, basename="user-edit")

urlpatterns = [
    *router.urls,
]
