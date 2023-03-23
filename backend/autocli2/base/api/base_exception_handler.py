# Rest framework - import:
from rest_framework.views import exception_handler
from rest_framework.response import Response

# Custom exception handler function: 
def custom_exception_handler(exc, context):
    """
    Custom exception handler to return JSON responses.
    """
    
    # Collect exception:
    response = exception_handler(exc, context)
    error_response = {
        'page_error': {
            'code': 'server_error',
            'message': 'Internal server error.',
            'errors': response.data
        }
    }
    # Prepare response:
    if response is not None:
        response.data = error_response
    # Return error response:
    return Response(response.data, status=response.status_code)
