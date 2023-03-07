# Crypto ETL (Extract Transform Load)

An ETL project to extract and transform data from https://coinmarketcap.com to up it in a database server

### Getting data from the CoinMarketCap through a request

![image](https://user-images.githubusercontent.com/56874672/223288676-0fbdaa3b-3ce4-42d0-91c3-c2c2eb6b0b81.png)

## Starting

### A local PostgreSQL test

To verify if the dataframe is organized, I created a table in my local computer. Using a .yaml to configure which server I want the table needs to be created. I can pass these parameters on the `DBConfig.yaml` archive in the main directory:

```
login:'postgres'
password:'1234'
ip:'localhost'
port:'5432'
```

When I want to up some data in a AWS server, I can just modify these parameters and then it'll connect with them.

After a simple start, we can see at the WSL terminal `Table created on database` as we expected. To find the table in the `psql` we can just typing `TABLE tb_coins`:

![image](https://user-images.githubusercontent.com/56874672/223557536-2a1092a4-e9cd-47eb-9b8d-6be3d5871604.png)

The table was created in my local DB server.

