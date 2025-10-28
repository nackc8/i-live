censorls() {
	ls "$@" | sed 's/kent/k**t/g'
}
