# Local preview server. `make serve` starts it in the background and tails its log;
# Ctrl-C stops the tail, not the server. `make stop` shuts it down.

PORT ?= 8000
PID  := .server.pid
LOG  := .server.log

.PHONY: serve start stop logs

serve: start logs

start:
	@if [ -f $(PID) ] && kill -0 $$(cat $(PID)) 2>/dev/null; then \
		echo "Server already running (pid $$(cat $(PID)))"; \
	else \
		python3 -u -m http.server $(PORT) > $(LOG) 2>&1 & echo $$! > $(PID); \
		sleep 0.5; \
		if kill -0 $$(cat $(PID)) 2>/dev/null; then \
			echo "Serving at http://localhost:$(PORT)/ (pid $$(cat $(PID)))"; \
		else \
			cat $(LOG); rm -f $(PID); exit 1; \
		fi; \
	fi

logs:
	@tail -n 20 -f $(LOG)

stop:
	@if [ -f $(PID) ]; then \
		kill $$(cat $(PID)) 2>/dev/null && echo "Server stopped"; rm -f $(PID); \
	else \
		echo "Server not running"; \
	fi
