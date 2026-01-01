#ogogdsn jagsaaltin buh element urjwer bustaa

lst = [1,2,3,4,5,6]

def multiple(lst):
    result=1
    for l in lst:
        result *=l
    print(result)

    multiple(lst)

#ogogdson 2 jagsaaltin utguudaas dor hayj 1 element adilhn bwl unen
    lst1=[11,12,13]
    lst2=[14,15,16,13]

    def isTrue(l1,l2):
        result = 'False'
        for l in l1:
            for i in l2:
                if l==i:
                    result = 'True'
        print(result)

        isTrue(lst1,lst2)


#ogogdsn temdegt mor bln jagsaaltas hamgi ih toog butsa
    import re # regular exp
    src = 'f3uywfv3872ry782yrf83g8y3fg873848g87rgf'

    def maxDigit(src):
        foundNumber = re.findall('\d+',src)
        too = map(int,foundNumber)
        print(max(too))

        maxDigit(src)

#bodit toon jagsaaltig buhel bolon butarhai hesgig tus tusd n jagsalat bolgo
    src=[2.5,5.6,7.8,12.1]
    
    def buhelBaButarhai(src):
        buhel = []
        butarhai = []
        i=0
        while i<len(src):
            st = repr(src[i])
            buh,but = st.split('.')
            buhel.append(int(buh))
            butarhai.append(float('0.'+but))
            i=i+1
            print(butarhai)
            print(buhel)
            buhelBaButarhai(src)