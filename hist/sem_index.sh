# === Semantic history indexer ===
index_last_command() {
    last=$(history 1 | sed 's/ *[0-9]\+ *//')
    case "$last" in
        "" | "ls" | "cd"* | "history" ) return ;;  # skip trivial
    esac
    python3 ~/.local/bin/vector_index.py "$last"
}

PROMPT_COMMAND="index_last_command; $PROMPT_COMMAND"

