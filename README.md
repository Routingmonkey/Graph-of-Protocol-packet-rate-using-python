# Graph-of-Protocol-packet-rate-using-python
Interactive Graph is plotted using python script form the packet rate captured using below command.
“show ddos-protection protocols statistics terse”

If you hover over plotted graph you will be able to see the exact packet count and time stamp.
Select the protocol from the left hand side to plot the graph.
You can further tweak the logic in the script to plot dropped packet or any other values against time.

open .svg file in any browser to view the graph and if you wanted to modify the script or regular expression from textfsm file

Below is sample output captured with the help of other polling script.
Complete captured log file size is very large so this graph will provide meaningful complete view about packet rate

Fri May  7 14:13:23 UTC 2021
============Start of iteration===================
================DDOS CLI commands================
####show ddos-protection protocols statistics terse####
Packet types: 226, Received traffic: 32, Currently violated: 0
Protocol    Packet      Received        Dropped        Rate     Violation State
group       type        (packets)       (packets)      (pps)    counts
resolve     aggregate   24              0              0        0         ok  
resolve     ucast-v6    24              0              0        0         ok  
icmp        aggregate   3587423         0              5        0         ok  
ospf        aggregate   42943271        0              12       0         ok  
rsvp        aggregate   6083027         0              2        0         ok  
ldp         aggregate   25881484        0              16       0         ok  
bgp         aggregate   70810876        0              36       0         ok  
ssh         aggregate   40960821        0              8        0         ok  
snmp        aggregate   129760723       0              2        0         ok  
bgpv6       aggregate   20011754        0              9        0         ok  
lacp        aggregate   187454039       0              62       0         ok  
arp         aggregate   347573631       0              107      0         ok  
pvstp       aggregate   1461277         0              0        0         ok  
ttl         aggregate   220783021       0              91       0         ok  
ip-opt      aggregate   760             0              0        0         ok  
ip-opt      unclass..   760             0              0        0         ok  
exception   aggregate   106             0              0        0         ok  
exception   mtu-exceed  106             0              0        0         ok  
reject      aggregate   9               0              0        0         ok  
tcp-flags   aggregate   95977615        0              30       0         ok  
tcp-flags   initial     15              0              0        0         ok  
tcp-flags   establish   95977600        0              30       0         ok  
ntp         aggregate   8615            0              0        0         ok  
tacacs      aggregate   11984031        0              1        0         ok  
dns         aggregate   4               0              0        0         ok  
icmpv6      aggregate   698421          0              0        0         ok  
ndpv6       aggregate   2540135         0              0        0         ok  
ndpv6       neighb-sol  1780436         0              0        0         ok  
ndpv6       neighb-adv  759699          0              0        0         ok  
uncls       aggregate   2042            0              0        0         ok  
uncls       host-rt-v4  2042            0              0        0         ok  
rejectv6    aggregate   304876          0              0        0         ok  

 
Fri May  7 14:13:41 UTC 2021
============Start of iteration===================
================DDOS CLI commands================
####show ddos-protection protocols statistics terse####
Packet types: 226, Received traffic: 32, Currently violated: 0
Protocol    Packet      Received        Dropped        Rate     Violation State
group       type        (packets)       (packets)      (pps)    counts
resolve     aggregate   24              0              0        0         ok  
resolve     ucast-v6    24              0              0        0         ok  
icmp        aggregate   3587462         0              1        0         ok  
ospf        aggregate   42943528        0              12       0         ok  
rsvp        aggregate   6083068         0              1        0         ok  
ldp         aggregate   25881678        0              16       0         ok  
bgp         aggregate   70811389        0              21       0         ok  
ssh         aggregate   40961032        0              6        0         ok  
snmp        aggregate   129761995       0              1        0         ok  
bgpv6       aggregate   20011895        0              6        0         ok  
lacp        aggregate   187455319       0              62       0         ok  
arp         aggregate   347575703       0              107      0         ok  
pvstp       aggregate   1461287         0              0        0         ok  
ttl         aggregate   220784755       0              86       0         ok  
ip-opt      aggregate   760             0              0        0         ok  
ip-opt      unclass..   760             0              0        0         ok  
exception   aggregate   106             0              0        0         ok  
exception   mtu-exceed  106             0              0        0         ok  
reject      aggregate   9               0              0        0         ok  
tcp-flags   aggregate   95978285        0              32       0         ok 
tcp-flags   initial     15              0              0        0         ok  
tcp-flags   establish   95978270        0              31       0         ok  
ntp         aggregate   8615            0              0        0         ok  
tacacs      aggregate   11984067        0              1        0         ok  
dns         aggregate   4               0              0        0         ok  
icmpv6      aggregate   698421          0              0        0         ok  
ndpv6       aggregate   2540153         0              1        0         ok  
ndpv6       neighb-sol  1780451         0              1        0         ok  
ndpv6       neighb-adv  759702          0              0        0         ok  
uncls       aggregate   2042            0              0        0         ok  
uncls       host-rt-v4  2042            0              0        0         ok  
rejectv6    aggregate   304876          0              0        0         ok   
