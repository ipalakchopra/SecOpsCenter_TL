import re

file = open("postfix_sanitized.log","r")
new_file = open("postfix_sanitized_domain.log","w")
# fields to change: to, from, msg_id

i = 0
    
to_val = "domain{d}.com"
mail_reg = re.compile("\w+@\w+[.\w+]*")

domains = []
domains_sub = []

for line in file:
    # print(line)
    x=re.findall(mail_reg,line)

    for id in x:
        domain = id.split('@')[1]
        if domain not in domains:
            domains.append(domain)
            id_new = id.split('@')            
            domains_sub.append(to_val.format(d=i)) 
            i+=1
        
        x_ind = domains.index(domain)
        
        line = line.replace(id, id.split('@')[0]+'@'+domains_sub[x_ind])
    

    new_file.write(line)

print(domains)
print(domains_sub)

file.close()

