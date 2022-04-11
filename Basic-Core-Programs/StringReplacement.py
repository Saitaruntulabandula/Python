'''
@Author: Sai Tarun
@Date: 2022-04-03 15: 00: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-03 15: 06: 00
@Title: String Replacement
'''
def string_replace_fun():
    """
        Description:
            Function is used to replace the string.
        Parameter:
            Not passed any parameter. 
        Return:
            Returns nothing but prints the replaced string with the subject
    """
    subject = "Hello <<UserName>>,How are you?"
    user_input=input("Enter the User Name:")
    if len(user_input)<3:
        print("Please enter the user name with more than 3 characters:")
        string_replace_fun()
    else:
        modified_subject=subject.replace("<<UserName>>",user_input)
        print(modified_subject)

string_replace_fun()