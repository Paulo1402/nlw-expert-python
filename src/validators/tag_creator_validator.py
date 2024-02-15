from cerberus import Validator

from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError


def tag_creator_validator(request: any) -> None:
    body_validator = Validator(
        {
            "product_code": {
                "type": "string",
                "required": True,
                "minlength": 1,
                "maxlength": 50,
            },
        }
    )

    response = body_validator.validate(request.json)

    if not response:
        raise HttpUnprocessableEntityError(body_validator.errors)
