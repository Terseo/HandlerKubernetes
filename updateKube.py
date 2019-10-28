import os
import random

loop=True
indexes= dict()
listOpt=[]

## Delete Pods file
deletePods = "rm -rf pods.txt"
os.system(deletePods)

## Get the list of pods 'Remove pod label from the begin"
getPods= "kubectl get pods -o name >> pods.txt"
os.system(getPods)

## Remove pod label from the command
removePod= "sed -i 's?pod/??g' pods.txt"
os.system(removePod)


    
def loadIndex():
    with open('pods.txt', 'r') as f:
        global indexes
        indexes = {index:value for index, value in enumerate(f)}

def searchPod():

    podName = raw_input("Pod Name: ")
    print
    with open('pods.txt', 'r') as searchfile:
        for num, line in enumerate(searchfile, 0):
            if podName in line:
                print ("\033[1;32;40m " +str(num)+" "+line)
                loadIndex()

def listarPods():

#    with open('pods.txt', 'r') as f:
#        global indexes
#        indexes = {index:value for index, value in enumerate(f)}
        loadIndex()
        print
        print ("\033[1;31;40m Pods Running:  \n")
        print
        for i in range(len(indexes)):
            print (str(i)+" "+indexes[i])

def readOptions():

    global listOpt
    idPods = raw_input("\033[1;37;40m Enter the list of pods with spaces: ")
    print
    listOpt = map(int,idPods.split())
    print

def detenerPods():

    readOptions()
    print
    for id in range(len(listOpt)):
        ## Uncomment variable command and os.system in order to execute the command
	    print ("\033[1;33;40m kubectl delete pods " + indexes[listOpt[id]])
#        command = "kubectl delete pods " + indexes[listOpt[id]]
#        os.system(command)
    print

def actualizarPods():

    readOptions()
    print
    for id in range(len(listOpt)):
        ## Uncomment variable command and os.system in order to execute the command
        print ("\033[1;33;40m kubectl depoly pods " + indexes[listOpt[id]])
#        command1 = "kubectl delete pods " + indexes[listOpt[id]]
#        command2 = "kubectl deploy pods " + indexes[listOpt[id]]
#        os.system(command1)
#        os.system(command2)
    print

def logTail():

    idPod = input("\033[1;37;40m Enter ID from pod:  ")
    color=random.randint(30,37)
#    print color
    print "\033[1;%s;40m kubectl logs -f --tail 500 %s " % (str(color), indexes[idPod] )
    logcommand = "kubectl logs -f --tail 500 " + indexes[idPod]
    os.system(logcommand)
    print

def main():

    while loop:
        menu()

def menu():

    print("\033[1;37;40m ********************** KUBERNETES DEMO ************************ \n")
    choice = input ("""
                      1: ListAllPods
                      2: SearchPod
                      3: Detener
                      4: Actualizar
                      5. Logs

Select your Choice: """ )
    print

    if choice == 1:

          listarPods()

    elif choice == 2:

          searchPod()

    elif choice == 3:

          detenerPods()

    elif choice == 4:

          actualizarPods()

    elif choice == 5:

         logTail()

    else:
          print("Unknown Option Selected")

## Corriendo todo
main()
