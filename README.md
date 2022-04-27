
# User Service

A user RESTFul API created in Flask. The Api currently has the functionality to get, create, update and delete user data.

Entities:

User:

    id: <int>
    first_name: <str>
    last_name: <str>
    emails: List<Email>
    phone_numbers: List<PhoneNumber>

Email:

    id: <int>
    mail: <str>
    
PhoneNumber:

    id: <int>
    number: <str>


## My Considerations

I am adding following consideration which explains some of my decision for this case study.

- **Consumer client**: I considered a `web` or `mobile` app as a consumer client which can perform the 
CRUD ( Create, Retrieve, Update and Delete) operations. The single endpoint `/users` provide a flexibility to 
update the data.

- **`snake_case` vs `camelCase`**: The response data is defined in a `snake_case` format which is preferred
by the python community. The included specification has the data in `camelCase`. 

- **Sqlite**: The project uses the Flash built-in sqlite database for the ease of simplicity. 
I am also open to the suggestions of using NoSQL databases for flexible data models, scaling and performance.

- **Validations**: The project a very basic email validations for the demonstration. There can be better validations done
by using well known packages and practices.


## Run Locally

Clone the project

```bash
  git clone https://github.com/saloni027/user-service.git
```

Go to the project directory

```bash
  cd userService
```

Install dependencies for a separate virtualenv

```bash
  pip nstall - r requirements.txt
```

Start the server

```bash
  python main.py
```


## API Reference

#### Get all users

```http
  GET /users
```
Get all users data including first_name, last_name, emails and phone_numbers.


#### Get item

```http
  GET /users/<id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. Id of the user  |


#### Find user by name

```http
  GET /users/<id>?name=<first_name>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. Id of the user  |
| `name`      | `str` | **Required**. First name of the user  |


#### POST /users

Add the user data to database.

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `first_name` | `str` | **Required**. First name of the User. |
| `last_name`  | `str` | **Required**. Last name of the User. |
| `emails`     | `list` | List of dictionaries containing key as mail and the value for mail.|
| `phone_numbers`| `list` | List of dictionaries containing key as number and the value for number. |

#### PUT /users

Modifies the user data to database.

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `first_name` | `str` | **Required**. First name of the User. |
| `last_name`  | `str` | **Required**. Last name of the User. |
| `emails`     | `list` | List of dictionaries containing key as mail and the value for mail.|
| `phone_numbers`| `list` | List of dictionaries containing key as number and the value for number. |

Updation of email and phone_numbers:

    For adding email, add the email dict(object) to the existing list of email dict(objects) along with the other data.

    For updating existing email, update in the existing email dict(obj) and also provide id of the email along with the rest of the data.

    For deleting an existing email, provide id of the email and a key value pair of "is_delete":"true" in the email dict object along with all other data.

    For adding phone_number, add the phone_number dict(object) to the existing list of phone_numbers dict(objects) along with the other data.

    For updating existing phone_number, update in the existing phone_number dict(obj) and also provide id of the phone_number along with the rest of the data.

    For deleting an existing phone_number, provide id of the phone_number and a key value pair of "is_delete":"true" in the phone_number- dict object along with all other data.


#### DELETE /users

Deletes the user with the given id.

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. Id of the user  |




## Usage/Examples

```
Get /users

Response:

[
    {
        "id": 1,
        "first_name": "saloni",
        "last_name": "sinha",
        "emails": [
            {
                "id": 1,
                "mail": "saloni@ex.com"
            
            }],
        "phone_numbers": [
            {
                "id": 1,
                "number": "7614247892"
            },
            {
                "id": 2,
                "number": "6534782345"
            }
        ]
    },
    {
        "id": 2,
        "first_name": "Jon",
        "last_name": "Doe",
        "emails": [
            {

                "id": 3,
                "mail": "jon@ex.com"

            },
            {
                "id": 4,
                "mail": "newjohn@ex.com"
            
            }
        ],
        "phone_numbers": [
            {
                "id": 3,
                "number": "2367289378"
            
            }
        ]
    }
    
]
```

```
Get /users/2

Response:

[
    {
        "id": 2,
        "first_name": "Jon",
        "last_name": "Doe",
        "emails": [
            {

                "id": 3,
                "mail": "jon@ex.com"

            },
            {
                "id": 4,
                "mail": "newjohn@ex.com"
            
            }
        ],
        "phone_numbers": [
            {
                "id": 3,
                "number": "2367289378"
            
            }
        ]
    }
]
```

