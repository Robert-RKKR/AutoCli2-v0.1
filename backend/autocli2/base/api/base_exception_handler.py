# Rest framework - import:
from rest_framework.views import exception_handler
from rest_framework.response import Response

# Custom exception handler function: 
def custom_exception_handler(exc, context):
    """
    Custom exception handler to return JSON responses.
    """
    
    # Prepare error response to return:
    error_response = {
        'page_results': False,
        'page_error': {
            'code': 'server_error',
            'message': 'Internal server error.',
            'error': False}}
    # Collect exception:
    response = exception_handler(exc, context)
    if response:
        try: # Try to collect response data:
            error_response['page_error']['error'] = response.data
        except: # If not available return response:
            error_response['page_error']['error'] = str(response)
         # Return error response:
        return Response(error_response, status=response.status_code)
    else: # If response if not available, raise exception:
        raise InterruptedError(exc)
