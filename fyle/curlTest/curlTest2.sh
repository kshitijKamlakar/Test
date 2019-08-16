//Curl Command to get the details by bank name and city with authorization code


curl -X GET \
  http://127.0.0.1:8000/getbyBnameAndCity/asdfgh/asdfgh/ \
  -H 'Accept: */*' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTY2Mzg3MjQ2LCJqdGkiOiI4YWRlNWNjZDk5Mjk0MzQ1YjE1ZmNkMDYxNjJkNWRkYiIsInVzZXJfaWQiOjF9.ndJ5CaIMcUMf6KmtILyk3gTaV2trQ0hUa5wBqgtoHG4' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Host: 127.0.0.1:8000' \
  -H 'Postman-Token: 108f294e-70d6-467d-916e-a221ea6d6b91,aaf5837e-32ab-4a79-9c80-64cb6c83dd4c' \
  -H 'User-Agent: PostmanRuntime/7.15.2' \
  -H 'cache-control: no-cache'
