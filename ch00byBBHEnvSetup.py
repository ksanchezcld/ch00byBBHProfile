#!/usr/bin/env python3
#_*_ coding: utf8 _*_

import os, subprocess, sys, getpass, time, smtplib, argparse, json, platform

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

########################
# WORDLISTS DEFINITION #
#######################

wordlist = 'wordlists/dirb_common.txt',
 
if platform.system == 'Linux':
    if os.getuid() != 0:
        print('\n' + R + '[-]' + C + ' Please run as Root' + '\n')
    else:
        pass
else:
    pass

#os.system(screen)                   # to keep the sesion open
#os.system(ttyrec)                   # to record the session
parent_dir = "/tmp/BBH/"             #Eliminar  :: parent_dir = "/mnt/bbh_home/tools/BBH"
directory = "MALWARE"                #Eliminar

# Welcome to the Bug Hunter Automation System

#def bugHunterProfile():

def versionCheck():
        print(G + '[+]' + C + ' Checking for Updates...', end='')
        versionUrl = 'https://raw.githubusercontent.com/ksanchezcld/MYOWNSCRIPTS/master/BBH_PROJECT-C-VID2020/version.txt?token=AAX4JZ7SNL3JC26U7QP7LDS62WHFU'
        try:
            vReq = requests.get(versionUrl, timeout=5)
            vScode = vReq.status_code
            if vScode == 200:
                gitVer = vReq.text
                gitVer = gitVer.strip()
                if version == gitVer:
                    print(C + '[' + G + 'Up-To-Date' + C + ']' + '\n')
                else:
                    print(C + '[' + G + 'Available' + C + ']' + '\n')
                else:
                    print(C + '[' + R + 'Status : {}'.format(vScode) + C + ']' + '\n')
        except Exception as e:
            print('\n\n' + R + '[-]' + C + ' Exception : ' + W + str(e))
            sys.exit()

def createSystemUser():
    system_user = input("Enter Username: ").lower()    #Convertir la entrada a minus.
    password = getpass.getpass()
    try:
        #subprocess.run(['useradd', '-p', password, system_user]) 
        subprocess.run(['useradd', password, system_user])  
        print ("The user {} was created".format(system_user))    
        time.sleep(5)    
    except: 
        print("Failed to add user")                      
        sys.exit(1) 


def firewallSetup():
    #UFW
    pass

def sshHardening():
    pass

def certificateSetup():
    pass



def createDirEstructure():
    #parent_dir = "/mnt/bbh_home/tools/BBH"
    parent_dir = "/tmp/BBH/"             #Eliminar
    directory = "MALWARE"                #Eliminar
    os.mkdir(parent_dir)
    if os.mkdir.exist:                  #Revisar
        print("The folder already exist. Check you installation")
    os.chdir(parent_dir)
    print(os.getcwd())


    l1_subdir = [
                 "RECON", "INJECTION","WEB-FUZZERS", "AUTH", "SOURCE-CODE", "EXPLOITS", "VULNERABILITY-SCANNER", "CMS", "MALWARE", "GIT-PROJECTS", "MYOWNSCRIPTS", "WAF", "WORDLISTS", "FRAMEWORKS", "BINARY", "INSTALLERS", 
                 "BACKUP", "REPORTS", "WEBSITE-MONITOR", "SCREENSHOTS", "CORS", "CLOUD"]

    l2_subdirInjection = ['XSS', 'SQLI', 'NO-SQL', 'HQL', 'LDAP', 'XPATH', 'XQUERY', 'XSLT', 'XML', 'OS-CMD-INJECTION','SSTI', 'CSTI', 'CRLF', 'CSRF', 'CSV', 'OPEN-REDIRECT', 'LFI-RFI']

    l2_subdirRecon = ['SUBDOMAIN', 'GIT', 'AWS', 'AZURE', 'WAF', 'SCREENSHOT', 'CMS', 'SERVICES', 'WEB-FUZZERS']

    l2_subdirWebfuz = ['DIRECTORY-SEARCH', 'URL-EXTRACTOR', 'SCRAPPERS']

    l2_subdirCms = ['JOOMLA', 'WORPRESS', 'WIX', 'OSCOMMERCE', 'WOOCOMERCE']

    l2_subdirSource_code = ['PYTHON', 'JAVASCRIPT','BASH','VULNERABLE-CODE-LAB']

    l2_subdirExploits = ['WEBSHELLS','PAYLOADS']

    l2_subdirMalware = ['WINDOWS', 'LINUX', 'MAC']

    
 
    #IMPROVE THIS CODE   :: os.walk()
    for sub in range(len(l1_subdir)):
        os.makedirs(l1_subdir[sub])

    os.chdir('INJECTION/')

    for i in range(len(l2_subdirinjection)):
        print(l2_subdirInjection[i])
        os.makedirs(l2_subdirInjection[i])
        
    os.chdir(parent_dir)
    os.chdir('RECON/')
    for i in range(len(l2_subdirRecon)):
        os.makedirs(l2_subdirRecon[i])  

    os.chdir(parent_dir)
    os.chdir('WEB-FUZZERS/')
    for i in range(len(l2_subdirWebfuz)):
        os.makedirs(l2_subdirWebfuz[i])

    os.chdir(parent_dir)
    os.chdir('CMS/')
    for i in range(len(l2_subdirCms)):
        os.makedirs(l2_subdirCms[i])

    os.chdir(parent_dir)
    os.chdir('SOURCE-CODE/')
    for i in range(len(l2_subdirSourceCode)):
        os.makedirs(l2_subdirSourceCode[i])

    os.chdir(parent_dir)
    os.chdir('EXPLOITS/')
    for i in range(len(l2_subdirExploits)):
        os.makedirs(l2_subdirExploits[i])

    os.chdir(parent_dir)
    os.chdir('MALWARE/')
    for i in range(len(l2_subdirMalware)):
        d = l2_subdirMalware[i]
        #os.makedirs(l2_subdir_malware[i])
        for parent_dir, directory, files in os.walk(d):
            print(files)

    os.chdir(parent_dir)
    print(os.listdir(os.getcwd()))

