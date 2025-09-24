
semantic_search() {
    # Write current session history to history file
    history -a
    
    # Get the absolute path to the script
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    SEARCH_SCRIPT="$SCRIPT_DIR/my_semantic_search"
    
    result=$(
        fzf --bind "change:reload:$SEARCH_SCRIPT {q}" \
            --phony \
            --ansi \
            --height 40% --reverse \
            --preview 'echo {}' \
            --preview-window 'down:3:wrap'
    )
    
    if [ -n "$result" ]; then
        READLINE_LINE="$result"
        READLINE_POINT=${#READLINE_LINE}
    fi
}
bind -x '"\C-r":semantic_search'

