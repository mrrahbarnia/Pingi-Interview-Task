class ApplicationException(Exception):
    status_code = 500
    detail = "Internal server error."


class ProductAlreadyExists(ApplicationException):
    status_code = 409
    detail = "Product already exists."
