# Test

To run the application.
1. Clone the code to the system
2. Enter into the folder 
3. To create docker image: docker compose up -d --build
4. To run the code command: docker compose up


Test command

curl --location --request POST 'localhost:8000/initialize_payment/' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=yXdXijgtjz3Usz2JhMpOMkVgIbMCBPQsTlCIBRxCZUeLKiNt5Q5y7z3tClo3LF0B' \
--data-raw '{
    "card_number": 4242424242424242, 
    "card_exp_month": "11", 
    "card_exp_year": 2021,  
    "card_cvv": "314",
    "card_name":"Kshitij"
}
