#!/usr/bin/env bash
printthis()
{
    echo '                                      
      $$$$$$\  $$\   $$\ 
    $$  __$$\ $$ |  $$ |
    $$ /  $$ |$$ |  $$ |
    $$ |  $$ |$$ |  $$ |
    $$$$$$$  |\$$$$$$$ |
    $$  ____/  \____$$ |
    $$ |      $$\   $$ |
    $$ |      \$$$$$$  |
    \__|       \______/                                        
    '
}



set -eo pipefail
IFS=$'\n\t'

helpFunction()
{
   echo ""
   echo "Usage: [./py install 3.8.6 ] "
   echo -e " ./unpy install 3.8. ----> Installs 3.8.6 from source"
   exit 1 # Exit script after printing help
}

# if [ -z "$3" ];then
printthis    
# fi


py ()
{    
    case $1 in
        install)
        if [ "$2" = "3.8.6" ];
            then
            sudo apt update
            sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev
            mkdir abc && cd abc
            sudo wget https://www.python.org/ftp/python/3.8.6/Python-3.8.6.tgz
            sudo tar xzf Python-3.8.6.tgz
            cd Python-3.8.6
            ./configure --enable-optimizations
            make -j 8
            python3.8 --version
            echo " Installed Python 3.8.6 "
            cd ..
            sudo rm -f Python-3.8.6.tgz
            sudo rm -r Python-3.8.6
            echo "########### Installation complete ###############"
        fi
        ;;
    esac  

}

pushd `dirname $0` > /dev/null
    py $@




# {
#     case $3 in
#     del)
#     echo "--- Deleting files --- "
#     echo "This will delete all selected python versions, select yes or no (y/n) :"
#     read value
#     if [ $value = y -o $value = Y ];then
#         $0 $1 $2 | sudo bash -v
#     elif [ $value = n -o $value = N ]; then
#         echo '-- Stopping the process --'
#         exit 9999
#     fi
    
#     ;;
#     esac
# } 
# {
#     case $2 in
#         all)
#         echo "---------------------------------- listing all python versions files  ------------------------------------------
#         "
#         echo "- below are  usr/local/bin
#         "
#         ls -l /usr/local/bin | grep /Library/Frameworks/Python.framework/Versions | awk '{print "rm \47/usr/local/bin/" $9 "\47"}'
#         echo "- below are all x.x Versions 
#         "
#         ls -d /Library/Frameworks/Python.framework/Versions/* 2> /dev/null | awk '{print "rm -rf \47" $0 "\47"}'
#         echo "- below are Applications under python        
#         "
#         ls -d /Applications/Python\ * 2> /dev/null | awk '{print "rm -rf \47" $0 "\47"}'
#         ;;
#         3)
#         echo "---------------------------------- listing all python versions files  ------------------------------------------"
#          echo "- below are  usr/local/bin   
#         "
#         ls -l /usr/local/bin | grep /Library/Frameworks/Python.framework/Versions/3 | awk '{print "rm \47/usr/local/bin/" $9 "\47"}'
#          echo "- below are all 3.x Versions       
#         "
#         ls -d /Library/Frameworks/Python.framework/Versions/3.* 2> /dev/null | awk '{print "rm -rf \47" $0 "\47"}'
#         echo "- below are Applications under 3.x python       
#         "
#         ls -d /Applications/Python\ 3.* 2> /dev/null | awk '{print "rm -rf \47" $0 "\47"}'
#         ;;
#         2)
#         echo "---------------------------------- listing all python versions files  ------------------------------------------"
#          echo "- below are  usr/local/bin     
#         "
#         ls -l /usr/local/bin | grep /Library/Frameworks/Python.framework/Versions/2 | awk '{print "rm \47/usr/local/bin/" $9 "\47"}'
#          echo "- below are all 2.x Versions 
#         "
#         ls -d /Library/Frameworks/Python.framework/Versions/2.* 2> /dev/null | awk '{print "rm -rf \47" $0 "\47"}'
#         echo "- below are Applications under 2.x python     
#         "
#         ls -d /Applications/Python\ 2.* 2> /dev/null | awk '{print "rm -rf \47" $0 "\47"}'
#         ;;
#         ############ testing #########
#         file-x)
#         ls -d /Users/ak/Desktop/Signoff/testme/lol* 2> /dev/null | awk '{print "rm -rf \47" $0 "\47"}'
#     esac
# }

