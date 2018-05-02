#http://adventofcode.com/2015/day/19


molecule="CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr"

def nth_repl(s, sub, repl, nth):
    occ = s.find(sub)
    i = occ != -1
    while occ != -1 and i != nth:
        occ = s.find(sub, occ + 1)
        i += 1
    if i == nth:
        return s[:occ]+repl+s[occ + len(sub):]
    return s


with open('medicine.input', 'r') as f:
    st=f.read()
    repl={}
    for sor in st.splitlines():
        d=sor.split(' => ')
        v=[d[1]]
        repl.setdefault(d[0], []).append(d[1])
    print(repl)
    vm=set()
    
    c=0
    for k, v in repl.items():
        for n in v:
            c=molecule.count(k)
            kukac=molecule.replace(k, '@')
            while c > 0:
                km = nth_repl(kukac, '@', n, c)
                mm=km.replace('@', k)
                vm.add(mm)
                c-=1
    print(len(vm))
