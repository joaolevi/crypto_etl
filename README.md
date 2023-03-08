# Crypto ETL (Extract Transform Load)

An ETL project to extract and transform data from https://coinmarketcap.com to up it in a database server

### Getting data from the CoinMarketCap through a request

![image](https://user-images.githubusercontent.com/56874672/223288676-0fbdaa3b-3ce4-42d0-91c3-c2c2eb6b0b81.png)

## Starting

### A local persistence on PostgreSQL

To verify if the dataframe is organized, I created a table in my local computer. Using a .yaml to configure which server I want the table needs to be created. I can pass these parameters on the `DBConfig.yaml` archive in the main directory:

```
'login':'postgres'
'password':'1234'
'ip':'localhost'
'port':'5432'
```

When I want to up some data in a AWS server, I can just modify these parameters and then it'll connect with them.

After a simple start, we can see at the WSL terminal `Table created on database` as we expected. To find the table in the `psql` we can just typing `TABLE tb_coins`:

![image](https://user-images.githubusercontent.com/56874672/223557536-2a1092a4-e9cd-47eb-9b8d-6be3d5871604.png)

The table was created in my local DB server.

### PostgreSQL Database on AWS

After create a Database named 'coins' on PostgreSQL on AWS:

![image](https://user-images.githubusercontent.com/56874672/223598125-4e781f33-6433-49eb-9ff6-0f8346ec72e2.png)

### Data Persistence

Finally, after run the `app.py`, the table was created on PostgreSQL on AWS server:

![image](https://user-images.githubusercontent.com/56874672/223860166-f5037354-80f3-4b66-ab04-178a8f65cf70.png)

And the Data was storaged successfully:

![image](https://user-images.githubusercontent.com/56874672/223859137-838c983b-7b7e-4f06-a273-83d868493319.png)



