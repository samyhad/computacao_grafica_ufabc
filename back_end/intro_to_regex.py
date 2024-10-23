
import re
p = re.compile('[a-z]+')
print(p.match("larissa"))

# Validador de ângulo
p =  re.compile('^(360|(3[0-5][0-9]|2[0-9][0-9]|1[0-9][0-9]|[1-9]?[0-9]),[0-9])$')
print(p.match("560"))
print(p.match("361"))
print(p.match("360,2"))
print(p.match("359,9"))
print(p.match("299,8"))
print(p.match("250,8"))
print(p.match("199,7"))
print(p.match("100,7"))
print(p.match("99,6"))
print(p.match("25,6"))
print(p.match("3,1"))
print(p.match("0,1"))

# Validador do protocolo
import re

#	exemplo do protocolo gerado pelo time de engenharia:
#	#p:256,8;s:on;l:off

protocolo = input("Entre com o protocolo:")

x = re.search("^#p:^(360|(3[0-5][0-9]|2[0-9][0-9]|1[0-9][0-9]|[1-9]?[0-9]),[0-9]);s:(on|off);l:(on|off)", protocolo)
print(x)