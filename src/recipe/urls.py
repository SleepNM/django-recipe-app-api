from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("tags", views.TagViewSet)
router.register("ingredients", views.IngredientViewSet)
router.register("recipes", views.RecipeViewSet)
# Path name is 'recipe-list' and 'recipe-detail'.
# RECIPES_URL = reverse("recipe:recipe-list") 'recipe' in an app_name.
# RECIPES_DETAIL_URL = reverse("recipe:recipe-detail", args=[recipe_id]) in a function.

app_name = "recipe"

urlpatterns = [
    path("", include(router.urls)),
]
