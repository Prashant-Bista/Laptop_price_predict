from sklearn.base import TransformerMixin, BaseEstimator
class Transformer(TransformerMixin,BaseEstimator):
    def __init__(self):
        self.wt=[]
        self.ram=[]
        self.x_res=[]
        self.y_res=[]
        self.all_res=[]
        self.scrn_type=[]
        self.cpu_freq=[]
        self.cpu_type=[]
    def fit(self,dataset,y=None):
        self.dataset=dataset
        for i in list(dataset.columns):
            X=dataset[i]
            if i=='Weight':
                for j in X:
                    self.wt.append(float(j.split("kg")[0]))
           
        
        
            elif i=="Ram":
                for j in X:
                    self.ram.append(int(j.split("GB")[0]))
            
            
    
            elif i=="ScreenResolution":
                most_freq=X.value_counts().keys()[0]
                for j in X.values:
                    temp=re.search(r"(\d{3,4}x\d{3,4})",j).group()
                    temp2=j.split(temp)
                    temp=temp.split('x')
                    if temp2[0]=='':
                        self.scrn_type.append(most_freq)
                        self.x_res.append(int(temp[0]))
                        self.y_res.append(int(temp[1]))
                        self.all_res.append([most_freq,int(temp[0]),int(temp[1])])
                    else:
                        self.scrn_type.append(temp2[0])
                        self.x_res.append(int(temp[0]))
                        self.y_res.append(int(temp[1]))
                        self.all_res.append([temp2[0],int(temp[0]),int(temp[1])])
            
            elif i=="Cpu":
                for j in X.values:
                    temp=re.search(r'(\d{1}.\d{0,2}GHz)',j)
                    if temp:
                        temp0=re.split(r'(\d{1}.\d{0,2}GHz)',j)[0]
                        temp=temp.group().split('GHz')[0]
                        if re.search(r'(\d \d)',temp):
                            temp=temp.split(" ")[1]
                            self.cpu_freq.append(float(temp))
                        else:
                            self.cpu_freq.append(float(temp))
                
                        self.cpu_type.append(temp0)
                    else:
                        temp0=re.split(r'(\d{1}GHz)',j)[0]
                        temp=re.search(r'(\d{1}GHz)',j).group().split('GHz')[0]
                        self.cpu_freq.append(float(temp))
                        self.cpu_type.append(temp0)
            elif i not in ["Ram",'Cpu',"Weight","ScreenResolution","Price_euros","Inches"]:
                self.dataset[i]=X.replace(to_replace=X.unique(),value=range(len(X.unique()))) 
        return self
    def transform(self,X):
        self.dataset.drop("Ram",axis=1,inplace=True)
        self.dataset["Ram(GB)"]=self.ram
        self.dataset.drop("Cpu",axis=1,inplace=True)
        self.dataset["Cpu_freq(GHz)"]=self.cpu_freq
        self.dataset["Cpu_type"]=self.cpu_type
        self.dataset["X_Res"]=self.x_res
        self.dataset["Y_Res"]=self.y_res
        self.dataset["Screen_type"]=self.scrn_type
        self.dataset.drop("ScreenResolution",axis=1,inplace=True)
        self.dataset["Screen_type"]   = self.dataset["Screen_type"].replace(to_replace= self.dataset["Screen_type"] .unique(),value=range(len( self.dataset["Screen_type"] .unique())))
        self.dataset["Cpu_type"]   = self.dataset["Cpu_type"].replace(to_replace= self.dataset["Cpu_type"] .unique(),value=range(len( self.dataset["Cpu_type"] .unique())))

        return self.dataset
       

    
            
