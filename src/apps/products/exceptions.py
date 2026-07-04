class ApplicationException(Exception):
    status_code = 500
    detail = "Internal server error."


class ProductAlreadyExists(ApplicationException):
    status_code = 409
    detail = "Product already exists."


class ProductNotFound(ApplicationException):
    status_code = 404
    detail = "Product not found."


class ProductCapacityExceeded(ApplicationException):
    status_code = 400
    detail = "Product capacity is full."
