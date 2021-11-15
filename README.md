# json

requirements

python -m pip install phone_gen transliterate 

microservice will serve as http service at port 8000 and will respond with random life-like data, encoded as utf-16 e..g


{
    "name": "Пелагея",
    
    "surname": "Корнева",
    
    "phone_full": "+74152556199",
    
    "email": "requirementspelageja06070@outlook.com",
    
    "password": "aae*cr7G58k",
    
    "phrase": "По поводу последней ссылки",
    
    "phrase2": "вывод средств"   
}



Docker:

docker pull ghcr.io/stopfraud/json:main


docker run -it --rm ghcr.io/stopfraud/json:main
