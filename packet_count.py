import textfsm
import datetime
import time
import pygal
from datetime import time
dateline = pygal.TimeLine(title="Received packets",x_label_rotation=25, width=1500, height=850, explicit_size=True)#, style=custom_style)

input_file = open("sample_data.txt")
raw_text_data = input_file.read()
input_file.close()

template = open("packet_count.textfsm")
re_table = textfsm.TextFSM(template)
fsm_results = re_table.ParseText(raw_text_data)
fsm_results.pop()

new_fsm_result = []

proto_grp = []
log_data = []

for x in fsm_results:
    j = x[1] + x[2]
    x[1] = j
    x.remove(x[2])
    
for y in fsm_results:
    if y[1] not in proto_grp:    
        proto_grp.append(y[1])
print proto_grp


for z in proto_grp:
    for i in fsm_results:
        if z in i:
                j = i[0]
                k = j.split(':')
                l = time(int(k[0]),int(k[1]),int(k[2]))
                log_data.append((l,int(i[4])))
    dateline.add(z, log_data)
    log_data = []

dateline.render_to_file('all_proto_RXPKT.svg')
