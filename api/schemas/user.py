from api import ma
from api.models.user import UserModel


#       schema        flask-restful
# object ------>  dict ----------> json


# Сериализация ответа(response)
class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = UserModel
        fields = ('id', 'username', "is_staff", "role")

#      schema         SQLAlcemy
# json-------> dict -------------> obj


# Десериализация запроса(request)
class UserRequestSchema(ma.SQLAlchemySchema):
   class Meta:
       model = UserModel

   username = ma.Str(required = True)
   password = ma.Str(required = True)
   role = ma.Str(required = False)


user_schema = UserSchema()
users_schema = UserSchema(many=True)
