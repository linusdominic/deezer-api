from turtle import title
import requests

app_id ="529542"
client_secret = "aae2d531a41a60acc8ded7bdc6f4908c"
redirect_uri = "https://example.com/topics"
permissions = "basic_access,email,manage_library"
token_uri = "https://connect.deezer.com/oauth/access_token.php"

auth_uri = f"https://connect.deezer.com/oauth/auth.php?app_id={app_id}&redirect_uri={redirect_uri}&perms={permissions}"
#Paste this url in your browser and get the authenticate the app
print(auth_uri)

#paste the code you get from the redirect url in the browser it will be in the form https://example.com/topics?code=frcf473b1b5ce645092e0e602588906c
code = "fr87e7d79c4a9741536d00b777184c0c"
access_token_uri = token_uri + f"?app_id={app_id}&secret={client_secret}&code={code}" 
#Now print the access token uri to confirm
print(access_token_uri)
response = requests.get(access_token_uri)
#now you will get the access token
print(response.text)
access_token = response.text

#Now you can use the access token to make requests to the api
response = requests.get(f"https://api.deezer.com/user/me?{access_token}")
data = response.json()
print(data)

print(data['id'])
user_id = data['id']

params = {
    'title': "Linus Deezer API",
}

add_playlist = f"https://api.deezer.com/user/{user_id}/playlists?{access_token}"
print(add_playlist)
response = requests.post(add_playlist, params=params)
print(response.text)

#Now go and check your deezer account, you will have successfully added a playlist