import logging
import os
import sys

import azure.functions as func
from django_serverless.wsgi import application


# def main(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info("Python HTTP trigger function processed a request.")

#     name = req.params.get("name")
#     if not name:
#         try:
#             req_body = req.get_json()
#         except ValueError:
#             pass
#         else:
#             name = req_body.get("name")

#     if name:
#         return func.HttpResponse(
#             f"Hello, {name}. This HTTP triggered function executed successfully."
#         )
#     else:
#         return func.HttpResponse(
#             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
#             status_code=200,
#         )


# os.environ.setdefault("FUNCTIONS_MOUNT_POINT", "api/httptrigger")


def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    logging.info("before set wsgi")
    return func.WsgiMiddleware(application).handle(req, context)


# import logging
# import os
# import sys

# import azure.functions as func
# from django_serverless.wsgi import application


# def main(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info("Python HTTP trigger function processed a request.")

#     name = req.params.get("name")
#     if not name:
#         try:
#             req_body = req.get_json()
#         except ValueError:
#             pass
#         else:
#             name = req_body.get("name")

#     if name:
#         return func.HttpResponse(
#             f"Hello, {name}. This HTTP triggered function executed successfully."
#         )
#     else:
#         return func.HttpResponse(
#             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
#             status_code=200,
#         )
