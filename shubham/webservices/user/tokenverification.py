from rest_framework import status, exceptions
from django.http import HttpResponse
from rest_framework.authentication import get_authorization_header, BaseAuthentication
from django.contrib.auth.models import User
import jwt
import json


class TokenAuthentication(BaseAuthentication):
    model = None



    def authenticate(self,request):
        print("self.request",self)
        auth = get_authorization_header(request).split()
        print("split",auth)
        print("len of auth ", len(auth))
        if not auth or auth[0].lower() != b'token':
            print("lower error ")
            return None

        if len(auth) == 1:

            msg = 'Invalid token header. No credentials provided.'
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = 'Invalid token header'
            raise exceptions.AuthenticationFailed(msg)

        try:

            token = auth[1]
            if token is None or token == 'null':
                msg = 'Null token not allowed'
                raise exceptions.AuthenticationFailed(msg)
            else:
                print("comes in else part")
                print("tokennnnnn", token,type(token))
                payload = jwt.decode(token, "SECRET_KEY",'utf-8')
                print("payload",payload)
                email = payload['email']
                userid = payload['id']
                username = payload['username']
                msg = {'Error': "Token mismatch", 'status': "401"}
                try:
                    print("comes in try")
                    user = User.objects.get(
                        username=username,
                    )

                except jwt.ExpiredSignature or jwt.DecodeError or jwt.InvalidTokenError:
                    print("hello403")
                    return HttpResponse({'Error': "Token is invalid"}, status="403")
                except User.DoesNotExist:
                    print("hello500")
                    return HttpResponse({'Error': "Internal server error"}, status="500")
                print("coming in ")
                print(user,token)
                return {'user':user,'token':token}

        except Exception as e:
            print("unicode error",e)
            msg = 'Invalid token header. Token string should not contain invalid characters.'
            raise exceptions.AuthenticationFailed(msg)

    # return self.authenticate_credentials(token)

    # def authenticate_credentials(self, token):
    #     model = self.get_model()
    #     payload = jwt.decode(token, "SECRET_KEY")
    #     email = payload['email']
    #     userid = payload['id']
    #     username = payload['username']
    #     msg = {'Error': "Token mismatch", 'status': "401"}
    #     try:
    #
    #         user = User.objects.get(
    #             username=username,
    #
    #         )
    #
    #         if not user.token['token'] == token:
    #             raise exceptions.AuthenticationFailed(msg)
    #
    #     except jwt.ExpiredSignature or jwt.DecodeError or jwt.InvalidTokenError:
    #         return HttpResponse({'Error': "Token is invalid"}, status="403")
    #     except:
    #         return HttpResponse({'Error': "Internal server error"}, status="500")
    #
    #     return (user, token)

    def authenticate_header(self, request):
        return 'Token'