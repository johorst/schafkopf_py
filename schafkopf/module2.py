import random
import copy
alleKartenWerte={"s7":0.001, "s8":0.002, "s9":0.003, "hsU":2.001, "hsO":3.001, "sK":4, "s10":10, "sAS":11, "h7":0.001, "h8":0.002, "h9":0.003, "hU":2.002, "hO":3.002, "hK":4, "h10":10, "hAS":11, "g7":0.001, "g8":0.002, "g9":0.003, "hgU":2.003, "hgO":3.003, "gK":4, "g10":10, "gAS":11, "e7":0.001, "e8":0.002, "e9":0.003, "heU":2.004, "heO":3.004, "eK":4, "e10":10, "eAS":11}
kartenRangfolge=["heO", "hgO", "hO", "hsO", "heU", "hgU", "hU", "hsU", "hAS", "h10", "hK", "h9", "h8", "h7", "eAS", "e10", "eK", "e9", "e8", "e7", "gAS", "g10", "gK", "g9", "g8", "g7", "sAS", "s10", "sK", "s9", "s8", "s7"]
shuffledkeys=copy.builtins.list(alleKartenWerte.keys());
random.shuffle(shuffledkeys);

alleFarben=["schelln","herz","gras","eichel"];
alleSpieler=["erster","zweiter","dritter","vierter"];

class Kartenhand ():

    def sortiereKarten(self):
        for n in iter(self.alleKartenWerteDesSpielers):
            if n.startswith("s"):self.kartens.append(n);
            if n.startswith("h"):self.kartenh.append(n);
            if n.startswith("g"):self.karteng.append(n);
            if n.startswith("e"):self.kartene.append(n);

    def bekenneFarbe(self,f):
        if(f==alleFarben[0] and len(self.kartens)>0):
            return self.kartenc.pop();
        if(f==alleFarben[1] and len(self.kartenh)>0):
            return self.kartenh.pop();
        if(f==alleFarben[2] and len(self.karteng)>0):
            return self.kartenp.pop();
        if(f==alleFarben[3] and len(self.kartene)>0):
            return self.kartenk.pop();
        ##return waehleKarteElse();

    def waehleKarteElse(self):
        if (self.kartens.length()>0):
            return self.kartens.pop();
        if (self.kartenh.length()>0):
            return self.karteh.pop();
        if (self.karteng.length()>0):
            return self.karteng.pop();
        if (self.kartene.length()>0):
            return self.kartene.pop();
        raise Exception;

    def __init__(self,karten,besitzer0):
##        Super.__init__(self);
        self.alleKartenWerteDesSpielers=[];
        self.kartens=[];
        self.kartenh=[];
        self.karteng=[];
        self.kartene=[];
        self.besitzer="";
        self.alleKartenWerteDesSpielers = karten;
        self.sortiereKarten();
        self.besitzer = besitzer0;

    def toString(self):
        for i in iter(self.alleKartenWerteDesSpielers):
            print(i);

    def versuchWas(self):
        for i in iter(self.kartens):
             if (alleKartenWerte.get(i) > 10):
                    return i;
        return"h";

alleHaende=[];
i = 0;
alterspielerindex = 0;
maxtrumph = 0;
for n in iter(alleSpieler):
    alleKartenWerteDesSpielers = shuffledkeys[8*i:8*(i+1)];
    k1= Kartenhand(alleKartenWerteDesSpielers, n);
    alleHaende.append(k1);
  ##  print(k1.toString());
    print(len(k1.kartenh));
    print("Truemphe");
    if(len(k1.kartenh) > maxtrumph):
        maxtrumph = len(k1.kartenh);
        alterspielerindex=i;
    i = i+1;

print("erster stich:");
##todo: add logic (?)
aktuellerStich={};
karte1=alleHaende[alterspielerindex].bekenneFarbe(alleFarben[1])
typ1=alleSpieler[alterspielerindex]
print(karte1);
print(typ1);
karte2=alleHaende[(alterspielerindex+1) % 4].bekenneFarbe(alleFarben[1])
typ2=alleSpieler[(alterspielerindex+1) % 4]
print(karte2);
print(typ2);
karte3=alleHaende[(alterspielerindex+2) % 4].bekenneFarbe(alleFarben[1])
typ3=alleSpieler[(alterspielerindex+2) % 4]
print(karte3);
print(typ3);
karte4=alleHaende[(alterspielerindex+3) % 4].bekenneFarbe(alleFarben[1])
typ4=alleSpieler[(alterspielerindex+3) % 4]
print(karte4);
print(typ4);
aktuellerStich={typ1:karte1,typ2:karte2,typ3:karte3,typ4:karte4}
class Tisch ():

    def besteKarte(aktuellerStich):
        maxKarte="s7";
        stecher=0;
        wertstich=0;
        for i in iter(alleSpieler):
            wertstich+=alleKartenWerte.get(aktuellerStich.get(i));
            if(kartenRangfolge.index(maxKarte)>kartenRangfolge.index(aktuellerStich.get(i))):
                maxKarte=aktuellerStich.get(i);
                stecher=i;
        print(stecher, wertstich);
        return stecher;

stecher = Tisch.besteKarte(aktuellerStich);
amZug=alleSpieler.index(stecher);
aktuellerStich={};
print(alleHaende[amZug].versuchWas());