```
Get /users?name=Jon

Response:

[
    {
        "id": 2,
        "first_name": "Jon",
        "last_name": "Doe",
        "emails": [
            {

                "id": 3,
                "mail": "jon@ex.com"

            },
            {
                "id": 4,
                "mail": "newjohn@ex.com"
            
            }
        ],
        "phone_numbers": [
            {
                "id": 3,
                "number": "2367289378"
            
            }
        ]
    }
]
```

```
POST /users

Request body:

    {
        
        "first_name": "Harry",
        "last_name": "Clinton"
        
        
    }

Response:

[
    {
        "id": 8,
        "first_name": "Harry",
        "last_name": "Clinton",
        "emails": [],
        "phone_numbers": []
    }
]
```

```
POST /users

Request body:

    {
        
        "first_name": "Harry",
        "last_name": "Clinton",
        "emails": [
            {
                "mail": "harry@ex.com"
            },
            {
                "mail": "clinton@ex.com"
            }
        ],
        "phone_numbers": [
            {
                "number": "2277739268"
            }
        ]
        
        
    }

Response:

[
    {
        "id": 9,
        "first_name": "Harry",
        "last_name": "Clinton",
        "emails": [
            {
                "id": 7,
                "mail": "harry@ex.com"
            },
            {
                "id": 8,
                "mail": "clinton@ex.com"
            }
        ],
        "phone_numbers": [
            {
                "id": 7,
                "number": "2277739268"
            }
        ]
    }
]
```

```
PUT /users/9

Change in first_name

Request body:

    {
        "id": 9,
        "first_name": "Hamy",
        "last_name": "Clinton",
        "emails": [
            {
                "id": 7,
                "mail": "harry@ex.com"
            },
            {
                "id": 8,
                "mail": "clinton@ex.com"
            }
        ],
        "phone_numbers": [
            {
                "id": 7,
                "number": "2277739268"
            }
        ]
    }


Response:

[
    {
        "id": 9,
        "first_name": "Hamy",
        "last_name": "Clinton",
        "emails": [
            {
                "id": 7,
                "mail": "harry@ex.com"
            },
            {
                "id": 8,
                "mail": "clinton@ex.com"
            }
        ],
        "phone_numbers": [
            {
                "id": 7,
                "number": "2277739268"
            }
        ]
    }
]
```

```

PUT /users/9

Add email

Request body:

    {
        "id": 9,
        "first_name": "Hamy",
        "last_name": "Clinton",
        "emails": [
            {
                "id": 7,
                "mail": "harry@ex.com"
            },
            {
                "id": 8,
                "mail": "clinton@ex.com"
            },
            {
                "mail": "Hamy@ex.com"
            }
        ],
        "phone_numbers": [
            {
                "id": 7,
                "number": "2277739268"
            }
        ]
    }


Response:

[
    {
        "id": 9,
        "first_name": "Hamy",
        "last_name": "Clinton",
        "emails": [
            {
                "id": 7,
                "mail": "harry@ex.com"
            },
            {
                "id": 8,
                "mail": "clinton@ex.com"
            },
            {
                "id": 9,
                "mail": "Hamy@ex.com"
            }
        ],
        "phone_numbers": [
            {
                "id": 7,
                "number": "2277739268"
            }
        ]
    }
]
```

```
PUT /users/9

Modify existing email

Request body:

    {
        "id": 9,
        "first_name": "Hamy",
        "last_name": "Clinton",
        "emails": [
            {
                "id": 7,
                "mail": "harry@ex.com"
            },
            {
                "id": 8,
                "mail": "clintonharry@ex.com"
            },
            {
                "id": 9,
                "mail": "Hamy@ex.com"
            }
        ],
        "phone_numbers": [
            {
                "id": 7,
                "number": "2277739268"
            }
        ]
    }


Response:

[
    {
        "id": 9,
        "first_name": "Hamy",
        "last_name": "Clinton",
        "emails": [
            {
                "id": 7,
                "mail": "harry@ex.com"
            },
            {
                "id": 8,
                "mail": "clintonharry@ex.com"
            },
            {
                "id": 9,
                "mail": "Hamy@ex.com"
            }
        ],
        "phone_numbers": [
            {
                "id": 7,
                "number": "2277739268"
            }
        ]
    }
]
```

