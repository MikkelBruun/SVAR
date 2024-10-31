import matplotlib.pyplot as plt
#used for bar plots
plt.set_cmap("plasma")
def getBuckets(R: range):
    b = {}
    for i in sorted(R,reverse=True):
        b[i] = 0
    return b
def bucketsInsert(b:dict,i:int):
    for key in b:
        key = int(key)
        if(i > key):
            b[key] += 1
            break

def barPlot(b,filename="test",median=None):
    buckets=[]
    counts=[]
    for key in sorted(b):
        buckets.append(key)
        counts.append(int(b[key]))
    plt.bar(buckets,counts,width=5000,color=[plt.get_cmap()(i/len(buckets)) for i in range(len(buckets))])
    #plt.xticks(range(len(buckets)),labels=[x if i%2==0 else "" for i,x in enumerate(buckets)],rotation=80)
    if median is not None: 
        height = plt.gca().get_yticks()
        height = height[len(height)-1]
        plt.vlines([median],0,height)
    plt.tight_layout()
    
    plt.savefig(filename)
    