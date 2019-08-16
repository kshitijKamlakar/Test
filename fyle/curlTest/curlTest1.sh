//Curl Command to get token with username and password

curl -X POST \
  http://127.0.0.1:8000/api/token/ \
  -H 'Accept: */*' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Content-Length: 287' \
  -H 'Content-Type: multipart/form-data; boundary=--------------------------405235577793856926580986' \
  -H 'Host: 127.0.0.1:8000' \
  -H 'Postman-Token: 3b6c1c83-9556-494a-b509-5a74cc26f373,c0353083-b372-4fd3-9d03-d6141ab1561f' \
  -H 'User-Agent: PostmanRuntime/7.15.2' \
  -H 'cache-control: no-cache' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F username=kshitij \
  -F password=kshitij.in