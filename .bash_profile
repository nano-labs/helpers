SHELL_SESSION_HISTORY=0
PS1='[\D{%T}]\[\033[00m\]\[\033[01;34m\]\W\[\033[00m\]\$ '
python /Users/fabio/motd.py

dshell(){
  if [ -z "$1" ]
  then
    docker exec -it "$(docker ps | grep api | awk '{print $1}')" bash;
  else
    docker exec -it "$(docker ps | grep $1 | awk '{print $1}')" bash;
  fi
}
dcp(){
  if [[ $1 == *":"* ]]; then
    container_name=$(echo $1 | cut -d: -f1)
    container_id=$(docker ps | grep -v CONTAINER | grep $container_name | awk '{print $1}' | cut -d_ -f2)
    src_file=$(echo $1 | cut -d: -f2)
    src=$container_id:$src_file
    dst=$2
  elif [[ $2 == *":"* ]]; then
    container_name=$(echo $2 | cut -d: -f1)
    container_id=$(docker ps | grep -v CONTAINER | grep $container_name | awk '{print $1}' | cut -d_ -f2)
    src=$1
    dst_file=$(echo $2 | cut -d: -f2)
    dst=$container_id:$dst_file
  else
    echo "error"
  fi
  echo docker cp $src $dst
  docker cp $src $dst
}
_dshell_autocomplete() 
{
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    opts=`docker ps | grep -v CONTAINER | awk '{print $NF}' | cut -d_ -f2`
    if [[ ${cur} == * ]] ; then
        COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
        return 0
    fi
}
complete -F _dshell_autocomplete dshell
complete -F _dshell_autocomplete dcp

alias gti=git
alias dhsell=dshell
alias fucking=sudo
alias would-you-kindly=sudo
