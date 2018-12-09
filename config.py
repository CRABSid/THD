import os,time,sys
from os import remove

z='\033[91m'
x='\033[0m'
w='\033[97m'

def bn():
      
      
      
###################
# isi file bash
###################


      bsh="""
command_not_found_handle() {
        /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
}
alias config='python THD/config.py'
python .banner.py
echo
PS1='\e[1;94m\w\e[0m\n# \e[92m'
"""
      bsf= open('bash.bashrc','w')
      bsf.write(bsh)
      bsf.close()
      os.system('mv bash.bashrc /data/data/com.termux/files/usr/etc')
      
      
      
#####################
# isi file banner
####################
      b ='''
import sys,time,os
x="'''+wr2+'''"
lr="'''+wr1+'''"

def wl():
      os.system('clear')
      bannerup = "╔════════════════════════════════╗".center(40)
      bnup = "   ║                                ║"
      bndn = "   ║           INDONESIA            ║"
      bann = "║   ██████████████████████████   ║"
      bann_= "║      "+x+"CRACKER NOOB SQUADS"+lr+"       ║"
      bann__="║   ██████████████████████████   ║"
      bannerdn = "╚════════════════════════════════╝".center(40)
      keterangan= ">'''+nam+'''<".center(40)
      for i in bannerup:
            print (lr+i, end=''),;sys.stdout.flush();time.sleep(0.01)
      print ('')
      print (lr+bnup)
      print (lr+bann.center(40)),;time.sleep(0.02)
      print (lr+bann_.center(50)),;time.sleep(0.02)
      print (lr+bann__.center(40)),;time.sleep(0.02)
      print (lr+bndn)
      for i in bannerdn:
            print (lr+i, end=''),;sys.stdout.flush();time.sleep(0.01)
      print ('')
      for i in keterangan:
            print (x+i, end=''),;sys.stdout.flush();time.sleep(0.01)
      print ("")
      print (lr+'++++++++++++++++++++++++++++++++++++++++')
if __name__=='__main__':
      wl()

'''
      bnrr = open('.banner.py','w')
      bnrr.write(b)
      bnrr.close()
      os.system('mv .banner.py $HOME')
      
      
      
      
      
      
#################
# isi dile kontol
#################

      for vvq in range(7):
            for i in s:
                  print (w+'\r[+]'+z+' Tunggu cook !! masih proses '+z,i+z, end=''),;sys.stdout.flush();time.sleep(0.1)
      os.system('clear')
      print (w+'Udah selesai ea djmbod..\nuntuk ngganti ketik "config" di terminal.\nTutup termux dan buka lagi/New session\nbuat nampilin hasilnya.\nEmmuuaacchhh !!!')
      for kis in range (3):
            print(w+':'+z+'* '+x, end=''),sys.stdout.flush();time.sleep(0.2)
      print('')


if __name__=='__main__':
      os.system('clear')
      wr1=""
      wr2=""
      lswr=['\033[91m','\033[92m','\033[93m','\033[94m','\033[95m','\033[96m','\033[97m']
      
#      s = ["[ =>     ] ","[  =>    ] ","[   =>   ] ","[     => ] ","[     <= ] ","[    <=  ] ","[   <=   ] ","[  <=    ] ","[ <=     ] "]
#      s = [">    O "," >   O ","  >  O ","   > O ","    >O ","     X ","     x ","     + "]
      s = [x+"o"+z+"______ ","_"+x+"o"+z+"_____ ","__"+x+"o"+z+"____ ","___"+x+"o"+z+"___ ","____"+x+"o"+z+"__ ","_____"+x+"o"+z+"_ ","______"+x+"o "+z,"_____"+x+"o"+z+"_ ","____"+x+"o"+z+"__ ","___"+x+"o"+z+"___ ","__"+x+"o"+z+"____ ","_"+x+"o"+z+"_____ "]
#      d = "/|\-/|\-"
#      s = [w+"L"+x+"OADING","L"+w+"O"+x+"ADING","LO"+w+"A"+x+"DING","LOA"+w+"D"+x+"ING","LOAD"+w+"I"+x+"NG","LOADI"+w+"N"+x+"G","LOADIN"+w+"G"+x,"LOADI"+w+"N"+x+"G","LOAD"+z+"I"+x+"NG","LOA"+z+"D"+x+"ING","LO"+z+"A"+x+"DING","L"+z+"O"+x+"ADING"]
      print (z+'TERMUX HOME DECORATOR'.center(40))
      print (w+("+"*30).center(40))

      print (z+'SELAMAT DATANG NOOB !! :"v'.center(40))
      print (w+"""
Ini cuma anu, script ampash buat ngasi
hiasan di termux, tapi ya jelek,
tapi nggak ribet. tapi kan gw mbikin sendiri.
tapikan nggak recode,
tapi kita kan CRABS :'V
oya, kalo lu bukan CRABS,
gaskeun aja ke https://t.me/CRABS_ID
kalo nggak suka, gelud kita :"""+z+"""*"""+w+"""
btw jangan ngacengan ea >"""+z+""":"""+w+"""(""")
      nam=input(w+"\n\n[+]"+z+" Masukkin nama mantan, kata-kata mutiara,\n    nama temen yg kek kontil, dll:\n    >> "+w).upper()
      wrn = input(w+'''
[+]'''+z+''' Pilih kombinasi warna:
    1. '''+lswr[0]+'''██'''+lswr[6]+'''██'''+z+'''   4. '''+lswr[3]+'''██'''+lswr[6]+'''██'''+z+'''   7. '''+lswr[1]+'''██'''+lswr[3]+'''██'''+z+'''
    2. '''+lswr[1]+'''██'''+lswr[0]+'''██'''+z+'''   5. '''+lswr[0]+'''██'''+lswr[5]+'''██'''+z+'''
    3. '''+lswr[2]+'''██'''+lswr[3]+'''██'''+z+'''   6. '''+lswr[5]+'''██'''+lswr[4]+'''██'''+z+'''
  
    >> '''+w)
                                                    
      if wrn=='1':
            wr1=lswr[0]
            wr2=lswr[6]
      elif wrn=='2':
            wr1=lswr[1]
            wr2=lswr[0]
      elif wrn=='3':
            wr1=lswr[2]
            wr2=lswr[3]
      elif wrn=='4':
            wr1=lswr[3]
            wr2=lswr[6]
      elif wrn=='5':
            wr1=lswr[0]
            wr2=lswr[5]
      elif wrn=='6':
            wr1=lswr[5]
            wr2=lswr[4]
      elif wrn=='7':
            wr1=lswr[1]
            wr2=lswr[3]
      else:
            wr1='\033[97m'
            wr2='\033[97m'


      bn()
           
