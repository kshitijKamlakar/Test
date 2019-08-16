//Curl Command to get the details by ifsc code with authorization code

curl -X GET \
  http://127.0.0.1:8000/getdetailsbyid/asdfgh/ \
  -H 'Accept: */*' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTY2Mzg3MjQ2LCJqdGkiOiI4YWRlNWNjZDk5Mjk0MzQ1YjE1ZmNkMDYxNjJkNWRkYiIsInVzZXJfaWQiOjF9.ndJ5CaIMcUMf6KmtILyk3gTaV2trQ0hUa5wBqgtoHG4' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Host: 127.0.0.1:8000' \
  -H 'Postman-Token: d1c8b16d-b523-4217-9690-061a33c30235,47fc7ae8-bba8-4925-8c59-1490440109cc' \
  -H 'User-Agent: PostmanRuntime/7.15.2' \
  -H 'cache-control: no-cache'