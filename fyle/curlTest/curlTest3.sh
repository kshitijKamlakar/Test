//Curl Command to get the all the details with authorization code

curl -X GET \
  http://127.0.0.1:8000/ \
  -H 'Accept: */*' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTY2Mzg3MjQ2LCJqdGkiOiI4YWRlNWNjZDk5Mjk0MzQ1YjE1ZmNkMDYxNjJkNWRkYiIsInVzZXJfaWQiOjF9.ndJ5CaIMcUMf6KmtILyk3gTaV2trQ0hUa5wBqgtoHG4' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Host: 127.0.0.1:8000' \
  -H 'Postman-Token: d7325cfc-4c7e-49cd-9cde-77f928c0db5c,90c5eb9f-ebc8-4bb8-8633-9c703a851e73' \
  -H 'User-Agent: PostmanRuntime/7.15.2' \
  -H 'cache-control: no-cache'

