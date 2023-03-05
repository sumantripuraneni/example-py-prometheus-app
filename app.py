# from prometheus_client import start_http_server, Summary
# import random
# import time

# # Create a metric to track time spent and requests made.
# REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# # Decorate function with metric.
# @REQUEST_TIME.time()
# def process_request(t):
#     """A dummy function that takes some time."""
#     time.sleep(t)

# if __name__ == '__main__':
#     # Start up the server to expose the metrics.
#     #start_http_server(8000)
#     start_http_server(port=8000, addr='localhost:8000/metrics')
#     # Generate some requests.
#     while True:
#         process_request(random.random())
from prometheus_client import make_wsgi_app
from wsgiref.simple_server import make_server

metrics_app = make_wsgi_app()

def my_app(environ, start_fn):
    if environ['PATH_INFO'] == '/metrics':
        return metrics_app(environ, start_fn)
    start_fn('200 OK', [])
    return [b'Hello World']

if __name__ == '__main__':
    httpd = make_server('', 8000, my_app)
    httpd.serve_forever()