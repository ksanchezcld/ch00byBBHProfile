#!/usr/bin/env python3
#_*_ coding: utf8 _*_

import os, subprocess, sys, getpass, time, smtplib, platform
from pathlib import Path

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white
Y = '\033[33m' # yellow

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
parent_dir = "/root/BBH/"            #Eliminar  :: parent_dir = "/mnt/bbh_home/tools/BBH"

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
                #else:
                    #print(C + '[' + R + 'Status : {}'.format(vScode) + C + ']' + '\n')
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
    Path("/root/BBH/").mkdir(parents=True, exist_ok=True)
    parent_dir = "/root/BBH/"
    #os.mkdir(parent_dir)
    #if os.mkdir.exists:                  #Revisar
    if not os.path.exists(parent_dir):
        print("Creating Directory....")
        os.makedirs(parent_dir)
    else:
        #os.rmdir()
        os.chdir(parent_dir)
        print(os.getcwd())


    l1_subdir = [
                 "RECON", "INJECTION","WEB-FUZZERS", "AUTH", "SOURCE-CODE", "EXPLOITS", "VULNERABILITY-SCANNER", "CMS", "MALWARE", "GIT-PROJECTS", "MYOWNSCRIPTS", "WAF", "WORDLISTS", "FRAMEWORKS", "BINARY", "INSTALLERS", 
                 "BACKUP", "REPORTS", "WEBSITE-MONITOR", "SCREENSHOTS", "CORS", "CLOUD"]

    l2_subdirInjection = ['XSS', 'SQLI', 'NO-SQL', 'HQL', 'LDAP', 'XPATH', 'XQUERY', 'XSLT', 'XML', 'OS-CMD-INJECTION','SSTI', 'CSTI', 'CRLF', 'CSRF', 'CSV', 'OPEN-REDIRECT', 'LFI-RFI']

    l2_subdirRecon = ['SUBDOMAIN', 'GIT', 'AWS', 'AZURE', 'WAF', 'SCREENSHOT', 'CMS', 'SERVICES', 'WEB-FUZZERS']

    l2_subdirWebfuz = ['DIRECTORY-SEARCH', 'URL-EXTRACTOR', 'SCRAPPERS']

    l2_subdirCms = ['JOOMLA', 'WORPRESS', 'WIX', 'OSCOMMERCE', 'WOOCOMERCE']

    l2_subdirSourceCode = ['PYTHON', 'JAVASCRIPT','BASH','VULNERABLE-CODE-LAB']

    l2_subdirExploits = ['WEBSHELLS','PAYLOADS']

    l2_subdirMalware = ['WINDOWS', 'LINUX', 'MAC']

    
 
    #IMPROVE THIS CODE   :: os.walk()
    for sub in range(len(l1_subdir)):
        if not os.path.exists(l1_subdir[sub]):
            os.makedirs(l1_subdir[sub])
        else:
            continue

    os.chdir('INJECTION/')
    for i in range(len(l2_subdirInjection)):
        if not os.path.exists(l2_subdirInjection[i]):
            os.makedirs(l2_subdirInjection[i])
            print(l2_subdirInjection[i])
        else:
            continue
        
    os.chdir(parent_dir)
    os.chdir('RECON/')
    for i in range(len(l2_subdirRecon)):
        if not os.path.exists(l2_subdirRecon[i]):
            os.makedirs(l2_subdirRecon[i])
            print(l2_subdirRecon[i])
        else:
            continue

    os.chdir(parent_dir)
    os.chdir('WEB-FUZZERS/')
    for i in range(len(l2_subdirWebfuz)):
        if not os.path.exists(l2_subdirWebfuz[i]):
            os.makedirs(l2_subdirWebfuz[i])
            print(l2_subdirWebfuz[i])
        else:
            continue

    os.chdir(parent_dir)
    os.chdir('CMS/')
    for i in range(len(l2_subdirCms)):
        if not os.path.exists(l2_subdirCms[i]):
            os.makedirs(l2_subdirCms[i])
            print(l2_subdirCms)
        else:
            continue

    os.chdir(parent_dir)
    os.chdir('SOURCE-CODE/')
    for i in range(len(l2_subdirSourceCode)):
        if not os.path.exists(l2_subdirSourceCode[i]):
            os.makedirs(l2_subdirSourceCode[i])
            print(l2_subdirSourceCode[i])
        else:
            continue

    os.chdir(parent_dir)
    os.chdir('EXPLOITS/')
    for i in range(len(l2_subdirExploits)):
        if not os.path.exists(l2_subdirExploits[i]):
            os.makedirs(l2_subdirExploits[i])
            print(l2_subdirExploits[i])
        else:
            continue

    os.chdir(parent_dir)
    os.chdir('MALWARE/')
    for i in range(len(l2_subdirMalware)):
        if not os.path.exists(l2_subdirMalware[i]):
            os.makedirs(l2_subdirMalware[i])
            print(l2_subdirMalware[i])
        # d = l2_subdirMalware[i]
        #for parent_dir, directory, files in os.walk(d):
            #print(files)
        else:
            continue

    os.chdir(parent_dir)
    print(os.listdir(os.getcwd()))
    print('\n' + C + '[*][*][*]' + Y + ' DIRECTORY STRUCTURE COMPLETED......Installing Tools ' + C + '[*][*][*]' '\n')
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
        print('\n' + C + '[*][*][*]' + Y + ' Installation Successfuly ' + C + '[*][*][*]' '\n')
                
        exit()

