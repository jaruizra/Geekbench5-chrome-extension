class tests:
    def __init__(self, test):
        d = test
        self.d_m = d["metrics"]
        self.frequency = d["processor_frequency"]["frequencies"]
        self.max_freq = max(self.frequency)
        self.min_freq = min(self.frequency)
        self.av_freq = sum(self.frequency)/len(self.frequency)
        self.all_freq = self.frequency
        self.prime_min_freq = int(self.find_data("Processor Frequency")["ivalue"])/1000000000
        self.prime_max_freq = self.prime_max_freq()
                
    def create_freq_str(self):
        freq_list = self.frequency
        max = self.max_freq
        min = self.min_freq
        table = []
        for i in freq_list:
            porcent = (i - min) / (max - min) * 100
            nueva_linea = '<div class="bar2" style="height: {}%"></div>'.format(porcent)
            table.append(nueva_linea)
        table_str = ''.join(table)
        return table_str
    
    def find_data(self, var_name):
        name = var_name
        exit = False
        index = 0
        while not exit:
            print(self.d_m[index])
            if self.d_m[index]["name"] == name:
                data = self.d_m[index]
                exit = True
                return data
            else:
                index += 1
        
    def prime_max_freq(self):
        o = self.find_data("Cluster Count")
        n = int(o["value"])
        cluster = "Cluster " + str(n) + " Maximum Frequency"
        d = self.find_data(cluster)
        max = int(d["ivalue"])/1000000000
        return max
        