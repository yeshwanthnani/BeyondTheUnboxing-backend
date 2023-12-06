import enum


class HttpStatus(enum.Enum):
    SUCCESS = 200
    CREATED = 201
    BAD_REQUEST = 400
    NOT_FOUND = 404
    UN_SUPPORTED_MEDIA_TYPE = 415
    INTERNAL_SERVER_ERROR = 500
    CONFLICT = 409


class ResponseMessages(enum.Enum):
    SUCCESS = 'Success'
    CREATED = 'Created successfully'
    BAD_REQUEST = 'Bad request'
    NOT_FOUND = 'Not Found'
    UN_SUPPORTED_MEDIA_TYPE = 'Unsupported Media Type'
    INTERNAL_SERVER_ERROR = 'Internal server error'
    UPDATED = 'Updated successfully'
    DELETED = 'Deleted successfully'


class MobileBrands(enum.Enum):
    SAMSUNG = 'SAMSUNG'
    MI = 'MI'
    REDMI = 'REDMI'
    POCO = 'POCO'
    APPLE = 'APPLE'
    ONEPLUS = 'ONEPLUS'
    OPPO = 'OPPO'
    VIVO = 'VIVO'
    REALME = 'REALME'
    MOTOROLA = 'MOTOROLA'
    NOKIA = 'NOKIA'
    ASUS = 'ASUS'
    GOOGLE_PIXEL = 'GOOGLE-PIXEL'
    INFINIX = 'INFINIX'
    TECNO = 'TECNO'
    MICROMAX = 'MICROMAX'
    LAVA = 'LAVA'