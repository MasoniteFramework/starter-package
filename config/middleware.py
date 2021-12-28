"""Middleware Configuration Settings."""

from masonite.middleware import (CorsMiddleware, ResponseMiddleware,
                                 SecureHeadersMiddleware,
                                 MaintenanceModeMiddleware)

from app.http.middleware.AuthenticationMiddleware import AuthenticationMiddleware
from app.http.middleware.CsrfMiddleware import CsrfMiddleware
from app.http.middleware.LoadUserMiddleware import LoadUserMiddleware


"""HTTP Middleware
HTTP middleware is middleware that will be ran on every request. Middleware
is only ran when a HTTP call is successful (a 200 response). This list
should contain a simple aggregate of middleware classes.
"""

HTTP_MIDDLEWARE = [
    CsrfMiddleware,
    LoadUserMiddleware,
    MaintenanceModeMiddleware,
    ResponseMiddleware,
    SecureHeadersMiddleware,
]

"""Route Middleware
Specify a dictionary of middleware to be used on a per route basis here. The key will
be the alias to use on routes and the value can be any middleware class or a list
of middleware (middleware stacks).
"""

ROUTE_MIDDLEWARE = {
    'auth': AuthenticationMiddleware,
}