'''
    l1_subdirectories = [
                         "RECON",['SUBDOMAIN', 'GIT', 'AWS', 'AZURE', 'WAF', 'SCREENSHOT', 'CMS', 'SERVICES', 'WEB-FUZZERS'], 
                         "INJECTION",['XSS', 'SQLI', 'NO-SQL', 'HQL', 'LDAP', 'XPATH', 'XQUERY', 'XSLT', 'XML', 'OS-CMD-INJECTION','SSTI', 'CSTI', 'CRLF', 'CSRF', 'CSV', 'OPEN-REDIRECT', 'LFI-RFI'], 
                         "WEB-FUZZERS", ['DIRECTORY-SEARCH', 'URL-EXTRACTOR', 'SCRAPPERS'],
                         "AUTH",['JWT'],
                         "SOURCE-CODE",['PYTHON', 'JAVASCRIPT','BASH','VULNERABLE-CODE-LAB'],
                         "EXPLOITS",['WEBSHELLS','PAYLOADS'],
                         "VULNERABILITY-SCANNER", ['RETIREJS'],
                         "CMS",['JOOMLA', 'WORPRESS', 'WIX', 'OSCOMMERCE', 'WOOCOMERCE'],
                         "MALWARE",['WINDOWS', 'LINUX', 'MAC'],
                         'GIT-PROJECTS',
                         'MYOWNSCRIPTS',
                         'WAF', 
                         'WORDLISTS',        
                         'FRAMEWORKS', 
                         'BINARY', 
                         'INSTALLERS', 
                         'BACKUP', 
                         'REPORTS', 
                         'WEBSITE-MONITOR', 
                         'SCREENSHOTS', 
                         'CORS', 
                         'CLOUD',   
                        ]
    
    os.mkdir(l1_subdirectories[0])
    os.chdir(l1_subdirectories[0])

    for n in range(len(l1_subdirectories[0])):
        for x in range(len(l1_subdirectories[n])):
            print(l1_subdirectories[n][x])

'''

def systemDependiencies():
    import importlib.util, pip

    with open('requirements.txt', 'r') as pckg:
        pckgReq = pckg.read().strip().split('\n')

    print('\n' + R + '[-]' + C + 'Hold on Ch00by I\'m Checking Dependencies....' + W + '\n')
    time.sleep(2)

    for pckg in pckgReq:
        spec = importlib.util.find_spec(pckg)
        if spec is None:
            print(R + '[-]' + W + ' {}'.format(pckg) + C + ' is not Installed' + W)
            fail = True
        else:
            pass
    if fail == True:
        #print('\n' + R + '[-]' + C + 'Please execute ' + W + 'pip3 install -r requirements.txt' + C + ' to install missing packages' + W + '\n')
        print('\n' + R + '[-]' + W + 'Please wait while I install all packages' '\n')
        for pckg in pckgReq:
            spect = importlib.util.find_spec(pckg)
            if spect is None:
                print('\n' + G + '[+] Installing ' + C + '{}'.format(pckg))
                #pip.main(['install', pckg])                                       # Version Too OLD.  https://pip.pypa.io/en/latest/user_guide/#using-pip-from-your-program
                #os.system('pip3 install -r', pckg)
                #subprocess.check_call([sys.executable, '-m', 'pip3', 'wfuzz'])
        print('\n' + C + '[*][*][*]' + G + ' Installation Successfuly ' + C + '[*][*][*]' '\n')
                
        exit()

