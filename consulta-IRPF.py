# -*- coding: utf-8 -*-
import pycurl
import sys
from bs4 import BeautifulSoup as bs
from HTMLParser import HTMLParser

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

class ParserHTMLZikaDORole(HTMLParser):
    def handle_data(self, data):
        if 'Sua declaração' in data:
            status = data.replace('							','')
            print "Status : ", status.replace('\n','')
        elif 'Prezado Contribuinte' in data:
            print "\nCPF : ", data
        elif 'Os dados da' in data:
            status = data.replace('							','')
            print "Status : ", status.replace('\n','')
            
def body(buf):
    try:
        element = bs(buf)
        contr = element.findAll('font', {'class':'txtDadosContribuinte'})
        cCpf = element.findAll('label', {'class':'txtCpfContribuinte'})
        parser = ParserHTMLZikaDORole()
        parser.feed(str(cCpf))
        parser.feed(str(contr))
        
        
    except Exception as e:
	print('\n[!] Error: %s' % (str(e)))
ans=True
while ans:
    sys.exc_clear
    print( bcolors.OKBLUE + '''
          
 _____                       _ _          _______________________ 
/  __ \                     | | |        |_   _| ___ \ ___ \  ___|
| /  \/ ___  _ __  ___ _   _| | |_ __ _    | | | |_/ / |_/ / |_   
| |    / _ \| '_ \/ __| | | | | __/ _` |   | | |    /|  __/|  _|  
| \__/\ (_) | | | \__ \ |_| | | || (_| |  _| |_| |\ \| |   | |    
 \____/\___/|_| |_|___/\__,_|_|\__\__,_|  \___/\_| \_\_|   \_|    
                                                            V 1.0
[+] Coder: Danilo Vaz                                                            
[+] E-mail: danilovazb[at]gmail[dot]com

[+] Greetz: Arthur Barros, Vinícius Henrique, Slayer and Canhoto
         
-----------------------------------------
1. Consulta CPF unico
2. Consulta lote de CPF
3. Exit

          '''+ bcolors.ENDC)
    ans=raw_input("~//#")
    if ans=="1":
        CPF = raw_input(bcolors.HEADER + "Digite o CPF que deseja consultar: \n" + bcolors.ENDC)
        biscoito = raw_input(bcolors.HEADER + "\nDigite o valor do ASPSESSIONIDSCTADABA que fica em seu cookie: \n" + bcolors.ENDC)
        c = pycurl.Curl()
        c.setopt(c.URL, 'http://www.receita.fazenda.gov.br/aplicacoes/atrjo/consrest/atual.app/paginas/view/restituicao.asp')
        c.setopt(c.COOKIE, 'ASPSESSIONIDSCTADABA=%s' % biscoito)
        c.setopt(pycurl.REFERER, 'http://www.receita.fazenda.gov.br/aplicacoes/atrjo/consrest/atual.app/paginas/view/restituicao.asp')
        c.setopt(c.POSTFIELDS, 'senha=&idSom=&valid=1&CPF=%s&exercicio=2014&Submit=Consultar' % CPF)
        c.setopt(c.VERBOSE, False)
        c.setopt(c.WRITEFUNCTION, body)
        c.perform()
        
    elif ans=="2":    
        arquivo = raw_input(bcolors.HEADER + "Digite o nome ou o caminho do seu arquivo: \n" + bcolors.ENDC)
        biscoito = raw_input(bcolors.HEADER + "\nDigite o valor do ASPSESSIONIDSCTADABA que fica em seu cookie: \n" + bcolors.ENDC)
        try:
            f = open(arquivo,"r")
            for linha in f:
                c = pycurl.Curl()
                c.setopt(c.URL, 'http://www.receita.fazenda.gov.br/aplicacoes/atrjo/consrest/atual.app/paginas/view/restituicao.asp')
                c.setopt(c.COOKIE, 'ASPSESSIONIDSCTADABA=%s' % biscoito)
                c.setopt(pycurl.REFERER, 'http://www.receita.fazenda.gov.br/aplicacoes/atrjo/consrest/atual.app/paginas/view/restituicao.asp')
                c.setopt(c.POSTFIELDS, 'senha=&idSom=&valid=1&CPF=%s&exercicio=2014&Submit=Consultar' % linha.rstrip())
                c.setopt(c.VERBOSE, False)
                c.setopt(c.WRITEFUNCTION, body)
                c.perform()
            f.close()
        except IOError:
                  print "\nO arquivo que voce tentou carregar nao existe ou foi digitado incorretamente!\n"
    elif ans=="4":
      break
    elif ans !="":
      print(bcolors.WARNING + "\nOpção errada!" + bcolors.ENDC)
