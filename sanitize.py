import re

file = open("postfix.log","r")
new_file = open("postfix_sanitized.log","w")
# fields to change: to, from, msg_id

i = 0
    
to_val = "user{d}"
mail_reg = re.compile("\w+@\w+[.\w+]*")

emails = []
email_sub = []

for line in file:
    # print(line)
    
    x=re.findall(mail_reg,line)

    for id in x:
        if id not in emails:
            emails.append(id)
            id_new = id.split('@')            
            # print(id_new)
            email_sub.append(to_val.format(d=i)+'@'+id_new[1]) 
            i+=1
        
        x_ind = emails.index(id)
        # print(id)
        # print(x_ind)
        # print(email_sub[x_ind])
        
        line = line.replace(id, email_sub[x_ind])
    
    # print(x)
    # print(emails)
    # print(email_sub)
    # print(line)
    # print("---")
    new_file.write(line)

# print(emails)
# print(email_sub)

file.close()

