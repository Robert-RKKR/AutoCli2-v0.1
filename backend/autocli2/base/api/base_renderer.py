# Rest framework - renderers import:
from rest_framework.renderers import JSONRenderer


# Base renderer class:
class BaseRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Renders the response in a custom JSON format with a "data" key.
        """
        
        # Prepare response:
        page_response = {
            'page_results': data
        }
        # Return response:
        return super().render(page_response, accepted_media_type, renderer_context)
