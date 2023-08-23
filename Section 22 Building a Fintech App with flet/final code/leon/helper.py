
"""
{
    "users" : [
        {
            "email" : "odulaja@hotmail.com",
            "full name" : "odulaja philip",
            "password" : "password",
            "image_url" : "image",
            "balance" : 6789.90,
            "account no" : 9806 4759 9550 4566
            "transactions" : [
                {
                    amount : 890.09,
                    receiver/sender : "bank user",
                    time : datetime
                }
            ]
        }
    ],
   "account_numbers" : {
        "odulaja philip" : 9505 3456 4566 4667,
   } 
}
"""

def user_info(users, email):
    for user in users:
        if user["email"] == email:
            return user

def user_info_name(users, name):
     for user in users:
        if user["full_name"] == name:
            return user

def generate_initial(full_name):
        return full_name.split(" ")[0][0].title() + full_name.split(" ")[1][0].title()
