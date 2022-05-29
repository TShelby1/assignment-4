
import requests







URL = "http://127.0.0.1:5000/users/"


USER_TEMPLATE = {
    "id":"0",
    "first_name":"John",
    "last_name":"Doe",
    "hobbies":"Chillen like a villain"
}
user_data = USER_TEMPLATE


# trying to get the user first, then update the user



def get_user(pk):
    url = "%s/%s" % (URL, pk)
    response = requests.get(url)
    my_response = response.json()
    return my_response
    

def update_user(pk, first_name, last_name, hobbies):
    user_data = USER_TEMPLATE
    url = "%s/%s" % (URL, pk)
    user_data.get["first_name"] = first_name
    user_data.get["last_name"] = last_name
    user_data.get["hobbies"] = hobbies
    response = requests.put(url, json=user_data)
    if response.status_code == 204:
        print("Updating user")
    else:
        print("Something went wrong")




if __name__ == "__main__":
    user_id = input("User ID: ")
    user = get_user(user_id)
    print('UPDATE USER', user)
    print("----------")
    fname = input("First Name: ")
    lname = input("Last Name: ")
    hobbies = input ("Hobbies: ")
    update_user(fname, lname, hobbies)
