# -*- coding: utf8


import threading
import requests


class Worker(threading.Thread):
    def __init__(self, id_, **kwargs):
        super(Worker, self).__init__(**kwargs)
        self.__path = 'http://www.gutenberg.org/files/{}/{}-0.txt'.format(id_, id_)
        self.__linha = 0
        
    def run(self):
        arq = requests.get(self.__path)
        for linha in arq.text.splitlines():
            self.__linha +=1
    
    def get_result(self):
        return self.__linha

def crawler(num_threads):

    linhas_totais = 0
    ids = [1342,11,1661,2701,25525,1952,1727,1080,98,84,2600,74,2591,28054,62610,1184]    
    while sorted([num_threads, len(ids)])[0]:
        threads = []
        for n in range(sorted([num_threads, len(ids)])[0]):
            threads.append(Worker(ids[n]))
            
        ids = ids[n+1:]
        
        for i in range(len(threads)): threads[i].start()
        for i in range(len(threads)): threads[i].join()
        
        linhas_totais+=sum([x.get_result() for x in threads])
    return linhas_totais