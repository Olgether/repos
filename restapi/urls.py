from rest_framework import routers

from .views import (
    MeViewSet,
    ProjectViewSet,
    PricingViewSet,
    SkillViewSet,
    ContactViewSet
)

router = routers.DefaultRouter()

router.register('api/me', MeViewSet, basename="me")
router.register('api/projects', ProjectViewSet, basename="projects")
router.register('api/pricings', PricingViewSet, basename="pricings")
router.register('api/skills', SkillViewSet, basename="skills")
router.register('api/contacts', ContactViewSet, basename="contacts")

urlpatterns = router.urls