def setupHackingTools():
    print(R + "[*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*]")
    print(G + "[*][*] Installing" + C + " {{XSS}} " + G + "TOOLS [*][*]")
    if os.path.exists(parent_dir+'INJECTION/XSS/'):
        os.chdir(parent_dir+'INJECTION/XSS/')
    else:
        os.makedirs(parent_dir + 'INJECTION/XSS/PAYLOADS')
    xssProjects = '/root/ch00byBBHProfile/xssGitProjects.txt' # TODO - FIX, Change for relative Path....
    with open(xssProjects, 'r') as xssGitProjects:
        for xssGit in xssGitProjects:
            #if xssGit.readlines:
            #    print("FIle Installed....")     # TODO
            #else:
                os.system('git clone ' + xssGit)
        print('\n' + C + '[*][*][*]' + Y + ' All ' + G + '{XSS}' + Y + ' Projects Susscessfully Installed....' + R + 'Happy Hunting :) ' + C + '[*][*][*]' '\n')


    #xssPackages = [
    #                'https://xsser.03c8.net/xsser/xsser_1.8.2_all.deb'
    #]

    #for xssPckg in xssPckgs:
     #   os.system('wget '+ xssPckg)
     #   os.system('dpkg', '-i', xssPckg)
    
    #os.chdir(parent_dir+'INJECTION/XSS/PAYLOADS')       # TODO - OPTIMIZE IN NEXT VERSION

    #with open('xssPayloads.txt', 'r') as xssPayloads:
    #    for xssPayload in xssPayloads:
    #        os.system('wget '+ xssPayload)

    # TODO - CONTINUAR EL MEJORANDO EL CODIGO A PARTIR DE ESTA LINEA
    
    print(R + "[*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*]")

    print(G + "[*][*] Installing" + C + " {{ RECON/FINGERPRINTING TOOLS }} "  + G + "[*][*]")

    # TODO - AQUI VA EL ARCHIVO DE HERRAMIENTAS PARA RECON/FINGERPRINTING

    print(G + "[*][*] Installing" + C + " {{ GIT ENUMERATION TOOLS }} " + G + "[*][*]")

    # TODO - AQUI VA EL ARCHIVO DE HERRAMIENTAS PARA GIT ENUM
    
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

#TODO - Move the banner to a file (banner.py)
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
#versionCheck()
#systemDependiencies()
createDirEstructure()
setupHackingTools()


###############
###   TODO  ###
###############

#1. Listar toda la estructura de directorio (tree -L2) y guardarlo en un log + timestamp para enviarlo via correo como evidencia de la instalacion.
# https://www.youtube.com/watch?v=10q_CKnM3x4