```
PUT /users/9

Remove email

Request body:

    {
        "id": 9,
        "first_name": "Hamy",
        "last_name": "Clinton",
        "emails": [
            {
                "id": 7,
                "mail": "harry@ex.com"
            },
            {
                "id": 8,
                "mail": "clintonharry@ex.com"
            },
            {
                "id": 9,
                "mail": "Hamy@ex.com",
                "is_delete": "true"
            }
        ],
        "phone_numbers": [
            {
                "id": 7,
                "number": "2277739268"
            }
        ]
    }


Response:

[
    {
        "id": 9,
        "first_name": "Hamy",
        "last_name": "Clinton",
        "emails": [
            {
                "id": 7,
                "mail": "harry@ex.com"
            },
            {
                "id": 8,
                "mail": "clintonharry@ex.com"
            }
        ],
        "phone_numbers": [
            {
                "id": 7,
                "number": "2277739268"
            }
        ]
    }
]

Note: Dont include the removed data for further Request.
```

```
PUT /users/9

Add phone_number

Request body:

    {
        "id": 9,
        "first_name": "Hamy",
        "last_name": "Clinton",
        "emails": [
            {
                "id": 7,
                "mail": "harry@ex.com"
            },
            {
                "id": 8,
                "mail": "clintonharry@ex.com"
            },
            
        ],
        "phone_numbers": [
            {
                "id": 7,
                "number": "2277739268"
            },
            {
                
                "number": "2435762893"
            }
        ]
    }


Response:

[
    {
        "id": 9,
        "first_name": "Hamy",
        "last_name": "Clinton",
        "emails": [
            {
                "id": 7,
                "mail": "harry@ex.com"
            },
            {
                "id": 8,
                "mail": "clintonharry@ex.com"
            }
        ],
        "phone_numbers": [
            {
                "id": 7,
                "number": "2277739268"
            },
            {
                "id": 8,
                "number": "2435762893"
            }
        ]
    }
]
```

```
PUT /users/9

Modify existing phone_number

Request body:

    {
        "id": 9,
        "first_name": "Hamy",
        "last_name": "Clinton",
        "emails": [
            {
                "id": 7,
                "mail": "harry@ex.com"
            },
            {
                "id": 8,
                "mail": "clintonharry@ex.com"
            }
            
        ],
        "phone_numbers": [
            {
                "id": 7,
                "number": "3628947"
            },
            {
                "id": 8,
                "number": "2435762893"
            }
        ]
    }


Response:

[
    {
        "id": 9,
        "first_name": "Hamy",
        "last_name": "Clinton",
        "emails": [
            {
                "id": 7,
                "mail": "harry@ex.com"
            },
            {
                "id": 8,
                "mail": "clintonharry@ex.com"
            }
        ],
        "phone_numbers": [
            {
                "id": 7,
                "number": "3628947"
            },
            {
                "id": 8,
                "number": "2435762893"
            }
        ]
    }
]
```

```
PUT /users/9

Delete a phone_number

Request body:

    {
        "id": 9,
        "first_name": "Hamy",
        "last_name": "Clinton",
        "emails": [
            {
                "id": 7,
                "mail": "harry@ex.com"
            },
            {
                "id": 8,
                "mail": "clintonharry@ex.com"
            }
            
        ],
        "phone_numbers": [
            {
                "id": 7,
                "number": "3628947"
            },
            {
                "id": 8,
                "number": "2435762893",
                "is_delete": "true"
            }
        ]
    }


Response:

[
    {
        "id": 9,
        "first_name": "Hamy",
        "last_name": "Clinton",
        "emails": [
            {
                "id": 7,
                "mail": "harry@ex.com"
            },
            {
                "id": 8,
                "mail": "clintonharry@ex.com"
            }
        ],
        "phone_numbers": [
            {
                "id": 7,
                "number": "3628947"
            }
        ]
    }
]

Note: Dont include the removed data in any further request.
```

```

DELETE /users/9

Delete user

Response:

[
    {
        "message": "User deleted Successfully"
    }
]

```



## Using Docker

Build docker image:
```
docker build -t user-service .   
```

Using compose
```
docker-compose up   
```


