# social_network
This is a social social netowrking application with users creations and send request to users

- [Installation](#installation)
- [Setup](#setup)
- [Running the Server](#running-the-server)
- [API Endpoints](#api-endpoints)
  - [User Registration](#user-registration)
  - [User Login](#user-login)
  - [Send Friend Request](#send-friend-request)
  - [Accept Friend Request](#accept-friend-request)
  - [Reject Friend Request](#reject-friend-request)
  - [List Friend Requests](#list-friend-requests)
  - [List Friends](#list-friends)
- [Using Postman](#using-postman)
  - [Postman Collection](#postman-collection)


Postman request:
1.url - http://127.0.0.1:8000/users/signup/
  body - {
          "username":"jhon",
          "email":"jhon@gmail.com",
          "password":"3289328uih"
          }
  response: success 200 ok
2. url - http://127.0.0.1:8000/users/login/
   body - {
        "username":"jhon",
        "password":"3289328uih"
        }
   response: authtoken, id
      
3. url - http://127.0.0.1:8000/friends/search?/serach=""
   Headers - Authorization: Token  authtoken(9y2ge23u9u391iu1oiw)
   response:  id,name, email

4. url - http://127.0.0.1:8000/friends/send-request/<user_id>/
   Headers - Authorization: Token  authtoken(9y2ge23u9u391iu1oiw)
   response: succes

5.  url - http://127.0.0.1:8000/friends/request
   Headers - Authorization: Token  authtoken(9y2ge23u9u391iu1oiw)
   response: id,form_id,name,email

6. url - http://127.0.0.1:8000/friends/accept-request/<request_id>/
   Headers - Authorization: Token  authtoken(9y2ge23u9u391iu1oiw)
   response: id,form_id,

7. url - http://127.0.0.1:8000/friends/reject-request/<request_id>/
   Headers - Authorization: Token  authtoken(9y2ge23u9u391iu1oiw)
   response: id,form_id,

8.url - http://127.0.0.1:8000/users/logut/
   Headers - Authorization: Token  authtoken(9y2ge23u9u391iu1oiw)
   response: messg
      
