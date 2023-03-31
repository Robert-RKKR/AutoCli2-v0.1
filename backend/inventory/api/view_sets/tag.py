# AutoCli2 - base pagination import:
from autocli2.base.api.base_pagination import BaseSmallPaginator

# AutoCli2 - base view set import:
from autocli2.base.api.base_model_viewset import BaseRwModelViewSet

# AutoCli2 - serializer import:
from inventory.api.serializers.tag import TagSerializer

# AutoCli2 - inventory model import:
from inventory.models.tag import Tag

# AutoCli2 - inventory filter import:
from inventory.filters.tag import TagFilter


# ViewSet model classes:
class TagView(BaseRwModelViewSet):
    """
    A ViewSet for viewing and editing object/s.
    """

    # Log changes:
    log_changes = True
    # Basic API view parameters:
    queryset = Tag.objects.all().order_by('pk')
    pagination_class = BaseSmallPaginator
    # Serializer classes:
    serializer_class = TagSerializer
    # Django rest framework filters:
    filterset_class = TagFilter
    ordering_fields = '__all__'
    search_fields = '__all__'
