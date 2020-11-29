# Rest API service

**REST** is acronym for REpresentational State Transfer. It is an architectural style, and an approach to communications that is often used in the development of Web services.

**REST** web services are a way of providing interoperability between computer systems on the Internet. REST-compliant Web services allow requesting systems to access and manipulate textual representations of Web resources using a uniform and predefined set of stateless operations.

## Installation

Install al the dependencies of the project by running the following comand:

```shell
pip3 install -r requirements.txt
```

Activate the virtual enviroment:

```shell
source env/bin/activate
```

Go to the src folder and run the application:

```shell
python3 run.py
```



## Tables

### Users

```sql
CREATE TABLE users (
	id integer NOT NULL PRIMARY KEY,
	firstname varchar(60) NOT NULL,
	lastname varchar(60),
	username varchar(30) NOT NULL,
	password varchar(30) NOT NULL,
	emailaddress varchar(200) NOT NULL,
	api_key varchar(200),
	CONSTRAINT username_unique UNIQUE (username),
	CONSTRAINT emailaddress_unique UNIQUE (emailaddress)
);
```



