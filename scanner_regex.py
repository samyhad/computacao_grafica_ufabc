import re

#	exemplo do protocolo gerado pelo time de engenharia:
#	#p:256,8;s:on;l:off

protocolo = input("Entre com o protocolo:")

x = re.search("^#p:[0-9],[0-9];s:(on|off);l:(on|off)", protocolo)
print(x)
