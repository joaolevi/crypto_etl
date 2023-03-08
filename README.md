# Crypto ETL (Extract Transform Load)

An ETL project to extract and transform data from https://coinmarketcap.com to up it in a database server

### Getting data from the CoinMarketCap through a request

![image](https://user-images.githubusercontent.com/56874672/223288676-0fbdaa3b-3ce4-42d0-91c3-c2c2eb6b0b81.png)

## Starting

Using a .yaml to configure which server I want the table needs to be created. I can pass these parameters on the `DBConfig.yaml` archive in the main directory:

```
'login':'postgres'
'password':'1234'
'ip':'localhost'
'port':'5432'
```

When I want to up some data in a AWS server, I can just modify these parameters and then it'll connect with them.

### PostgreSQL Database on AWS and Data persistence

Finally, after run the `app.py`, the table was created on PostgreSQL on AWS server:

![image](https://user-images.githubusercontent.com/56874672/223860166-f5037354-80f3-4b66-ab04-178a8f65cf70.png)

And the Data was storaged successfully:

![image](https://user-images.githubusercontent.com/56874672/223859137-838c983b-7b7e-4f06-a273-83d868493319.png)



