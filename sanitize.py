import re

file = open("postfix.log","r")
new_file = open("postfix_sanitized.log","w")
# fields to change: to, from, msg_id

i = 0
    
to_val = "user{d}"
mail_reg = re.compile("\w+@\w+[.\w+]*")

emails = []
users = []
users_sub = []

for line in file:
    # print(line)
    
    x=re.findall(mail_reg,line)

    for id in x:
        uname = id.split('@')[0] 
        if uname not in users:
            # emails.append(id)
            users.append(uname)      
            users_sub.append(to_val.format(d=i)) 
            i+=1
    
    for user in users: 
        x_ind = users.index(user)
        # print(id)
        # print(x_ind)
        # print(email_sub[x_ind])
        
        line = line.replace(user, users_sub[x_ind])
    
    # print(x)
    # print(emails)
    # print(email_sub)
    # print(line)
    # print("---")
    new_file.write(line)

print(emails)
print(users)
print(users_sub)

file.close()

