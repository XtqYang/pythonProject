from scapy.all import *


# count:抓取报的数量，设置为0时则一直捕获
# store:保存抓取的数据包或者丢弃，1保存，0丢弃
# offline:从pcap文件中读取数据包，而不进行嗅探，默认为None
# prn:为每个数据包定义一个回调函数，通常使用lambda表达式来写回调函数
# filter:过滤规则，可以在里面定义winreshark里面的过滤语法，使用 Berkeley Packet Filter (BPF)语法，具体参考：[http://blog.csdn.net/qwertyupoiuytr/article/details/54670477](http://blog.csdn.net/qwertyupoiuytr/article/details/54670477)
# L2socket:使用给定的L2socket
# timeout:在给定的事件后停止嗅探，默认为None
# opened_socket:对指定的对象使用.recv进行读取
# stop_filter:定义一个函数，决定在抓到指定的数据之后停止
# iface:指定抓包的网卡,不指定则代表所有网卡

def handelPacket(p):  # p捕获到的数据包
    p.show()


filter_f = {
    "port 80"
}

sniff(count=0,
      store=1,
      offline=None,
      prn=handelPacket,
      filter=filter_f,
      L2socket=None,
      timeout=None,
      opened_socket=None,
      stop_filter=None,
      iface=None
      )
