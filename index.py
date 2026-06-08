import os
import sys
import traceback

# Ensure the current directory is in sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

def handler(environ, start_response):
    try:
        from app import create_app
        _app = create_app()
        return _app(environ, start_response)
    except Exception as e:
        status = '500 Internal Server Error'
        error_msg = f"Final Diagnostic Error:\n{str(e)}\n\n{traceback.format_exc()}\n\nPath: {sys.path}\nFiles: {os.listdir(BASE_DIR)}"
        response_headers = [('Content-type', 'text/plain'), ('Content-Length', str(len(error_msg)))]
        start_response(status, response_headers)
        return [error_msg.encode('utf-8')]

app = handler
