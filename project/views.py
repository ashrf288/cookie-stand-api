from rest_framework_simplejwt.views import TokenObtainPairView 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        ## this will get the old token and store it in token (dictionary)
        token= super().get_token(user)
        ## add the values that you want to retrive

        token['email']= user.email
        token['username'] = user.username
        return token

class MyTokenObtainPairView (TokenObtainPairView) :
    serializer_class= MyTokenObtainPairSerializer
    