def setupHackingTools():
    print(R + "[*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*]")
    print(G + "[*][*] Installing" + C + " {{XSS}} " + G + "TOOLS [*][*]")
    os.chdir(parent_dir+'INJECTION/XSS/')
    try:
        os.makedirs(parent_dir+'INJECTION/XSS/PAYLOADS')
    except:
        pass
    #os.system('git clone https://github.com/s0md3v/XSStrike.git')
    with open('packages.xssGitProjects.txt', 'r') as xssGitProjects:
        for xssGit in xssGitProjects:
            os.system('git clone ' + xssGit)

    xssPackages = [
                    'https://xsser.03c8.net/xsser/xsser_1.8.2_all.deb'
    ]

    for xssPckg in xssPckgs:    
        os.system('wget '+ xssPckg)
        os.system('dpkg', '-i', xssPckg)
    
    os.chdir(parent_dir+'INJECTION/XSS/PAYLOADS')       #OPTIMIZE IN NEXT VERSION 

    with open('xssPayloads.txt', 'r') as xssPayloads:
        for xssPayload in xssPayloads:    
            os.system('wget '+ xssPayload)    
    
    print(R + "[*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*]")

    print(G + "[*][*] Installing" + C + " {{ RECON/FINGERPRINT }} "  + G + "TOOLS [*][*]")

    print(G + "[*][*] Installing"  + C + " {{ GIT ENUMERATION TOOLS }} " + G + "[*][*]")
    
    with open('packages.reconGitProjects.txt', 'r') as reconGit:
        for reconGit in reconGit:
            os.system('git clone '+reconGit)

    goReconTool = [
                    'github.com/michenriksen/gitrob'
                   ]
    for goRecon in goReconTool:    
        os.system('go get '+ goRecon) 
 

    reconPackages = [
                      'https://github.com/internetwache/GitTools/blob/master/Dumper/gitdumper.sh',
                      'https://raw.githubusercontent.com/internetwache/GitTools/master/Extractor/extractor.sh'
                      ]
    for reconPckg in reconPckgs:    
        os.system('wget '+ reconPckg) 

    print(R + "[*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*]")

    print(G + "[*][*] Installing" + C + " {{ JWT CRACKING }} " + G + "TOOLS [*][*]")

    with open('packages.jwtGitProjects.txt', 'r') as jwtGit:
        for jwtGit in jwtGit:
            os.system('git clone '+ jwtGit)

    print(R + "[*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*]")


'''
def systemInstallNotes():
    #read bucket.txt, github_projects.txt file with the packages to install
    
    #proc = subprocess.Popen('apt-get install -y FILE', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash")
    #proc.wait()

    pkg_name = "vlock"    # Read packages from file. lnxPackages.txt

    cache = apt.cache.Cache()
    cache.open()
    cache.update()

    pkg = cache[pkg_name]
    if pkg.is_installed:
        print "{pkg_name} already installed".format(pkg_name=pkg_name)
    else:
        pkg.mark_install()

        try:
            cache.commit()
        except Exception, arg:
            print >> sys.stderr, "Sorry, package installation failed [{err}]".format(err=str(arg))
'''

def logFiles():
    #box_setup = BBH_Installation.log
    #print(os.stat(box_setup))
    pass

def sendEmail():
    message = MIMEMultipart()
    password = 'xxxxx'
    message['From'] = 'autosystem365@gmail.com'
    message['To'] = 'ksanchez.bughunter@gmail.com'
    message['Subject'] = 'Bug Hunter System Installation'
    message['Body'] = 'The Bug Hunter System Installation Profile its ready. Happy Hacking!!!!'
    
    message.attach(MIMEText(file('BBH_Installation.log').read()))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(message['From'], password)
        server.sendmail(message['From'], message['To'], message.as_string())
        server.quit()
    except:
        pass

#def boxHardening():
    # Install SSL, SSH, UFW, 


def banner():
    os.system('clear')
    print(G + "______________________")
    print(G + "|"   + G + "                    |")
    print(G + "|" + R +" WELCOME CH00BY AND"+ G + " |")
    print(G + "|" + R +" HAPPY BUG HUNTING" + G + "  |")
    print(G + "|____________________|")
    print(G + "     " +G+  " ||")
    print(R + "(\_/)" +G+  " ||")
    print(R + "( *,*)"+G+  "||")
    print(R + '(")_(")')
    print(G + '--^--^--^--^--^--^--^--')
    print(C + "[*] Building my " + R + "{\{BUG HUNTING HOME}\}" + C + "[*]")
    print(C + "[*] Created By " + R + "{\{@ksanchez_cld}\}" + C + "[*]")
    print(C + "[*] Version " + G + "version 0.0.1" + C + "[*]")
    #time.sleep(5)

'''
if __name__ == '__main__':
    main()
'''

banner()
versionCheck()
systemDependiencies()
createDirEstructure()
setupHackingTools()


###############
###   TODO  ###
###############

#1. Listar toda la estructura de directorio (tree -L2) y guardarlo en un log + timestamp para enviarlo via correo como evidencia de la instalacion.
# https://www.youtube.com/watch?v=10q_CKnM3x4